from typing import Any, Dict, List, Tuple
from .models import ActionEvent, ActionSegment, Track

def run_validation_checks(
    tracks: Dict[str, Track],
    events: List[ActionEvent],
    segments: List[ActionSegment],
    metadata: Dict[str, Any],
    config: Dict[str, Any]
) -> Tuple[Dict[str, Any], List[str], List[str]]:
    """
    Runs pipeline-level validation checks.
    
    Returns:
        A tuple of:
          - dict of validation metrics (counts, stats)
          - list of warnings
          - list of errors (which might halt execution in strict mode)
    """
    warnings: List[str] = []
    errors: List[str] = []
    
    start_frame = metadata.get("start_frame", 0)
    stop_frame = metadata.get("stop_frame", 0)
    
    # 1. Gather count statistics
    num_tracks = len(tracks)
    num_players = sum(1 for t in tracks.values() if t.label == config.get("labels", {}).get("player_label", "player"))
    num_balls = sum(1 for t in tracks.values() if t.label == config.get("labels", {}).get("ball_label", "ball"))
    num_events = len(events)
    num_segments = len(segments)
    
    # 2. Check XML Bounding Boxes for Coordinate Sanity (Spec 6.17)
    invalid_box_count = 0
    for xml_id, track in tracks.items():
        for frame, box in track.boxes_by_frame.items():
            if not box.outside:
                if box.xbr <= box.xtl or box.ybr <= box.ytl:
                    warnings.append(f"Track '{xml_id}' frame {frame} has invalid bounding box: [{box.xtl}, {box.ytl}, {box.xbr}, {box.ybr}].")
                    invalid_box_count += 1
                    
    # 3. Check for CSV actions starting on a frame where player has no box (Spec 6.6)
    for seg in segments:
        track = tracks.get(seg.xml_track_id)
        if not track:
            continue
        
        # Check start frame specifically
        start_box = track.boxes_by_frame.get(seg.start_frame)
        if start_box is None or start_box.outside:
            warnings.append(f"Action '{seg.action}' for track '{seg.xml_track_id}' starts at frame {seg.start_frame}, but the player has no visible bounding box on this frame.")
            
        # Check for missing boxes in the entire action range
        missing_boxes_in_range = 0
        for f in range(seg.start_frame, seg.end_frame + 1):
            box = track.boxes_by_frame.get(f)
            if box is None or box.outside:
                missing_boxes_in_range += 1
                
        if missing_boxes_in_range > 0:
            warnings.append(f"Action '{seg.action}' range [{seg.start_frame}-{seg.end_frame}] for track '{seg.xml_track_id}' has {missing_boxes_in_range} frames without a visible bounding box.")

    # 4. Check for multiple primary actions per player per frame (Spec 3.5 / 6.8)
    # Check for any overlapping segments for the same track
    segments_by_track = {}
    for seg in segments:
        segments_by_track.setdefault(seg.xml_track_id, []).append(seg)
        
    for xml_id, track_segs in segments_by_track.items():
        # Sort by start frame
        sorted_segs = sorted(track_segs, key=lambda s: s.start_frame)
        for i in range(len(sorted_segs) - 1):
            s1 = sorted_segs[i]
            s2 = sorted_segs[i+1]
            if s1.end_frame >= s2.start_frame:
                err_msg = f"Overlapping action segments for track '{xml_id}': '{s1.action}' [{s1.start_frame}-{s1.end_frame}] and '{s2.action}' [{s2.start_frame}-{s2.end_frame}]."
                errors.append(err_msg)
                
    # 5. Check for unknown action labels (Spec 6.18)
    valid_actions = set(config.get("csv", {}).get("action_columns", {}).values())
    for seg in segments:
        if seg.action not in valid_actions and seg.action != "Action_None":
            warnings.append(f"Track '{seg.xml_track_id}' uses unknown action label '{seg.action}'.")
            
    # 6. Check for undefined track-level attributes (Spec 3.8 / 6.12)
    for xml_id, track in tracks.items():
        if track.label == config.get("labels", {}).get("player_label", "player"):
            if not track.position or track.position == "undefined":
                warnings.append(f"Player track '{xml_id}' has undefined position. Will map to Position_Unknown.")
            if not track.team_side or track.team_side == "undefined":
                warnings.append(f"Player track '{xml_id}' has undefined team_side. Will map to Team_Unknown.")

    metrics = {
        "num_tracks": num_tracks,
        "num_player_tracks": num_players,
        "num_ball_tracks": num_balls,
        "num_events_parsed": num_events,
        "num_action_segments": num_segments,
        "num_invalid_boxes": invalid_box_count,
        "start_frame": start_frame,
        "stop_frame": stop_frame
    }
    
    return metrics, warnings, errors
