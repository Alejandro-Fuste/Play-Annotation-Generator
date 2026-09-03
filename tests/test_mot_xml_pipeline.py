import os
import tempfile
import unittest
import xml.etree.ElementTree as ET

from play_annotation_generator.config import DEFAULT_CONFIG
from play_annotation_generator.mot_parser import parse_mot_gt, parse_mot_labels
from play_annotation_generator.player_track_sheet_parser import parse_player_track_csv
from play_annotation_generator.sheet_group_resolver import resolve_group_targets
from play_annotation_generator.cvat_xml_generator import generate_base_cvat_xml
from play_annotation_generator.pipeline_generate_and_enrich import run_generate_and_enrich_pipeline
from play_annotation_generator.models import Track

MOCK_GT = """1,1,100.0,200.0,50.0,80.0,1,1,0.9
1,2,150.0,250.0,40.0,60.0,1,2,0.8
2,1,102.0,201.0,50.0,80.0,1,1,0.95
2,2,151.0,251.0,40.0,60.0,1,2,0.85
"""

MOCK_LABELS = """player
ball
"""

MOCK_PLAYER_TRACK_CSV = """video_name,video_id,team_side,assignments,notes
TestPlay,1,offense,"QB,1;LG,3",
TestPlay,1,defense,"FS,2",
"""

