"""Focused regression tests for RPO blocking and batch exclusions."""
import copy
import json
import os
import tempfile
import unittest
from pathlib import Path

from play_annotation_generator.rpo_parser import (
    parse_rpo_run_block, load_rpo_excluded_ids, is_rpo_excluded,
)
from play_annotation_generator.config import DEFAULT_CONFIG
from play_annotation_generator.models import ActionEvent, Track, TrackBox
from play_annotation_generator.action_event_normalizer import normalize_and_match_events
from play_annotation_generator.action_rules import infer_action_segments
from play_annotation_generator.wide_action_csv_parser import (
    parse_rpo_route_descriptor, parse_wide_action_csv,
)
from play_annotation_generator.writers.play_annotation_json_writer import write_play_annotation_json
from play_annotation_generator.writers.batch_report_writer import (
    write_batch_manifest_csv, write_batch_summary_markdown,
)


class TestRpoBlocking(unittest.TestCase):
    def test_three_schemes_and_explicit_throw_endpoint(self):
        for code, scheme, action in [
            ("Z", "zone", "Action_ZoneBlock"),
            ("G", "gap", "Action_RunBlock"),
            ("P", "pass", "Action_PassBlock"),
        ]:
            with self.subTest(code=code):
                value, error = parse_rpo_run_block(f"88,{code},OL", "134,145,18")
                self.assertIsNone(error)
                self.assertEqual(value, {
                    "action": action, "blocking_scheme": scheme,
                    "start_frame": 88, "end_frame": 145,
                    "actor_group": "OL", "source_column": "Run Block",
                })

    def test_missing_reversed_and_out_of_order_endpoints_fail(self):
        cases = [
            ("88,G,OL", "-", "explicit Throw Pass"),
            ("88,Z,OL", "134,18", "explicit Throw Pass"),
            ("88,P,OL", "150,135,18", "reversed"),
            ("150,Z,OL", "134,145,18", "must precede"),
            ("-,G,OL", "134,145,18", "Invalid RPO"),
            ("81,10,OL", "134,145,18", "Invalid RPO"),
            ("88,X,OL", "134,145,18", "Invalid RPO"),
        ]
        for source, throw, reason in cases:
            with self.subTest(source=source, throw=throw):
                block, error = parse_rpo_run_block(source, throw)
                self.assertIsNone(block)
                self.assertIn(reason, error)

    def test_real_wide_csv_routes_only_rpo_to_special_parser(self):
        fixture = (
            "Video Name:,RPO\n"
            ",Key Actions\n"
            "Video #,Pre Snap,Run Block,Read Defender,Pull Ball,Throw Pass,Route,End of Play\n"
            '1,"0,ALL","88,G,OL","100,18","121,133,18","134,145,18","post,7",Tac\n'
        )
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "rpo.csv"
            path.write_text(fixture, encoding="utf-8")
            events, rows, errors = parse_wide_action_csv(
                str(path), copy.deepcopy(DEFAULT_CONFIG), target_video="RPO_1"
            )
        self.assertEqual(errors, [])
        block = [e for e in events if e.blocking_scheme == "gap"]
        self.assertEqual(len(block), 1)
        self.assertEqual((block[0].action, block[0].end_frame, block[0].actor_track_id),
                         ("Action_RunBlock", 145, "OL"))

    def test_group_expansion_and_dense_timeline_preserve_scheme(self):
        boxes = {f: TrackBox(
            frame=f, xtl=0, ytl=0, xbr=10, ybr=10,
            outside=False, occluded=False, keyframe=False
        ) for f in range(151)}
        positions = ["LT", "LG", "C", "RG", "RT"]
        tracks = {
            str(i): Track(xml_track_id=str(i), label="player", source="test",
                          custom_track_id=str(i), position=position,
                          team_side="offense", boxes_by_frame=boxes)
            for i, position in enumerate(positions, start=1)
        }
        cfg = copy.deepcopy(DEFAULT_CONFIG)
        event = ActionEvent(
            play_tag="Play_Pass_RPO", action="Action_ZoneBlock",
            start_frame=88, end_frame=145, annotated_frame=88,
            actor_track_id="OL", target_kind="group",
            source_column="Run Block", blocking_scheme="zone",
        )
        resolved, errors = normalize_and_match_events([event], tracks, cfg)
        self.assertEqual(errors, [])
        self.assertEqual(len(resolved), 5)
        self.assertEqual({e.actor_position for e in resolved}, set(positions))
        self.assertTrue(all(e.blocking_scheme == "zone" for e in resolved))
        segments, _ = infer_action_segments(
            resolved, tracks, {"start_frame": 0, "stop_frame": 150,
                               "play_tag": "Play_Pass_RPO"}, cfg
        )
        blocking = [s for s in segments if s.action == "Action_ZoneBlock"]
        self.assertEqual(len(blocking), 5)
        self.assertTrue(all(s.blocking_scheme == "zone" for s in blocking))
        self.assertTrue(all((s.start_frame, s.end_frame) == (88, 145) for s in blocking))
        with tempfile.TemporaryDirectory() as temp:
            out = str(Path(temp) / "annotations.json")
            write_play_annotation_json(
                out, tracks, {"start_frame": 0, "stop_frame": 150,
                              "video_name": "RPO_1", "play_tag": "Play_Pass_RPO"},
                segments, [], cfg, "demo.xml", "RPO.csv",
            )
            data = json.loads(Path(out).read_text(encoding="utf-8"))
        selected = [s for s in data["actions"]["segments"]
                    if s["action"] == "Action_ZoneBlock"]
        self.assertEqual(len(selected), 5)
        self.assertTrue(all(s["blocking_scheme"] == "zone" for s in selected))
        self.assertNotIn("blocking_scheme", next(
            s for s in data["actions"]["segments"] if s["action"] == "Action_None"
        ))

    def test_non_rpo_generic_runblock_is_unchanged(self):
        fixture = (
            "Video Name:,InsideZone\n"
            ",Key Actions\n"
            "Video #,Run Block,End of Play\n"
            '1,"20,OL",Tac\n'
        )
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "InsideZone.csv"
            path.write_text(fixture, encoding="utf-8")
            events, _, errors = parse_wide_action_csv(
                str(path), copy.deepcopy(DEFAULT_CONFIG), target_video="InsideZone_1"
            )
        self.assertEqual(errors, [])
        blocks = [e for e in events if e.action == "Action_RunBlock"]
        self.assertEqual(len(blocks), 1)
        self.assertIsNone(blocks[0].blocking_scheme)

    def test_incomplete_ol_group_is_rejected(self):
        tracks = {"1": Track(xml_track_id="1", label="player", source="test",
                             custom_track_id="1", position="LT", team_side="offense")}
        e = ActionEvent(
            action="Action_RunBlock", start_frame=88, end_frame=145,
            actor_track_id="OL", target_kind="group", blocking_scheme="gap",
        )
        resolved, errors = normalize_and_match_events([e], tracks, DEFAULT_CONFIG)
        self.assertEqual(resolved, [])
        self.assertTrue(any("exactly five" in error for error in errors))

    def test_route_formats_do_not_silently_relocate_results(self):
        descriptor, error = parse_rpo_route_descriptor(",43 Tac")
        self.assertIsNone(descriptor)
        self.assertIn("end-of-play", error)
        valid, error = parse_rpo_route_descriptor("post,7")
        self.assertIsNone(error)
        self.assertEqual(valid["actor_track_id"], "7")
        for source, label in (("seam,14", "Action_RunSeamRoute"),
                              ("comeback,4", "Action_RunComebackRoute")):
            descriptor, error = parse_rpo_route_descriptor(source)
            self.assertIsNone(error)
            self.assertEqual(descriptor["canonical_action"], label)
        for bad in ("slant,6,24", "slant:[?],22"):
            descriptor, error = parse_rpo_route_descriptor(bad)
            self.assertIsNone(descriptor)
            self.assertIsNotNone(error, bad)


