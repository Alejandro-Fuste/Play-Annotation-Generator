from typing import Any, Dict, List, Tuple, Optional
from .models import ActionEvent, Track

def normalize_and_match_events(
    events: List[ActionEvent],
    tracks: Dict[str, Track],
    config: Dict[str, Any]
) -> Tuple[List[ActionEvent], List[str]]:
    """
    Normalizes a list of parsed ActionEvent records:
      - Matches individual track IDs to XML tracks.
      - Expands group targets (OL, ALL_OFFENSE, SKILL) to individual player tracks.
      - Resolves ball and global events.
      
    Returns:
        A tuple of:
          - list of resolved ActionEvent records
          - list of resolution errors/warnings
    """
    resolved_events: List[ActionEvent] = []
    errors: List[str] = []
    
    pos_groups = config.get("position_groups", {})
    
    # 1. Build lookup tables from XML tracks
    custom_id_to_track_ids: Dict[str, List[str]] = {}
    xml_id_to_track_id: Dict[str, str] = {}
    
    for xml_id, track in tracks.items():
        xml_id_to_track_id[xml_id] = xml_id
        if track.custom_track_id:
            custom_id_to_track_ids.setdefault(track.custom_track_id, []).append(xml_id)
            
    # Check for duplicate custom track IDs (ambiguity check - Spec 6.16)
    # Ignore default or unassigned values like "0", "undefined", or empty string
    duplicate_custom_ids = {
        cid: ids for cid, ids in custom_id_to_track_ids.items()
        if len(ids) > 1 and cid not in ("0", "undefined", "")
    }
    if duplicate_custom_ids:
        err_msg = f"Ambiguous custom track IDs: { {cid: ids for cid, ids in duplicate_custom_ids.items()} }."
        if config.get("validation", {}).get("strict", False):
            raise ValueError(err_msg)
        else:
            errors.append(err_msg + " Will attempt to match first occurrence.")

    # Helper function to match a single actor_track_id string to XML track id
    def match_track_id(actor_id: str) -> Optional[str]:
        # Try custom track ID attribute first
        if actor_id in custom_id_to_track_ids:
            return custom_id_to_track_ids[actor_id][0]
        # Try XML track ID
        if actor_id in xml_id_to_track_id:
            return xml_id_to_track_id[actor_id]
        return None

    # 2. Process each event
    for event in events:
        if event.target_kind == "global_event":
            # Global events don't target any specific track
            resolved_events.append(event)
            continue
            
        elif event.target_kind == "ball":
            # Match ball track
            ball_tracks = [t for t in tracks.values() if t.label.lower() == "ball"]
            if ball_tracks:
                event.resolved_xml_track_id = ball_tracks[0].xml_track_id
                resolved_events.append(event)
            else:
                errors.append(f"Event '{event.action}' at frame {event.start_frame} targets ball, but no ball track exists in XML.")
                
        # Group or position expansion check
        elif event.target_kind == "group" or (
            event.actor_track_id in ["ALL", "ALL_OFFENSE", "ALL_DEFENSE", "OL", "SKILL"]
        ) or (
            event.actor_track_id and any(t.position == event.actor_track_id for t in tracks.values() if t.position)
        ):
            # Expand group/position target
            group_name = event.actor_track_id
            from .sheet_group_resolver import resolve_group_targets
            matched_tracks = resolve_group_targets(group_name, tracks, config)
            
            if not matched_tracks:
                errors.append(f"Group/position target '{group_name}' for action '{event.action}' at frame {event.start_frame} could not be resolved to any XML tracks (position/team_side missing).")
                continue
                
            for track in matched_tracks:
                actor_id = track.custom_track_id if track.custom_track_id else track.xml_track_id
                expanded_event = ActionEvent(
                    video_name=event.video_name,
                    video_id=event.video_id,
                    play_tag=event.play_tag,
                    result_tag=event.result_tag,
                    result_frame=event.result_frame,
                    action=event.action,
                    start_frame=event.start_frame,
                    annotated_frame=event.annotated_frame,
                    annotated_frame_role=event.annotated_frame_role,
                    event_type=event.event_type,
                    actor_track_id=actor_id,
                    resolved_xml_track_id=track.xml_track_id,
                    target_kind="track_id",
                    source_column=f"{event.source_column}_group_{group_name}",
                    actor_position=track.position,
                    notes=event.notes
                )
                resolved_events.append(expanded_event)
                
        elif event.target_kind == "track_id":
            # Match individual player track
            xml_id = match_track_id(event.actor_track_id)
            if xml_id:
                event.resolved_xml_track_id = xml_id
                event.actor_position = tracks[xml_id].position
                resolved_events.append(event)
            else:
                errors.append(f"Event '{event.action}' at frame {event.start_frame} targets track ID '{event.actor_track_id}', but it is not found in XML.")
                
    return resolved_events, errors
