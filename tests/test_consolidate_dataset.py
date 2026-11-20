import csv
import importlib.util
import json
from pathlib import Path
import pytest

spec=importlib.util.spec_from_file_location('consolidate',Path(__file__).parents[1]/'scripts/consolidate_dataset.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def dump_csv(path, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

@pytest.fixture
def dataset(tmp_path):
    repo=tmp_path/'repo'; (repo/'data').mkdir(parents=True)
    (repo/'data/plays.json').write_text(json.dumps({'playLabels':['Counter','DeepCross'],'formattedPlayLabels':['Play_Run_Counter','Play_Pass_DeepCross']}))
    (repo/'data/rpo_excluded_video_ids.txt').write_text('# none\n')
    video_dir=tmp_path/'videos'; video_dir.mkdir()
    anns=[]; vids=[]; meta=[]
    for label,ids in [('Counter',[1,2,3,4,5,6,7,8,9,10,11,12]),('DeepCross',[1,2,10,11,12])]:
        for i in ids:
            clip=f'{label}_{i}'; view=('S' if i%2 else 'E') if label=='Counter' else 'S'
            path=repo/'outputs/batch'/label/label/clip/'annotations.json'; path.parent.mkdir(parents=True)
            path.write_text(json.dumps({'clip':{'video_name':clip},'play':{'play_tag':('Play_Run_' if label=='Counter' else 'Play_Pass_')+label},'tracks':{},'actions':{}}))
            path.with_name('validation_report.json').write_text(json.dumps({'errors':[], 'warnings':[]}))
            anns.append({'filename':'annotations.json','repository_path':str(path.relative_to(repo)),'file_size_bytes':path.stat().st_size}); vids.append({'File_Name':clip+'.mp4','File_ID':clip+'ID'})
            meta.append({'output_file':clip+'.mp4','view':view,'input_file':label+'.mp4','start_time':f'00:{i:02}:00','end_time':f'00:{i:02}:10'})
            (video_dir/(clip+'.mp4')).write_bytes(clip.encode())
    dump_csv(repo/'data/DatasetSummary.csv',meta)
    dump_csv(tmp_path/'annotations.csv',anns[::-1]); dump_csv(tmp_path/'videos.csv',vids[::-1])
    return repo,tmp_path/'annotations.csv',tmp_path/'videos.csv',video_dir,tmp_path/'dest'

def test_split_numeric_and_adjacent_pairs(dataset):
    repo,a,v,_,_=dataset
    rows,b,s=m.plan(repo,a,v)
    assert s['matched']==17 and s['eligible']==17
    assert [(x['play_type'],x['train'],x['test']) for x in b]==[('Counter',8,4),('DeepCross',3,2)]
    assert [r['clip_id'] for r in rows if r['play_type']=='DeepCross' and r['split']=='train']==['DeepCross_1','DeepCross_2','DeepCross_10']
    with pytest.raises(ValueError,match='Unsafe boundary'): m.plan(repo,a,v,{'Counter':7})

def test_failed_annotation_held(dataset):
    repo,a,v,_,_=dataset
    path=repo/'outputs/batch/Counter/_batch/batch_manifest.csv'
    dump_csv(path,[{'clip_name':'Counter_12','status':'FAILED','error_count':1}])
    rows,_,s=m.plan(repo,a,v)
    assert s['held']=={'Counter_12':'batch failure'} and len(rows)==16

def test_copy_resume_conflict_and_verify(dataset):
    repo,a,v,video,dest=dataset
    rows,_,_=m.plan(repo,a,v)
    m.copy_dataset(repo,rows,dest,local=video); m.verify(dest,rows)
    m.copy_dataset(repo,rows,dest,local=video); m.verify(dest,rows)
    assert len(list(video.glob('*.mp4')))==17
    p=dest/rows[0]['video_path']; p.write_bytes(b'corrupt')
    with pytest.raises(ValueError,match='Verification failed'): m.verify(dest,rows)
    with pytest.raises(ValueError,match='Destination conflict'): m.copy_dataset(repo,rows,dest,local=video)

def test_duplicate_content_across_splits(dataset):
    repo,a,v,video,dest=dataset
    rows,_,_=m.plan(repo,a,v)
    train=next(r for r in rows if r['split']=='train'); test=next(r for r in rows if r['split']=='test')
    (video/(test['clip_id']+'.mp4')).write_bytes((video/(train['clip_id']+'.mp4')).read_bytes())
    m.copy_dataset(repo,rows,dest,local=video)
    with pytest.raises(ValueError,match='Identical video content'): m.verify(dest,rows)

def test_changed_source_after_preview(dataset):
    repo,a,v,video,dest=dataset
    rows,_,_=m.plan(repo,a,v)
    (repo/rows[0]['source_annotation']).write_text('{}')
    with pytest.raises(ValueError,match='changed since preview'): m.copy_dataset(repo,rows,dest,local=video)

def test_unmatched_metadata_prevents_false_pair():
    rows=[dict(output_file=f'Counter_{i}.mp4',input_file='source',view=view,start_time=f'00:0{i}:00',end_time=f'00:0{i}:10') for i,view in [(1,'S'),(2,''),(3,'E')]]
    assert m.metadata_pairs(rows)==set()

def test_real_inventory_matching():
    # Optional real-input test; never needs cloud credentials.
    root=Path(__file__).parents[1]/'data/dataset_inventory'
    if not (root/'Annotation_File_Inventory.csv').exists(): pytest.skip('Inventories not installed')
    a=m.unique(m.read_csv(root/'Annotation_File_Inventory.csv'),lambda r:Path(r['repository_path']).parent.name)
    v=m.unique(m.read_csv(root/'Videos_Inventory_GoogleDrive.csv'),lambda r:Path(r['File_Name']).stem)
    assert len(a)==4075 and len(v)==5140 and len(a.keys()&v.keys())==4075

def test_cli_workflow(dataset,monkeypatch):
    import subprocess,sys
    repo,a,v,video,dest=dataset
    subprocess.run(['git','init','-q',str(repo)],check=True)
    subprocess.run(['git','-C',str(repo),'-c','user.name=Test','-c','user.email=test@example.org','commit','--allow-empty','-qm','fixture'],check=True)
    plan=repo/'plan.json'
    common=['consolidate','--repo',str(repo),'--plan',str(plan)]
    monkeypatch.setattr(sys,'argv',common+['--preview','--annotations',str(a),'--videos',str(v)])
    m.main(); assert plan.exists() and not dest.exists()
    copy_args=common+['--copy','--destination',str(dest),'--local-videos',str(video)]
    monkeypatch.setattr(sys,'argv',copy_args)
    with pytest.raises(SystemExit): m.main()
    assert not dest.exists()
    monkeypatch.setattr(sys,'argv',copy_args+['--approve-boundaries'])
    m.main(); assert (dest/'README.md').is_file()
    m.main() # same plan can be resumed
    monkeypatch.setattr(sys,'argv',common+['--verify','--destination',str(dest)])
    m.main()

def test_rclone_transfer_with_mocked_remote(dataset,monkeypatch):
    repo,a,v,video,dest=dataset
    rows,_,_=m.plan(repo,a,v)
    listing=[]
    for r in rows:
        p=video/(r['clip_id']+'.mp4')
        listing.append(dict(ID=r['drive_id'],Name=p.name,Path='clips/'+p.name,Size=p.stat().st_size,Hashes={'MD5':m.hash_file(p,'md5')}))
    def fake_run(*args):
        assert args[0]=='rclone'
        if args[1]=='lsjson': return json.dumps(listing)
        assert args[1]=='copyto' and args[2].startswith('gdrive:football/clips/')
        Path(args[3]).write_bytes((video/args[2].rsplit('/',1)[-1]).read_bytes())
        return ''
    monkeypatch.setattr(m,'run',fake_run)
    m.copy_dataset(repo,rows,dest,remote='gdrive:football'); m.verify(dest,rows)

def test_validation_error_held(dataset):
    repo,a,v,_,_=dataset
    p=repo/'outputs/batch/Counter/Counter/Counter_12/validation_report.json'
    p.write_text(json.dumps({'errors':['bad frame'],'warnings':[]}))
    rows,_,s=m.plan(repo,a,v)
    assert s['held']=={'Counter_12':'validation errors or unknown report schema'} and len(rows)==16
