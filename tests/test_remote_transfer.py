"""Remote transfer integration tests with a mock cloud (no credentials or network)."""
import csv
import hashlib
import importlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import consolidate_dataset as base
import remote_transfer as remote


def test_remote_path_rejects_traversal():
    import pytest
    assert remote.remote_path('onedrive:dataset','train/Counter/a.mp4')=='onedrive:dataset/train/Counter/a.mp4'
    with pytest.raises(ValueError): remote.remote_path('onedrive:dataset','../secret')


def test_pilot_transfer_and_resume_with_mocked_remotes(tmp_path,monkeypatch):
    repo=tmp_path/'repo'; (repo/'data').mkdir(parents=True)
    (repo/'data/plays.json').write_text(json.dumps({'formattedPlayLabels':['Play_Run_Counter']}))
    video_dir=tmp_path/'gdrive'; video_dir.mkdir()
    rows=[]; entries={}
    for i in range(1,7):
        clip=f'Counter_{i}'
        ann=repo/f'outputs/batch/Counter/Counter/{clip}/annotations.json'; ann.parent.mkdir(parents=True)
        ann.write_text(json.dumps({'clip':{'video_name':clip},'play':{'play_tag':'Play_Run_Counter'},'tracks':{},'actions':{}}))
        vid=video_dir/f'{clip}.mp4'; vid.write_bytes(f'video::{clip}'.encode())
        rows.append(dict(clip_id=clip,play_type='Counter',split='train' if i<=3 else 'test',
            source_annotation=str(ann.relative_to(repo)),annotation_source_bytes=ann.stat().st_size,
            annotation_sha256='',video_path=f"{'train' if i<=3 else 'test'}/Counter/videos/{clip}.mp4",
            annotation_path=f"{'train' if i<=3 else 'test'}/Counter/annotations/{clip}.json",
            drive_id=f'id{i}',view='S',batch_status='NOT_FAILED_BY_BATCH_MANIFEST'))
        entries[f'id{i}']={'ID':f'id{i}','Name':vid.name,'Path':vid.name,'Size':vid.stat().st_size,'Hashes':{'MD5':base.hash_file(vid,'md5')}}
    plan=tmp_path/'plan.json';plan.write_text(json.dumps({'rows':rows,'summary':{'include_batch_failures':True},'commit':'HEAD-FIXTURE'}))
    monkeypatch.setattr(remote,'output',lambda *a:'HEAD-FIXTURE\n')
    monkeypatch.setattr(base,'remote_index',lambda *a:entries)
    cloud=tmp_path/'onedrive';cloud.mkdir()
    def cloud_path(r):return cloud/r.removeprefix('onedrive:pilot/')
    transfer_actions=[]
    def fake_execute(*cmd):
        assert cmd[0]=='rclone'
        if cmd[1]=='copyto':
            src,dst=cmd[2],cmd[3]
            if src.startswith('gdrive:'):
                shutil.copyfile(video_dir/src.removeprefix('gdrive:').lstrip('/'),dst)
            else:
                assert dst.startswith('onedrive:pilot/')
                target=cloud_path(dst);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target)
        elif cmd[1]=='moveto':
            source=cloud_path(cmd[2]);target=cloud_path(cmd[3]);source.rename(target)
        else: raise AssertionError(cmd)
        transfer_actions.append(cmd)
    monkeypatch.setattr(remote,'execute',fake_execute)
    real_subprocess_run=subprocess.run
    def fake_probe(cmd,**kwargs):
        assert cmd[:2]==['rclone','lsjson']
        path=cloud_path(cmd[2])
        return subprocess.CompletedProcess(cmd,0 if path.exists() else 1,
                                           stdout='{}' if path.exists() else '',
                                           stderr='' if path.exists() else 'directory not found')
    monkeypatch.setattr(remote.subprocess,'run',fake_probe)
    monkeypatch.setattr(remote,'sha256_remote',lambda path:base.hash_file(cloud_path(path)))
    state=tmp_path/'state.json'
    remote.transfer(repo,plan,'onedrive:pilot','gdrive:',pilot_per_split=2,state_file=state)
    assert len(json.loads(state.read_text())['completed'])==4
    assert len(list(cloud.rglob('*.mp4')))==4
    assert len(list(cloud.rglob('*.json')))==4
    manifest=list(csv.DictReader((cloud/'dataset_manifest.csv').open()))
    assert len(manifest)==4
    assert {r['split'] for r in manifest}=={'train','test'}
    remote.transfer(repo,plan,'onedrive:pilot','gdrive:',pilot_per_split=2,state_file=state)
    assert len(list(cloud.rglob('*.mp4')))==4


def test_pilot_requires_isolated_destination():
    import pytest
    with pytest.raises(ValueError): remote.remote_path('missingremote','train/a.mp4')
