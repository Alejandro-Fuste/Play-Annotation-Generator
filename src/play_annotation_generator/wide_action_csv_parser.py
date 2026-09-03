import csv
import os
import re
from typing import Any, Dict, List, Tuple, Optional
from .models import ActionEvent

def parse_cell_entries(
    cell_value: str,
    pair_sep: str = ",",
    multi_seps: List[str] = None
) -> List[Tuple[Optional[int], Optional[str], Optional[str]]]:
    """
    Parses a single wide CSV action cell.
    Returns a list of tuples: (frame_number, actor_track_id, error_message)
    """
    if multi_seps is None:
        multi_seps = [";", "|", "\n"]
        
    cell_value = cell_value.strip()
    if not cell_value or cell_value in ["-", "--", "N/A", "n/a", "none", "None"]:
        return []
        
    # Split by any of the multi-entry separators
    raw_entries = [cell_value]
    for sep in multi_seps:
        next_entries = []
        for entry in raw_entries:
            next_entries.extend(entry.split(sep))
        raw_entries = next_entries
        
    parsed = []
    for entry in raw_entries:
        entry = entry.strip()
        if not entry:
            continue
            
        # Split into frame and track_id by pair separator
        parts = [p.strip() for p in entry.split(pair_sep) if p.strip()]
        if len(parts) == 0:
            continue
        elif len(parts) == 1:
            # Could be just a frame number (for global event) or a text label
            val = parts[0]
            try:
                frame = int(val)
                parsed.append((frame, None, None))
            except ValueError:
                # Text label like "Tackle"
                parsed.append((None, val, f"Single text entry '{val}' could not be parsed as a frame number."))
        elif len(parts) == 2:
            frame_str, actor_str = parts[0], parts[1]
            try:
                frame = int(frame_str)
                parsed.append((frame, actor_str, None))
            except ValueError:
                parsed.append((None, None, f"Could not parse frame number from '{frame_str}' in entry '{entry}'."))
        else:
            parsed.append((None, None, f"Too many components in entry '{entry}'. Expected 'frame,track_id'."))
            
    return parsed

