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


def test_semicolon_continuation_parsing_and_formats():
    """12. Semicolon continuation parsing and various cell formats."""
    # 52,19 -> one event: frame 52, actor 19
    e1 = parse_cell_entries("52,19")
    assert len(e1) == 1
    assert e1[0][0] == 52 and e1[0][1] == "19" and e1[0][2] is None

    # 52,19;55,14 -> frame 52 actor 19; frame 55 actor 14
    e2 = parse_cell_entries("52,19;55,14")
    assert len(e2) == 2
    assert e2[0][0] == 52 and e2[0][1] == "19"
    assert e2[1][0] == 55 and e2[1][1] == "14"

    # 52,19;14;20;18 -> frame 52 for actors 19, 14, 20, 18
    e3 = parse_cell_entries("52,19;14;20;18")
    assert len(e3) == 4
    for item in e3:
        assert item[0] == 52
        assert item[2] is None
    assert [item[1] for item in e3] == ["19", "14", "20", "18"]

    # 361,11,18,21 -> frame 361 for actors 11, 18, 21
    e4 = parse_cell_entries("361,11,18,21")
    assert len(e4) == 3
    for item in e4:
        assert item[0] == 361
        assert item[2] is None
    assert [item[1] for item in e4] == ["11", "18", "21"]

    # 191,261,OL -> explicit range 191-261 for group OL
    e5 = parse_cell_entries("191,261,OL")
    assert len(e5) == 1
    assert e5[0][0] == 191 and e5[0][1] == "OL" and e5[0].end_frame == 261

    # 20,30,4;40,50,7 -> actor 4 range 20-30; actor 7 range 40-50
    e6 = parse_cell_entries("20,30,4;40,50,7")
    assert len(e6) == 2
    assert e6[0][0] == 20 and e6[0][1] == "4" and e6[0].end_frame == 30
    assert e6[1][0] == 40 and e6[1][1] == "7" and e6[1].end_frame == 50


def test_duo_1_combo_blocks_regression():
    """13. Duo_1 Combo Blocks parses exactly 4 events at frame 52 for 19,14,20,18 with 0 global events."""
    config = load_config()
    events, rows, errors = parse_wide_action_csv(
        "data/key_actions/Duo.csv", config, target_video="Duo_1"
    )
    combo_events = [e for e in events if e.action == "Action_ComboBlock"]
    assert len(combo_events) == 4, f"Expected 4 ComboBlock events, got {len(combo_events)}"
    for e in combo_events:
        assert e.start_frame == 52
        assert e.target_kind == "track_id"
        assert e.actor_track_id in ["19", "14", "20", "18"]

    # Zero global ComboBlock events
    global_combos = [e for e in combo_events if e.target_kind == "global_event"]
    assert len(global_combos) == 0

    # Duo canonical play label
    assert all(e.play_tag == "Play_Run_Duo" for e in events)


def test_canonical_play_label_resolution():
    """14. Canonical play label resolution without JetSweep fallback."""
    config = load_config()
    expected_labels = {
        "BootPass_1": ("data/key_actions/BootPass.csv", "Play_Pass_BootPass"),
        "Counter_1": ("data/key_actions/Counter.csv", "Play_Run_Counter"),
        "Duo_1": ("data/key_actions/Duo.csv", "Play_Run_Duo"),
        "QuickScreens_1": ("data/key_actions/QuickScreens.csv", "Play_Pass_QuickScreens"),
        "FieldGoalBlock_3": ("data/key_actions/FieldGoalBlock.csv", "Play_SpecialTeams_FieldGoalBlock"),
        "JetSweep_1": ("data/key_actions/JetSweep.csv", "Play_Run_JetSweep"),
    }

    for clip_id, (csv_path, expected_tag) in expected_labels.items():
        events, rows, errors = parse_wide_action_csv(csv_path, config, target_video=clip_id)
        assert len(events) > 0, f"No events parsed for {clip_id}"
        assert all(e.play_tag == expected_tag for e in events), (
            f"Clip {clip_id} expected {expected_tag}, got {[e.play_tag for e in events[:3]]}"
        )