class TestRpoExclusions(unittest.TestCase):
    def test_excluded_rpo_ids_and_non_rpo_safety(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "exclude.txt"
            path.write_text("# intentional\n9\n010\n27 # notes\n", encoding="utf-8")
            ids = load_rpo_excluded_ids(str(path))
            self.assertEqual(ids, {"9", "10", "27"})
            self.assertTrue(is_rpo_excluded("RPO", "9", ids))
            self.assertFalse(is_rpo_excluded("Sack", "9", ids))
            self.assertFalse(is_rpo_excluded("RPO", "11", ids))
            path.write_text("9\nnot-a-number\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_rpo_excluded_ids(str(path))

    def test_excluded_manifest_and_summary_are_not_failures(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest_path = str(Path(temp) / "manifest.csv")
            summary_path = str(Path(temp) / "summary.md")
            excluded = {
                "play_name": "RPO", "video_id": "9",
                "clip_name": "RPO_9", "execution_state": "EXCLUDED",
                "preflight_status": "EXCLUDED", "status": "EXCLUDED",
                "error_count": 0, "warning_count": 0,
            }
            write_batch_manifest_csv(manifest_path, [excluded])
            write_batch_summary_markdown(
                summary_md_path=summary_path, results=[excluded],
                total_discovered=1, total_preflight_ready=0,
                total_preflight_failed=0, total_selected=0,
                total_elapsed_seconds=0.0,
            )
            text = Path(summary_path).read_text(encoding="utf-8")
            self.assertIn("EXCLUDED: 1", text)
            self.assertIn("FAILED: 0", text)


if __name__ == "__main__":
    unittest.main()
