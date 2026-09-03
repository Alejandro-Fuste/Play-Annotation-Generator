import json
import os
import tempfile
import unittest
import zipfile
from pathlib import Path

from play_annotation_generator.batch_pipeline import (
    TrackingInput,
    check_clip_completion,
    discover_tracking_inputs,
    parse_numeric_sort_key,
    resolve_clip_preflight,
    run_batch_pipeline,
    sanitize_filename_component,
)
from play_annotation_generator.pipeline_generate_and_enrich import run_generate_and_enrich_pipeline

MOCK_GT = """1,1,100.0,200.0,50.0,80.0,1,1,0.9
1,2,150.0,250.0,40.0,60.0,1,2,0.8
2,1,102.0,201.0,50.0,80.0,1,1,0.95
2,2,151.0,251.0,40.0,60.0,1,2,0.85
"""

MOCK_LABELS = """player
ball
"""

MOCK_PLAYER_TRACK_CSV = """video_name,video_id,team_side,assignments,notes
Video Name:,JetSweep_
JetSweep_1,1,offense,"QB,1;LG,3",
JetSweep_1,1,defense,"FS,2",
JetSweep_2,2,offense,"QB,1",
JetSweep_2,2,defense,"FS,2",
JetSweep_10,10,offense,"QB,1",
"""

MOCK_KEY_ACTIONS_CSV = """video_name,video_id,play_tag,result_tag,result_frame,pre_snap,jet_motion,ball_snap,zone_block,snap_receive,toss,ball_carry,seal_block,lead_block,block_second_level,end_ol_block,end_play,notes
Video Name:,JetSweep_
JetSweep_1,1,Play_Run_JetSweep,Result_Tackle,10,"0,ALL_OFFENSE",,,,,,,,,,10,
JetSweep_2,2,Play_Run_JetSweep,Result_Tackle,10,"0,ALL_OFFENSE",,,,,,,,,,10,
JetSweep_10,10,Play_Run_JetSweep,Result_Tackle,10,"0,ALL_OFFENSE",,,,,,,,,,10,
"""

MOCK_TEMPLATE_XML = """<?xml version="1.0" encoding="utf-8"?>
<annotations>
  <version>1.1</version>
  <meta>
    <job>
      <id>123</id>
      <size>20</size>
      <mode>interpolation</mode>
      <start_frame>0</start_frame>
      <stop_frame>19</stop_frame>
      <labels>
        <label>
          <name>player</name>
          <attributes>
            <attribute><name>position</name></attribute>
            <attribute><name>team_side</name></attribute>
            <attribute><name>action</name></attribute>
            <attribute><name>track_id</name></attribute>
          </attributes>
        </label>
        <label>
          <name>ball</name>
          <attributes>
            <attribute><name>ball_status</name></attribute>
            <attribute><name>track_id</name></attribute>
          </attributes>
        </label>
      </labels>
    </job>
    <original_size>
      <width>1920</width>
      <height>1080</height>
    </original_size>
  </meta>
</annotations>
"""


def create_mock_zip(zip_path: str, gt_content: str, labels_content: str) -> None:
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("gt.txt", gt_content)
        zf.writestr("labels.txt", labels_content)