MOCK_KEY_ACTIONS_CSV = """video_name,video_id,play_tag,result_tag,result_frame,pre_snap,jet_motion,ball_snap,zone_block,snap_receive,toss,ball_carry,seal_block,lead_block,block_second_level,end_ol_block,end_play,notes
TestPlay,1,Play_Run_JetSweep,Result_Tackle,10,"0,ALL_OFFENSE",,,,,,,,,,10,
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

class TestMOTXMLPipeline(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        
        self.gt_file = os.path.join(self.temp_dir.name, "gt.txt")
        with open(self.gt_file, "w") as f:
            f.write(MOCK_GT)
            
        self.labels_file = os.path.join(self.temp_dir.name, "labels.txt")
        with open(self.labels_file, "w") as f:
            f.write(MOCK_LABELS)
            
        self.player_track_file = os.path.join(self.temp_dir.name, "player_tracks.csv")
        with open(self.player_track_file, "w") as f:
            f.write(MOCK_PLAYER_TRACK_CSV)
            
        self.key_actions_file = os.path.join(self.temp_dir.name, "key_actions.csv")
        with open(self.key_actions_file, "w") as f:
            f.write(MOCK_KEY_ACTIONS_CSV)
            
        self.template_file = os.path.join(self.temp_dir.name, "template.xml")
        with open(self.template_file, "w") as f:
            f.write(MOCK_TEMPLATE_XML)
            
        self.config = DEFAULT_CONFIG.copy()
        
    def tearDown(self):
        self.temp_dir.cleanup()
        
    def test_mot_row_parsing(self):
        labels = parse_mot_labels(self.labels_file)
        self.assertEqual(labels, ["player", "ball"])
        
        tracks = parse_mot_gt(self.gt_file, labels, self.config)
        self.assertIn(1, tracks)
        self.assertIn(2, tracks)
        
        # Check frame-offset logic (MOT 1-indexed to CVAT 0-indexed)
        # MOT frame 1 -> CVAT frame 0
        self.assertEqual(tracks[1].boxes[0].frame, 0)
        self.assertEqual(tracks[1].boxes[1].frame, 1)
        self.assertEqual(tracks[1].label, "player")
        self.assertEqual(tracks[2].label, "ball")
        
        # Check xywh -> xyxy conversion
        # MOT row 1: bb_left=100.0, bb_top=200.0, bb_width=50.0, bb_height=80.0
        # CVAT box: xtl=100.0, ytl=200.0, xbr=150.0, ybr=280.0
        self.assertEqual(tracks[1].boxes[0].xtl, 100.0)
        self.assertEqual(tracks[1].boxes[0].ytl, 200.0)
        self.assertEqual(tracks[1].boxes[0].xbr, 150.0)
        self.assertEqual(tracks[1].boxes[0].ybr, 280.0)
        
    def test_player_track_sheet_parsing(self):
        assignments, warnings = parse_player_track_csv(
            self.player_track_file,
            target_video_name="TestPlay",
            target_video_id="1"
        )
        self.assertEqual(len(warnings), 0)
        self.assertIn("1", assignments)
        self.assertIn("2", assignments)
        self.assertEqual(assignments["1"].position, "QB")
        self.assertEqual(assignments["1"].team_side, "offense")
        self.assertEqual(assignments["2"].position, "FS")
        self.assertEqual(assignments["2"].team_side, "defense")
        
    def test_group_expansion(self):
        tracks = {
            "0": Track(xml_track_id="0", label="player", source="file", position="QB", team_side="offense", custom_track_id="1"),
            "1": Track(xml_track_id="1", label="player", source="file", position="FS", team_side="defense", custom_track_id="2"),
        }
        
        # Test ALL_OFFENSE expansion
        offense_tracks = resolve_group_targets("ALL_OFFENSE", tracks, self.config)
        self.assertEqual(len(offense_tracks), 1)
        self.assertEqual(offense_tracks[0].custom_track_id, "1")
        
        # Test ALL_DEFENSE expansion
        defense_tracks = resolve_group_targets("ALL_DEFENSE", tracks, self.config)
        self.assertEqual(len(defense_tracks), 1)
        self.assertEqual(defense_tracks[0].custom_track_id, "2")
        
        # Test position expansion
        qb_tracks = resolve_group_targets("QB", tracks, self.config)
        self.assertEqual(len(qb_tracks), 1)
        self.assertEqual(qb_tracks[0].custom_track_id, "1")
        
    def test_base_xml_generation(self):
        labels = parse_mot_labels(self.labels_file)
        mot_tracks = parse_mot_gt(self.gt_file, labels, self.config)
        assignments, _ = parse_player_track_csv(self.player_track_file, "TestPlay", "1")
        
        output_xml = os.path.join(self.temp_dir.name, "generated_base.xml")
        count = generate_base_cvat_xml(self.template_file, output_xml, mot_tracks, assignments, self.config)
        self.assertEqual(count, 2)
        self.assertTrue(os.path.exists(output_xml))
        
        # Verify XML contents
        tree = ET.parse(output_xml)
        root = tree.getroot()
        tracks = root.findall("track")
        self.assertEqual(len(tracks), 2)
        
        # Track 0 (player) checks
        t0 = [t for t in tracks if t.attrib["label"] == "player"][0]
        self.assertEqual(t0.attrib["source"], "file")
        boxes0 = t0.findall("box")
        # active frames 0 and 1, plus outside box at frame 2
        self.assertEqual(len(boxes0), 3)
        self.assertEqual(boxes0[0].attrib["outside"], "0")
        self.assertEqual(boxes0[1].attrib["outside"], "0")
        self.assertEqual(boxes0[2].attrib["outside"], "1")
        self.assertEqual(boxes0[2].attrib["frame"], "2")
        
        # Track 1 (ball) checks
        t1 = [t for t in tracks if t.attrib["label"] == "ball"][0]
        boxes1 = t1.findall("box")
        self.assertEqual(len(boxes1), 3)
        
    def test_end_to_end_generate_and_enrich_pipeline(self):
        output_dir = os.path.join(self.temp_dir.name, "outputs")
        
        (
            tracks,
            metadata,
            events,
            segments,
            dense_annotations,
            metrics,
            warnings,
            errors
        ) = run_generate_and_enrich_pipeline(
            gt_path=self.gt_file,
            labels_path=self.labels_file,
            template_path=self.template_file,
            key_actions_csv=self.key_actions_file,
            player_tracks_csv=self.player_track_file,
            config=self.config,
            output_dir=output_dir,
            target_video_name="TestPlay",
            target_video_id="1"
        )
        
        self.assertEqual(len(errors), 0)
        self.assertTrue(os.path.exists(os.path.join(output_dir, "generated_base_cvat.xml")))
        
        # Player track ID 1 (QB) has pre_snap action at frame 0.
        # It expands ALL_OFFENSE to QB (since LG has no MOT boxes in MOCK_GT, only 1 and 2 exist in GT).
        # Wait, so the group resolver expands ALL_OFFENSE to only active player tracks present in generated XML.
        # In our XML generator, we generate tracks for tracks present in gt.txt (1 and 2).
        # Custom track ID 1 is player, custom track ID 2 is ball.
        # So offenses is only QB (custom track ID 1).
        # QB gets pre_snap event at frame 0, ending at play end frame 10.
        self.assertEqual(metrics["num_mot_tracks"], 2)
        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0].action, "Action_PreSnap")
        self.assertEqual(segments[0].start_frame, 0)
        self.assertEqual(segments[0].end_frame, 2) # Clamped to visible track range (includes outside="1" frame 2 as part of track bounds)
        
    def test_mot_zip_archive_parsing(self):
        import zipfile
        zip_path = os.path.join(self.temp_dir.name, "test_mot.zip")
        with zipfile.ZipFile(zip_path, "w") as z:
            z.writestr("gt/gt.txt", MOCK_GT)
            z.writestr("gt/labels.txt", MOCK_LABELS)
            
        labels = parse_mot_labels(zip_path)
        self.assertEqual(labels, ["player", "ball"])
        
        tracks = parse_mot_gt(zip_path, labels, self.config)
        self.assertIn(1, tracks)
        self.assertIn(2, tracks)
        self.assertEqual(tracks[1].boxes[0].xtl, 100.0)
        
if __name__ == "__main__":
    unittest.main()
