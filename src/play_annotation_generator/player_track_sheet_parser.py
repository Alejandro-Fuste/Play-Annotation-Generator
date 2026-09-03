import csv
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any

@dataclass
class PlayerTrackAssignment:
    video_name: str
    video_id: str
    track_id: str
    position: str
    team_side: str
    notes: Optional[str] = None
    source_cell: Optional[str] = None

def parse_assignments_cell(cell_value: str) -> List[Tuple[str, str]]:
    """
    Parses a single cell containing assignments, e.g. "QB,8;TE-Y,10;LG,2".
    Returns a list of (position, track_id) tuples.
    """
    cell_value = cell_value.strip()
    if not cell_value:
        return []
        
    # Split by semicolon
    entries = [e.strip() for e in cell_value.split(";") if e.strip()]
    parsed = []
    
    for entry in entries:
        # Split on first occurrence of , or : or = or space/whitespace
        # (e.g. POSITION,TRACK_ID or POSITION:TRACK_ID or POSITION=TRACK_ID or POSITION TRACK_ID)
        parts = re.split(r'[,:=]|\s+', entry, maxsplit=1)
        if len(parts) == 2:
            pos = parts[0].strip()
            tid = parts[1].strip()
            if pos and tid:
                parsed.append((pos, tid))
                
    return parsed

