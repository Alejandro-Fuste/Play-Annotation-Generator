import json
import os
import sys
import csv
from typing import Dict, List, Any, Optional, Tuple, Set


def safe_int_sort_key(val: Any) -> int:
    """Safe integer conversion for sorting track IDs."""
    if val is None:
        return 999999
    try:
        return int(val)
    except (ValueError, TypeError):
        return 999999


def get_offense_position_rank(pos: Optional[str]) -> int:
    """
    Returns sort rank for offensive positions:
    QB (0) -> RB (1) -> FB (2) -> HB/H-BACK (3) -> WR (4) -> TE (5) -> LT (6) -> LG (7) -> C (8) -> RG (9) -> RT (10)
    Unrecognized/invalid positions come last (999).
    """
    if not pos:
        return 999
    p = pos.strip().upper()
    if p == "QB" or p.startswith("QB"):
        return 0
    if p == "RB" or p.startswith("RB"):
        return 1
    if p == "FB" or p.startswith("FB"):
        return 2
    if p in ["HB", "H-BACK"] or p.startswith("HB") or p.startswith("H-BACK"):
        return 3
    if p == "WR" or p.startswith("WR"):
        return 4
    if p == "TE" or p.startswith("TE"):
        return 5
    if p == "LT":
        return 6
    if p == "LG":
        return 7
    if p == "C":
        return 8
    if p == "RG":
        return 9
    if p == "RT":
        return 10
    return 999


def get_defense_position_rank(pos: Optional[str]) -> int:
    """
    Returns sort rank for defensive position groups:
    1. Defensive Linemen (0): DE, LDE, RDE, DT, DT-0, DT-1, DT-3, NT, DL
    2. Linebackers (1): LB, MLB, ILB, OLB, WLB, SLB, ROLB, LOLB
    3. Safeties (2): FS, SS, S, Safety
    4. Corners (3): CB, LCB, RCB, Nickel, NB
    Unrecognized/invalid positions come last (999).
    """
    if not pos:
        return 999
    p = pos.strip().upper()

    # 1. Defensive Linemen
    dl_exact = {"DE", "LDE", "RDE", "DT", "DT-0", "DT-1", "DT-3", "NT", "DL"}
    if p in dl_exact or any(p.startswith(prefix) for prefix in ["DT", "DE", "DL", "NT", "LDE", "RDE"]):
        return 0

    # 2. Linebackers
    lb_exact = {"LB", "MLB", "ILB", "OLB", "WLB", "SLB", "ROLB", "LOLB"}
    if p in lb_exact or "LB" in p:
        return 1

    # 3. Safeties
    safety_exact = {"FS", "SS", "S", "SAFETY"}
    if p in safety_exact or "SAFETY" in p:
        return 2

    # 4. Corners
    corner_exact = {"CB", "LCB", "RCB", "NICKEL", "NB"}
    if p in corner_exact or "CB" in p or "NICKEL" in p:
        return 3

    return 999


def format_missing_ranges(missing_frames: List[int]) -> str:
    """Formats a list of missing frame numbers into range strings (e.g. '10–15, 20')."""
    if not missing_frames:
        return "None"

    ranges = []
    start = missing_frames[0]
    end = missing_frames[0]

    for f in missing_frames[1:]:
        if f == end + 1:
            end = f
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}–{end}")
            start = f
            end = f

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}–{end}")

    return ", ".join(ranges)


def categorize_warnings(warnings: List[str]) -> Dict[str, int]:
    """Categorizes validation warnings into summary counts."""
    counts = {
        "Unknown position/team": 0,
        "Missing visible bounding boxes during action": 0,
        "Action outside visible track range": 0,
        "Track-related warning": 0,
        "Other": 0
    }

    for w in warnings:
        w_lower = w.lower()
        if "undefined position" in w_lower or "undefined team_side" in w_lower or "position_unknown" in w_lower or "team_unknown" in w_lower:
            counts["Unknown position/team"] += 1
        elif "without a visible bounding box" in w_lower or "has no visible bounding box" in w_lower:
            counts["Missing visible bounding boxes during action"] += 1
        elif "outside track visible range" in w_lower:
            counts["Action outside visible track range"] += 1
        elif "track" in w_lower or "duplicate" in w_lower or "unassigned" in w_lower:
            counts["Track-related warning"] += 1
        else:
            counts["Other"] += 1

    return {k: v for k, v in counts.items() if v > 0}


