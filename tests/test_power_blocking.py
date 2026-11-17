"""Power blocking grammar, wide CSV integration and dense timeline regression."""
import copy
import tempfile
import unittest
from pathlib import Path

from play_annotation_generator.config import DEFAULT_CONFIG
from play_annotation_generator.models import Track, TrackBox
from play_annotation_generator.power_parser import parse_power_blocks
from play_annotation_generator.wide_action_csv_parser import parse_wide_action_csv
from play_annotation_generator.action_event_normalizer import normalize_and_match_events
from play_annotation_generator.action_rules import infer_action_segments


class TestPowerBlocking(unittest.TestCase):
    def test_both_formats(self):
        expected = [
            ("Action_DownBlock", "8", 239, 289),
            ("Action_DownBlock", "13", 239, 289),
            ("Action_PullBlock", "2", 239, 289),
        ]
        for down in ("239;8,13", "239,8,13"):
            for pull in ("239,289;2", "239,289,2"):
                with self.subTest(down=down, pull=pull):
                    self.assertEqual(parse_power_blocks(down, pull), expected)

    def test_single_actor_zero_and_distinct_starts(self):
        self.assertEqual(parse_power_blocks("250;0", "239,289;2"), [
            ("Action_DownBlock", "0", 250, 289),
            ("Action_PullBlock", "2", 239, 289),
        ])

    def test_invalid_inputs(self):
        for down, pull in [
            ("239;8", "-"), ("239;8", "239,2"),
            ("239;8", "289,239;2"), ("290;8", "239,289;2"),
            ("239;?", "239,289;2"), ("239;8", "239,289;[?]"),
            ("239;8,8", "239,289;2"), ("239;8,", "239,289;2"),
            ("239;8", "239,289;2;3"),
        ]:
            with self.subTest(down=down, pull=pull):
                with self.assertRaises(ValueError):
                    parse_power_blocks(down, pull)
        self.assertEqual(parse_power_blocks("-", "-"), [])

    def parse_fixture(self, down, pull, result="Tac", play="Power"):
        fixture = (
            f"Video Name:,{play}\n"
            ",Key Actions\n"
            "Video #,Pre Snap,Down Block,Pull Block,Result\n"
            f'376,"5,ALL","{down}","{pull}",{result}\n'
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / f"{play}.csv"
            path.write_text(fixture, encoding="utf-8")
            return parse_wide_action_csv(str(path), copy.deepcopy(DEFAULT_CONFIG),
                                         target_video=f"{play}_376")

    def test_wide_csv_and_dense_segments(self):
        events, _, errors = self.parse_fixture("239;8,13", "239,289;2")
        self.assertEqual(errors, [])
        blocking = [e for e in events if e.action in ("Action_DownBlock", "Action_PullBlock")]
        self.assertEqual(len(blocking), 3)
        self.assertTrue(all(e.result_tag == "Result_Tackle" for e in events))
        self.assertTrue(all(e.result_frame is None for e in events))
        tracks = {
            str(i): Track(xml_track_id=str(i), label="player", source="test",
                          custom_track_id=str(i), position=position, team_side="offense",
                          boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True)
                                          for f in range(330)})
            for i, position in ((8, "LT"), (13, "C"), (2, "LG"))
        }
        cfg = copy.deepcopy(DEFAULT_CONFIG)
        resolved, errors = normalize_and_match_events(events, tracks, cfg)
        self.assertEqual(errors, [])
        segments, _ = infer_action_segments(
            resolved, tracks, {"play_tag": "Play_Run_Power", "start_frame": 0, "stop_frame": 329}, cfg
        )
        self.assertEqual(
            {(s.action, s.actor_track_id, s.start_frame, s.end_frame)
             for s in segments if s.action in ("Action_DownBlock", "Action_PullBlock")},
            set(parse_power_blocks("239;8,13", "239,289;2")),
        )

    def test_result_mapping_and_missing(self):
        for raw, expected in (("TD", "Result_Touchdown"), ("OOB", "Result_OutOfBounds"),
                              ("Tac", "Result_Tackle"), ("-", None)):
            events, _, errors = self.parse_fixture("239,8,13", "239,289,2", raw)
            self.assertEqual(errors, [])
            self.assertTrue(all(e.result_tag == expected for e in events))

    def test_invalid_row_does_not_fall_back_to_generic_parser(self):
        events, _, errors = self.parse_fixture("239;?", "239,289;2")
        self.assertTrue(errors)
        self.assertFalse(any(e.action in ("Action_DownBlock", "Action_PullBlock") for e in events))

    def test_non_power_unchanged(self):
        events, _, errors = self.parse_fixture("239,8", "239,289,2", play="PinAndPull")
        self.assertEqual(errors, [])
        down = next(e for e in events if e.action == "Action_DownBlock")
        self.assertIsNone(down.end_frame)

    def test_real_power_csv(self):
        events, _, errors = parse_wide_action_csv(
            "data/key_actions/Power.csv", copy.deepcopy(DEFAULT_CONFIG), target_video="Power_376")
        self.assertEqual(errors, [])
        self.assertEqual(
            {(e.action, e.actor_track_id, e.start_frame, e.end_frame)
             for e in events if e.action in ("Action_DownBlock", "Action_PullBlock")},
            set(parse_power_blocks("239;8,13", "239,289;2")),
        )
