import os
import tempfile
import unittest
from tapevision_enricher.enricher import run_enrichment_pipeline
from tapevision_enricher.config import DEFAULT_CONFIG

MOCK_XML = """<?xml version="1.0" encoding="utf-8"?>
<annotations>
  <version>1.1</version>
  <meta>
    <job>
      <id>123</id>
      <size>50</size>
      <mode>interpolation</mode>
      <start_frame>0</start_frame>
      <stop_frame>49</stop_frame>
    </job>
    <original_size>
      <width>1920</width>
      <height>1080</height>
    </original_size>
  </meta>
  <track id="0" label="player" source="manual">
    <box frame="0" keyframe="1" outside="0" occluded="0" xtl="100" ytl="200" xbr="150" ybr="300">
      <attribute name="position">QB</attribute>
      <attribute name="team_side">offense</attribute>
      <attribute name="track_id">8</attribute>
    </box>
    <box frame="10" keyframe="1" outside="0" occluded="0" xtl="105" ytl="205" xbr="155" ybr="305">
      <attribute name="position">QB</attribute>
      <attribute name="team_side">offense</attribute>
      <attribute name="track_id">8</attribute>
    </box>
    <box frame="20" keyframe="1" outside="0" occluded="0" xtl="110" ytl="210" xbr="160" ybr="310">
      <attribute name="position">QB</attribute>
      <attribute name="team_side">offense</attribute>
      <attribute name="track_id">8</attribute>
    </box>
  </track>
</annotations>
"""

MOCK_CSV = """video_name,video_id,play_tag,result_tag,result_frame,pre_snap,jet_motion,ball_snap,zone_block,snap_receive,toss,ball_carry,seal_block,lead_block,block_second_level,end_ol_block,end_play,notes
TestPlay,1,Play_Run_JetSweep,Result_Tackle,40,"0,8",,,,"10,8",,,,,,,,,
"""

class TestEnricherIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_xml = tempfile.NamedTemporaryFile(suffix=".xml", delete=False)
        self.temp_xml.write(MOCK_XML.encode("utf-8"))
        self.temp_xml.close()

        self.temp_csv = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
        self.temp_csv.write(MOCK_CSV.encode("utf-8"))
        self.temp_csv.close()

        self.config = DEFAULT_CONFIG.copy()

    def tearDown(self):
        os.unlink(self.temp_xml.name)
        os.unlink(self.temp_csv.name)

    def test_full_enrichment_pipeline(self):
        (
            tracks,
            metadata,
            events,
            segments,
            dense_annotations,
            metrics,
            warnings,
            errors
        ) = run_enrichment_pipeline(
            self.temp_xml.name,
            self.temp_csv.name,
            self.config,
            target_video="TestPlay"
        )
        
        self.assertEqual(len(errors), 0)
        self.assertEqual(metrics["num_player_tracks"], 1)
        self.assertEqual(metrics["num_events_parsed"], 2)
        self.assertEqual(len(segments), 3)
        
        # Verify play-level metadata extraction
        self.assertEqual(metadata["play_tag"], "Play_Run_JetSweep")
        self.assertEqual(metadata["result_tag"], "Result_Tackle")
        self.assertEqual(metadata["result_frame"], 49)
        
        # Segment 1: Action_PreSnap at frame 0
        # Segment 2: Action_SnapReceive at frame 10
        # Segment 3: Action_None at frame 20
        segments = sorted(segments, key=lambda s: s.start_frame)
        self.assertEqual(segments[0].action, "Action_PreSnap")
        self.assertEqual(segments[0].start_frame, 0)
        self.assertEqual(segments[0].end_frame, 0)
        
        self.assertEqual(segments[1].action, "Action_SnapReceive")
        self.assertEqual(segments[1].start_frame, 10)
        self.assertEqual(segments[1].end_frame, 10)

        self.assertEqual(segments[2].action, "Action_None")
        self.assertEqual(segments[2].start_frame, 20)
        self.assertEqual(segments[2].end_frame, 20)
        
        dense_ann_frames = [da.frame for da in dense_annotations]
        self.assertIn(0, dense_ann_frames)
        self.assertIn(10, dense_ann_frames)
        self.assertIn(20, dense_ann_frames)
        
        ann0 = [da for da in dense_annotations if da.frame == 0][0]
        self.assertEqual(ann0.action, "Action_PreSnap")
        
        ann10 = [da for da in dense_annotations if da.frame == 10][0]
        self.assertEqual(ann10.action, "Action_SnapReceive")
        
        ann20 = [da for da in dense_annotations if da.frame == 20][0]
        self.assertEqual(ann20.action, "Action_None")

if __name__ == "__main__":
    unittest.main()
