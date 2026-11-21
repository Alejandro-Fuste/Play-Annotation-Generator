#!/usr/bin/env python3
"""Preview, copy and verify TapeVision v1.0. Never deletes source files."""
import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

FIELDS = ['clip_id','play_type','split','view','video_path','annotation_path',
          'drive_id','source_annotation','annotation_sha256','video_sha256','video_bytes']


def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    temp=path.with_name(path.name+'.partial')
    with temp.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)
    temp.replace(path)


def hash_file(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def unique(rows, key):
    out = {}
    for row in rows:
        k = key(row)
        if not k or k in out:
            raise ValueError(f'Missing or duplicate identity: {k!r}')
        out[k] = row
    return out


def safe_path(root, rel):
    p = PurePosixPath(rel)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError(f'Unsafe path: {rel}')
    result = root.joinpath(*p.parts)
    if not result.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes root: {rel}')
    return result


def normalized_view(value):
    return {'s':'S','sideline':'S','e':'E','endzone':'E','end zone':'E'}.get(value.strip().lower(), 'unknown')


def seconds(value):
    try:
        h,m,s = map(float,value.split(':')); return h*3600+m*60+s
    except (ValueError, AttributeError):
        return None


def metadata_pairs(rows):
    """Candidate pairs from complete source sequences, not filtered inventory."""
    groups = defaultdict(list)
    counts = Counter(Path(r['output_file'].strip()).stem for r in rows)
    for r in rows:
        start = seconds(r.get('start_time','')); source = r.get('input_file','').strip()
        if source and start is not None:
            groups[source].append((start,r))
    pairs = set()
    for group in groups.values():
        group.sort(key=lambda x:x[0]); starts = Counter(s for s,_ in group)
        for (s,a),(t,b) in zip(group,group[1:]):
            x,y = (Path(r['output_file'].strip()).stem for r in (a,b))
            e,f = seconds(a.get('end_time','')),seconds(b.get('end_time',''))
            if (x != y and counts[x] == counts[y] == starts[s] == starts[t] == 1
                and normalized_view(a.get('view','')) == 'S' and normalized_view(b.get('view','')) == 'E'
                and e is not None and f is not None and s < e <= t < f):
                pairs.add(frozenset((x,y)))
    return pairs


def choose_boundary(clips, pairs, override=None):
    n = len(clips)
    if n < 2:
        if override is not None and override != n: raise ValueError('Singleton must stay in training')
        return n
    target = (3*n+2)//5
    index = {r['clip_id']:i for i,r in enumerate(clips)}
    forbidden = set()
    for pair in pairs:
        if pair <= index.keys():
            a,b = sorted(index[x] for x in pair); forbidden.update(range(a+1,b+1))
    legal = [k for k in range(1,n) if k not in forbidden]
    if not legal: raise ValueError('No legal boundary with both partitions; review class')
    if override is not None:
        if override not in legal: raise ValueError(f'Unsafe boundary override {override}')
        return override
    return min(legal,key=lambda k:(abs(k-target),abs(5*k-3*n),k))


def valid_annotation(obj, clip, label, tags):
    if not isinstance(obj, dict) or not all(isinstance(obj.get(k),dict) for k in ('clip','play','tracks','actions')):
        return False
    tag=obj['play'].get('play_tag','')
    return (tag in tags and tag.endswith('_'+label)
            and Path(str(obj['clip'].get('video_name',''))).stem == clip)


def validate_source_annotation(src, row, tags):
    """Deferred full validation, performed during copy only."""
    if not src.is_file() or src.stat().st_size != row['annotation_source_bytes']:
        raise ValueError(f'Annotation missing or changed since preview: {src}')
    try:
        obj=json.loads(src.read_text())
        if not valid_annotation(obj,row['clip_id'],row['play_type'],tags):
            raise ValueError('Annotation identity or schema mismatch')
        report=src.with_name('validation_report.json')
        if report.is_file():
            data=json.loads(report.read_text())
            if not isinstance(data.get('errors'),list) or data['errors']:
                raise ValueError('Annotation validation report contains errors')
    except (OSError,TypeError,AttributeError,json.JSONDecodeError) as exc:
        raise ValueError(f'Invalid annotation or report: {src}: {exc}') from exc
    return hash_file(src)


def plan(repo, annotation_csv, video_csv, overrides=None, fast=False):
    """Build split plan. fast=True reads inventories and small metadata only.

    The fast plan deliberately leaves annotation_sha256 empty: content is
    validated and fingerprinted later during --copy, not during --preview.
    """
    overrides = overrides or {}
    anns = unique(read_csv(annotation_csv),lambda r:PurePosixPath(r['repository_path']).parent.name)
    videos = unique(read_csv(video_csv),lambda r:Path(r['File_Name']).stem)
    unique(videos.values(),lambda r:r['File_ID'])
    meta = read_csv(repo/'data/DatasetSummary.csv')
    metadata = defaultdict(list)
    for r in meta: metadata[Path(r['output_file'].strip()).stem].append(r)
    taxonomy_data = json.loads((repo/'data/plays.json').read_text())
    taxonomy = set(taxonomy_data['playLabels'])
    tags = set(taxonomy_data['formattedPlayLabels'])
    excludes = {line.strip() for line in (repo/'data/rpo_excluded_video_ids.txt').read_text().splitlines() if line.strip() and not line.lstrip().startswith('#')}
    failures = set()
    # Avoid walking thousands of clip-output directories during preview.
    # Batch manifests live in per-play _batch subdirectories.
    manifest_files = sorted((repo/'outputs/batch').glob('*/_batch/batch_manifest.csv'))
    manifest_files += sorted((repo/'outputs/batch').glob('*/*/_batch/batch_manifest.csv'))
    for f in manifest_files:
        for r in read_csv(f):
            if r.get('status','').upper() == 'FAILED' or int(r.get('error_count') or 0)>0:
                failures.add(r['clip_name'])
    groups = defaultdict(list); held = {}; warning_count = 0; missing_report_count = 0
    for clip,a in sorted(anns.items()):
        if clip not in videos: held[clip]='missing video'; continue
        p = PurePosixPath(a['repository_path']); match = re.fullmatch(r'(.+)_(\d+)',clip)
        if (not match or len(p.parts)<5 or p.parts[:2]!=('outputs','batch') or p.name!='annotations.json'
            or match[1]!=p.parts[2] or match[1] not in taxonomy):
            held[clip]='noncanonical identity'; continue
        label = match[1]
        if label=='RPO' and match[2] in excludes: held[clip]='intentional exclusion'; continue
        if clip in failures: held[clip]='batch failure'; continue
        src = safe_path(repo,str(p))
        m=metadata[clip]; view=normalized_view(m[0].get('view','')) if len(m)==1 else 'unknown'
        digest = ''
        if not fast:
            if not src.is_file() or src.stat().st_size != int(a['file_size_bytes']):
                held[clip]='annotation missing or inventory size changed'; continue
            try:
                obj=json.loads(src.read_text()); report=src.with_name('validation_report.json')
                if not valid_annotation(obj,clip,label,tags):
                    held[clip]='annotation identity or schema mismatch'; continue
                if report.is_file():
                    validation=json.loads(report.read_text())
                    if not isinstance(validation.get('errors'),list) or validation['errors']:
                        held[clip]='validation errors or unknown report schema'; continue
                    warning_count += bool(validation.get('warnings'))
                else: missing_report_count += 1
                embedded=normalized_view(str((obj['clip'].get('source') or {}).get('view') or ''))
                if view=='unknown' and len(m)<=1: view=embedded
                elif embedded!='unknown' and embedded!=view: view='unknown'
                digest=hash_file(src)
            except (ValueError,OSError,AttributeError,TypeError):
                held[clip]='unreadable annotation or report'; continue
        groups[label].append(dict(clip_id=clip,play_type=label,view=view,drive_id=videos[clip]['File_ID'],source_annotation=str(p),annotation_sha256=digest,video_sha256='',video_bytes='',number=int(match[2]),annotation_source_bytes=int(a['file_size_bytes'])))
    if set(overrides)-groups.keys(): raise ValueError('Boundary override for absent play type')
    pairs=metadata_pairs(meta); result=[]; boundaries=[]
    for label,clips in sorted(groups.items()):
        clips.sort(key=lambda r:r['number']); n=len(clips); k=choose_boundary(clips,pairs,overrides.get(label))
        left=clips[k-1] if k else None; right=clips[k] if k<n else None
        boundaries.append(dict(play_type=label,total=n,train=k,test=n-k,target=(3*n+2)//5,
                               left=f"{left['clip_id']} ({left['view']})" if left else '-',right=f"{right['clip_id']} ({right['view']})" if right else '-',
                               review_required=True,
                               nearby=[dict(clip_id=r['clip_id'],view=r['view'],metadata=metadata[r['clip_id']]) for r in clips[max(0,k-2):min(n,k+2)]]))
        for i,r in enumerate(clips):
            r['split']='train' if i<k else 'test'; prefix=f"{r['split']}/{label}"
            r['video_path']=f"{prefix}/videos/{r['clip_id']}.mp4"; r['annotation_path']=f"{prefix}/annotations/{r['clip_id']}.json"; result.append(r)
    # Guard even against candidate pairs spanning different canonical labels.
    assignments={r['clip_id']:r['split'] for r in result}
    crossing=[sorted(p) for p in pairs if p<=assignments.keys() and len({assignments[x] for x in p})>1]
    if crossing: raise ValueError(f'Cross-class candidate pair leakage: {crossing}')
    summary=dict(fast_inventory_only=fast,validation_deferred=fast,video_inventory=len(videos),annotation_inventory=len(anns),matched=len(anns.keys()&videos.keys()),held=held,unmatched_videos=len(videos.keys()-anns.keys()),warning_reports=warning_count,missing_reports=missing_report_count,eligible=len(result))
    return result,boundaries,summary


def run(*args):
    return subprocess.check_output(args,text=True)


def remote_index(remote):
    listing=json.loads(run('rclone','lsjson',remote,'--recursive','--files-only','--hash'))
    return unique((r for r in listing if r.get('ID')),lambda r:r['ID'])


def copy_verified(src, dest, digest):
    if dest.exists():
        if hash_file(dest)!=digest: raise ValueError(f'Destination conflict: {dest}')
        return
    dest.parent.mkdir(parents=True,exist_ok=True); temp=dest.with_name(dest.name+'.partial')
    shutil.copyfile(src,temp)
    if hash_file(temp)!=digest: raise ValueError(f'Copy hash mismatch: {dest}')
    temp.replace(dest)


def copy_dataset(repo, rows, dest, remote=None, local=None):
    tags=set(json.loads((repo/'data/plays.json').read_text())['formattedPlayLabels'])
    if dest.resolve().is_relative_to(repo.resolve()) or repo.resolve().is_relative_to(dest.resolve()):
        raise ValueError('Destination must not overlap repository')
    if local and (dest.resolve().is_relative_to(local.resolve()) or local.resolve().is_relative_to(dest.resolve())):
        raise ValueError('Destination must not overlap local videos')
    dest.mkdir(parents=True,exist_ok=True)
    index=remote_index(remote) if remote else None
    if index is not None:
        seen=defaultdict(set)
        for r in rows:
            entry=index.get(r['drive_id']); expected=r['clip_id']+'.mp4'
            if not entry or entry['Name']!=expected or not entry.get('Hashes',{}).get('MD5') or entry.get('Size',0)<=0:
                raise ValueError(f'Google Drive identity or MD5 unavailable: {expected}')
            seen[entry['Hashes']['MD5'].lower()].add(r['split'])
        if any(len(splits)>1 for splits in seen.values()): raise ValueError('Identical Google Drive video content appears across splits; review before transfer')
    for i,r in enumerate(rows,1):
        src=safe_path(repo,r['source_annotation']); ann=safe_path(dest,r['annotation_path']); video=safe_path(dest,r['video_path'])
        if r.get('annotation_source_bytes') is not None:
            current_digest=validate_source_annotation(src,r,tags)
        else:
            current_digest=hash_file(src)
        if r['annotation_sha256'] and current_digest!=r['annotation_sha256']:
            raise ValueError(f'Annotation changed since preview: {src}')
        r['annotation_sha256']=current_digest
        if local:
            original=local/(r['clip_id']+'.mp4'); digest=hash_file(original); copy_verified(original,video,digest)
        else:
            entry=index.get(r['drive_id']); expected=r['clip_id']+'.mp4'
            if not entry or entry['Name']!=expected or not entry.get('Hashes',{}).get('MD5'):
                raise ValueError(f'Google Drive identity or MD5 unavailable: {expected}')
            md5=entry['Hashes']['MD5'].lower()
            if not video.exists():
                video.parent.mkdir(parents=True,exist_ok=True); temp=video.with_name(video.name+'.partial')
                run('rclone','copyto',remote.rstrip('/')+'/'+entry['Path'],str(temp),'--ignore-times')
                if temp.stat().st_size!=entry['Size'] or hash_file(temp,'md5')!=md5: raise ValueError(f'Drive download mismatch: {expected}')
                temp.replace(video)
            if video.stat().st_size!=entry['Size'] or hash_file(video,'md5')!=md5: raise ValueError(f'Existing video conflict: {video}')
            digest=hash_file(video)
        copy_verified(src,ann,r['annotation_sha256']); r['video_sha256']=digest; r['video_bytes']=video.stat().st_size
        if i%100==0 or i==len(rows): print(f'Copied/verified {i}/{len(rows)} pairs',flush=True)
    return rows


def verify(dest, rows):
    expected=set(); digests=defaultdict(set)
    unique(rows,lambda r:r['clip_id'])
    for r in rows:
        if r['split'] not in ('train','test'): raise ValueError('Invalid split')
        if r['video_path'] != f"{r['split']}/{r['play_type']}/videos/{r['clip_id']}.mp4" or r['annotation_path'] != f"{r['split']}/{r['play_type']}/annotations/{r['clip_id']}.json": raise ValueError('Invalid destination assignment')
        digests[r['video_sha256']].add(r['split'])
        for key,digest in [('video_path','video_sha256'),('annotation_path','annotation_sha256')]:
            p=safe_path(dest,r[key]); expected.add(p)
            if not r[digest] or not p.is_file() or hash_file(p)!=r[digest]: raise ValueError(f'Verification failed: {p}')
    if any(len(splits)>1 for splits in digests.values()): raise ValueError('Identical video content appears across splits; review before release')
    actual={p for split in ('train','test') for p in (dest/split).rglob('*') if p.is_file() and not p.name.startswith('.')}
    if actual!=expected: raise ValueError(f'Unexpected files: {actual-expected}')
    print(f'Verified {len(rows)} video/annotation pairs locally; OneDrive cloud sync must be checked separately.')


def main():
    p=argparse.ArgumentParser(description=__doc__); mode=p.add_mutually_exclusive_group(required=True)
    for flag in ('preview','copy','verify'): mode.add_argument('--'+flag,action='store_true')
    p.add_argument('--repo',type=Path,default=Path.cwd()); p.add_argument('--annotations',type=Path,default=Path('data/dataset_inventory/Annotation_File_Inventory.csv')); p.add_argument('--videos',type=Path,default=Path('data/dataset_inventory/Videos_Inventory_GoogleDrive.csv')); p.add_argument('--plan',type=Path,default=Path('dataset_plan.json')); p.add_argument('--destination',type=Path); p.add_argument('--drive-remote'); p.add_argument('--local-videos',type=Path); p.add_argument('--boundary',action='append',default=[],metavar='PLAY=TRAIN_COUNT'); p.add_argument('--approve-boundaries',action='store_true'); a=p.parse_args()
    if a.preview:
        overrides={k:int(v) for k,v in (s.split('=',1) for s in a.boundary)}
        if a.plan.exists(): p.error('Plan already exists; choose a new --plan filename')
        rows,boundaries,summary=plan(a.repo,a.annotations,a.videos,overrides,fast=True)
        if not rows: p.error('No eligible clips')
        commit=run('git','-C',str(a.repo),'rev-parse','HEAD').strip()
        payload=dict(rows=rows,boundaries=boundaries,summary=summary,commit=commit)
        with a.plan.open('x') as f: json.dump(payload,f,indent=2)
        for b in boundaries: print(f"{b['play_type']:24} {b['train']:4} / {b['test']:4} | {b['left']} -> {b['right']}")
        print(json.dumps({k:v for k,v in summary.items() if k!='held'},indent=2)); print('Held clips:',len(summary['held']), 'Plan:',a.plan); print('Hold reasons:',dict(Counter(summary['held'].values()))); print('Training:',sum(b['train'] for b in boundaries),'Testing:',sum(b['test'] for b in boundaries))
        print('FAST INVENTORY PREVIEW: annotation JSONs, local annotation existence and validation reports were NOT read. Content validation and SHA-256 are deferred to --copy.')
        print('Review every boundary, especially unknown views; rerun with --boundary PLAY=TRAIN_COUNT if needed. Preview counts are provisional.')
    elif a.verify:
        if not a.destination: p.error('--destination required')
        verify(a.destination,read_csv(a.destination/'dataset_manifest.csv'))
    else:
        if not a.destination or not a.approve_boundaries or bool(a.drive_remote)==bool(a.local_videos): p.error('Copy requires destination, explicit boundary approval and exactly one video source')
        payload=json.loads(a.plan.read_text()); rows=payload['rows']
        if not rows: p.error('Plan is empty')
        if run('git','-C',str(a.repo),'rev-parse','HEAD').strip()!=payload['commit']: p.error('Repository HEAD changed; regenerate and review preview')
        # Refuse a changed split when resuming a version.
        saved=a.destination/'dataset_manifest.csv'
        if saved.exists():
            old=read_csv(saved)
            identity_fields=[k for k in FIELDS if k not in ('video_sha256','video_bytes','annotation_sha256')]
            if [tuple(r[k] for k in identity_fields) for r in old]!=[tuple(str(r[k]) for k in identity_fields) for r in rows]:
                raise ValueError('Existing dataset has different assignments')
            # Restore verified digests when resuming a partially copied version.
            for r,previous in zip(rows,old):
                if previous['annotation_sha256']:
                    r['annotation_sha256']=previous['annotation_sha256']
        else:
            if a.destination.exists() and any(a.destination.iterdir()): raise ValueError('Destination is not empty and has no saved manifest')
            if a.destination.resolve().is_relative_to(a.repo.resolve()) or a.repo.resolve().is_relative_to(a.destination.resolve()): raise ValueError('Destination overlaps repository')
            if a.local_videos and (a.destination.resolve().is_relative_to(a.local_videos.resolve()) or a.local_videos.resolve().is_relative_to(a.destination.resolve())): raise ValueError('Destination overlaps videos')
            a.destination.mkdir(parents=True,exist_ok=True); write_csv(saved,rows)
        rows=copy_dataset(a.repo,rows,a.destination,a.drive_remote,a.local_videos); verify(a.destination,rows)
        write_csv(saved,rows)
        counts=Counter((r['play_type'],r['split']) for r in rows)
        lines=['# TapeVision dataset v1.0','','Sequential numeric-ID 60/40 target per canonical play type. Known adjacent source-camera pairs protected; all boundaries manually reviewed. Nonadjacent duplicates and missing metadata may still cause leakage.','',f"Annotation repository commit: `{payload['commit']}`",'',f"Eligible: {len(rows)}; held: {len(payload['summary']['held'])}; training: {sum(r['split']=='train' for r in rows)}; testing: {sum(r['split']=='test' for r in rows)}.",'','| Play | Train | Test |','|---|---:|---:|']
        for label in sorted({r['play_type'] for r in rows}): lines.append(f'| {label} | {counts[label,"train"]} | {counts[label,"test"]} |')
        lines+=['','Videos and renamed annotation JSON files are copied, not moved. Paths and SHA-256 hashes are in dataset_manifest.csv. Fast preview did not inspect annotation contents; each source JSON and available validation report was checked during copying. Missing validation reports may be included if approved. Local verification does not certify cloud synchronization.']
        (a.destination/'README.md').write_text('\n'.join(lines)+'\n')


if __name__=='__main__': main()
