import json
import os
import tempfile
import unittest
from tapevision_enricher.reviewer import review_play_outputs, get_offense_position_rank, get_defense_position_rank


class TestReviewer(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.output_dir = self.test_dir.name

    def tearDown(self):
        self.test_dir.cleanup()

    def _create_mock_outputs(self, players, ball, segments, events_rows, warnings=None, errors=None):
        json_data = {
            "schema_version": "tapevision_annotation_enrichment_v1.0",
            "clip": {
                "video_name": "TestClip_1",
                "frame_start": 0,
                "frame_end": 100,
                "num_frames": 101
            },
            "play": {
                "play_tag": "Play_Pass",
                "result_tag": "Result_Complete",
                "result_frame": 100
            },
            "tracks": {
                "players": players,
                "ball": ball
            },
            "actions": {
                "segments": segments
            }
        }
        with open(os.path.join(self.output_dir, "tapevision_annotations.json"), "w", encoding="utf-8") as f:
            json.dump(json_data, f)

        val_data = {
            "warnings": warnings or [],
            "errors": errors or []
        }
        with open(os.path.join(self.output_dir, "validation_report.json"), "w", encoding="utf-8") as f:
            json.dump(val_data, f)

        if events_rows is not None:
            csv_path = os.path.join(self.output_dir, "normalized_action_events.csv")
            fieldnames = ["video_name", "video_id", "source_column", "action", "start_frame", "annotated_frame_role", "actor_track_id", "target_kind", "play_tag", "result_tag", "result_frame", "notes"]
            import csv
            with open(csv_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for r in events_rows:
                    writer.writerow(r)

    def test_offense_position_ranking(self):
        self.assertEqual(get_offense_position_rank("QB"), 0)
        self.assertEqual(get_offense_position_rank("RB"), 1)
        self.assertEqual(get_offense_position_rank("FB"), 2)
        self.assertEqual(get_offense_position_rank("H-BACK"), 3)
        self.assertEqual(get_offense_position_rank("WR-X"), 4)
        self.assertEqual(get_offense_position_rank("TE-Y"), 5)
        self.assertEqual(get_offense_position_rank("LT"), 6)
        self.assertEqual(get_offense_position_rank("LG"), 7)
        self.assertEqual(get_offense_position_rank("C"), 8)
        self.assertEqual(get_offense_position_rank("RG"), 9)
        self.assertEqual(get_offense_position_rank("RT"), 10)

        # Invalid/unrecognized offensive position must fall after recognized positions
        self.assertEqual(get_offense_position_rank("WLB"), 999)
        self.assertEqual(get_offense_position_rank("Position_Unknown"), 999)

    def test_defense_position_ranking(self):
        # 1. DL group
        self.assertEqual(get_defense_position_rank("DT"), 0)
        self.assertEqual(get_defense_position_rank("RDE"), 0)
        self.assertEqual(get_defense_position_rank("LDE"), 0)
        self.assertEqual(get_defense_position_rank("DT-3"), 0)

        # 2. LB group
        self.assertEqual(get_defense_position_rank("MLB"), 1)
        self.assertEqual(get_defense_position_rank("WLB"), 1)
        self.assertEqual(get_defense_position_rank("OLB"), 1)

        # 3. Safety group
        self.assertEqual(get_defense_position_rank("FS"), 2)
        self.assertEqual(get_defense_position_rank("SS"), 2)

        # 4. Corner group
        self.assertEqual(get_defense_position_rank("LCB"), 3)
        self.assertEqual(get_defense_position_rank("RCB"), 3)
        self.assertEqual(get_defense_position_rank("Nickel"), 3)

        # Unknown defensive position
        self.assertEqual(get_defense_position_rank("Position_Unknown"), 999)

    def test_split_action_tables_and_collapsible_audit(self):
        players = [
            {"xml_track_id": "1", "actor_track_id": "10", "position": "QB", "team_side": "offense", "samples": [{"frame": 0}, {"frame": 50}]}
        ]
        segments = [
            {"actor_track_id": "10", "xml_track_id": "1", "position": "QB", "team_side": "offense", "action": "Action_Pass", "start_frame": 10, "end_frame": 50, "source": "csv_rules"}
        ]
        events = [
            {"video_name": "TestClip_1", "video_id": "1", "source_column": "Pass", "action": "Action_Pass", "start_frame": "10", "actor_track_id": "10", "target_kind": "track_id"}
        ]
        self._create_mock_outputs(players, [], segments, events)

        report = review_play_outputs(self.output_dir)

        # Check section headings and collapsible blocks
        self.assertIn("# TapeVision Annotation Review — TestClip_1", report)
        self.assertIn("## 1. Clip & Validation Summary", report)
        self.assertIn("## 2. Action Annotation Audit", report)
        self.assertIn("<details>\n<summary><strong>Open Action Audit</strong></summary>", report)

        # Check split tables headings
        self.assertIn("### Player / Track Mapping", report)
        self.assertIn("### Timing Mapping", report)

        # Check exact headers
        self.assertIn("| Status | Action | Position | Team | actor_track_id | xml_track_id |", report)
        self.assertIn("| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |", report)

        # Verify Notes is not a Timing Mapping column
        timing_table_section = report.split("### Timing Mapping")[1].split("###")[0]
        self.assertNotIn("| Notes |", timing_table_section)
        self.assertNotIn("Notes", timing_table_section.split("\n")[2]) # Header line

    def test_offensive_and_defensive_ordering_in_report(self):
        # Scrambled offensive players including an invalid offensive position WLB
        players = [
            {"xml_track_id": "1", "actor_track_id": "8", "position": "RT", "team_side": "offense", "samples": [{"frame": 0}]},
            {"xml_track_id": "2", "actor_track_id": "14", "position": "QB", "team_side": "offense", "samples": [{"frame": 0}]},
            {"xml_track_id": "3", "actor_track_id": "4", "position": "WLB", "team_side": "offense", "samples": [{"frame": 0}]}, # Invalid position on offense
            {"xml_track_id": "4", "actor_track_id": "3", "position": "LG", "team_side": "offense", "samples": [{"frame": 0}]},
            {"xml_track_id": "5", "actor_track_id": "12", "position": "H-BACK", "team_side": "offense", "samples": [{"frame": 0}]}
        ]
        self._create_mock_outputs(players, [], [], [])

        report = review_play_outputs(self.output_dir)

        # Extract Offense section (between Offense summary and Defense summary)
        offense_section = report.split("<summary><strong>Offense</strong></summary>")[1].split("<summary><strong>Defense</strong></summary>")[0]

        qb_idx = offense_section.find("QB — actor_track_id `14`")
        hback_idx = offense_section.find("H-BACK — actor_track_id `12`")
        lg_idx = offense_section.find("LG — actor_track_id `3`")
        rt_idx = offense_section.find("RT — actor_track_id `8`")
        wlb_idx = offense_section.find("WLB — actor_track_id `4`")

        self.assertTrue(qb_idx < hback_idx < lg_idx < rt_idx < wlb_idx,
                        f"Expected ordering QB -> H-BACK -> LG -> RT -> WLB, got indices {qb_idx}, {hback_idx}, {lg_idx}, {rt_idx}, {wlb_idx}")

    def test_defensive_group_ordering(self):
        players = [
            {"xml_track_id": "1", "actor_track_id": "1", "position": "LCB", "team_side": "defense", "samples": [{"frame": 0}]},
            {"xml_track_id": "2", "actor_track_id": "2", "position": "FS", "team_side": "defense", "samples": [{"frame": 0}]},
            {"xml_track_id": "3", "actor_track_id": "3", "position": "MLB", "team_side": "defense", "samples": [{"frame": 0}]},
            {"xml_track_id": "4", "actor_track_id": "4", "position": "RDE", "team_side": "defense", "samples": [{"frame": 0}]}
        ]
        self._create_mock_outputs(players, [], [], [])

        report = review_play_outputs(self.output_dir)

        defense_section = report.split("<summary><strong>Defense</strong></summary>")[1].split("<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>")[0]

        rde_idx = defense_section.find("RDE — actor_track_id `4`")
        mlb_idx = defense_section.find("MLB — actor_track_id `3`")
        fs_idx = defense_section.find("FS — actor_track_id `2`")
        lcb_idx = defense_section.find("LCB — actor_track_id `1`")

        self.assertTrue(rde_idx < mlb_idx < fs_idx < lcb_idx,
                        f"Expected DL (RDE) -> LB (MLB) -> Safety (FS) -> Corner (LCB), got indices {rde_idx}, {mlb_idx}, {fs_idx}, {lcb_idx}")

    def test_collapsible_sections_and_warnings(self):
        players = [
            {"xml_track_id": "1", "actor_track_id": "0", "position": "Position_Unknown", "team_side": "Team_Unknown", "samples": [{"frame": 0}]}
        ]
        warnings = [
            "Player track '1' has undefined position. Will map to Position_Unknown.",
            "Action 'Action_PreSnap' range [0-10] for track '1' has 2 frames without a visible bounding box."
        ]
        self._create_mock_outputs(players, [], [], [], warnings=warnings)

        report = review_play_outputs(self.output_dir)

        self.assertIn("<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>", report)
        self.assertIn("### Validation Warnings by Category", report)
        self.assertIn("| Category | Count |", report)
        self.assertIn("<summary><strong>Detailed Validation Warnings</strong></summary>", report)
        self.assertIn("- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.", report)

    def test_start_changed_and_missing_segments_diagnostics(self):
        players = [
            {"xml_track_id": "1", "actor_track_id": "19", "position": "Position_Unknown", "team_side": "Team_Unknown", "samples": [{"frame": 0}]}
        ]
        segments = [
            {"actor_track_id": "19", "xml_track_id": "1", "position": "Position_Unknown", "team_side": "Team_Unknown", "action": "Action_JetMotion", "start_frame": 122, "end_frame": 159, "source": "csv_rules"}
        ]
        events = [
            {"video_name": "TestClip_1", "video_id": "1", "source_column": "Jet Motion", "action": "Action_JetMotion", "start_frame": "96", "actor_track_id": "19", "target_kind": "track_id"},
            {"video_name": "TestClip_1", "video_id": "1", "source_column": "Ball Carry", "action": "Action_BallCarry", "start_frame": "160", "actor_track_id": "19", "target_kind": "track_id"}
        ]
        self._create_mock_outputs(players, [], segments, events)

        report = review_play_outputs(self.output_dir)

        self.assertIn("⚠️ START CHANGED", report)
        self.assertIn("❌ MISSING SEGMENT", report)
        self.assertIn("### Action Mapping Issues", report)
        self.assertIn("Annotated start 96 != Inferred start 122", report)
        self.assertIn("Missing segment for action `Action_BallCarry`", report)

    def test_reviewer_cleanup_patch_classifications(self):
        players = [
            {"xml_track_id": "6", "actor_track_id": "7", "position": "C", "team_side": "offense", "samples": [{"frame": 133}]},
            {"xml_track_id": "12", "actor_track_id": "13", "position": "RT", "team_side": "offense", "samples": [{"frame": 133}]}
        ]
        segments = [
            {"actor_track_id": "7", "xml_track_id": "6", "position": "C", "team_side": "offense", "action": "Action_BallSnap", "start_frame": 132, "end_frame": 144, "source": "key_actions_csv_plus_temporal_rules"},
            {"actor_track_id": "7", "xml_track_id": "6", "position": "C", "team_side": "offense", "action": "Action_ZoneBlock", "start_frame": 145, "end_frame": 192, "source": "key_actions_csv_plus_temporal_rules"},
            {"actor_track_id": "13", "xml_track_id": "12", "position": "RT", "team_side": "offense", "action": "Action_BlockSecondLevel", "start_frame": 165, "end_frame": 192, "source": "key_actions_csv_plus_temporal_rules"},
            {"actor_track_id": "13", "xml_track_id": "12", "position": "RT", "team_side": "offense", "action": "Action_None", "start_frame": 193, "end_frame": 329, "source": "inferred_complete_timeline"}
        ]
        events = [
            {"video_name": "TestClip_1", "video_id": "1", "source_column": "Ball Snap", "action": "Action_BallSnap", "start_frame": "132", "actor_track_id": "7", "target_kind": "track_id", "annotated_frame_role": "START"},
            {"video_name": "TestClip_1", "video_id": "1", "source_column": "Zone Block", "action": "Action_ZoneBlock", "start_frame": "133", "actor_track_id": "7", "target_kind": "track_id", "annotated_frame_role": "START"},
            {"video_name": "TestClip_1", "video_id": "1", "source_column": "end_ol_block", "action": "Action_None", "start_frame": "192", "actor_track_id": "13", "target_kind": "track_id", "annotated_frame_role": "BOUNDARY"}
        ]
        self._create_mock_outputs(players, [], segments, events)

        report = review_play_outputs(self.output_dir)

        self.assertIn("PRIORITY_ADJUSTED", report)
        self.assertIn("BOUNDARY_TERMINATED", report)
        self.assertNotIn("AMBIGUOUS MATCH", report)
        self.assertIn("Inferred Coverage Segments (Action_None)", report)


if __name__ == "__main__":
    unittest.main()

