import xml.etree.ElementTree as ET
import os
from typing import Dict, List, Any, Optional
from .mot_parser import MOTTrack
from .player_track_sheet_parser import PlayerTrackAssignment

def generate_base_cvat_xml(
    template_path: str,
    output_xml_path: str,
    mot_tracks: Dict[int, MOTTrack],
    assignments: Dict[str, PlayerTrackAssignment],
    config: Dict[str, Any]
) -> int:
    """
    Generates a base CVAT XML file from MOT tracks and player assignments, using the XML template.
    Returns the total number of tracks generated.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"XML template not found: {template_path}")
        
    tree = ET.parse(template_path)
    root = tree.getroot()
    
    # 1. Parse video boundaries from template
    start_frame = 0
    stop_frame = 239 # fallback
    
    meta_elem = root.find("meta")
    if meta_elem is not None:
        start_elem = meta_elem.find(".//start_frame")
        if start_elem is not None and start_elem.text:
            start_frame = int(start_elem.text)
        stop_elem = meta_elem.find(".//stop_frame")
        if stop_elem is not None and stop_elem.text:
            stop_frame = int(stop_elem.text)
            
    # Determine the maximum frame index in the MOT tracking data
    max_mot_frame = 0
    for track in mot_tracks.values():
        for box in track.boxes:
            if box.frame > max_mot_frame:
                max_mot_frame = box.frame
                
    # If MOT frame index exceeds template stop_frame, adjust stop_frame
    if max_mot_frame > stop_frame:
        stop_frame = max_mot_frame
        if meta_elem is not None:
            stop_elems = meta_elem.findall(".//stop_frame")
            for se in stop_elems:
                se.text = str(stop_frame)
            size_elems = meta_elem.findall(".//size")
            for se in size_elems:
                se.text = str(stop_frame - start_frame + 1)
                
    # 2. Clear all existing track elements
    for track_elem in root.findall("track"):
        root.remove(track_elem)
        
    # 3. Create a track for each MOT track
    xml_track_id = 0
    player_lbl = config.get("labels", {}).get("player_label", "player")
    ball_lbl = config.get("labels", {}).get("ball_label", "ball")
    
    # Sort mot tracks by track ID
    for mot_tid in sorted(mot_tracks.keys()):
        mot_track = mot_tracks[mot_tid]
        
        # Check if we have assignment for this track
        mot_tid_str = str(mot_tid)
        assignment = assignments.get(mot_tid_str)
        
        # Create track element
        track_elem = ET.Element("track", {
            "id": str(xml_track_id),
            "label": mot_track.label,
            "source": "file"
        })
        xml_track_id += 1
        
        # Write boxes
        boxes = mot_track.boxes
        if not boxes:
            continue
            
        # Get list of frames where box is present
        boxes_by_frame = {b.frame: b for b in boxes}
        active_frames = sorted(boxes_by_frame.keys())
        
        for idx, f in enumerate(active_frames):
            box = boxes_by_frame[f]
            
            # Write box with outside="0"
            box_elem = ET.Element("box", {
                "frame": str(f),
                "keyframe": "1",
                "outside": "0",
                "occluded": "1" if (box.visibility is not None and box.visibility < 0.5) else "0",
                "xtl": f"{box.xtl:.2f}",
                "ytl": f"{box.ytl:.2f}",
                "xbr": f"{box.xbr:.2f}",
                "ybr": f"{box.ybr:.2f}"
            })
            
            # Add attributes
            if mot_track.label == player_lbl:
                pos = assignment.position if assignment else "undefined"
                team = assignment.team_side if assignment else "undefined"
                
                # If defensive player, default initial action to Action_DefenseNotAnnotated
                initial_action = "undefined"
                if team == "defense":
                    initial_action = "Action_DefenseNotAnnotated"
                    
                # Attributes: position, team_side, action, track_id
                ET.SubElement(box_elem, "attribute", name="position").text = pos
                ET.SubElement(box_elem, "attribute", name="team_side").text = team
                ET.SubElement(box_elem, "attribute", name="action").text = initial_action
                ET.SubElement(box_elem, "attribute", name="track_id").text = mot_tid_str
            elif mot_track.label == ball_lbl:
                # Attributes: ball_status, track_id
                ET.SubElement(box_elem, "attribute", name="ball_status").text = "undefined"
                ET.SubElement(box_elem, "attribute", name="track_id").text = mot_tid_str
                
            track_elem.append(box_elem)
            
            # Visibility logic: check if there's a gap or track ends
            is_last = (idx + 1 == len(active_frames))
            next_f = active_frames[idx + 1] if not is_last else None
            
            write_outside = False
            outside_frame = None
            
            if not is_last and next_f > f + 1:
                write_outside = True
                outside_frame = f + 1
            elif is_last and f < stop_frame:
                write_outside = True
                outside_frame = f + 1
                
            if write_outside and outside_frame is not None:
                outside_elem = ET.Element("box", {
                    "frame": str(outside_frame),
                    "keyframe": "1",
                    "outside": "1",
                    "occluded": "0",
                    "xtl": f"{box.xtl:.2f}",
                    "ytl": f"{box.ytl:.2f}",
                    "xbr": f"{box.xbr:.2f}",
                    "ybr": f"{box.ybr:.2f}"
                })
                
                # Add attributes to outside box
                if mot_track.label == player_lbl:
                    pos = assignment.position if assignment else "undefined"
                    team = assignment.team_side if assignment else "undefined"
                    initial_action = "Action_DefenseNotAnnotated" if team == "defense" else "undefined"
                    ET.SubElement(outside_elem, "attribute", name="position").text = pos
                    ET.SubElement(outside_elem, "attribute", name="team_side").text = team
                    ET.SubElement(outside_elem, "attribute", name="action").text = initial_action
                    ET.SubElement(outside_elem, "attribute", name="track_id").text = mot_tid_str
                elif mot_track.label == ball_lbl:
                    ET.SubElement(outside_elem, "attribute", name="ball_status").text = "undefined"
                    ET.SubElement(outside_elem, "attribute", name="track_id").text = mot_tid_str
                    
                track_elem.append(outside_elem)
                
        root.append(track_elem)
        
    # Formatting and saving
    try:
        ET.indent(root, space="  ")
    except AttributeError:
        pass
        
    with open(output_xml_path, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
        
    return len(mot_tracks)