def test_special_teams_row_side_assignment():
    """15. Special teams positional grid team-side assignment from row order."""
    from play_annotation_generator.player_track_sheet_parser import parse_player_track_csv

    # FieldGoalBlock_3
    fg_assigns, fg_warn = parse_player_track_csv("data/player_tracks/FieldGoalBlock.csv", target_video_id="3")
    assert len(fg_assigns) > 0
    # First row: Long_Snapper (20), Holder (8), Kicker (11) must be offense
    assert fg_assigns["20"].position == "Long_Snapper" and fg_assigns["20"].team_side == "offense"
    assert fg_assigns["8"].position == "Holder" and fg_assigns["8"].team_side == "offense"
    assert fg_assigns["11"].position == "Kicker" and fg_assigns["11"].team_side == "offense"
    # Second row: Left_Edge_Rusher (2), Interior_Rusher1 (7) must be defense
    assert fg_assigns["2"].position == "Left_Edge_Rusher" and fg_assigns["2"].team_side == "defense"
    assert fg_assigns["7"].position == "Interior_Rusher1" and fg_assigns["7"].team_side == "defense"

    # PuntBlock_1
    pb_assigns, pb_warn = parse_player_track_csv("data/player_tracks/PuntBlock.csv", target_video_id="1")
    assert len(pb_assigns) > 0
    # First row: Long_Snapper (17), Punter (16) must be offense
    assert pb_assigns["17"].position == "Long_Snapper" and pb_assigns["17"].team_side == "offense"
    assert pb_assigns["16"].position == "Punter" and pb_assigns["16"].team_side == "offense"
    # Second row: Interior_Rusher1 (4) must be defense
    assert pb_assigns["4"].team_side == "defense"

    # KickoffReturnTouchdown_6
    ko_assigns, ko_warn = parse_player_track_csv("data/player_tracks/KickoffReturnTouchdown.csv", target_video_id="6")
    assert len(ko_assigns) > 0
    # First row: Kicker (8) must be offense
    assert ko_assigns["8"].position == "Kicker" and ko_assigns["8"].team_side == "offense"
    # Second row: Front_Blocker2 (4) must be defense
    assert ko_assigns["4"].position == "Front_Blocker2" and ko_assigns["4"].team_side == "defense"


def test_special_teams_presnap_and_long_snap_timing():
    """16. Special-teams PreSnap fallback boundaries and Action_LongSnap non-stretching."""
    config = load_config()

    # FieldGoalBlock_3 PreSnap ends at Long Snap - 1, and LongSnap doesn't stretch to play end
    track_ls = Track(
        xml_track_id="20",
        label="player",
        source="mot",
        position="Long_Snapper",
        team_side="offense",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(0, 100)}
    )
    track_rusher = Track(
        xml_track_id="7",
        label="player",
        source="mot",
        position="Interior_Rusher1",
        team_side="defense",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(0, 100)}
    )
    tracks = {"20": track_ls, "7": track_rusher}

    ls_event = ActionEvent(
        video_name="FieldGoalBlock_3",
        video_id="3",
        action="Action_LongSnap",
        start_frame=4,
        annotated_frame=4,
        actor_track_id="20",
        resolved_xml_track_id="20",
        target_kind="track_id"
    )
    place_event = ActionEvent(
        video_name="FieldGoalBlock_3",
        video_id="3",
        action="Action_PlaceBall",
        start_frame=21,
        annotated_frame=21,
        actor_track_id="8",
        resolved_xml_track_id="8",
        target_kind="track_id"
    )
    kick_event = ActionEvent(
        video_name="FieldGoalBlock_3",
        video_id="3",
        action="Action_KickBall",
        start_frame=46,
        annotated_frame=46,
        actor_track_id="11",
        resolved_xml_track_id="11",
        target_kind="track_id"
    )

    metadata = {"start_frame": 0, "stop_frame": 99, "play_name": "FieldGoalBlock"}
    segments, warnings = infer_action_segments(
        [ls_event, place_event, kick_event], tracks, metadata, config
    )

    # Rusher has no explicit action: PreSnap should end at Long Snap - 1 = 3
    rusher_presnap = [s for s in segments if s.xml_track_id == "7" and s.action == "Action_PreSnap"]
    assert len(rusher_presnap) == 1
    assert rusher_presnap[0].start_frame == 0
    assert rusher_presnap[0].end_frame == 3

    # Long Snap segment should not stretch to play end (frame 99)
    ls_segs = [s for s in segments if s.xml_track_id == "20" and s.action == "Action_LongSnap"]
    assert len(ls_segs) == 1
    assert ls_segs[0].start_frame == 4
    assert ls_segs[0].end_frame < 46  # stops before kick/place


