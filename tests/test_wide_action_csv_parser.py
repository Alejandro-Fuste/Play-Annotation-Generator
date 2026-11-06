import os
import tempfile
import unittest
from play_annotation_generator.wide_action_csv_parser import parse_wide_action_csv, parse_cell_entries
from play_annotation_generator.config import DEFAULT_CONFIG

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
        
        # 3-part range entry (start_frame, end_frame, actor_track_id)
        res = parse_cell_entries("98,110,4")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0], (98, "4", None))
        self.assertEqual(res[0].end_frame, 110)

        # Blank cell
        res = parse_cell_entries("")
        self.assertEqual(res, [])
        
        # Malformed
        res = parse_cell_entries("abc")
        self.assertEqual(len(res), 1)
        self.assertIsNotNone(res[0][2]) # Error message is populated

    def test_unknown_actor_and_range_endpoint_are_not_valid_events(self):
        for cell in ("731,?", "731,??", "731,[?]", "570,?,24", "100,110,?", "50,18;?"):
            entries = parse_cell_entries(cell)
            self.assertTrue(any(error for _, _, error in entries), cell)
            self.assertFalse(all(error is None for _, _, error in entries), cell)
        self.assertEqual(parse_cell_entries("731,51"), [(731, "51", None)])
        valid = parse_cell_entries("570,596,24")
        self.assertEqual(valid[0].end_frame, 596)

    def test_parse_wide_action_csv_all(self):
        # Parse without filtering
        events, all_rows, errors = parse_wide_action_csv(self.temp_csv.name, self.config, target_video=None)
        self.assertEqual(len(all_rows), 2)
        self.assertEqual(len(errors), 0)
        
        # Check some fields
        self.assertEqual(all_rows[0]["video_name"], "JetSweep_69")
        self.assertEqual(all_rows[1]["video_name"], "OtherPlay_70")

    def test_stop_and_go_route_columns_are_mapped(self):
        stop_and_go_csv = """Video Name:,Stop and Go,,,,,,,,,,\n,"Key Actions (Frame Number, player track id)",,,,,,,,,,\nVideo #,Pre Snap,Ball Snap,Pass Block,Snap Receive,Pump Fake,Throw Pass,Vertical Stem,Sell Stop,Run Go Route,End of Play\n1,"0,ALL","20,18","23,OL","36,15","84,15","112,126,15","36,12","78,12","91,12",Rec\n"""
        tmp = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
        try:
            tmp.write(stop_and_go_csv.encode("utf-8"))
            tmp.close()

            events, _, errors = parse_wide_action_csv(
                tmp.name,
                self.config,
                target_video="1",
            )

            self.assertEqual(errors, [])
            by_action = {event.action: event for event in events}
            self.assertEqual(by_action["Action_VerticalStem"].start_frame, 36)
            self.assertEqual(by_action["Action_VerticalStem"].actor_track_id, "12")
            self.assertEqual(by_action["Action_SellStop"].start_frame, 78)
            self.assertEqual(by_action["Action_SellStop"].actor_track_id, "12")
            self.assertEqual(by_action["Action_RunGoRoute"].start_frame, 91)
            self.assertEqual(by_action["Action_RunGoRoute"].actor_track_id, "12")
        finally:
            if os.path.exists(tmp.name):
                os.unlink(tmp.name)

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
