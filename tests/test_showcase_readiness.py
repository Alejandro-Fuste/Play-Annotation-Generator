import json
import os
import tempfile
from pathlib import Path
import pytest

from play_annotation_generator.config import DEFAULT_CONFIG, load_config
from play_annotation_generator.models import Track, TrackBox, ActionEvent
from play_annotation_generator.action_rules import infer_action_segments
from play_annotation_generator.action_event_normalizer import normalize_and_match_events
from play_annotation_generator.batch_pipeline import discover_tracking_inputs
from play_annotation_generator.wide_action_csv_parser import (
    parse_wide_action_csv,
    parse_cell_entries,
    normalize_column_name,
)
from play_annotation_generator.showcase import (
    audit_showcase_readiness,
    generate_showcase,
)


def test_every_unique_populated_showcase_action_header_maps():
    """1. Every unique populated showcase action header maps to a canonical action."""
    manifest_path = "data/showcase/showcase_clips.json"
    assert os.path.exists(manifest_path), "Showcase manifest must exist"

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    config = load_config()
    action_cols_map = config.get("csv", {}).get("action_columns", {})
    norm_action_cols = {normalize_column_name(k): v for k, v in action_cols_map.items()}

    non_action_norm = {
        "videoname", "videoid", "video", "originalid", "coverage", "ol",
        "result", "notes", "playtag", "resulttag", "resultframe", "play", "endofplay", "endplay"
    }

    unmapped = []
    for item in manifest:
        ka_path = item["key_actions_source"]
        vid_id = str(item["video_id"]).strip()
        if not os.path.exists(ka_path):
            continue

        events, all_rows, errors = parse_wide_action_csv(ka_path, config, target_video=item["logical_clip_name"])
        for err in errors:
            if "UNMAPPED_ACTION_COLUMN" in err:
                unmapped.append((item["logical_clip_name"], err))

    assert len(unmapped) == 0, f"Found unmapped populated action columns: {unmapped}"


def test_every_mapped_action_exists_in_actions_json():
    """2. Every mapped Action_* exists in actions.json."""
    config = load_config()
    action_cols_map = config.get("csv", {}).get("action_columns", {})

    with open("data/actions.json", "r", encoding="utf-8") as f:
        actions_data = json.load(f)
    canonical_actions = set(actions_data.get("formattedActionLabels", []))

    for col, act_label in action_cols_map.items():
        if act_label in ("Action_PlayEnd", "Action_None"):
            continue  # boundary / sentinel events
        assert act_label in canonical_actions, f"Action '{act_label}' for column '{col}' is not in actions.json"


def test_duo_filename_compatibility_clip1(tmp_path):
    """3. Duo_clip1 -> Duo_1."""
    duo_dir = tmp_path / "Duo"
    duo_dir.mkdir(parents=True)
    zip_path = duo_dir / "Duo_clip1_cvat_mot.zip"
    zip_path.touch()

    inputs = discover_tracking_inputs(tmp_path)
    assert len(inputs) == 1
    inp = inputs[0]
    assert inp.folder_play_name == "Duo"
    assert inp.filename_play_name == "Duo"
    assert inp.video_id == "1"
    assert inp.clip_name == "Duo_1"


def test_duo_filename_compatibility_clip100(tmp_path):
    """4. Duo_clip100 -> Duo_100."""
    duo_dir = tmp_path / "Duo"
    duo_dir.mkdir(parents=True)
    zip_path = duo_dir / "Duo_clip100_cvat_mot.zip"
    zip_path.touch()

    inputs = discover_tracking_inputs(tmp_path)
    assert len(inputs) == 1
    inp = inputs[0]
    assert inp.folder_play_name == "Duo"
    assert inp.filename_play_name == "Duo"
    assert inp.video_id == "100"
    assert inp.clip_name == "Duo_100"


def test_normal_filenames_unchanged(tmp_path):
    """5. Normal filenames such as BootPass_1 and JetSweep_2 are unchanged."""
    bp_dir = tmp_path / "BootPass"
    bp_dir.mkdir(parents=True)
    (bp_dir / "BootPass_1_cvat_mot.zip").touch()

    js_dir = tmp_path / "JetSweep"
    js_dir.mkdir(parents=True)
    (js_dir / "JetSweep_2_cvat_mot.zip").touch()

    inputs = discover_tracking_inputs(tmp_path)
    assert len(inputs) == 2
    inputs_by_clip = {inp.clip_name: inp for inp in inputs}

    assert "BootPass_1" in inputs_by_clip
    assert inputs_by_clip["BootPass_1"].filename_play_name == "BootPass"
    assert inputs_by_clip["BootPass_1"].video_id == "1"

    assert "JetSweep_2" in inputs_by_clip
    assert inputs_by_clip["JetSweep_2"].filename_play_name == "JetSweep"
    assert inputs_by_clip["JetSweep_2"].video_id == "2"