def test_malformed_cells_cause_blocked_readiness():
    """17. Malformed cells (?,51) cause BLOCKED readiness status."""
    summary = audit_showcase_readiness()
    blocked_clips = {r.logical_clip_name: r for r in summary.results if r.status == "BLOCKED"}

    assert len(blocked_clips) == 0  # 50-clip showcase manifest has 0 blocked clips
    assert "KickoffReturnTouchdown_5" not in {r.logical_clip_name for r in summary.results}

    # When auditing a manifest with a malformed cell like KickoffReturnTouchdown_5 (?,51), it causes BLOCKED
    with tempfile.NamedTemporaryFile("w+", suffix=".json", delete=False) as tf:
        json.dump([{
            "logical_clip_name": "KickoffReturnTouchdown_5",
            "play_name": "KickoffReturnTouchdown",
            "video_id": "5",
            "tracking_source": "data/tracking/KickoffReturnTouchdown/KickoffReturnTouchdown_5_cvat_mot.zip",
            "key_actions_source": "data/key_actions/KickoffReturnTouchdown.csv",
            "player_tracks_source": "data/player_tracks/KickoffReturnTouchdown.csv"
        }], tf)
        tmp_manifest = tf.name

    try:
        tmp_summary = audit_showcase_readiness(manifest_path=tmp_manifest)
        tmp_blocked = {r.logical_clip_name: r for r in tmp_summary.results if r.status == "BLOCKED"}
        assert "KickoffReturnTouchdown_5" in tmp_blocked
        assert any("Malformed action cell" in b for b in tmp_blocked["KickoffReturnTouchdown_5"].errors)
    finally:
        os.unlink(tmp_manifest)



def test_semantic_action_alias_audit_classification():
    """18. Every approximate alias in SEMANTIC_ACTION_ALIAS_AUDIT is classified."""
    from play_annotation_generator.semantic_audit import SEMANTIC_ACTION_ALIAS_AUDIT

    expected_headers = {
        "press interior gap", "pass drop", "clear out route",
        "dig route", "sell slant", "run go route", "onside kick"
    }

    found_headers = {e["source_header"].lower().strip() for e in SEMANTIC_ACTION_ALIAS_AUDIT}
    assert expected_headers.issubset(found_headers)

    for entry in SEMANTIC_ACTION_ALIAS_AUDIT:
        assert entry["classification"] in ["EXACT", "INTENTIONAL_ALIAS", "NEEDS_SOURCE_REVIEW"]
        assert len(entry["reason"]) > 10
        assert entry["classification"] != "NEEDS_SOURCE_REVIEW"