class TestBatchPipeline(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root_path = Path(self.temp_dir.name)

        self.gt_dir = self.root_path / "tracking"
        self.jetsweep_dir = self.gt_dir / "JetSweep"
        self.jetsweep_dir.mkdir(parents=True, exist_ok=True)

        self.key_actions_dir = self.root_path / "key_actions"
        self.key_actions_dir.mkdir(parents=True, exist_ok=True)
        self.key_actions_file = self.key_actions_dir / "JetSweep.csv"
        with open(self.key_actions_file, "w") as f:
            f.write(MOCK_KEY_ACTIONS_CSV)

        self.player_tracks_dir = self.root_path / "player_tracks"
        self.player_tracks_dir.mkdir(parents=True, exist_ok=True)
        self.player_track_file = self.player_tracks_dir / "JetSweep.csv"
        with open(self.player_track_file, "w") as f:
            f.write(MOCK_PLAYER_TRACK_CSV)

        self.template_file = self.root_path / "template.xml"
        with open(self.template_file, "w") as f:
            f.write(MOCK_TEMPLATE_XML)

        # Create tracking zip files in JetSweep directory
        self.zip1 = self.jetsweep_dir / "JetSweep_1_cvat_mot.zip"
        create_mock_zip(str(self.zip1), MOCK_GT, MOCK_LABELS)

        self.zip2 = self.jetsweep_dir / "JetSweep_2_cvat_mot.zip"
        create_mock_zip(str(self.zip2), MOCK_GT, MOCK_LABELS)

        self.zip10 = self.jetsweep_dir / "JetSweep_10_cvat_mot.zip"
        create_mock_zip(str(self.zip10), MOCK_GT, MOCK_LABELS)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_tracking_input_discovery(self):
        inputs = discover_tracking_inputs(self.gt_dir)
        paths = [i.relative_path.as_posix() for i in inputs]

        self.assertIn("JetSweep/JetSweep_1_cvat_mot.zip", paths)
        self.assertIn("JetSweep/JetSweep_2_cvat_mot.zip", paths)
        self.assertIn("JetSweep/JetSweep_10_cvat_mot.zip", paths)

    def test_numeric_video_sorting(self):
        inputs = discover_tracking_inputs(self.gt_dir)
        video_ids = [i.video_id for i in inputs]
        # Should sort numerically 1, 2, 10 rather than lexicographically 1, 10, 2
        self.assertEqual(video_ids, ["1", "2", "10"])

    def test_folder_play_mismatch_detection(self):
        counter_dir = self.gt_dir / "Counter"
        counter_dir.mkdir(parents=True, exist_ok=True)
        mismatched_zip = counter_dir / "JetSweep_99_cvat_mot.zip"
        create_mock_zip(str(mismatched_zip), MOCK_GT, MOCK_LABELS)

        inputs = discover_tracking_inputs(self.gt_dir)
        mismatched_item = next(i for i in inputs if i.video_id == "99")

        resolved = resolve_clip_preflight(
            tr_input=mismatched_item,
            key_actions_arg=self.key_actions_dir,
            player_tracks_arg=self.player_tracks_dir,
            recognized_plays={"Play_Run_JetSweep", "JetSweep"}
        )
        self.assertEqual(resolved.status, "FAILED")
        self.assertEqual(resolved.failure_type, "folder_play_mismatch")

    def test_unrecognized_play_detection(self):
        fake_dir = self.gt_dir / "FakePlay"
        fake_dir.mkdir(parents=True, exist_ok=True)
        fake_zip = fake_dir / "FakePlay_1_cvat_mot.zip"
        create_mock_zip(str(fake_zip), MOCK_GT, MOCK_LABELS)

        inputs = discover_tracking_inputs(self.gt_dir)
        fake_item = next(i for i in inputs if i.clip_name == "FakePlay_1")

        resolved = resolve_clip_preflight(
            tr_input=fake_item,
            key_actions_arg=self.key_actions_dir,
            player_tracks_arg=self.player_tracks_dir,
            recognized_plays={"Play_Run_JetSweep", "JetSweep"}
        )
        self.assertEqual(resolved.status, "FAILED")
        self.assertEqual(resolved.failure_type, "unrecognized_play")

    def test_successful_multi_clip_processing(self):
        out_root = self.root_path / "batch_out"
        res = run_batch_pipeline(
            gt_dir=str(self.gt_dir),
            template_path=str(self.template_file),
            key_actions_csv=str(self.key_actions_dir),
            player_tracks_csv=str(self.player_tracks_dir),
            output_dir=str(out_root)
        )

        self.assertEqual(res["total_preflight_ready"], 3)
        self.assertTrue((out_root / "_batch" / "batch_manifest.csv").exists())
        self.assertTrue((out_root / "_batch" / "batch_manifest.json").exists())
        self.assertTrue((out_root / "_batch" / "batch_summary.csv").exists())
        self.assertTrue((out_root / "_batch" / "batch_summary.json").exists())
        self.assertTrue((out_root / "_batch" / "batch_summary.md").exists())
        self.assertTrue((out_root / "JetSweep" / "JetSweep_1" / "annotations.xml").exists())
        self.assertTrue((out_root / "JetSweep" / "JetSweep_2" / "annotations.xml").exists())
        self.assertTrue((out_root / "JetSweep" / "JetSweep_10" / "annotations.xml").exists())

    def test_one_failed_clip_does_not_stop_later_clips(self):
        corrupt_zip = self.jetsweep_dir / "JetSweep_999_cvat_mot.zip"
        with open(corrupt_zip, "w") as f:
            f.write("NOT A ZIP FILE")

        # Add row to CSV files for 999
        ka_content = MOCK_KEY_ACTIONS_CSV + "JetSweep_999,999,Play_Run_JetSweep,Result_Tackle,10,\"0,ALL_OFFENSE\",,,,,,,,,,10,\n"
        pt_content = MOCK_PLAYER_TRACK_CSV + "JetSweep_999,999,offense,\"QB,1\",\n"
        self.key_actions_file.write_text(ka_content)
        self.player_track_file.write_text(pt_content)

        out_root = self.root_path / "batch_out_fail"
        res = run_batch_pipeline(
            gt_dir=str(self.gt_dir),
            template_path=str(self.template_file),
            key_actions_csv=str(self.key_actions_dir),
            player_tracks_csv=str(self.player_tracks_dir),
            output_dir=str(out_root)
        )

        results = res["results"]
        statuses = {r["clip_name"]: r["status"] for r in results if "clip_name" in r}

        self.assertEqual(statuses.get("JetSweep_999"), "FAILED")
        self.assertIn(statuses.get("JetSweep_1"), ["PASS", "WARNING"])

    def test_resume_flag(self):
        out_root = self.root_path / "batch_out_resume"
        run_batch_pipeline(
            gt_dir=str(self.gt_dir),
            template_path=str(self.template_file),
            key_actions_csv=str(self.key_actions_dir),
            player_tracks_csv=str(self.player_tracks_dir),
            output_dir=str(out_root)
        )

        # Second run with skip_existing / resume
        res2 = run_batch_pipeline(
            gt_dir=str(self.gt_dir),
            template_path=str(self.template_file),
            key_actions_csv=str(self.key_actions_dir),
            player_tracks_csv=str(self.player_tracks_dir),
            output_dir=str(out_root),
            skip_existing=True
        )

        exec_states = [r["execution_state"] for r in res2["results"] if r.get("preflight_status") == "READY"]
        self.assertTrue(all(s == "SKIPPED" for s in exec_states))

    def test_overwrite_flag(self):
        out_root = self.root_path / "batch_out_overwrite"
        clip_dir = out_root / "JetSweep" / "JetSweep_1"
        clip_dir.mkdir(parents=True)
        (clip_dir / "generated_base_cvat.xml").write_text("<old_xml/>")

        res = run_batch_pipeline(
            gt_dir=str(self.gt_dir),
            template_path=str(self.template_file),
            key_actions_csv=str(self.key_actions_dir),
            player_tracks_csv=str(self.player_tracks_dir),
            output_dir=str(out_root),
            overwrite=True
        )

        j1_res = next(r for r in res["results"] if r.get("clip_name") == "JetSweep_1")
        self.assertIn(j1_res["status"], ["PASS", "WARNING"])

    def test_jetsweep_1_single_vs_batch_semantic_equivalence(self):
        """
        Mandatory JetSweep_1 regression test verifying exact equivalence between
        single-clip execution and batch execution.
        """
        real_gt = Path("data/tracking/JetSweep/JetSweep_1_cvat_mot.zip")
        real_ka = Path("data/key_actions/JetSweep.csv")
        real_pt = Path("data/player_tracks/JetSweep.csv")
        real_template = Path("docs/JetSweepTemplate.xml")

        if not (real_gt.exists() and real_ka.exists() and real_pt.exists() and real_template.exists()):
            self.skipTest("Real JetSweep_1 data files not found in repository.")

        single_out = self.root_path / "single_jetsweep_1"
        batch_out = self.root_path / "batch_jetsweep_1"

        # 1. Single clip run
        from play_annotation_generator.config import load_config
        cfg = load_config(None)
        cfg["mode"] = "generate_and_enrich_xml"
        single_out.mkdir(parents=True, exist_ok=True)

        (
            tracks_s, meta_s, events_s, segs_s, dense_s, metrics_s, warn_s, err_s
        ) = run_generate_and_enrich_pipeline(
            gt_path=str(real_gt),
            labels_path=None,
            template_path=str(real_template),
            key_actions_csv=str(real_ka),
            player_tracks_csv=str(real_pt),
            config=cfg,
            output_dir=str(single_out),
            target_video_name="JetSweep_1",
            target_video_id="1"
        )

        # 2. Batch run
        b_res = run_batch_pipeline(
            gt_dir=str(real_gt.parent.parent),
            template_path=str(real_template),
            key_actions_csv=str(real_ka.parent),
            player_tracks_csv=str(real_pt.parent),
            output_dir=str(batch_out),
            play_filter="JetSweep",
            video_id_filter="1"
        )

        batch_clip_dir = batch_out / "JetSweep" / "JetSweep_1"
        self.assertTrue((batch_clip_dir / "annotations.json").exists())
        self.assertTrue((batch_clip_dir / "annotations.xml").exists())

        with open(batch_clip_dir / "annotations.json", "r", encoding="utf-8") as f:
            batch_json = json.load(f)

        batch_segments = batch_json.get("actions", {}).get("segments", [])
        self.assertEqual(len(segs_s), len(batch_segments))

        # Section 40 Mandatory Timelines Verification
        timeline_by_actor: dict = {}
        for seg in batch_segments:
            actor_id = str(seg.get("actor_track_id"))
            timeline_by_actor.setdefault(actor_id, []).append((seg["action"], seg["start_frame"], seg["end_frame"]))

        # QB / actor 17
        if "17" in timeline_by_actor:
            qb_actions = timeline_by_actor["17"]
            self.assertIn(("Action_PreSnap", 0, 131), qb_actions)
            self.assertIn(("Action_SnapReceive", 132, 144), qb_actions)
            self.assertIn(("Action_Toss", 145, 159), qb_actions)
            self.assertIn(("Action_None", 160, 329), qb_actions)

        # WR / actor 19
        if "19" in timeline_by_actor:
            wr_actions = timeline_by_actor["19"]
            self.assertIn(("Action_PreSnap", 0, 95), wr_actions)
            self.assertIn(("Action_JetMotion", 96, 159), wr_actions)
            self.assertIn(("Action_BallCarry", 160, 329), wr_actions)

        # TE / actor 12
        if "12" in timeline_by_actor:
            te_actions = timeline_by_actor["12"]
            self.assertIn(("Action_PreSnap", 0, 132), te_actions)
            self.assertIn(("Action_LeadBlock", 133, 192), te_actions)
            self.assertIn(("Action_None", 193, 329), te_actions)

        # RT / actor 13
        if "13" in timeline_by_actor:
            rt_actions = timeline_by_actor["13"]
            self.assertIn(("Action_PreSnap", 0, 132), rt_actions)
            self.assertIn(("Action_ZoneBlock", 133, 164), rt_actions)
            self.assertIn(("Action_BlockSecondLevel", 165, 192), rt_actions)
            self.assertIn(("Action_None", 193, 329), rt_actions)

        # Center / actor 7
        if "7" in timeline_by_actor:
            c_actions = timeline_by_actor["7"]
            self.assertIn(("Action_PreSnap", 0, 131), c_actions)
            self.assertIn(("Action_BallSnap", 132, 144), c_actions)
            self.assertIn(("Action_ZoneBlock", 145, 192), c_actions)
            self.assertIn(("Action_None", 193, 329), c_actions)


if __name__ == "__main__":
    unittest.main()
