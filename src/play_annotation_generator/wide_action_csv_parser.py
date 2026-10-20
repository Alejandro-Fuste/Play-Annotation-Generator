import csv
import os
import re
from typing import Any, Dict, List, Tuple, Optional
from .models import ActionEvent

class ParsedEntry(tuple):
    def __new__(cls, start_frame, actor_id, err, end_frame=None):
        return super().__new__(cls, (start_frame, actor_id, err))
    def __init__(self, start_frame, actor_id, err, end_frame=None):
        self.end_frame = end_frame

def normalize_column_name(name: str) -> str:
    name = str(name).lower().strip()
    name = re.sub(r'\b(of|the|a)\b', '', name)
    name = re.sub(r'[^a-z0-9]', '', name)
    return name

def parse_cell_entries(
    cell_value: str,
    pair_sep: str = ",",
    multi_seps: List[str] = None
) -> List[Tuple[Optional[int], Optional[str], Optional[str]]]:
    """
    Parses a single wide CSV action cell.
    Supports semicolon continuation parsing where a full tuple establishes frame context
    and subsequent bare numeric tokens inherit the frame context (e.g. 52,19;14;20;18).
    Returns a list of tuples: (frame_number, actor_track_id, error_message).
    Entries may also carry an .end_frame attribute if a 3-part range was provided (start, end, track_id).
    """
    cell_value = cell_value.strip()
    if not cell_value or cell_value in ["-", "--", "N/A", "n/a", "none", "None"]:
        return []

    # First split by line / pipe breaks to isolate records
    line_splits = [cell_value]
    for sep in ["\n", "|"]:
        next_lines = []
        for l in line_splits:
            next_lines.extend(l.split(sep))
        line_splits = next_lines

    parsed = []
    for line in line_splits:
        line = line.strip()
        if not line:
            continue

        # Split by semicolon continuation within this line
        semi_parts = [p.strip() for p in line.split(";") if p.strip()]
        if not semi_parts:
            continue

        current_frame: Optional[int] = None
        current_end_frame: Optional[int] = None

        for sub_entry in semi_parts:
            raw_parts = [p.strip() for p in sub_entry.split(pair_sep)]
            if len(raw_parts) == 0 or all(not p for p in raw_parts):
                continue
            elif len(raw_parts) == 1:
                val = raw_parts[0]
                if current_frame is not None:
                    # Bare token inherits current_frame (and current_end_frame if range)
                    if val in ["?", "??"] or not val:
                        parsed.append(ParsedEntry(None, val, f"Invalid continuation actor ID '{val}'."))
                    else:
                        parsed.append(ParsedEntry(current_frame, val, None, end_frame=current_end_frame))
                else:
                    # No active frame context: could be a global frame number or a text label
                    try:
                        frame = int(val)
                        parsed.append(ParsedEntry(frame, None, None))
                    except ValueError:
                        parsed.append(ParsedEntry(None, val, f"Single text entry '{val}' could not be parsed as a frame number."))
            elif len(raw_parts) == 2:
                frame_str, actor_str = raw_parts[0], raw_parts[1]
                if not frame_str or frame_str in ["?", "??"]:
                    current_frame = None
                    current_end_frame = None
                    parsed.append(ParsedEntry(None, actor_str, f"Unknown/missing frame number '{frame_str}' in entry '{sub_entry}'."))
                else:
                    try:
                        frame = int(frame_str)
                        current_frame = frame
                        current_end_frame = None
                        parsed.append(ParsedEntry(frame, actor_str, None))
                    except ValueError:
                        current_frame = None
                        current_end_frame = None
                        parsed.append(ParsedEntry(None, actor_str, f"Could not parse frame number from '{frame_str}' in entry '{sub_entry}'."))
            elif len(raw_parts) == 3:
                start_str, end_str, actor_str = raw_parts[0], raw_parts[1], raw_parts[2]
                start_frame = None
                end_frame = None
                try:
                    start_frame = int(start_str)
                except ValueError:
                    pass
                try:
                    end_frame = int(end_str)
                except ValueError:
                    pass
                if start_frame is not None and end_frame is not None:
                    if end_frame >= start_frame:
                        current_frame = start_frame
                        current_end_frame = end_frame
                        parsed.append(ParsedEntry(start_frame, actor_str, None, end_frame=end_frame))
                    else:
                        current_frame = start_frame
                        current_end_frame = None
                        parsed.append(ParsedEntry(start_frame, end_str, None))
                        parsed.append(ParsedEntry(start_frame, actor_str, None))
                elif start_frame is not None:
                    current_frame = start_frame
                    current_end_frame = None
                    parsed.append(ParsedEntry(start_frame, actor_str, None))
                else:
                    current_frame = None
                    current_end_frame = None
                    parsed.append(ParsedEntry(None, actor_str, f"Could not parse frame numbers from '{sub_entry}'."))
            else:
                frame_str = raw_parts[0]
                try:
                    frame = int(frame_str)
                    current_frame = frame
                    current_end_frame = None
                    for actor_id in raw_parts[1:]:
                        if actor_id:
                            parsed.append(ParsedEntry(frame, actor_id, None))
                except ValueError:
                    current_frame = None
                    current_end_frame = None
                    parsed.append(ParsedEntry(None, None, f"Too many components in entry '{sub_entry}'. Expected 'frame,track_id' or 'start,end,track_id'."))

    return parsed

