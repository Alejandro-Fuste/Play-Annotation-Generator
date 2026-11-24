"""Resumable rclone-based TapeVision remote transfers; never changes source files.

This module is invoked by consolidate_dataset.py. Remote verification downloads
uploaded content again and hashes it, so it is integrity-first, not bandwidth-first.
"""
import csv
import hashlib
import json
import os
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


def execute(*args):
    subprocess.run(args, check=True)


def output(*args):
    return subprocess.check_output(args, text=True)


def sha256_remote(remote_path):
    """Verify remote bytes, rather than trusting cloud checksum metadata."""
    digest = hashlib.sha256()
    proc = subprocess.Popen(['rclone', 'cat', remote_path], stdout=subprocess.PIPE)
    try:
        for chunk in iter(lambda: proc.stdout.read(1024 * 1024), b''):
            digest.update(chunk)
    finally:
        proc.stdout.close()
    if proc.wait() != 0:
        raise RuntimeError(f'Remote read failed: {remote_path}')
    return digest.hexdigest()


def remote_path(root, relative):
    from pathlib import PurePosixPath
    path = PurePosixPath(relative)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError(f'Unsafe remote path {relative!r}')
    if ':' not in root or root.startswith(':'):
        raise ValueError('Remote destination must be an rclone remote:folder path')
    root = root.rstrip('/')
    return root + ('' if root.endswith(':') else '/') + path.as_posix()


def verified_upload(local, destination, expected_sha):
    """Upload to temp name, verify remote SHA-256 and rename into final name.

    Repeated runs verify and reuse an existing final file; conflicts fail closed.
    """
    local = Path(local)
    if not local.is_file():
        raise ValueError(f'Missing source: {local}')
    import consolidate_dataset as base
    if base.hash_file(local) != expected_sha:
        raise ValueError(f'Local SHA-256 mismatch: {local}')
    # Rclone lsjson --stat exits nonzero for missing paths.
    probe = subprocess.run(['rclone', 'lsjson', destination, '--stat'], capture_output=True, text=True)
    if probe.returncode == 0:
        if sha256_remote(destination) != expected_sha:
            raise ValueError(f'Existing remote file conflicts: {destination}')
        return 'reused'
    # Do not interpret arbitrary remote/API failures as "missing".
    msg = (probe.stderr or '').lower()
    if not any(x in msg for x in ('not found', 'directory not found', 'object not found', 'does not exist', '404')):
        raise RuntimeError(f'Unable to check remote path {destination}: {probe.stderr.strip()}')
    staging = destination + '.tapevision-partial'
    execute('rclone', 'copyto', str(local), staging, '--retries', '3')
    try:
        if sha256_remote(staging) != expected_sha:
            raise ValueError(f'Remote upload hash mismatch: {staging}')
        execute('rclone', 'moveto', staging, destination)
    except Exception:
        # Leave .partial for debugging/retry; next copyto safely replaces it.
        raise
    return 'uploaded'


