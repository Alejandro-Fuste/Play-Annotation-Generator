from typing import Any, Dict, List, Tuple, Optional
import os

from .models import Track, ActionEvent, ActionSegment, DenseActionAnnotation
from .cvat_xml_parser import parse_cvat_xml
from .wide_action_csv_parser import parse_wide_action_csv
from .action_event_normalizer import normalize_and_match_events
from .action_rules import infer_action_segments
from .validators import run_validation_checks

def run_enrichment_pipeline(
    xml_path: str,
    csv_path: str,
    config: Dict[str, Any],
    target_video: Optional[str] = None
) -> Tuple[Dict[str, Track], Dict[str, Any], List[ActionEvent], List[ActionSegment], List[DenseActionAnnotation], Dict[str, Any], List[str], List[str]]:
    """
    Orchestrates the entire XML and CSV enrichment process.
    
    Returns:
        A tuple of:
          - tracks: parsed XML tracks dict
          - metadata: parsed XML metadata dict
          - events: resolved ActionEvent list
          - segments: inferred ActionSegment list
          - dense_annotations: generated DenseActionAnnotation list
          - validation_metrics: dict of counts/stats
          - warnings: list of warning strings
          - errors: list of error strings
    """
    warnings: List[str] = []
    errors: List[str] = []
    
    # 1. Parse CVAT XML
    player_lbl = config.get("labels", {}).get("player_label", "player")
    ball_lbl = config.get("labels", {}).get("ball_label", "ball")
    tracks, metadata = parse_cvat_xml(xml_path, player_lbl, ball_lbl)
    
    # 2. Parse wide CSV
    events, all_csv_rows, csv_errors = parse_wide_action_csv(csv_path, config, target_video)
    errors.extend(csv_errors)
    
    # If no target video was specified and we found multiple videos, print warning and pick first
    if target_video is None and all_csv_rows:
        col_video_name = config.get("csv", {}).get("columns", {}).get("video_name", "video_name")
        first_video_name = all_csv_rows[0].get(col_video_name)
        if first_video_name:
            target_video = first_video_name
            # Re-parse with target video to filter events
            events, _, csv_errors_retry = parse_wide_action_csv(csv_path, config, target_video)
            
    # Set video metadata in output
    metadata["video_name"] = target_video if target_video else "Unknown_Video"
    
    # 3. Normalize and match track IDs
    resolved_events, match_issues = normalize_and_match_events(events, tracks, config)
    for issue in match_issues:
        if "position/team_side missing" in issue:
            warnings.append(issue)
        else:
            errors.append(issue)
    
    # Extract play-level fields from events
    play_tag = "Play_Unknown"
    result_tag = "Result_Unknown"
    
    for ev in resolved_events:
        if ev.play_tag and ev.play_tag != "Play_Unknown":
            play_tag = ev.play_tag
        if ev.result_tag and ev.result_tag != "Result_Unknown":
            result_tag = ev.result_tag
            
    # Result frame is the last frame of the video clip (stop_frame)
    result_frame = metadata.get("stop_frame", None)
    
    metadata["play_tag"] = play_tag
    metadata["result_tag"] = result_tag
    metadata["result_frame"] = result_frame
    
    # 4. Infer action segments
    segments, rules_warnings = infer_action_segments(resolved_events, tracks, metadata, config)
    warnings.extend(rules_warnings)
    
    # 5. Run validation checks
    validation_metrics, val_warnings, val_errors = run_validation_checks(tracks, resolved_events, segments, metadata, config)
    warnings.extend(val_warnings)
    errors.extend(val_errors)
    
    # 6. Generate dense frame-level annotations
    dense_annotations: List[DenseActionAnnotation] = []
    
    # Pre-build lookup for segments: track_id -> list of segments
    segs_by_track: Dict[str, List[ActionSegment]] = {}
    for seg in segments:
        segs_by_track.setdefault(seg.xml_track_id, []).append(seg)
        
    start_frame = metadata.get("start_frame", 0)
    stop_frame = metadata.get("stop_frame", 0)
    
    policy_cfg = config.get("action_policy", {})
    default_offense_act = policy_cfg.get("default_unlabeled_offense_action", "Action_Unknown")
    default_defense_act = policy_cfg.get("default_unlabeled_defense_action", "Action_Defense_NotAnnotated")
    missing_box_policy = policy_cfg.get("missing_box_policy", "skip")
    
    for xml_track_id, track in tracks.items():
        if track.label != player_lbl:
            continue
            
        is_offense = track.team_side == "offense"
        track_segs = segs_by_track.get(xml_track_id, [])
        
        # We loop over all frames in the video
        for f in range(start_frame, stop_frame + 1):
            box = track.boxes_by_frame.get(f)
            if box is None or box.outside:
                # No box exists or player is outside on this frame
                # Check if there is an active segment on this frame and handle missing box policy
                has_active_seg = any(seg.start_frame <= f <= seg.end_frame for seg in track_segs)
                if has_active_seg and missing_box_policy == "error":
                    errors.append(f"Track '{xml_track_id}' is missing a visible box at frame {f} which is inside an action range.")
                continue
                
            # Find active action segment for this track on this frame
            active_action = None
            for seg in track_segs:
                if seg.start_frame <= f <= seg.end_frame:
                    active_action = seg.action
                    break
                    
            if active_action is None:
                # No active action segment, assign default unlabeled action
                active_action = default_offense_act if is_offense else default_defense_act
                
            # Compute bbox coordinates
            bbox_xyxy = [box.xtl, box.ytl, box.xbr, box.ybr]
            w = box.xbr - box.xtl
            h = box.ybr - box.ytl
            bbox_xywh = [box.xtl, box.ytl, w, h]
            
            # Map undefined positions or team_sides
            resolved_pos = track.position if track.position and track.position != "undefined" else "Position_Unknown"
            resolved_team = track.team_side if track.team_side and track.team_side != "undefined" else "Team_Unknown"
            
            dense_ann = DenseActionAnnotation(
                frame=f,
                actor_track_id=track.custom_track_id if track.custom_track_id else xml_track_id,
                xml_track_id=xml_track_id,
                position=resolved_pos,
                team_side=resolved_team,
                action=active_action,
                bbox_xyxy=bbox_xyxy,
                bbox_xywh=bbox_xywh,
                source="xml_geometry_csv_action"
            )
            dense_annotations.append(dense_ann)
            
    return tracks, metadata, resolved_events, segments, dense_annotations, validation_metrics, warnings, errors