def load_canonical_plays_map(plays_json_path: Optional[str] = None) -> Dict[str, str]:
    if not plays_json_path:
        for p in ["data/plays.json", "plays.json", "configs/plays.json"]:
            if os.path.exists(p):
                plays_json_path = p
                break
    mapping = {}
    if plays_json_path and os.path.exists(plays_json_path):
        import json
        with open(plays_json_path, "r", encoding="utf-8") as f:
            d = json.load(f)
        for fl in d.get("formattedPlayLabels", []):
            mapping[fl] = fl
            base = fl.split("_")[-1]
            mapping[base] = fl
            mapping[base.lower()] = fl
            mapping[re.sub(r'[^a-zA-Z0-9]', '', base).lower()] = fl
    return mapping

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
    
    plays_json_path = config.get("input", {}).get("plays_json", config.get("plays_json"))
    canonical_plays_map = load_canonical_plays_map(plays_json_path)

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
            
        # Resolve canonical play label from plays.json (NO JetSweep fallback)
        resolved_play = None
        if p_tag and p_tag != "✓":
            if p_tag in canonical_plays_map.values():
                resolved_play = p_tag
            elif p_tag in canonical_plays_map:
                resolved_play = canonical_plays_map[p_tag]
            elif p_tag.startswith("Play_"):
                resolved_play = p_tag

        if not resolved_play:
            candidates = []
            if metadata_video_name:
                candidates.append(metadata_video_name)
            if target_video:
                t_str = str(target_video).strip()
                candidates.append(re.sub(r'_\d+$', '', t_str))
                candidates.append(re.sub(r'\d+$', '', t_str))
            if v_name:
                v_str = str(v_name).strip()
                candidates.append(re.sub(r'_\d+$', '', v_str))
                candidates.append(re.sub(r'\d+$', '', v_str))
            csv_base = os.path.splitext(os.path.basename(csv_path))[0]
            if csv_base:
                candidates.append(csv_base)

            for cand in candidates:
                cand_clean = cand.strip()
                cand_norm = re.sub(r'[^a-zA-Z0-9]', '', cand_clean).lower()
                if cand_clean in canonical_plays_map:
                    resolved_play = canonical_plays_map[cand_clean]
                    break
                if cand_norm in canonical_plays_map:
                    resolved_play = canonical_plays_map[cand_norm]
                    break

        if resolved_play:
            p_tag = resolved_play
        else:
            errors.append(f"ERROR / BLOCKED: Could not resolve canonical play label for row {row_idx} (video '{v_name}').")
            p_tag = ""
            
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
                
        col_video_name_norm = normalize_column_name(col_video_name)
        col_video_id_norm = normalize_column_name(col_video_id)
        col_play_tag_norm = normalize_column_name(col_play_tag)
        col_result_tag_norm = normalize_column_name(col_result_tag)
        col_result_frame_norm = normalize_column_name(col_result_frame)
        col_notes_norm = normalize_column_name(col_notes)

        non_action_norm = {
            col_video_name_norm, col_video_id_norm, col_play_tag_norm,
            col_result_tag_norm, col_result_frame_norm, col_notes_norm,
            "videoname", "videoid", "video", "originalid", "coverage", "ol", "result", "notes"
        }
        norm_action_cols = {normalize_column_name(k): v for k, v in action_cols_map.items()}

        # Parse action columns directly from the row to prevent double-parsing and detect unmapped columns
        for orig_col_name, cell_val in cleaned_row.items():
            if not orig_col_name:
                continue
            norm_col = normalize_column_name(orig_col_name)
            if norm_col in non_action_norm:
                continue
            if not cell_val or cell_val in ["-", "--", "N/A", "n/a", "none", "None"]:
                continue

            if norm_col not in norm_action_cols:
                errors.append(f"UNMAPPED_ACTION_COLUMN: play={p_tag} video_id={v_id} column={orig_col_name} value={cell_val}")
                continue

            action_label = norm_action_cols[norm_col]
            if norm_col == "route":
                val_lower = str(cell_val).lower().strip()
                if val_lower.startswith("post"):
                    action_label = "Action_RunPostRoute"
                elif val_lower.startswith("slant"):
                    action_label = "Action_RunSlantRoute"
                elif val_lower.startswith("fade"):
                    action_label = "Action_RunFadeRoute"
                elif val_lower.startswith("hitch"):
                    action_label = "Action_RunHitchRoute"

            entries = parse_cell_entries(cell_val, pair_sep, multi_seps)
            for entry_item in entries:
                frame, actor_id, err = entry_item
                end_frame = getattr(entry_item, "end_frame", None)
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
                    end_frame=end_frame,
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