def transfer(repo, plan_path, dest_remote, source_remote, pilot_per_split=0, state_file=None):
    """Transfer approved plan to a remote destination, or isolated pilot subset."""
    import consolidate_dataset as base
    repo = Path(repo).resolve()
    plan_path = Path(plan_path).resolve()
    raw = plan_path.read_bytes()
    plan_digest = hashlib.sha256(raw).hexdigest()
    plan = json.loads(raw)
    all_rows = plan['rows']
    if not all_rows:
        raise ValueError('Empty plan')
    if len({r['clip_id'] for r in all_rows}) != len(all_rows):
        raise ValueError('Duplicate clip IDs in plan')
    if not plan.get('summary', {}).get('include_batch_failures'):
        raise ValueError('Plan does not explicitly include batch failures; check selected plan')
    if output('git', '-C', str(repo), 'rev-parse', 'HEAD').strip() != plan['commit']:
        raise ValueError('Repository HEAD changed since plan; regenerate approved plan or restore matching commit')
    if source_remote.rstrip('/') == dest_remote.rstrip('/'):
        raise ValueError('Source and destination remotes must differ')
    if pilot_per_split < 0:
        raise ValueError('Invalid pilot size')
    if pilot_per_split:
        selected=[]
        for partition in ('train', 'test'):
            candidates=[r for r in all_rows if r['split']==partition]
            if len(candidates)<pilot_per_split:
                raise ValueError(f'Not enough {partition} clips for pilot')
            selected.extend(candidates[:pilot_per_split])
    else:
        selected=list(all_rows)
    state_file = Path(state_file or (str(plan_path) + ('.pilot-state.json' if pilot_per_split else '.remote-state.json')))
    if state_file.exists():
        state=json.loads(state_file.read_text())
        if (state.get('plan_sha256'), state.get('remote'), state.get('source_remote'), state.get('pilot_per_split')) != (plan_digest, dest_remote, source_remote, pilot_per_split):
            raise ValueError('Transfer state belongs to a different plan, remote or pilot size')
    else:
        state={'plan_sha256':plan_digest, 'remote':dest_remote, 'source_remote':source_remote,
               'pilot_per_split':pilot_per_split, 'completed':{}}
    completed=state['completed']
    tags=set(json.loads((repo/'data/plays.json').read_text())['formattedPlayLabels'])
    # Get Google Drive's ID, size and MD5 once for identity assurance.
    index=base.remote_index(source_remote)
    splits_by_md5=defaultdict(set)
    for row in all_rows:
        entry=index.get(row['drive_id'])
        if (not entry or entry.get('Name') != row['clip_id']+'.mp4'
            or not entry.get('Hashes',{}).get('MD5') or int(entry.get('Size') or 0)<=0):
            raise ValueError('Source Drive identity, size or MD5 unavailable: '+row['clip_id'])
        splits_by_md5[entry['Hashes']['MD5'].lower()].add(row['split'])
    if any(len(s)>1 for s in splits_by_md5.values()):
        raise ValueError('Identical Google Drive videos cross train/test partitions')
    print(f"{'PILOT' if pilot_per_split else 'FULL'} transfer: {len(selected)} pairs to {dest_remote}",flush=True)
    def persist():
        tmp=state_file.with_name(state_file.name+'.partial')
        tmp.write_text(json.dumps(state,indent=2)+'\n')
        tmp.replace(state_file)
    for number, row in enumerate(selected, 1):
        clip=row['clip_id']; ann=base.safe_path(repo,row['source_annotation'])
        entry=index[row['drive_id']]
        ann_sha=base.validate_source_annotation(ann,row,tags,allow_report_errors=True)
        if row.get('annotation_sha256') and ann_sha!=row['annotation_sha256']:
            raise ValueError('Annotation changed since preview: '+clip)
        # Existing checkpoints are not trusted blindly: remote files are rehashed.
        ann_dest=remote_path(dest_remote,row['annotation_path'])
        video_dest=remote_path(dest_remote,row['video_path'])
        with tempfile.TemporaryDirectory(prefix='tapevision-transfer-') as tmpdir:
            temp_video=Path(tmpdir)/(clip+'.mp4')
            prev=completed.get(clip)
            if prev and (prev.get('annotation_sha256') != ann_sha or int(prev.get('video_bytes',0)) != entry['Size']):
                raise ValueError('Checkpoint does not match source: '+clip)
            if prev:
                # True resume: rehash both remote objects, but do not redownload
                # or reupload the source video from Google Drive.
                if sha256_remote(video_dest) != prev['video_sha256']:
                    raise ValueError('Previously completed remote video missing or changed: '+clip)
                if sha256_remote(ann_dest) != ann_sha:
                    raise ValueError('Previously completed remote annotation missing or changed: '+clip)
                vid_sha=prev['video_sha256']
            else:
                # Video is downloaded into temporary space one file at a time.
                source_file=remote_path(source_remote,entry['Path'])
                execute('rclone','copyto',source_file,str(temp_video),'--retries','3')
                if temp_video.stat().st_size!=entry['Size'] or base.hash_file(temp_video,'md5').lower()!=entry['Hashes']['MD5'].lower():
                    raise ValueError('Downloaded Google Drive video differs from inventory: '+clip)
                vid_sha=base.hash_file(temp_video)
                verified_upload(temp_video,video_dest,vid_sha)
                verified_upload(ann,ann_dest,ann_sha)
        completed[clip]={'video_sha256':vid_sha,'annotation_sha256':ann_sha,'video_bytes':entry['Size']}
        persist()
        print(f'Verified remote pair {number}/{len(selected)}: {clip}',flush=True)
    # Do not publish a full-dataset manifest before every file is validated.
    completed_rows=[]
    for r in selected:
        new=dict(r)
        new.update(completed[r['clip_id']]); completed_rows.append(new)
    with tempfile.TemporaryDirectory(prefix='tapevision-manifest-') as tmpdir:
        manifest=Path(tmpdir)/'dataset_manifest.csv'
        base.write_csv(manifest, completed_rows)
        lines=['# TapeVision dataset v1.0', '',
          'PILOT ONLY — not a full v1.0 dataset.' if pilot_per_split else 'Approved complete v1.0 dataset.',
          '',f'Video/annotation pairs: {len(selected)}.',
          f"Train: {sum(r['split']=='train' for r in selected)}; Test: {sum(r['split']=='test' for r in selected)}.",
          'Sequential numeric-ID 60/40 per play type (full approved plan).',
          'Source files were copied, not moved. Batch FAILED annotations were included intentionally.',
          'Each remote upload was read back and SHA-256 verified. Source Google Drive MD5s were checked.',
          'See dataset_manifest.csv for individual clip checksums and batch status.']
        readme=Path(tmpdir)/'README.md';readme.write_text('\n'.join(lines)+'\n')
        verified_upload(manifest,remote_path(dest_remote,'dataset_manifest.csv'),base.hash_file(manifest))
        verified_upload(readme,remote_path(dest_remote,'README.md'),base.hash_file(readme))
    counts=Counter(r['split'] for r in selected)
    print(f"Remote transfer complete: {len(selected)} pairs ({counts['train']} train, {counts['test']} test).",flush=True)
    print('Checkpoint:',state_file,flush=True)
