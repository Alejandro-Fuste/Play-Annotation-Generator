from typing import Any, Dict, List, Tuple, Optional
from .models import ActionEvent, ActionSegment, Track

def infer_action_segments(
    resolved_events: List[ActionEvent],
    tracks: Dict[str, Track],
    metadata: Dict[str, Any],
    config: Dict[str, Any]
) -> Tuple[List[ActionSegment], List[str]]:
    """
    Infers start and end frames for action segments for each player track.
    Implements complete per-player frame coverage with Action_None gap filling,
    paired Ball Snap / Snap Receive intervals, cross-actor transitions, inclusive boundary events,
    Center priority resolution, and validation duration warnings.
    """
    warnings: List[str] = []
    
    # 1. Determine clip boundaries
    start_clip = metadata.get("start_frame", 0)
    stop_clip = metadata.get("stop_frame", 239)
    
    # Find play-end / result frame fallbacks
    result_frame = None
    for event in resolved_events:
        if event.result_frame is not None and event.result_frame > 0:
            result_frame = event.result_frame
            break
            
    play_end_frame = None
    for event in resolved_events:
        if event.action == "Action_PlayEnd" and event.start_frame > 0:
            play_end_frame = event.start_frame
            break
            
    final_play_frame = result_frame if result_frame is not None else play_end_frame
    if final_play_frame is None:
        final_play_frame = stop_clip
        warnings.append(f"No result_frame or PlayEnd action found in CSV. Using final clip frame {stop_clip} as fallback play end.")
    else:
        final_play_frame = min(final_play_frame, stop_clip)
        
    # 2. Paired event detection (Action_BallSnap and Action_SnapReceive)
    ball_snap_events = [e for e in resolved_events if e.action == "Action_BallSnap"]
    snap_receive_events = [e for e in resolved_events if e.action == "Action_SnapReceive"]
    
    ball_snap_start = ball_snap_events[0].annotated_frame if ball_snap_events else None
    snap_receive_end = snap_receive_events[0].annotated_frame if snap_receive_events else None
    
    if ball_snap_events and not snap_receive_events:
        warnings.append("Action_BallSnap present in CSV, but paired Action_SnapReceive is missing.")
    elif snap_receive_events and not ball_snap_events:
        warnings.append("Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.")
        
    if ball_snap_start is not None and snap_receive_end is None:
        snap_receive_end = ball_snap_start

    # Index all events by action name for cross-actor rules
    all_events_by_action: Dict[str, List[int]] = {}
    for e in resolved_events:
        all_events_by_action.setdefault(e.action, []).append(e.annotated_frame)
    for act in all_events_by_action:
        all_events_by_action[act].sort()
        
    # 3. Boundary events indexing (xml_track_id -> list of (boundary_frame, inclusive) tuples)
    boundary_events_by_track: Dict[str, List[Tuple[int, bool]]] = {}
    global_boundary_tuples: List[Tuple[int, bool]] = []
    boundary_rules = config.get("boundary_events", {})
    
    for e in resolved_events:
        if e.event_type == "BOUNDARY" or e.action == "Action_None":
            b_info = boundary_rules.get(e.action, {})
            inclusive = b_info.get("inclusive_boundary", False) or b_info.get("source_column_alias") == "end_ol_block" or e.action == "Action_None"
            global_boundary_tuples.append((e.annotated_frame, inclusive))
            if e.resolved_xml_track_id:
                boundary_events_by_track.setdefault(e.resolved_xml_track_id, []).append((e.annotated_frame, inclusive))
    global_boundary_tuples.sort(key=lambda b: b[0])
                
    # 4. Group primary action events by resolved XML track ID
    events_by_track: Dict[str, List[ActionEvent]] = {}
    for event in resolved_events:
        if (
            event.resolved_xml_track_id
            and event.event_type != "BOUNDARY"
            and event.action not in ("Action_None", "Action_PreSnap")
        ):
            events_by_track.setdefault(event.resolved_xml_track_id, []).append(event)

    rules_cfg = config.get("action_end_rules", {})
    cross_actor_rules = config.get("cross_actor_rules", {})
    terminal_actions = config.get("terminal_actions", {})
    duration_thresholds = config.get("validation_duration_thresholds", {})
    player_lbl = config.get("labels", {}).get("player_label", "player")

    final_segments: List[ActionSegment] = []

    for xml_track_id, track in tracks.items():
        if track.label != player_lbl:
            continue
            
        visible_frames = sorted(track.boxes_by_frame.keys()) if track.boxes_by_frame else []
        if visible_frames:
            min_track_frame = visible_frames[0]
            max_track_frame = visible_frames[-1]
        else:
            min_track_frame = start_clip
            max_track_frame = stop_clip
            
        track_events = events_by_track.get(xml_track_id, [])
        
        # Deduplicate identical events for this track
        deduped_events: List[ActionEvent] = []
        seen_keys = set()
        for e in track_events:
            key = (e.action, e.annotated_frame)
            if key not in seen_keys:
                seen_keys.add(key)
                deduped_events.append(e)
            else:
                warnings.append(f"Deduplicated duplicate event '{e.action}' at frame {e.annotated_frame} for track '{xml_track_id}'.")
                
        # Sort events by annotated frame
        sorted_events = sorted(deduped_events, key=lambda e: e.annotated_frame)
        unique_start_events: List[ActionEvent] = []
        for e in sorted_events:
            if unique_start_events and unique_start_events[-1].annotated_frame == e.annotated_frame:
                prev_e = unique_start_events[-1]
                warnings.append(f"Overlapping action conflict at frame {e.annotated_frame} for track '{xml_track_id}': '{prev_e.action}' vs '{e.action}'. Overriding with '{e.action}'.")
                unique_start_events[-1] = e
            else:
                unique_start_events.append(e)
        sorted_events = unique_start_events

        # PASS 1: Build explicit primary action segments
        explicit_segs: List[ActionSegment] = []

        # A. PreSnap segment (applies to ALL mapped players)
        pre_snap_start = min_track_frame
        
        if sorted_events:
            first_post_snap_start = sorted_events[0].annotated_frame
            if sorted_events[0].action == "Action_SnapReceive" and ball_snap_start is not None:
                first_post_snap_start = ball_snap_start
            pre_snap_end = first_post_snap_start - 1
        else:
            # Player has no explicit post-snap action
            if ball_snap_start is not None:
                pre_snap_end = ball_snap_start - 1
            else:
                pre_snap_end = final_play_frame
                
        if pre_snap_end >= pre_snap_start:
            explicit_segs.append(ActionSegment(
                actor_track_id=track.custom_track_id or xml_track_id,
                xml_track_id=xml_track_id,
                position=track.position,
                team_side=track.team_side,
                action="Action_PreSnap",
                start_frame=pre_snap_start,
                end_frame=pre_snap_end,
                source="inference_pre_snap"
            ))

        # B. Post-snap explicit actions
        track_boundaries = sorted(boundary_events_by_track.get(xml_track_id, []), key=lambda b: b[0])
        
        for i, event in enumerate(sorted_events):
            act_name = event.action
            
            # Start and End frame computation
            if act_name == "Action_SnapReceive":
                seg_start = ball_snap_start if ball_snap_start is not None else event.annotated_frame
                seg_end = event.annotated_frame
            elif act_name == "Action_BallSnap":
                seg_start = event.annotated_frame
                seg_end = snap_receive_end if snap_receive_end is not None else event.annotated_frame
            else:
                seg_start = event.annotated_frame
                seg_end = event.end_frame if event.end_frame is not None else None
                
                # Check cross-actor rules (e.g. Action_Toss -> ends before Action_BallCarry)
                if seg_end is None and act_name in cross_actor_rules:
                    ca_rule = cross_actor_rules[act_name]
                    target_act = ca_rule.get("target_action")
                    if target_act and target_act in all_events_by_action:
                        subsequent = [f for f in all_events_by_action[target_act] if f > seg_start]
                        if subsequent:
                            seg_end = subsequent[0] - 1

                # Check terminal actions (e.g. Action_BallCarry -> ends at final clip frame)
                if seg_end is None and (act_name in terminal_actions or act_name == "Action_BallCarry"):
                    seg_end = stop_clip
                    
                # Check next same-actor explicit action
                if seg_end is None and i + 1 < len(sorted_events):
                    next_evt = sorted_events[i + 1]
                    next_start = next_evt.annotated_frame
                    if next_evt.action == "Action_SnapReceive" and ball_snap_start is not None:
                        next_start = ball_snap_start
                    seg_end = next_start - 1
                    
                # Check boundary events for this track or global blocking boundaries
                if seg_end is None:
                    future_boundaries = [b for b in track_boundaries if b[0] >= seg_start]
                    if not future_boundaries and act_name in ("Action_LeadBlock", "Action_ZoneBlock", "Action_ReachBlock", "Action_DownBlock", "Action_PullBlock", "Action_BlockSecondLevel", "Action_RunBlock"):
                        future_boundaries = [b for b in global_boundary_tuples if b[0] >= seg_start]
                    if future_boundaries:
                        b_frame, b_inc = future_boundaries[0]
                        seg_end = b_frame if b_inc else b_frame - 1
                    else:
                        rule = rules_cfg.get(act_name, {})
                        if rule.get("ends_at_result_or_play_end"):
                            seg_end = final_play_frame
                        else:
                            seg_end = min(final_play_frame, max_track_frame)

            # Clamp to visible track range
            if seg_end is not None:
                seg_end = min(seg_end, max_track_frame)
            seg_start = max(seg_start, min_track_frame)
            
            if seg_end < seg_start:
                warnings.append(f"Segment '{act_name}' for track '{xml_track_id}' has invalid range: start={seg_start}, end={seg_end}. Clamping end to start.")
                seg_end = seg_start
                
            # Check validation duration threshold (DO NOT truncate segment)
            duration = seg_end - seg_start + 1
            thresh_info = duration_thresholds.get(act_name, {})
            warn_limit = thresh_info.get("warn_over_frames")
            if warn_limit and duration > warn_limit:
                warnings.append(
                    f"Validation warning: Action '{act_name}' for track '{xml_track_id}' "
                    f"({track.position or 'Unknown'}) duration {duration} frames exceeds threshold {warn_limit} frames "
                    f"[start={seg_start}, end={seg_end}]."
                )

            explicit_segs.append(ActionSegment(
                actor_track_id=event.actor_track_id or track.custom_track_id or xml_track_id,
                xml_track_id=xml_track_id,
                position=track.position,
                team_side=track.team_side,
                action=act_name,
                start_frame=seg_start,
                end_frame=seg_end,
                source="csv_explicit_event"
            ))

        # Check Center Priority Rules (e.g. Action_BallSnap > Action_ZoneBlock on Center)
        if track.position == "C":
            ball_snap_segs = [s for s in explicit_segs if s.action == "Action_BallSnap"]
            if ball_snap_segs:
                bs_end = ball_snap_segs[0].end_frame
                for s in explicit_segs:
                    if s.action not in ("Action_BallSnap", "Action_PreSnap"):
                        if s.start_frame <= bs_end:
                            old_start = s.start_frame
                            s.start_frame = bs_end + 1
                            warnings.append(
                                f"Resolved action overlap for track '{xml_track_id}' (C): "
                                f"higher_priority='Action_BallSnap' [{ball_snap_segs[0].start_frame}–{bs_end}], "
                                f"lower_priority='{s.action}' annotated_start={old_start}, "
                                f"effective_{s.action}_start={s.start_frame}."
                            )

        # PASS 2: Frame-by-frame map & Action_None filling for visible frames
        track_visible_set = set(visible_frames) if visible_frames else set(range(min_track_frame, max_track_frame + 1))
        frame_action_map: Dict[int, str] = {}
        
        for seg in explicit_segs:
            for f in range(seg.start_frame, seg.end_frame + 1):
                if f in track_visible_set:
                    frame_action_map[f] = seg.action
                    
        # Fill uncovered visible frames with Action_None
        for f in sorted(list(track_visible_set)):
            if f not in frame_action_map:
                frame_action_map[f] = "Action_None"
                
        # Collapse contiguous frame_action_map into final ActionSegments
        if frame_action_map:
            sorted_f = sorted(frame_action_map.keys())
            curr_action = frame_action_map[sorted_f[0]]
            curr_start = sorted_f[0]
            prev_f = sorted_f[0]
            
            for f in sorted_f[1:]:
                act = frame_action_map[f]
                if act == curr_action and f == prev_f + 1:
                    prev_f = f
                else:
                    final_segments.append(ActionSegment(
                        actor_track_id=track.custom_track_id or xml_track_id,
                        xml_track_id=xml_track_id,
                        position=track.position,
                        team_side=track.team_side,
                        action=curr_action,
                        start_frame=curr_start,
                        end_frame=prev_f,
                        source="inferred_complete_timeline"
                    ))
                    curr_action = act
                    curr_start = f
                    prev_f = f
                    
            final_segments.append(ActionSegment(
                actor_track_id=track.custom_track_id or xml_track_id,
                xml_track_id=xml_track_id,
                position=track.position,
                team_side=track.team_side,
                action=curr_action,
                start_frame=curr_start,
                end_frame=prev_f,
                source="inferred_complete_timeline"
            ))

    return final_segments, warnings