def parse_wide_action_csv(
    csv_path: str,
    config: Dict[str, Any],
    target_video: Optional[str] = None
) -> Tuple[List[ActionEvent], List[Dict[str, Any]], List[str]]:
    """
    Parses the wide action CSV.
    
    Returns:
        A tuple of:
          - list of ActionEvent records matching target_video
          - list of parsed row dicts (for all videos in the CSV)
          - list of validation errors/warnings during CSV parsing
    """
    errors = []
    events = []
    all_rows = []
    
    if not os.path.exists(csv_path):
        errors.append(f"CSV file not found: {csv_path}")
        return events, all_rows, errors
        
    csv_cols = config.get("csv", {}).get("columns", {})
    action_cols_map = config.get("csv", {}).get("action_columns", {})
    cell_parsing_cfg = config.get("csv", {}).get("cell_parsing", {})
    
    pair_sep = cell_parsing_cfg.get("pair_separator", ",")
    multi_seps = cell_parsing_cfg.get("multi_entry_separators", [";", "|", "\n"])
    
    col_video_name = csv_cols.get("video_name", "video_name")
    col_video_id = csv_cols.get("video_id", "video_id")
    col_play_tag = csv_cols.get("play_tag", "play_tag")
    col_result_tag = csv_cols.get("result_tag", "result_tag")
    col_result_frame = csv_cols.get("result_frame", "result_frame")
    col_notes = csv_cols.get("notes", "notes")
    
    # Load shorthand mappings
    shorthand_path = config.get("input", {}).get("result_shorthand_json")
    if not shorthand_path:
        for fallback in ["docs/endOfPlayEventsShortHand.json", "configs/endOfPlayEventsShortHand.json"]:
            if os.path.exists(fallback):
                shorthand_path = fallback
                break
    shorthand_map = {}
    if shorthand_path and os.path.exists(shorthand_path):
        try:
            import json
            with open(shorthand_path, "r", encoding="utf-8") as sf:
                shorthand_map = json.load(sf)
        except Exception as e:
            errors.append(f"Failed to load result shorthand JSON: {e}")
            
    def normalize_column_name(name: str) -> str:
        name = str(name).lower().strip()
        name = re.sub(r'\b(of|the|a)\b', '', name)
        name = re.sub(r'[^a-z0-9]', '', name)
        return name

    with open(csv_path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        
    if not lines:
        errors.append("CSV file is empty.")
        return events, all_rows, errors
        
    # Detect delimiter
    delimiter = "\t" if "\t" in lines[0] else ","
    
    # Skip metadata lines at the top to find the headers row
    header_idx = 0
    for i, line in enumerate(lines):
        parts = [p.strip().strip('"').strip("'") for p in line.split(delimiter)]
        if parts and parts[0] in ["Video #", "video_name", "video_id", "video #", "Video#"]:
            header_idx = i
            break
            
    # Extract metadata video name prefix if present in skipped rows
    metadata_video_name = ""
    for line in lines[:header_idx]:
        if "Video Name:" in line:
            parts = line.split(delimiter)
            if len(parts) > 1:
                metadata_video_name = parts[1].strip().strip('"').strip("'")
                
    reader = csv.DictReader(lines[header_idx:], delimiter=delimiter)
    
    # Clean headers (strip whitespace and quotes)
    if reader.fieldnames:
        reader.fieldnames = [name.strip().strip('"').strip("'") for name in reader.fieldnames]
        
    for row_idx, row in enumerate(reader, header_idx + 1):
        # Clean keys and values
        cleaned_row = {k.strip().strip('"').strip("'"): (v.strip() if v else "") for k, v in row.items() if k is not None}
        all_rows.append(cleaned_row)
        
        # Extract video identifier
        v_name = cleaned_row.get(col_video_name, "")
        if not v_name:
            v_name = cleaned_row.get("Video Name", cleaned_row.get("video_name", ""))
            
        v_id = cleaned_row.get(col_video_id, "")
        if not v_id:
            v_id = cleaned_row.get("Video #", cleaned_row.get("Video ID", cleaned_row.get("video_id", "")))
            
        if not v_name and metadata_video_name:
            v_name = f"{metadata_video_name}{v_id}" if v_id else metadata_video_name
            
        # Check if this row matches our target video
        is_match = False
        if target_video is None:
            is_match = True  # process all or first if not specified (caller decides)
        else:
            target_video_str = str(target_video).strip()
            target_clean = target_video_str[:-4] if target_video_str.lower().endswith(".mp4") else target_video_str
            
            if v_name in (target_video_str, target_clean) or v_id in (target_video_str, target_clean):
                is_match = True
            elif v_name == f"JetSweep_{target_clean}" or v_name.endswith(f"_{target_clean}"):
                is_match = True
            elif target_clean == f"JetSweep_{v_id}" or target_clean.endswith(f"_{v_id}"):
                is_match = True
                
        if not is_match:
            continue
            
        # Extract row-level tags
        p_tag = cleaned_row.get(col_play_tag, "")
        r_tag = cleaned_row.get(col_result_tag, "")
        r_frame_str = cleaned_row.get(col_result_frame, "")
        if not r_frame_str:
            r_frame_str = cleaned_row.get("End of Play", cleaned_row.get("end_play", ""))
        notes = cleaned_row.get(col_notes, "")
        
        # Map result tag using shorthand
        if r_tag in shorthand_map:
            r_tag = shorthand_map[r_tag]
            
        # Standardize default tags if empty
        if not p_tag or p_tag == "✓": # Check if checkmark used
            p_tag = "Play_Run_JetSweep" # default fallback
            
        r_frame = None
        if r_frame_str:
            try:
                r_frame = int(r_frame_str)
            except ValueError:
                # If it's a text string like "Tackle", treat it as a result_tag if empty
                if not r_tag:
                    r_tag = shorthand_map.get(r_frame_str, r_frame_str)
                    if not r_tag.startswith("Result_") and r_tag != "undefined":
                        r_tag = f"Result_{r_tag}"
                # The caller will handle play end frames and tags later
                pass
                
        # Create a lookup for normalized keys to original cleaned keys
        normalized_keys = {normalize_column_name(k): k for k in cleaned_row.keys()}
        
        # Parse action columns
        for config_col, action_label in action_cols_map.items():
            norm_config_col = normalize_column_name(config_col)
            if norm_config_col not in normalized_keys:
                continue
                
            orig_col_name = normalized_keys[norm_config_col]
            cell_val = cleaned_row[orig_col_name]
            if not cell_val:
                continue
                
            entries = parse_cell_entries(cell_val, pair_sep, multi_seps)
            for frame, actor_id, err in entries:
                if err:
                    # Ignore parsing error if it is a single text entry in an end/result column
                    is_result_text = False
                    if actor_id:
                        is_end_column = any(k in orig_col_name.lower() for k in ["end", "play", "result"])
                        if is_end_column:
                            is_result_text = True
                            
                    if is_result_text:
                        err = None
                    else:
                        errors.append(f"Row {row_idx}, Column '{orig_col_name}': {err}")
                        continue
                    
                # Build ActionEvent
                target_kind = "track_id"
                if actor_id is None:
                    target_kind = "global_event"
                elif actor_id in ["OL", "ALL_OFFENSE", "SKILL", "ALL", "ALL_DEFENSE"]:
                    target_kind = "group"
                elif actor_id.lower() == "ball":
                    target_kind = "ball"
                    
                # Determine frame role and event type
                frame_role = "START"
                evt_type = "PRIMARY_ACTION"
                
                semantics_cfg = config.get("action_frame_semantics", {}).get(action_label, {})
                if "annotated_frame_role" in semantics_cfg:
                    frame_role = semantics_cfg["annotated_frame_role"]
                elif action_label == "Action_SnapReceive":
                    frame_role = "END"
                    
                boundary_cfg = config.get("boundary_events", {})
                if action_label in boundary_cfg:
                    evt_type = boundary_cfg[action_label].get("event_type", "BOUNDARY")
                    frame_role = "BOUNDARY"
                elif "end_ol_block" in orig_col_name.lower() or action_label == "Action_None":
                    evt_type = "BOUNDARY"
                    frame_role = "BOUNDARY"
                elif action_label == "Action_PlayEnd" or "end of play" in orig_col_name.lower():
                    evt_type = "PLAY_END"
                    frame_role = "BOUNDARY"
                    
                evt_frame = frame if frame is not None else 0
                event = ActionEvent(
                    video_name=v_name,
                    video_id=v_id,
                    play_tag=p_tag,
                    result_tag=r_tag if r_tag else None,
                    result_frame=r_frame,
                    action=action_label,
                    start_frame=evt_frame,
                    annotated_frame=evt_frame,
                    annotated_frame_role=frame_role,
                    event_type=evt_type,
                    actor_track_id=actor_id,
                    target_kind=target_kind,
                    source_column=orig_col_name,
                    notes=notes
                )
                
                # If actor_id is not a frame number but was returned as actor_id because frame was None:
                if frame is None:
                    event.target_kind = "global_event"
                    event.actor_track_id = None
                    if r_frame is not None:
                        event.start_frame = r_frame
                    if actor_id:
                        mapped_id = shorthand_map.get(actor_id, actor_id)
                        if not mapped_id.startswith("Result_") and mapped_id != "undefined":
                            mapped_id = f"Result_{mapped_id}"
                        event.result_tag = mapped_id
                        
                events.append(event)
                
    return events, all_rows, errors