def test_handoff_generic_configured_termination():
    """19. Generic ends_when_any_action_starts rule terminates Handoff before BallCarry/TakeHandoff."""
    config = load_config()

    track_qb = Track(
        xml_track_id="1",
        label="player",
        source="mot",
        position="QB",
        team_side="offense",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(50, 200)}
    )
    track_rb = Track(
        xml_track_id="2",
        label="player",
        source="mot",
        position="RB",
        team_side="offense",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(50, 200)}
    )
    tracks = {"1": track_qb, "2": track_rb}

    handoff_evt = ActionEvent(
        video_name="TestPlay",
        video_id="1",
        action="Action_Handoff",
        start_frame=100,
        annotated_frame=100,
        actor_track_id="1",
        resolved_xml_track_id="1",
        target_kind="track_id"
    )
    ball_carry_evt = ActionEvent(
        video_name="TestPlay",
        video_id="1",
        action="Action_BallCarry",
        start_frame=120,
        annotated_frame=120,
        actor_track_id="2",
        resolved_xml_track_id="2",
        target_kind="track_id"
    )

    metadata = {"start_frame": 50, "stop_frame": 199}
    segments, warnings = infer_action_segments([handoff_evt, ball_carry_evt], tracks, metadata, config)

    handoff_segs = [s for s in segments if s.xml_track_id == "1" and s.action == "Action_Handoff"]
    assert len(handoff_segs) == 1
    assert handoff_segs[0].start_frame == 100
    assert handoff_segs[0].end_frame == 119  # 120 - 1

    # Explicit Handoff end frame takes precedence
    handoff_explicit = ActionEvent(
        video_name="TestPlay",
        video_id="1",
        action="Action_Handoff",
        start_frame=100,
        end_frame=115,
        annotated_frame=100,
        actor_track_id="1",
        resolved_xml_track_id="1",
        target_kind="track_id"
    )
    segments_exp, _ = infer_action_segments([handoff_explicit, ball_carry_evt], tracks, metadata, config)
    handoff_exp_segs = [s for s in segments_exp if s.xml_track_id == "1" and s.action == "Action_Handoff"]
    assert len(handoff_exp_segs) == 1
    assert handoff_exp_segs[0].start_frame == 100
    assert handoff_exp_segs[0].end_frame == 115


def test_counter_1_handoff_regression():
    """20. Counter_1 authoritative data generates Handoff 381-387 and BallCarry starts 388."""
    from play_annotation_generator.batch_pipeline import run_generate_and_enrich_pipeline
    config = load_config()

    with tempfile.TemporaryDirectory() as tmpdir:
        tracks, metadata, events, segments, dense, metrics, warns, errs = run_generate_and_enrich_pipeline(
            gt_path="data/tracking/Counter/Counter_1_cvat_mot.zip",
            labels_path=None,
            template_path="docs/JetSweepTemplate.xml",
            key_actions_csv="data/key_actions/Counter.csv",
            player_tracks_csv="data/player_tracks/Counter.csv",
            config=config,
            output_dir=tmpdir,
            target_video_name="Counter_1",
            target_video_id="1"
        )
        assert len(errs) == 0, f"Unexpected errors: {errs}"
        assert metadata.get("play_tag") == "Play_Run_Counter"

        handoff_segs = [s for s in segments if s.action == "Action_Handoff"]
        assert len(handoff_segs) == 1
        assert handoff_segs[0].actor_track_id == "16"
        assert handoff_segs[0].start_frame == 381
        assert handoff_segs[0].end_frame == 387

        carry_segs = [s for s in segments if s.action == "Action_BallCarry"]
        assert len(carry_segs) >= 1
        assert carry_segs[0].actor_track_id == "12"
        assert carry_segs[0].start_frame == 388


def test_non_temporal_rpo_route_descriptors():
    """21. RPO Route column parses as non-temporal descriptor without creating timed segments."""
    from play_annotation_generator.wide_action_csv_parser import parse_rpo_route_descriptor

    desc_post, err_post = parse_rpo_route_descriptor("post,7", "Route")
    assert err_post is None
    assert desc_post["canonical_action"] == "Action_RunPostRoute"
    assert desc_post["actor_track_id"] == "7"
    assert desc_post["temporal"] is False

    desc_slant, err_slant = parse_rpo_route_descriptor("slant,3", "Route")
    assert err_slant is None
    assert desc_slant["canonical_action"] == "Action_RunSlantRoute"
    assert desc_slant["actor_track_id"] == "3"
    assert desc_slant["temporal"] is False

    # Malformed route descriptors block
    _, err_bare = parse_rpo_route_descriptor("post", "Route")
    assert err_bare is not None

    _, err_lead_comma = parse_rpo_route_descriptor(",7", "Route")
    assert err_lead_comma is not None

    _, err_unknown = parse_rpo_route_descriptor("unknownroute,7", "Route")
    assert err_unknown is not None

    _, err_unassigned = parse_rpo_route_descriptor("post,[?]", "Route")
    assert err_unassigned is not None


