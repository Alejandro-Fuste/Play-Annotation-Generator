from typing import Dict, List, Any
from .models import Track

def resolve_group_targets(
    group_name: str,
    tracks: Dict[str, Track],
    config: Dict[str, Any]
) -> List[Track]:
    """
    Expands group names (ALL, ALL_OFFENSE, ALL_DEFENSE, OL, SKILL) or position names (QB, WR-F, etc.)
    into a list of matching Track objects.
    """
    group_name_upper = group_name.strip().upper()
    
    # Check both position_groups and groups in config
    pos_groups = config.get("position_groups", {})
    if not pos_groups:
        pos_groups = config.get("groups", {})
        
    matched_tracks: List[Track] = []
    
    # 1. Expand standard groups
    if group_name_upper in ["ALL", "ALL_OFFENSE"]:
        matched_tracks = [t for t in tracks.values() if t.team_side == "offense" and t.label == "player"]
    elif group_name_upper == "ALL_DEFENSE":
        matched_tracks = [t for t in tracks.values() if t.team_side == "defense" and t.label == "player"]
    elif group_name_upper == "OL":
        ol_positions = pos_groups.get("OL", ["LT", "LG", "C", "RG", "RT"])
        matched_tracks = [
            t for t in tracks.values() 
            if t.team_side == "offense" and t.position in ol_positions and t.label == "player"
        ]
    elif group_name_upper == "SKILL":
        skill_positions = pos_groups.get("SKILL", ["QB", "RB", "FB", "H-BACK", "HB", "WR-X", "WR-Y", "WR-Z", "WR-F", "TE-Y", "TE-H", "TE-F"])
        matched_tracks = [
            t for t in tracks.values() 
            if t.team_side == "offense" and t.position in skill_positions and t.label == "player"
        ]
    else:
        # 2. Check if the target matches a position name directly (e.g. QB, WR-F)
        # Positions are case-sensitive usually (e.g., "QB").
        matched_tracks = [
            t for t in tracks.values()
            if t.position == group_name and t.label == "player"
        ]
        
    return matched_tracks
