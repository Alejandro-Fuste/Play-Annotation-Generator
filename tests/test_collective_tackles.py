import csv
import json
import os
import tempfile
import unittest

from play_annotation_generator.action_event_normalizer import normalize_and_match_events
from play_annotation_generator.models import ActionEvent, Track
from play_annotation_generator.validators import run_validation_checks
from play_annotation_generator.wide_action_csv_parser import parse_wide_action_csv
from play_annotation_generator.writers.play_annotation_json_writer import write_play_annotation_json
from play_annotation_generator.reviewer import review_play_outputs
from play_annotation_generator.config import DEFAULT_CONFIG


class CollectiveTackleTests(unittest.TestCase):
    def test_collective_tackle_is_not_expanded_or_assigned_to_track(self):
        tracks = {"1": Track(xml_track_id="1", label="player", source="manual",
                              custom_track_id="11", position="MLB", team_side="defense")}
        event = ActionEvent(action="Action_Tackle", start_frame=22, actor_track_id="group",
                            target_kind="collective_tackle", source_column="Tackle")
        resolved, errors = normalize_and_match_events([event], tracks, DEFAULT_CONFIG)
        self.assertFalse(errors)
        self.assertEqual(len(resolved), 1)
        self.assertEqual(resolved[0].target_kind, "collective_tackle")
        self.assertEqual(resolved[0].actor_track_id, "group")
        self.assertIsNone(resolved[0].resolved_xml_track_id)
        metrics, warnings, errors = run_validation_checks(
            tracks, resolved, [], {"start_frame": 0, "stop_frame": 40}, DEFAULT_CONFIG)
        self.assertFalse(errors)

    def test_json_preserves_sparse_and_dense_collective_event(self):
        tracks = {}
        events = [ActionEvent(action="Action_Tackle", start_frame=22, end_frame=24,
                              actor_track_id="group", target_kind="collective_tackle",
                              source_column="Tackle")]
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, "annotations.json")
            write_play_annotation_json(target, tracks,
                                       {"start_frame": 0, "stop_frame": 40,
                                        "video_name": "Test_1"}, [], [],
                                       DEFAULT_CONFIG, "input.xml", "actions.csv",
                                       events=events)
            with open(target, encoding="utf-8") as fh:
                actions = json.load(fh)["actions"]
            self.assertEqual(len(actions["collective_events"]), 1)
            self.assertEqual(actions["collective_events"][0]["actor_scope"], "collective")
            self.assertIsNone(actions["collective_events"][0]["actor_track_id"])
            self.assertEqual([e["frame"] for e in actions["collective_dense_frame_annotations"]],
                             [22, 23, 24])
            self.assertEqual(actions["segments"], [])
            self.assertEqual(actions["dense_frame_annotations"], [])

    def test_reviewer_reports_collective_event_as_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            data = {"clip": {"video_name": "Test_1", "frame_start": 0, "frame_end": 40},
                    "play": {"play_tag": "Test", "result_tag": "Tackle"},
                    "tracks": {"players": [], "ball": []},
                    "actions": {"segments": [], "collective_events": [
                        {"action": "Action_Tackle", "start_frame": 22, "actor_scope": "collective"}
                    ]}}
            with open(os.path.join(tmp, "annotations.json"), "w", encoding="utf-8") as fh:
                json.dump(data, fh)
            with open(os.path.join(tmp, "validation_report.json"), "w", encoding="utf-8") as fh:
                json.dump({"warnings": [], "errors": []}, fh)
            with open(os.path.join(tmp, "normalized_action_events.csv"), "w",
                      newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=[
                    "action", "actor_track_id", "target_kind", "start_frame",
                    "annotated_frame_role", "source_column"])
                w.writeheader()
                w.writerow({"action": "Action_Tackle", "actor_track_id": "group",
                            "target_kind": "collective_tackle", "start_frame": 22,
                            "annotated_frame_role": "START", "source_column": "Tackle"})
            report = review_play_outputs(tmp)
            self.assertIn("COLLECTIVE TACKLE", report)
            self.assertNotIn("GROUP_EXPANDED", report)


if __name__ == "__main__":
    unittest.main()