def parse_player_track_csv(
    csv_path: str,
    target_video_name: Optional[str] = None,
    target_video_id: Optional[str] = None
) -> Tuple[Dict[str, PlayerTrackAssignment], List[str]]:
    """
    Parses the Player Track ID CSV.
    Supports wide assignment sheets, normalized sheets, and column-wise grid sheets.
    Returns:
      - dict mapping track_id (str) to PlayerTrackAssignment objects
      - list of parsing warning/error messages
    """
    warnings = []
    assignments: Dict[str, PlayerTrackAssignment] = {}
    
    if not os.path.exists(csv_path):
        warnings.append(f"Player track CSV file not found: {csv_path}")
        return assignments, warnings
        
    with open(csv_path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        
    if not lines:
        warnings.append("Player track CSV is empty.")
        return assignments, warnings
        
    # Detect delimiter
    first_line = lines[0]
    delimiter = "\t" if "\t" in first_line else ","
    
    # Skip metadata lines at the top (e.g. title/info rows) to find the headers row
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
                
    header_parts = [p.strip().strip('"').strip("'") for p in lines[header_idx].split(delimiter)]
    
    is_wide = "assignments" in header_parts
    is_normalized = "position" in header_parts and "track_id" in header_parts
    
    if is_wide or is_normalized:
        reader = csv.DictReader(lines[header_idx:], delimiter=delimiter)
        # Clean field names
        if reader.fieldnames:
            reader.fieldnames = [name.strip().strip('"').strip("'") for name in reader.fieldnames]
            
        for row_idx, row in enumerate(reader, header_idx + 1):
            row = {k: (v.strip() if v else "") for k, v in row.items() if k is not None}
            
            # Extract video identifiers
            v_name = row.get("video_name", row.get("Video #", ""))
            v_id = row.get("video_id", row.get("Video #", ""))
            if not v_id and row.get("Video #"):
                v_id = row.get("Video #", "")
            if not v_name and metadata_video_name:
                v_name = f"{metadata_video_name}{v_id}" if v_id else metadata_video_name
                
            # Check match
            if not is_video_match(v_name, v_id, target_video_name, target_video_id):
                continue
                
            team_side = row.get("team_side", "offense")
            notes = row.get("notes", "")
            
            if is_wide:
                cell_val = row.get("assignments", "")
                parsed_entries = parse_assignments_cell(cell_val)
                for pos, tid in parsed_entries:
                    if tid in assignments:
                        warnings.append(f"Row {row_idx}: Duplicate assignment for track ID '{tid}'. Overwriting previous assignment.")
                    assignments[tid] = PlayerTrackAssignment(
                        video_name=v_name,
                        video_id=v_id,
                        track_id=tid,
                        position=pos,
                        team_side=team_side,
                        notes=notes,
                        source_cell=f"assignments:{pos},{tid}"
                    )
            elif is_normalized:
                pos = row.get("position", "")
                tid = row.get("track_id", "")
                if pos and tid:
                    if tid in assignments:
                        warnings.append(f"Row {row_idx}: Duplicate assignment for track ID '{tid}'. Overwriting previous assignment.")
                    assignments[tid] = PlayerTrackAssignment(
                        video_name=v_name,
                        video_id=v_id,
                        track_id=tid,
                        position=pos,
                        team_side=team_side,
                        notes=notes,
                        source_cell=f"normalized:pos={pos},track_id={tid}"
                    )
    else:
        # Positional Grid format (columns 1 to N contain POSITION,TRACK_ID)
        for row_idx in range(header_idx + 1, len(lines)):
            line = lines[row_idx]
            # Use csv.reader to handle quoted commas correctly
            row_parts = next(csv.reader([line], delimiter=delimiter))
            if not row_parts:
                continue
                
            row_parts = [p.strip() for p in row_parts]
            if not row_parts or not row_parts[0]:
                continue
                
            v_id = row_parts[0]
            v_name = f"{metadata_video_name}{v_id}" if metadata_video_name else v_id
            
            # Check match
            if not is_video_match(v_name, v_id, target_video_name, target_video_id):
                continue
                
            # Parse all cells in the row after column 0
            for cell_idx in range(1, len(row_parts)):
                cell_val = row_parts[cell_idx]
                if not cell_val or cell_val == "-":
                    continue
                    
                parsed_entries = parse_assignments_cell(cell_val)
                for pos, tid in parsed_entries:
                    pos_upper = pos.upper()
                    OFFENSE_POSITIONS = {
                        "QB", "RB", "FB", "H-BACK", "HB", "LT", "LG", "C", "RG", "RT",
                        "WR-X", "WR-Y", "WR-Z", "WR-F", "TE-Y", "TE-H", "TE-F", "WR", "TE", "OL", "SKILL"
                    }
                    
                    is_offense = False
                    if pos_upper in OFFENSE_POSITIONS:
                        is_offense = True
                    elif any(p in pos_upper for p in ["WR", "TE", "LT", "LG", "RG", "RT", "QB", "RB", "FB", "HB", "C"]):
                        if not any(d in pos_upper for d in ["DT", "MLB", "WLB", "LDE", "RDE", "FS", "SS", "DE", "CB"]):
                            is_offense = True
                            
                    team_side = "offense" if is_offense else "defense"
                    
                    if tid in assignments:
                        warnings.append(f"Row {row_idx + 1}: Duplicate assignment for track ID '{tid}' in grid. Overwriting previous assignment.")
                        
                    assignments[tid] = PlayerTrackAssignment(
                        video_name=v_name,
                        video_id=v_id,
                        track_id=tid,
                        position=pos,
                        team_side=team_side,
                        notes="",
                        source_cell=f"grid:{pos},{tid}"
                    )
                    
    return assignments, warnings

def is_video_match(row_name: str, row_id: str, target_name: Optional[str], target_id: Optional[str]) -> bool:
    if not target_name and not target_id:
        return True
        
    row_name = str(row_name).strip()
    row_id = str(row_id).strip()
    
    t_name = str(target_name).strip() if target_name else ""
    t_id = str(target_id).strip() if target_id else ""
    
    if t_id and row_id and t_id == row_id:
        return True
    if t_name and row_name and t_name == row_name:
        return True
    if t_name and row_id and (t_name == f"JetSweep_{row_id}" or t_name.endswith(f"_{row_id}")):
        return True
    if t_id and row_name and (row_name == f"JetSweep_{t_id}" or row_name.endswith(f"_{t_id}")):
        return True
        
    return False