def test_showcase_manifest_50_clips():
    """22. Showcase manifest has exactly 50 clips with correct replacements."""
    with open("data/showcase/showcase_clips.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    assert len(manifest) == 50
    clip_names = {c["logical_clip_name"] for c in manifest}
    assert "OutAndUp_3" in clip_names
    assert "OutAndUp_1" not in clip_names
    assert "Post10to15_1" in clip_names
    assert "Post10to15_2" not in clip_names

    # Replacements:
    assert "PuntReturnTouchdown_9" in clip_names
    assert "KickoffReturnTouchdown_13" in clip_names
    assert "KickoffReturnTouchdown_14" in clip_names

    assert "PuntReturnTouchdown_2" not in clip_names
    assert "KickoffReturnTouchdown_5" not in clip_names
    assert "KickoffReturnTouchdown_6" not in clip_names

    # Assert replacement tracking ZIPs exist
    for item in manifest:
        if item["logical_clip_name"] in {"PuntReturnTouchdown_9", "KickoffReturnTouchdown_13", "KickoffReturnTouchdown_14"}:
            assert os.path.exists(item["tracking_source"]), f"Missing tracking zip: {item['tracking_source']}"


def test_krt_id_switch_independent_actors():
    """23. KickoffReturnTouchdown_6 retains independent actor IDs for return actions."""
    from play_annotation_generator.batch_pipeline import run_generate_and_enrich_pipeline
    config = load_config()

    with tempfile.TemporaryDirectory() as tmpdir:
        tracks, metadata, events, segments, dense, metrics, warns, errs = run_generate_and_enrich_pipeline(
            gt_path="data/tracking/KickoffReturnTouchdown/KickoffReturnTouchdown_6_cvat_mot.zip",
            labels_path=None,
            template_path="docs/JetSweepTemplate.xml",
            key_actions_csv="data/key_actions/KickoffReturnTouchdown.csv",
            player_tracks_csv="data/player_tracks/KickoffReturnTouchdown.csv",
            config=config,
            output_dir=tmpdir,
            target_video_name="KickoffReturnTouchdown_6",
            target_video_id="6"
        )
        assert len(errs) == 0, f"Unexpected errors: {errs}"

        catch_segs = [s for s in segments if s.action == "Action_CatchKick"]
        assert len(catch_segs) == 1
        assert catch_segs[0].actor_track_id == "50"

        carry_segs = [s for s in segments if s.action == "Action_BallCarry"]
        assert len(carry_segs) >= 1
        assert carry_segs[0].actor_track_id == "61"

        cgl_segs = [s for s in segments if s.action == "Action_CrossGoalLine"]
        assert len(cgl_segs) == 1
        assert cgl_segs[0].actor_track_id == "61"


def test_rpo_presnap_boundary_and_coverage():
    """24. RPO PreSnap end frame is Run Block start - 2, and Action_None begins at start - 1."""
    config = load_config()

    track_ol = Track(
        xml_track_id="1",
        label="player",
        source="mot",
        position="LG",
        team_side="offense",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(0, 150)}
    )
    track_wr = Track(
        xml_track_id="2",
        label="player",
        source="mot",
        position="WR",
        team_side="offense",
        boxes_by_frame={f: TrackBox(f, 0, 0, 10, 10, False, False, True) for f in range(0, 150)}
    )
    tracks = {"1": track_ol, "2": track_wr}

    presnap_evt = ActionEvent(
        video_name="RPO_1",
        video_id="1",
        action="Action_PreSnap",
        start_frame=0,
        annotated_frame=0,
        actor_track_id="ALL",
        target_kind="all"
    )
    run_block_evt = ActionEvent(
        video_name="RPO_1",
        video_id="1",
        action="Action_RunBlock",
        start_frame=88,
        annotated_frame=88,
        actor_track_id="1",
        resolved_xml_track_id="1",
        target_kind="track_id"
    )

    metadata = {"play_tag": "Play_RPO", "play_name": "RPO", "start_frame": 0, "stop_frame": 149}
    segments, warnings = infer_action_segments([presnap_evt, run_block_evt], tracks, metadata, config)

    # Track 2 (no post-snap action): PreSnap 0..86, Action_None 87..149
    wr_presnap = [s for s in segments if s.xml_track_id == "2" and s.action == "Action_PreSnap"]
    assert len(wr_presnap) == 1
    assert wr_presnap[0].start_frame == 0
    assert wr_presnap[0].end_frame == 86

    wr_none = [s for s in segments if s.xml_track_id == "2" and s.action == "Action_None"]
    assert len(wr_none) == 1
    assert wr_none[0].start_frame == 87
    assert wr_none[0].end_frame == 149


