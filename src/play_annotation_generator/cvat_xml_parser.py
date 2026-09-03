import xml.etree.ElementTree as ET
from typing import Any, Dict, Tuple, Optional
from collections import Counter
from .models import Track, TrackBox

def parse_cvat_xml(
    xml_path: str,
    player_label: str = "player",
    ball_label: str = "ball"
) -> Tuple[Dict[str, Track], Dict[str, Any]]:
    """
    Parses a CVAT for Video XML export file.
    
    Returns:
        A tuple of:
          - dict mapping xml_track_id (str) to Track objects
          - dict containing metadata (width, height, total_frames, start_frame, stop_frame)
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # 1. Parse Metadata
    metadata: Dict[str, Any] = {
        "width": 0,
        "height": 0,
        "start_frame": 0,
        "stop_frame": 0,
        "total_frames": 0,
        "job_id": None,
        "task_name": None
    }
    
    meta_elem = root.find("meta")
    if meta_elem is not None:
        # Find original_size
        size_elem = meta_elem.find(".//original_size")
        if size_elem is not None:
            w_elem = size_elem.find("width")
            h_elem = size_elem.find("height")
            if w_elem is not None and w_elem.text:
                metadata["width"] = int(w_elem.text)
            if h_elem is not None and h_elem.text:
                metadata["height"] = int(h_elem.text)
        
        # Find job or task info
        job_elem = meta_elem.find(".//job")
        if job_elem is not None:
            id_elem = job_elem.find("id")
            if id_elem is not None and id_elem.text:
                metadata["job_id"] = id_elem.text
            
            size_elem = job_elem.find("size")
            if size_elem is not None and size_elem.text:
                metadata["total_frames"] = int(size_elem.text)
                
            start_elem = job_elem.find("start_frame")
            if start_elem is not None and start_elem.text:
                metadata["start_frame"] = int(start_elem.text)
                
            stop_elem = job_elem.find("stop_frame")
            if stop_elem is not None and stop_elem.text:
                metadata["stop_frame"] = int(stop_elem.text)
                if not metadata["total_frames"]:
                    metadata["total_frames"] = metadata["stop_frame"] - metadata["start_frame"] + 1
                    
        # Try finding task (if it's a task export instead of job)
        task_elem = meta_elem.find(".//task")
        if task_elem is not None:
            name_elem = task_elem.find("name")
            if name_elem is not None and name_elem.text:
                metadata["task_name"] = name_elem.text
            size_elem = task_elem.find("size")
            if size_elem is not None and size_elem.text:
                metadata["total_frames"] = int(size_elem.text)
            start_elem = task_elem.find("start_frame")
            if start_elem is not None and start_elem.text:
                metadata["start_frame"] = int(start_elem.text)
            stop_elem = task_elem.find("stop_frame")
            if stop_elem is not None and stop_elem.text:
                metadata["stop_frame"] = int(stop_elem.text)
                if not metadata["total_frames"]:
                    metadata["total_frames"] = metadata["stop_frame"] - metadata["start_frame"] + 1

    # 2. Parse Tracks
    tracks: Dict[str, Track] = {}
    
    for track_elem in root.findall("track"):
        xml_track_id = track_elem.attrib.get("id", "")
        label = track_elem.attrib.get("label", "")
        source = track_elem.attrib.get("source", "")
        
        # We only care about player and ball tracks (or all tracks, but let's parse all and let enricher decide)
        track = Track(
            xml_track_id=xml_track_id,
            label=label,
            source=source
        )
        
        boxes_by_frame = {}
        
        # Temporary lists to find majority attributes
        positions = []
        team_sides = []
        custom_ids = []
        
        for box_elem in track_elem.findall("box"):
            frame = int(box_elem.attrib.get("frame", "0"))
            xtl = float(box_elem.attrib.get("xtl", "0.0"))
            ytl = float(box_elem.attrib.get("ytl", "0.0"))
            xbr = float(box_elem.attrib.get("xbr", "0.0"))
            ybr = float(box_elem.attrib.get("ybr", "0.0"))
            outside = box_elem.attrib.get("outside", "0") == "1"
            occluded = box_elem.attrib.get("occluded", "0") == "1"
            keyframe = box_elem.attrib.get("keyframe", "0") == "1"
            
            # Parse attributes
            attrs = {}
            for attr_elem in box_elem.findall("attribute"):
                name = attr_elem.attrib.get("name", "")
                val = attr_elem.text or ""
                attrs[name] = val.strip()
                
                # Check for position, team_side, track_id
                if name == "position" and val and val != "undefined":
                    positions.append(val)
                elif name == "team_side" and val and val != "undefined":
                    team_sides.append(val)
                elif name == "track_id" and val and val != "undefined":
                    custom_ids.append(val)
            
            box = TrackBox(
                frame=frame,
                xtl=xtl,
                ytl=ytl,
                xbr=xbr,
                ybr=ybr,
                outside=outside,
                occluded=occluded,
                keyframe=keyframe,
                attributes=attrs
            )
            boxes_by_frame[frame] = box
            
        track.boxes_by_frame = boxes_by_frame
        
        # Infer track-level metadata from box attributes
        if positions:
            track.position = Counter(positions).most_common(1)[0][0]
        else:
            # Check track element itself for attributes if boxes don't have them
            track.position = None
            
        if team_sides:
            track.team_side = Counter(team_sides).most_common(1)[0][0]
        else:
            track.team_side = None
            
        if custom_ids:
            track.custom_track_id = Counter(custom_ids).most_common(1)[0][0]
        else:
            track.custom_track_id = None
            
        tracks[xml_track_id] = track
        
    return tracks, metadata