def test_draw_1_resolves_all_three_sources():
    """6. Draw_1 resolves tracking + Key Actions + PlayerTrack inputs."""
    assert os.path.exists("data/tracking/Draw/Draw_1_cvat_mot.zip")
    assert os.path.exists("data/key_actions/Draw.csv")
    assert os.path.exists("data/player_tracks/Draw.csv")

    # Verify Draw video 1 exists in Key Actions
    with open("data/key_actions/Draw.csv", "r", encoding="utf-8") as f:
        ka_lines = f.readlines()
    assert any(l.split(",")[0].strip().strip('"') == "1" for l in ka_lines)

    # Verify Draw video 1 exists in PlayerTrack
    with open("data/player_tracks/Draw.csv", "r", encoding="utf-8") as f:
        pt_lines = f.readlines()
    assert any(l.split(",")[0].strip().strip('"') == "1" for l in pt_lines)


def test_field_goal_block_naming_singular():
    """7. FieldGoalBlock naming remains singular."""
    with open("data/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    labels = plays.get("playLabels", [])
    assert "FieldGoalBlock" in labels
    assert "FieldGoalBlocks" not in labels

    assert os.path.exists("data/key_actions/FieldGoalBlock.csv")
    assert os.path.exists("data/player_tracks/FieldGoalBlock.csv")
    assert os.path.isdir("data/tracking/FieldGoalBlock")


def test_explicit_start_end_ranges_retained():
    """8. Explicit start,end,track_id ranges retain the explicit end."""
    # Test cell parser retains end_frame
    entries = parse_cell_entries("191,261,OL")
    assert len(entries) == 1
    assert entries[0][0] == 191
    assert entries[0][1] == "OL"
    assert entries[0].end_frame == 261

    # Test ActionEvent expansion retains end_frame
    ev = ActionEvent(
        video_name="Test_1",
        video_id="1",
        action="Action_ZoneBlock",
        start_frame=191,
        end_frame=261,
        annotated_frame=191,
        actor_track_id="OL",
        target_kind="group"
    )

    track_c = Track(
        xml_track_id="10",
        label="player",
        source="mot",
        position="C",
        team_side="offense",
        custom_track_id="13",
        boxes_by_frame={191: TrackBox(191, 0, 0, 10, 10, False, False, True), 261: TrackBox(261, 0, 0, 10, 10, False, False, True)}
    )
    tracks = {"10": track_c}
    config = load_config()

    resolved, errors = normalize_and_match_events([ev], tracks, config)
    assert len(resolved) == 1
    assert resolved[0].start_frame == 191
    assert resolved[0].end_frame == 261


def test_newly_enabled_blocking_honors_end_of_ol_block():
    """9. Newly enabled blocking actions honor End-of-OL-Block logic where appropriate."""
    track = Track(
        xml_track_id="5",
        label="player",
        source="mot",
        position="LG",
        custom_track_id="5",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(10, 200)}
    )
    tracks = {"5": track}

    # Action_PullLeadBlock starts at 20, boundary at 50
    pull_lead = ActionEvent(
        video_name="Counter_1",
        video_id="1",
        action="Action_PullLeadBlock",
        start_frame=20,
        annotated_frame=20,
        actor_track_id="5",
        resolved_xml_track_id="5",
        target_kind="track_id"
    )
    boundary = ActionEvent(
        video_name="Counter_1",
        video_id="1",
        action="Action_None",
        start_frame=50,
        annotated_frame=50,
        event_type="BOUNDARY"
    )

    config = load_config()
    metadata = {"start_frame": 0, "stop_frame": 199}

    segments, warnings = infer_action_segments([pull_lead, boundary], tracks, metadata, config)

    pull_segs = [s for s in segments if s.action == "Action_PullLeadBlock"]
    assert len(pull_segs) == 1
    assert pull_segs[0].start_frame == 20
    assert pull_segs[0].end_frame == 50  # inclusive boundary


def test_unknown_populated_action_column_fails():
    """10. An unknown populated action column fails readiness rather than being ignored."""
    with tempfile.NamedTemporaryFile("w+", suffix=".csv", delete=False) as f:
        f.write("Video #,Pre Snap,Ball Snap,Trick Fake Play,End of Play\n")
        f.write('1,"0,ALL","10,5","20,12",Tac\n')
        temp_csv = f.name

    try:
        config = load_config()
        events, rows, errors = parse_wide_action_csv(temp_csv, config, target_video="1")
        assert any("UNMAPPED_ACTION_COLUMN" in e and "Trick Fake Play" in e for e in errors)
    finally:
        os.unlink(temp_csv)


def test_existing_bootpass_and_jetsweep_green():
    """11. Existing BootPass and JetSweep tests remain green."""
    config = load_config()
    # Parse BootPass_1
    bp_events, bp_rows, bp_errors = parse_wide_action_csv(
        "data/key_actions/BootPass.csv", config, target_video="BootPass_1"
    )
    assert len(bp_rows) > 0
    assert any(e.action == "Action_BootAway" for e in bp_events)
    assert any(e.action == "Action_RunFlatRoute" for e in bp_events)

    # Parse JetSweep_1
    js_events, js_rows, js_errors = parse_wide_action_csv(
        "data/key_actions/JetSweep.csv", config, target_video="JetSweep_1"
    )
    assert len(js_rows) > 0
    assert any(e.action == "Action_JetMotion" for e in js_events)
    assert any(e.action == "Action_LeadBlock" for e in js_events)
