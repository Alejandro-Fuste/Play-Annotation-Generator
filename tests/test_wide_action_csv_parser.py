import os
import tempfile
import unittest
from tapevision_enricher.wide_action_csv_parser import parse_wide_action_csv, parse_cell_entries
from tapevision_enricher.config import DEFAULT_CONFIG

MOCK_CSV = """video_name,video_id,play_tag,result_tag,result_frame,pre_snap,jet_motion,ball_snap,zone_block,snap_receive,toss,ball_carry,seal_block,lead_block,block_second_level,end_ol_block,end_play,notes
JetSweep_69,69,Play_Run_JetSweep,Result_Tackle,116,"0,ALL_OFFENSE","33,16","34,33","43,OL","49,8","55,8","65,16",,"35,11","67,2","100,OL",116,"some notes"
OtherPlay_70,70,Play_Run_InsideZone,Result_FirstDown,80,"0,ALL_OFFENSE",,"10,12",,,,"15,22",,,,,,
"""

class TestWideActionCSVParser(unittest.TestCase):
    def setUp(self):
        self.temp_csv = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
        self.temp_csv.write(MOCK_CSV.encode("utf-8"))
        self.temp_csv.close()
        self.config = DEFAULT_CONFIG

    def tearDown(self):
        os.unlink(self.temp_csv.name)

    def test_parse_cell_entries(self):
        # Single entry
        res = parse_cell_entries("43,2")
        self.assertEqual(res, [(43, "2", None)])
        
        # Multi entry
        res = parse_cell_entries("43,2;43,4")
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], (43, "2", None))
        self.assertEqual(res[1], (43, "4", None))
        
        # Group target
        res = parse_cell_entries("0,ALL_OFFENSE")
        self.assertEqual(res, [(0, "ALL_OFFENSE", None)])
        
        # Global frame only event
        res = parse_cell_entries("116")
        self.assertEqual(res, [(116, None, None)])
        
        # Blank cell
        res = parse_cell_entries("")
        self.assertEqual(res, [])
        
        # Malformed
        res = parse_cell_entries("abc")
        self.assertEqual(len(res), 1)
        self.assertIsNotNone(res[0][2]) # Error message is populated

    def test_parse_wide_action_csv_all(self):
        # Parse without filtering
        events, all_rows, errors = parse_wide_action_csv(self.temp_csv.name, self.config, target_video=None)
        self.assertEqual(len(all_rows), 2)
        self.assertEqual(len(errors), 0)
        
        # Check some fields
        self.assertEqual(all_rows[0]["video_name"], "JetSweep_69")
        self.assertEqual(all_rows[1]["video_name"], "OtherPlay_70")

    def test_parse_wide_action_csv_filtered(self):
        # Filter by name
        events, _, errors = parse_wide_action_csv(self.temp_csv.name, self.config, target_video="JetSweep_69")
        self.assertEqual(len(errors), 0)
        self.assertTrue(len(events) > 0)
        
        # Check that we parsed the columns properly
        jet_motion_events = [e for e in events if e.action == "Action_JetMotion"]
        self.assertEqual(len(jet_motion_events), 1)
        self.assertEqual(jet_motion_events[0].start_frame, 33)
        self.assertEqual(jet_motion_events[0].actor_track_id, "16")
        
        # Check global events
        play_end_events = [e for e in events if e.action == "Action_PlayEnd"]
        self.assertEqual(len(play_end_events), 1)
        self.assertEqual(play_end_events[0].start_frame, 116)
        self.assertIsNone(play_end_events[0].actor_track_id)

if __name__ == "__main__":
    unittest.main()