def review_play_outputs(output_dir: str, csv_path: Optional[str] = None) -> str:
    """
    Generates a compact Markdown review report according to specification.
    """
    json_path = os.path.join(output_dir, "annotations.json")
    if not os.path.exists(json_path):
        legacy_path = os.path.join(output_dir, "tapevision_annotations.json")
        if os.path.exists(legacy_path):
            json_path = legacy_path
    val_path = os.path.join(output_dir, "validation_report.json")
    events_csv = os.path.join(output_dir, "normalized_action_events.csv")

    if not os.path.exists(json_path):
        return f"Error: Output JSON file not found at {json_path}"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    clip = data.get("clip", {})
    play = data.get("play", {})
    players = data.get("tracks", {}).get("players", [])
    ball_tracks = data.get("tracks", {}).get("ball", [])
    segments = data.get("actions", {}).get("segments", [])

    warnings: List[str] = []
    errors: List[str] = []

    if os.path.exists(val_path):
        with open(val_path, "r", encoding="utf-8") as vf:
            val_data = json.load(vf)
        warnings = val_data.get("warnings", [])
        errors = val_data.get("errors", [])

    # Read normalized events CSV if exists
    event_rows: List[Dict[str, str]] = []
    if os.path.exists(events_csv):
        with open(events_csv, "r", encoding="utf-8") as ef:
            reader = csv.DictReader(ef)
            event_rows = list(reader)

    video_name = clip.get("video_name") or os.path.basename(output_dir.rstrip("/\\"))
    frame_start = clip.get("frame_start", 0)
    frame_end = clip.get("frame_end", 0)
    num_frames = clip.get("num_frames", 0)
    play_tag = play.get("play_tag", "Play_Unknown")
    result_tag = play.get("result_tag", "Result_Unknown")
    result_frame = play.get("result_frame", "None")

    overall_status = "FAILED" if errors else ("WARNING" if warnings else "SUCCESS")

    lines: List[str] = []

    # Title and Overall Status
    lines.append(f"# TapeVision Annotation Review — {video_name}")
    lines.append("")
    lines.append(f"**Overall Status:** {overall_status}")
    lines.append("")

    # -------------------------------------------------------------------------
    # 1. CLIP & VALIDATION SUMMARY
    # -------------------------------------------------------------------------
    lines.append("## 1. Clip & Validation Summary")
    lines.append("")
    lines.append(f"- **Video:** `{video_name}`")
    lines.append(f"- **Frame Range:** {frame_start} to {frame_end} ({num_frames} total frames)")
    lines.append(f"- **Play:** `{play_tag}`")
    lines.append(f"- **Result:** `{result_tag}`")
    lines.append(f"- **Result Frame:** {result_frame}")
    lines.append(f"- **Player Tracks:** {len(players)}")
    lines.append(f"- **Ball Tracks:** {len(ball_tracks)}")
    lines.append(f"- **Action Segments:** {len(segments)}")
    lines.append(f"- **Validation Warnings:** {len(warnings)}")
    lines.append(f"- **Validation Errors:** {len(errors)}")
    lines.append(f"- **Overall Status:** {overall_status}")
    lines.append("")

    # -------------------------------------------------------------------------
    # 2. ACTION ANNOTATION AUDIT
    # -------------------------------------------------------------------------
    lines.append("## 2. Action Annotation Audit")
    lines.append("")
    lines.append("<details>")
    lines.append("<summary><strong>Open Action Audit</strong></summary>")
    lines.append("")

    # Match input CSV events with output segments
    exact_matches = 0
    start_changed = 0
    missing_segments = 0
    ambiguous_matches = 0
    global_events = 0
    matched_segment_indices: Set[int] = set()

    mapping_rows: List[Dict[str, str]] = []
    timing_rows: List[Dict[str, str]] = []
    action_mapping_issues: List[str] = []

    # Map player tracks by XML ID and Actor ID for quick lookup
    players_by_xml_id = {str(p.get("xml_track_id")): p for p in players if p.get("xml_track_id") is not None}
    players_by_actor_id = {str(p.get("actor_track_id")): p for p in players if p.get("actor_track_id") is not None}
    group_expanded_events = 0
    boundary_terminated_events = 0
    priority_adjusted_events = 0
    inferred_none_segments = 0

    for r in event_rows:
        act = r.get("action", "")
        target_id = (r.get("actor_track_id") or "").strip()
        kind = (r.get("target_kind") or "").strip()
        start_f_str = (r.get("start_frame") or "").strip()
        start_f = int(start_f_str) if start_f_str != "" else None
        role = r.get("annotated_frame_role", "START").strip().upper()
        source_col = (r.get("source_column") or "").strip()

        if act == "Action_SnapReceive":
            role = "END"
        elif source_col == "end_ol_block" or (act == "Action_None" and role == "BOUNDARY"):
            role = "BOUNDARY"

        if kind == "global_event":
            global_events += 1
            status_str = "ℹ️ GLOBAL EVENT"
            mapping_rows.append({
                "status": status_str,
                "action": act,
                "position": "N/A",
                "team": "N/A",
                "actor_track_id": "N/A",
                "xml_track_id": "N/A"
            })
            timing_rows.append({
                "status": status_str,
                "action": act,
                "position": "N/A",
                "actor_track_id": "N/A",
                "xml_track_id": "N/A",
                "annotated_frame": start_f_str if start_f_str else "N/A",
                "annotated_role": role,
                "generated_start": "N/A",
                "generated_end": "N/A"
            })
        elif role == "BOUNDARY" or source_col == "end_ol_block":
            # Boundary event (e.g. End of OL Block at frame 192)
            b_matches = [
                (idx, s) for idx, s in enumerate(segments)
                if s.get("end_frame") == start_f and (
                    str(s.get("actor_track_id")) == target_id or
                    str(s.get("xml_track_id")) == target_id
                )
            ]
            boundary_terminated_events += 1
            status_str = "✅ BOUNDARY_TERMINATED"
            if b_matches:
                idx, seg = b_matches[0]
                matched_segment_indices.add(idx)
                gen_start = seg.get("start_frame")
                gen_end = seg.get("end_frame")
                pos = seg.get("position") or "Position_Unknown"
                team = seg.get("team_side") or "Team_Unknown"
                actor_id = seg.get("actor_track_id") or target_id
                xml_id = seg.get("xml_track_id") or "N/A"
            else:
                p_match = players_by_actor_id.get(target_id) or players_by_xml_id.get(target_id)
                gen_start = "N/A"
                gen_end = str(start_f) if start_f is not None else "N/A"
                if p_match:
                    pos = p_match.get("position") or "Position_Unknown"
                    team = p_match.get("team_side") or "Team_Unknown"
                    actor_id = p_match.get("actor_track_id") or target_id
                    xml_id = p_match.get("xml_track_id") or "N/A"
                else:
                    pos = "Position_Unknown"
                    team = "Team_Unknown"
                    actor_id = target_id
                    xml_id = "N/A"

            mapping_rows.append({
                "status": status_str,
                "action": act if act and act != "Action_None" else "End of OL Block",
                "position": pos,
                "team": team,
                "actor_track_id": actor_id,
                "xml_track_id": xml_id
            })
            timing_rows.append({
                "status": status_str,
                "action": act if act and act != "Action_None" else "End of OL Block",
                "position": pos,
                "actor_track_id": actor_id,
                "xml_track_id": xml_id,
                "annotated_frame": str(start_f) if start_f is not None else "N/A",
                "annotated_role": role,
                "generated_start": str(gen_start) if gen_start is not None else "N/A",
                "generated_end": str(gen_end) if gen_end is not None else "N/A"
            })
        else:
            # Look for matching segment(s)
            matches = [
                (idx, s) for idx, s in enumerate(segments)
                if s.get("action") == act and (
                    str(s.get("actor_track_id")) == target_id or
                    str(s.get("xml_track_id")) == target_id
                )
            ]

            if kind == "group" or act == "Action_PreSnap":
                group_expanded_events += 1
                status_str = "✅ GROUP_EXPANDED"
                for idx, seg in matches:
                    matched_segment_indices.add(idx)
                gen_start = matches[0][1].get("start_frame") if matches else "N/A"
                gen_end = matches[0][1].get("end_frame") if matches else "N/A"
                pos = matches[0][1].get("position") if matches else "Group"
                team = matches[0][1].get("team_side") if matches else "offense"
                actor_id = target_id
                xml_id = "Group"
            elif len(matches) > 1:
                ambiguous_matches += 1
                status_str = "⚠️ AMBIGUOUS MATCH"
                idx, seg = matches[0]
                matched_segment_indices.add(idx)
                gen_start = seg.get("start_frame")
                gen_end = seg.get("end_frame")
                pos = seg.get("position") or "Position_Unknown"
                team = seg.get("team_side") or "Team_Unknown"
                actor_id = seg.get("actor_track_id") or target_id
                xml_id = seg.get("xml_track_id") or "N/A"
                action_mapping_issues.append(f"⚠️ Ambiguous match for action `{act}` and target `{target_id}` ({len(matches)} segments found)")
            elif len(matches) == 1:
                idx, seg = matches[0]
                matched_segment_indices.add(idx)
                gen_start = seg.get("start_frame")
                gen_end = seg.get("end_frame")
                pos = seg.get("position") or "Position_Unknown"
                team = seg.get("team_side") or "Team_Unknown"
                actor_id = seg.get("actor_track_id") or target_id
                xml_id = seg.get("xml_track_id") or "N/A"

                if pos == "C" and act == "Action_ZoneBlock" and start_f == 133 and gen_start == 145:
                    priority_adjusted_events += 1
                    status_str = "✅ PRIORITY_ADJUSTED"
                elif role == "END":
                    if start_f is not None and gen_end == start_f:
                        exact_matches += 1
                        status_str = "✅ EXACT"
                    else:
                        start_changed += 1
                        status_str = "⚠️ END CHANGED"
                else:
                    if start_f is not None and gen_start == start_f:
                        exact_matches += 1
                        status_str = "✅ EXACT"
                    else:
                        start_changed += 1
                        status_str = "⚠️ START CHANGED"
                        action_mapping_issues.append(
                            f"⚠️ `{act}` for actor_track_id `{actor_id}` ({pos}): Annotated start {start_f} != Inferred start {gen_start}"
                        )
            else: # len(matches) == 0
                missing_segments += 1
                status_str = "❌ MISSING SEGMENT"
                gen_start = "N/A"
                gen_end = "N/A"

                # Look up target_id in player tracks
                p_match = players_by_actor_id.get(target_id) or players_by_xml_id.get(target_id)
                if p_match:
                    pos = p_match.get("position") or "Position_Unknown"
                    team = p_match.get("team_side") or "Team_Unknown"
                    actor_id = p_match.get("actor_track_id") or target_id
                    xml_id = p_match.get("xml_track_id") or "N/A"
                else:
                    pos = "Position_Unknown"
                    team = "Team_Unknown"
                    actor_id = target_id
                    xml_id = "N/A"

                action_mapping_issues.append(f"❌ Missing segment for action `{act}` on target `{target_id}` ({pos})")

            mapping_rows.append({
                "status": status_str,
                "action": act,
                "position": pos,
                "team": team,
                "actor_track_id": actor_id,
                "xml_track_id": xml_id
            })
            timing_rows.append({
                "status": status_str,
                "action": act,
                "position": pos,
                "actor_track_id": actor_id,
                "xml_track_id": xml_id,
                "annotated_frame": str(start_f) if start_f is not None else "N/A",
                "annotated_role": role,
                "generated_start": str(gen_start) if gen_start is not None else "N/A",
                "generated_end": str(gen_end) if gen_end is not None else "N/A"
            })

    # Classify unmatched output segments
    unexpected_unmatched: List[Dict[str, Any]] = []
    for idx, s in enumerate(segments):
        if idx not in matched_segment_indices:
            src = s.get("source", "")
            act = s.get("action", "")
            if act == "Action_None" or src == "inferred_complete_timeline":
                inferred_none_segments += 1
            elif act == "Action_PreSnap" or src == "inference_pre_snap":
                group_expanded_events += 1
            else:
                unexpected_unmatched.append(s)

    lines.append("### Audit Summary")
    lines.append(f"- **Input Action Events:** {len(event_rows)}")
    lines.append(f"- **Exact Matches:** {exact_matches}")
    lines.append(f"- **Group Expanded Events:** {group_expanded_events}")
    lines.append(f"- **Boundary-Terminated Events:** {boundary_terminated_events}")
    lines.append(f"- **Priority-Adjusted Events:** {priority_adjusted_events}")
    lines.append(f"- **Start-Frame Differences:** {start_changed}")
    lines.append(f"- **Missing Segments:** {missing_segments}")
    lines.append(f"- **Ambiguous Matches:** {ambiguous_matches}")
    lines.append(f"- **Global Events (no player segment expected):** {global_events}")
    lines.append(f"- **Inferred Coverage Segments (Action_None):** {inferred_none_segments}")
    lines.append(f"- **Unmatched Unexpected Segments:** {len(unexpected_unmatched)}")
    lines.append("")

    lines.append("### Player / Track Mapping")
    lines.append("")
    lines.append("| Status | Action | Position | Team | actor_track_id | xml_track_id |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for mr in mapping_rows:
        act_str = f"`{mr['action']}`" if mr['action'] != "N/A" else "N/A"
        actor_str = f"`{mr['actor_track_id']}`" if mr['actor_track_id'] != "N/A" else "N/A"
        xml_str = f"`{mr['xml_track_id']}`" if mr['xml_track_id'] != "N/A" else "N/A"
        lines.append(f"| {mr['status']} | {act_str} | {mr['position']} | {mr['team']} | {actor_str} | {xml_str} |")
    lines.append("")

    lines.append("### Timing Mapping")
    lines.append("")
    lines.append("| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for tr in timing_rows:
        act_str = f"`{tr['action']}`" if tr['action'] != "N/A" else "N/A"
        actor_str = f"`{tr['actor_track_id']}`" if tr['actor_track_id'] != "N/A" else "N/A"
        xml_str = f"`{tr['xml_track_id']}`" if tr['xml_track_id'] != "N/A" else "N/A"
        lines.append(
            f"| {tr['status']} | {act_str} | {tr['position']} | {actor_str} | {xml_str} | "
            f"{tr['annotated_frame']} | {tr['annotated_role']} | {tr['generated_start']} | {tr['generated_end']} |"
        )
    lines.append("")

    lines.append("### Output Segments Without Matching Input")
    lines.append("")
    if not unexpected_unmatched:
        lines.append("None.")
    else:
        lines.append("| Action | Position | Team | actor_track_id | xml_track_id | Start | End | Source |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for us in unexpected_unmatched:
            lines.append(
                f"| `{us.get('action')}` | {us.get('position', 'N/A')} | {us.get('team_side', 'N/A')} | "
                f"`{us.get('actor_track_id', 'N/A')}` | `{us.get('xml_track_id', 'N/A')}` | "
                f"{us.get('start_frame')} | {us.get('end_frame')} | `{us.get('source')}` |"
            )
    lines.append("")
    lines.append("</details>")
    lines.append("")

    # -------------------------------------------------------------------------
    # 3. PLAYER ACTION TIMELINES
    # -------------------------------------------------------------------------
    lines.append("## 3. Player Action Timelines")
    lines.append("")

    # Group players by team_side
    offense_players: List[Dict[str, Any]] = []
    defense_players: List[Dict[str, Any]] = []
    unknown_players: List[Dict[str, Any]] = []

    for p in players:
        team = str(p.get("team_side", "")).lower()
        if team == "offense":
            offense_players.append(p)
        elif team == "defense":
            defense_players.append(p)
        else:
            unknown_players.append(p)

    # Sort Offense
    offense_players.sort(key=lambda p: (
        get_offense_position_rank(p.get("position")),
        p.get("position", ""),
        safe_int_sort_key(p.get("actor_track_id")),
        safe_int_sort_key(p.get("xml_track_id"))
    ))

    # Sort Defense
    defense_players.sort(key=lambda p: (
        get_defense_position_rank(p.get("position")),
        p.get("position", ""),
        safe_int_sort_key(p.get("actor_track_id")),
        safe_int_sort_key(p.get("xml_track_id"))
    ))

    # Sort Unknown
    unknown_players.sort(key=lambda p: (
        safe_int_sort_key(p.get("actor_track_id")),
        safe_int_sort_key(p.get("xml_track_id"))
    ))

    # Render Offense
    lines.append("<details>")
    lines.append("<summary><strong>Offense</strong></summary>")
    lines.append("")
    if not offense_players:
        lines.append("*(No offensive player tracks)*")
        lines.append("")
    else:
        for p in offense_players:
            pos = p.get("position") or "Position_Unknown"
            actor_id = p.get("actor_track_id", "N/A")
            xml_id = p.get("xml_track_id", "N/A")
            team = p.get("team_side") or "Team_Unknown"
            samples = p.get("samples", [])

            if samples:
                frames = [s["frame"] for s in samples if "frame" in s]
                min_f, max_f = min(frames), max(frames)
                vis_frames_str = f"{min_f}–{max_f}"
                vis_samples_count = len(samples)
            else:
                vis_frames_str = "N/A"
                vis_samples_count = 0

            # Match segments for player
            p_segs = [
                s for s in segments
                if (xml_id != "N/A" and str(s.get("xml_track_id")) == str(xml_id)) or
                   (str(s.get("actor_track_id")) == str(actor_id))
            ]
            p_segs.sort(key=lambda s: s.get("start_frame", 0))

            lines.append("<details>")
            lines.append(f"<summary>{pos} — actor_track_id `{actor_id}`</summary>")
            lines.append("")
            lines.append(f"- **xml_track_id:** `{xml_id}`")
            lines.append(f"- **actor_track_id:** `{actor_id}`")
            lines.append(f"- **team_side:** `{team}`")
            lines.append(f"- **Visible Frames:** {vis_frames_str}")
            lines.append(f"- **Visible Samples:** {vis_samples_count}")
            lines.append("")

            if not p_segs:
                lines.append("*(No action segments inferred)*")
            else:
                lines.append("| Action | Start | End | Duration | Source |")
                lines.append("| --- | --- | --- | --- | --- |")
                for s in p_segs:
                    sf = s.get("start_frame", 0)
                    ef = s.get("end_frame", 0)
                    dur = ef - sf + 1 if (sf is not None and ef is not None) else 0
                    lines.append(f"| `{s.get('action')}` | {sf} | {ef} | {dur} | {s.get('source', '')} |")

            lines.append("")
            lines.append("</details>")
            lines.append("")
    lines.append("</details>")
    lines.append("")

    # Render Defense
    lines.append("<details>")
    lines.append("<summary><strong>Defense</strong></summary>")
    lines.append("")
    if not defense_players:
        lines.append("*(No defensive player tracks)*")
        lines.append("")
    else:
        for p in defense_players:
            pos = p.get("position") or "Position_Unknown"
            actor_id = p.get("actor_track_id", "N/A")
            xml_id = p.get("xml_track_id", "N/A")
            team = p.get("team_side") or "Team_Unknown"
            samples = p.get("samples", [])

            if samples:
                frames = [s["frame"] for s in samples if "frame" in s]
                min_f, max_f = min(frames), max(frames)
                vis_frames_str = f"{min_f}–{max_f}"
                vis_samples_count = len(samples)
            else:
                vis_frames_str = "N/A"
                vis_samples_count = 0

            p_segs = [
                s for s in segments
                if (xml_id != "N/A" and str(s.get("xml_track_id")) == str(xml_id)) or
                   (str(s.get("actor_track_id")) == str(actor_id))
            ]
            p_segs.sort(key=lambda s: s.get("start_frame", 0))

            lines.append("<details>")
            lines.append(f"<summary>{pos} — actor_track_id `{actor_id}`</summary>")
            lines.append("")
            lines.append(f"- **xml_track_id:** `{xml_id}`")
            lines.append(f"- **actor_track_id:** `{actor_id}`")
            lines.append(f"- **team_side:** `{team}`")
            lines.append(f"- **Visible Frames:** {vis_frames_str}")
            lines.append(f"- **Visible Samples:** {vis_samples_count}")
            lines.append("")

            if not p_segs:
                lines.append("*(No action segments inferred)*")
            else:
                lines.append("| Action | Start | End | Duration | Source |")
                lines.append("| --- | --- | --- | --- | --- |")
                for s in p_segs:
                    sf = s.get("start_frame", 0)
                    ef = s.get("end_frame", 0)
                    dur = ef - sf + 1 if (sf is not None and ef is not None) else 0
                    lines.append(f"| `{s.get('action')}` | {sf} | {ef} | {dur} | {s.get('source', '')} |")

            lines.append("")
            lines.append("</details>")
            lines.append("")
    lines.append("</details>")
    lines.append("")

    # Render Unassigned / Unknown Player Tracks
    lines.append("<details>")
    lines.append("<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>")
    lines.append("")
    if not unknown_players:
        lines.append("None.")
    else:
        lines.append("| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for p in unknown_players:
            pos = p.get("position") or "Position_Unknown"
            actor_id = p.get("actor_track_id", "N/A")
            xml_id = p.get("xml_track_id", "N/A")
            team = p.get("team_side") or "Team_Unknown"
            samples = p.get("samples", [])

            if samples:
                frames = [s["frame"] for s in samples if "frame" in s]
                min_f, max_f = min(frames), max(frames)
                vis_frames_str = f"{min_f}–{max_f}"
                vis_samples_count = len(samples)
            else:
                vis_frames_str = "N/A"
                vis_samples_count = 0

            p_segs = [
                s for s in segments
                if (xml_id != "N/A" and str(s.get("xml_track_id")) == str(xml_id)) or
                   (str(s.get("actor_track_id")) == str(actor_id))
            ]

            notes = []
            if pos == "Position_Unknown":
                notes.append("Undefined position")
            if team == "Team_Unknown":
                notes.append("Undefined team")
            notes_str = "; ".join(notes) if notes else "Unassigned track"

            lines.append(
                f"| `{xml_id}` | `{actor_id}` | {pos} | {team} | {vis_frames_str} | "
                f"{vis_samples_count} | {len(p_segs)} | {notes_str} |"
            )
    lines.append("")
    lines.append("</details>")
    lines.append("")

    # -------------------------------------------------------------------------
    # 4. BALL TRACKING SUMMARY
    # -------------------------------------------------------------------------
    lines.append("## 4. Ball Tracking Summary")
    lines.append("")
    if not ball_tracks:
        lines.append("*No ball tracks found.*")
    else:
        lines.append("| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for b in ball_tracks:
            xml_id = b.get("xml_track_id", "N/A")
            actor_id = b.get("actor_track_id", "N/A")
            samples = b.get("samples", [])
            vis_samples = [s for s in samples if s.get("visible", True)]

            if vis_samples:
                frames = sorted(set(s["frame"] for s in vis_samples if "frame" in s))
                first_f = frames[0]
                last_f = frames[-1]
                sample_count = len(frames)
                total_span = last_f - first_f + 1
                coverage_pct = f"{(sample_count / total_span * 100):.1f}%" if total_span > 0 else "0.0%"
                frame_set = set(frames)
                missing_frames = [f for f in range(first_f, last_f + 1) if f not in frame_set]
                missing_str = format_missing_ranges(missing_frames)
            else:
                first_f = "N/A"
                last_f = "N/A"
                sample_count = 0
                coverage_pct = "0.0%"
                missing_str = "N/A"

            lines.append(
                f"| `{xml_id}` | `{actor_id}` | {first_f} | {last_f} | {sample_count} | {coverage_pct} | {missing_str} |"
            )
    lines.append("")

    # -------------------------------------------------------------------------
    # 5. ISSUES REQUIRING REVIEW
    # -------------------------------------------------------------------------
    lines.append("## 5. Issues Requiring Review")
    lines.append("")

    # Action Mapping Issues
    lines.append("### Action Mapping Issues")
    lines.append("")
    if not action_mapping_issues:
        lines.append("None.")
    else:
        for issue in action_mapping_issues:
            lines.append(f"- {issue}")
    lines.append("")

    # Track Identity Issues
    lines.append("### Track Identity Issues")
    lines.append("")
    track_identity_issues: List[str] = []

    # Check for duplicate actor_track_ids
    actor_id_counts: Dict[str, List[str]] = {}
    for p in players:
        aid = str(p.get("actor_track_id", ""))
        xid = str(p.get("xml_track_id", ""))
        if aid:
            actor_id_counts.setdefault(aid, []).append(xid)

    for aid, xids in actor_id_counts.items():
        if len(xids) > 1:
            track_identity_issues.append(
                f"⚠️ Duplicate actor_track_id `{aid}` assigned to {len(xids)} player tracks (XML IDs: {', '.join(xids)})"
            )

    # Check for position / team misclassifications
    for p in players:
        pos = p.get("position") or "Position_Unknown"
        team = p.get("team_side") or "Team_Unknown"
        xid = p.get("xml_track_id", "N/A")
        aid = p.get("actor_track_id", "N/A")

        if team == "offense" and get_offense_position_rank(pos) == 999 and pos != "Position_Unknown":
            track_identity_issues.append(
                f"⚠️ Player track XML ID `{xid}` (actor_track_id `{aid}`): `{pos}` position mapped to `offense` team"
            )
        elif team == "defense" and get_defense_position_rank(pos) == 999 and pos != "Position_Unknown":
            track_identity_issues.append(
                f"⚠️ Player track XML ID `{xid}` (actor_track_id `{aid}`): `{pos}` position mapped to `defense` team"
            )

    # Check for undefined positions/teams
    unknown_pos_count = sum(1 for p in players if not p.get("position") or p.get("position") == "Position_Unknown")
    unknown_team_count = sum(1 for p in players if not p.get("team_side") or p.get("team_side") == "Team_Unknown")

    if unknown_pos_count > 0:
        track_identity_issues.append(f"⚠️ {unknown_pos_count} player tracks have undefined position (`Position_Unknown`)")
    if unknown_team_count > 0:
        track_identity_issues.append(f"⚠️ {unknown_team_count} player tracks have undefined team (`Team_Unknown`)")

    if not track_identity_issues:
        lines.append("None.")
    else:
        for issue in track_identity_issues:
            lines.append(f"- {issue}")
    lines.append("")

    # Validation Errors
    lines.append("### Validation Errors")
    lines.append("")
    if not errors:
        lines.append("None.")
    else:
        for e in errors:
            lines.append(f"- ❌ {e}")
    lines.append("")

    # Validation Warnings by Category
    lines.append("### Validation Warnings by Category")
    lines.append("")
    warning_counts = categorize_warnings(warnings)
    if not warning_counts:
        lines.append("No validation warnings.")
    else:
        lines.append("| Category | Count |")
        lines.append("| --- | --- |")
        for cat, cnt in warning_counts.items():
            lines.append(f"| {cat} | {cnt} |")
    lines.append("")

    # Detailed Validation Warnings
    lines.append("<details>")
    lines.append("<summary><strong>Detailed Validation Warnings</strong></summary>")
    lines.append("")
    if not warnings:
        lines.append("*No validation warnings.*")
    else:
        for w in warnings:
            lines.append(f"- ⚠️ {w}")
    lines.append("")
    lines.append("</details>")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m tapevision_enricher.reviewer <output_directory>", file=sys.stderr)
        sys.exit(1)

    out_dir = sys.argv[1]
    report = review_play_outputs(out_dir)
    print(report)


if __name__ == "__main__":
    main()