def test_regression_source_identities():
    """25. Current source rows contain required authoritative identities."""
    config = load_config()

    # PuntReturnTouchdown_9: Snap Receive actor 1, Catch Punt/Ball Carry/Cross Goal Line actor 27
    prt_events, _, prt_errs = parse_wide_action_csv(
        "data/key_actions/PuntReturnTouchdown.csv", config, target_video="9"
    )
    assert not prt_errs
    assert any(e.action == "Action_SnapReceive" and e.actor_track_id == "1" for e in prt_events)
    assert any(e.action == "Action_CatchPunt" and e.actor_track_id == "27" for e in prt_events)
    assert any(e.action == "Action_BallCarry" and e.actor_track_id == "27" for e in prt_events)
    assert any(e.action == "Action_CrossGoalLine" and e.actor_track_id == "27" for e in prt_events)

    # KickoffReturnTouchdown_13: Catch Kick/Ball Carry/Cross Goal Line actor 45
    krt13_events, _, krt13_errs = parse_wide_action_csv(
        "data/key_actions/KickoffReturnTouchdown.csv", config, target_video="13"
    )
    assert not krt13_errs
    assert any(e.action == "Action_CatchKick" and e.actor_track_id == "45" for e in krt13_events)
    assert any(e.action == "Action_BallCarry" and e.actor_track_id == "45" for e in krt13_events)
    assert any(e.action == "Action_CrossGoalLine" and e.actor_track_id == "45" for e in krt13_events)

    # KickoffReturnTouchdown_14: Catch Kick/Ball Carry/Cross Goal Line actor 13
    krt14_events, _, krt14_errs = parse_wide_action_csv(
        "data/key_actions/KickoffReturnTouchdown.csv", config, target_video="14"
    )
    assert not krt14_errs
    assert any(e.action == "Action_CatchKick" and e.actor_track_id == "13" for e in krt14_events)
    assert any(e.action == "Action_BallCarry" and e.actor_track_id == "13" for e in krt14_events)
    assert any(e.action == "Action_CrossGoalLine" and e.actor_track_id == "13" for e in krt14_events)


def test_rpo_1_pipeline_regression():
    """26. RPO_1 generates with canonical play label, non-temporal route, PreSnap ending at 86, and Action_None starting at 87."""
    from play_annotation_generator.batch_pipeline import run_generate_and_enrich_pipeline
    config = load_config()

    with tempfile.TemporaryDirectory() as tmpdir:
        tracks, metadata, events, segments, dense, metrics, warns, errs = run_generate_and_enrich_pipeline(
            gt_path="data/tracking/RPO/RPO_1_cvat_mot.zip",
            labels_path=None,
            template_path="docs/JetSweepTemplate.xml",
            key_actions_csv="data/key_actions/RPO.csv",
            player_tracks_csv="data/player_tracks/RPO.csv",
            config=config,
            output_dir=tmpdir,
            target_video_name="RPO_1",
            target_video_id="1"
        )
        assert len(errs) == 0, f"Unexpected errors: {errs}"
        assert metadata.get("play_tag") == "Play_Pass_RPO" or metadata.get("play_tag") == "Play_RPO"

        non_temp = metadata.get("non_temporal_action_descriptors", [])
        assert any(d.get("canonical_action") == "Action_RunPostRoute" and d.get("actor_track_id") == "7" for d in non_temp)

        route_segs = [s for s in segments if s.action == "Action_RunPostRoute"]
        assert len(route_segs) == 0

        rb_segs = [s for s in segments if s.action == "Action_RunBlock"]
        assert len(rb_segs) >= 1
        assert any(s.start_frame == 88 for s in rb_segs)

        for seg in segments:
            if seg.action == "Action_PreSnap":
                assert seg.end_frame <= 86, f"PreSnap segment extended past 86: {seg}"


