import json
import os
import tempfile
import unittest

from tapevision_enricher.annotation_metadata import (
    parse_dataset_timestamp,
    parse_from_youtube,
    load_dataset_summary,
    resolve_clip_source_metadata,
    load_action_definitions,
    resolve_used_action_definitions,
    load_play_definitions,
    resolve_play_definition,
)


class TestAnnotationMetadata(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_parse_dataset_timestamp(self):
        # Normal timestamps
        sec, w = parse_dataset_timestamp("0:00:02")
        self.assertEqual(sec, 2.0)
        self.assertIsNone(w)

        sec, w = parse_dataset_timestamp("0:02:35")
        self.assertEqual(sec, 155.0)
        self.assertIsNone(w)

        sec, w = parse_dataset_timestamp("1:04:40")
        self.assertEqual(sec, 3880.0)
        self.assertIsNone(w)

        # Blank timestamps
        sec, w = parse_dataset_timestamp("")
        self.assertIsNone(sec)
        self.assertIsNone(w)

        sec, w = parse_dataset_timestamp(None)
        self.assertIsNone(sec)
        self.assertIsNone(w)

        # Invalid timestamp
        sec, w = parse_dataset_timestamp("invalid:time:format:extra")
        self.assertIsNone(sec)
        self.assertIsNotNone(w)

        sec, w = parse_dataset_timestamp("abc")
        self.assertIsNone(sec)
        self.assertIsNotNone(w)

    def test_parse_from_youtube(self):
        val, w = parse_from_youtube("TRUE")
        self.assertTrue(val)
        self.assertIsNone(w)

        val, w = parse_from_youtube("FALSE")
        self.assertFalse(val)
        self.assertIsNone(w)

        val, w = parse_from_youtube("")
        self.assertIsNone(val)
        self.assertIsNone(w)

        val, w = parse_from_youtube("maybe")
        self.assertIsNone(val)
        self.assertIsNotNone(w)

    def test_dataset_summary_matching_and_clip_length(self):
        csv_path = os.path.join(self.temp_dir.name, "DatasetSummary.csv")
        content = (
            "start_time,end_time,play,view,fromYouTube,input_file,output_file,name,file extension,date,\n"
            "0:00:02,0:00:13,Kickoff,Sideline,FALSE,rooski.mp4,JetSweep_1.mp4,JetSweep_,.mp4,2026-03-17,\n"
            "0:00:20,0:00:10,Run,Endzone,TRUE,rooski.mp4,BadTiming_1.mp4,BadTiming_,.mp4,2026-03-17,\n"
            "0:00:00,0:00:05,Run,Sideline,FALSE,rooski.mp4,Dup_1.mp4,Dup_,.mp4,2026-03-17,\n"
            "0:00:10,0:00:15,Run,Sideline,FALSE,rooski.mp4,Dup_1.mp4,Dup_,.mp4,2026-03-17,\n"
        )
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write(content)

        index, err = load_dataset_summary(csv_path)
        self.assertIsNone(err)

        # 1. Exact match with .mp4
        source, warnings, errors = resolve_clip_source_metadata(index, "JetSweep_1.mp4")
        self.assertEqual(source["start_time"], 2.0)
        self.assertEqual(source["end_time"], 13.0)
        self.assertEqual(source["clip_length"], 11.0)
        self.assertEqual(source["view"], "Sideline")
        self.assertFalse(source["from_youtube"])
        self.assertEqual(len(warnings), 0)
        self.assertEqual(len(errors), 0)

        # 2. Match target without .mp4 (JetSweep_1)
        source, warnings, errors = resolve_clip_source_metadata(index, "JetSweep_1")
        self.assertEqual(source["start_time"], 2.0)
        self.assertEqual(source["end_time"], 13.0)
        self.assertEqual(source["clip_length"], 11.0)

        # 3. end_time precedes start_time
        source, warnings, errors = resolve_clip_source_metadata(index, "BadTiming_1.mp4")
        self.assertIsNone(source["clip_length"])
        self.assertTrue(any("end_time precedes start_time" in e for e in errors))

        # 4. Duplicate output_file
        source, warnings, errors = resolve_clip_source_metadata(index, "Dup_1.mp4")
        self.assertIsNone(source["start_time"])
        self.assertTrue(any("ambiguous" in e for e in errors))

        # 5. Missing row
        source, warnings, errors = resolve_clip_source_metadata(index, "NonExistent_1.mp4")
        self.assertIsNone(source["start_time"])
        self.assertTrue(any("no Dataset Summary row found" in w for w in warnings))

    def test_action_definitions_loading_and_resolution(self):
        actions_json_path = os.path.join(self.temp_dir.name, "actions11.json")
        data = {
            "formattedActionLabels": ["Action_JetMotion", "Action_BallSnap"],
            "actionLabels": ["Jet Motion", "Ball Snap"],
            "actionDefinitions": {
                "Jet Motion": {"definition": "A pre-snap motion across formation."},
                "Ball Snap": {"definition": "The start of the play."}
            }
        }
        with open(actions_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        c_map, a_defs, err = load_action_definitions(actions_json_path)
        self.assertIsNone(err)
        self.assertEqual(c_map["Action_JetMotion"], "Jet Motion")

        segments = [
            {"action": "Action_JetMotion"},
            {"action": "Action_BallSnap"},
            {"action": "Action_JetMotion"},  # duplicate used action
            {"action": "Action_UnknownDefined"}
        ]

        res_defs, warnings = resolve_used_action_definitions(segments, c_map, a_defs)
        self.assertEqual(list(res_defs.keys()), ["Action_BallSnap", "Action_JetMotion", "Action_UnknownDefined"])
        self.assertEqual(res_defs["Action_JetMotion"]["definition"], "A pre-snap motion across formation.")
        self.assertIsNone(res_defs["Action_UnknownDefined"]["definition"])
        self.assertTrue(any("no definition found" in w for w in warnings))

    def test_play_definitions_loading_and_resolution(self):
        plays_json_path = os.path.join(self.temp_dir.name, "plays.json")
        data = {
            "formattedPlayLabels": ["Play_Run_JetSweep", "Play_Run_Counter"],
            "playLabels": ["JetSweep", "Counter"],
            "defintions": {  # Misspelled key test
                "JetSweep": {"definition": "Speed sweep action to edge."}
            }
        }
        with open(plays_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        p_map, p_defs, err = load_play_definitions(plays_json_path)
        self.assertIsNone(err)

        def_text, warnings = resolve_play_definition("Play_Run_JetSweep", p_map, p_defs)
        self.assertEqual(def_text, "Speed sweep action to edge.")
        self.assertEqual(len(warnings), 0)

        def_text, warnings = resolve_play_definition("Play_Run_Counter", p_map, p_defs)
        self.assertIsNone(def_text)
        self.assertTrue(any("no definition found" in w for w in warnings))


if __name__ == "__main__":
    unittest.main()
