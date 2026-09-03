import os
import zipfile
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple

@dataclass
class MOTBox:
    frame: int
    track_id: int
    xtl: float
    ytl: float
    xbr: float
    ybr: float
    confidence: Optional[float]
    class_id: Optional[int]
    visibility: Optional[float]

@dataclass
class MOTTrack:
    track_id: int
    label: str
    boxes: List[MOTBox]

def extract_mot_zip(
    zip_path: str,
    extract_dir: Optional[str] = None
) -> Tuple[str, Optional[str]]:
    """
    Extracts a MOT zip archive (containing a 'gt' folder with gt.txt and labels.txt)
    and returns a tuple of (gt_txt_path, labels_txt_path).
    """
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"MOT zip file not found: {zip_path}")
        
    if extract_dir is None:
        extract_dir = os.path.join(os.path.dirname(os.path.abspath(zip_path)), "unpacked_mot")
        
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_dir)
        
    gt_path = None
    labels_path = None
    
    # Search extracted directory for gt.txt and labels.txt
    for root, _, files in os.walk(extract_dir):
        if "gt.txt" in files:
            gt_path = os.path.join(root, "gt.txt")
        if "labels.txt" in files:
            labels_path = os.path.join(root, "labels.txt")
            
    if not gt_path:
        raise FileNotFoundError(f"Could not find gt.txt inside zip archive: {zip_path}")
        
    return gt_path, labels_path

def parse_mot_labels(labels_path: Optional[str]) -> List[str]:
    """Reads labels.txt and returns a list of label names."""
    if labels_path and os.path.exists(labels_path) and zipfile.is_zipfile(labels_path):
        _, labels_path = extract_mot_zip(labels_path)
    if not labels_path or not os.path.exists(labels_path):
        return []
    with open(labels_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def parse_mot_gt(
    gt_path: str,
    labels_list: List[str],
    config: Dict[str, Any]
) -> Dict[int, MOTTrack]:
    """
    Parses MOT gt.txt file (or MOT zip file).
    Applies coordinate conversion (xywh -> xyxy), clamping, and frame index offset.
    Groups boxes by track_id.
    """
    if gt_path and os.path.exists(gt_path) and zipfile.is_zipfile(gt_path):
        gt_path, extracted_labels = extract_mot_zip(gt_path)
        if not labels_list and extracted_labels:
            labels_list = parse_mot_labels(extracted_labels)
    # 1. Read config options
    frame_indexing = config.get("frame_indexing", {})
    mot_base = frame_indexing.get("mot_frame_index_base", 1)
    cvat_base = frame_indexing.get("cvat_frame_index_base", 0)
    frame_offset = cvat_base - mot_base
    
    video_cfg = config.get("video", {})
    video_width = video_cfg.get("width", 1920)
    video_height = video_cfg.get("height", 1080)
    
    mot_cfg = config.get("mot", {})
    class_id_to_label = mot_cfg.get("class_id_to_label", {1: "player", 2: "ball"})
    # Convert keys to int just in case they were parsed as strings from YAML
    class_id_to_label = {int(k): v for k, v in class_id_to_label.items()}
    default_label = mot_cfg.get("default_label", "player")
    
    tracks: Dict[int, MOTTrack] = {}
    
    if not os.path.exists(gt_path):
        raise FileNotFoundError(f"MOT gt.txt file not found: {gt_path}")
        
    with open(gt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",") if p.strip()]
            if len(parts) < 6:
                # Malformed line or too few fields
                continue
                
            try:
                raw_frame = int(parts[0])
                track_id = int(parts[1])
                bb_left = float(parts[2])
                bb_top = float(parts[3])
                bb_width = float(parts[4])
                bb_height = float(parts[5])
                
                conf = float(parts[6]) if len(parts) > 6 else 1.0
                class_id = int(parts[7]) if len(parts) > 7 else 1
                visibility = float(parts[8]) if len(parts) > 8 else 1.0
            except ValueError:
                # Skip invalid lines
                continue
                
            # Apply frame offset
            frame = raw_frame + frame_offset
            
            # Convert xywh to xyxy and clamp to video size
            xtl = max(0.0, min(bb_left, float(video_width)))
            ytl = max(0.0, min(bb_top, float(video_height)))
            xbr = max(0.0, min(bb_left + bb_width, float(video_width)))
            ybr = max(0.0, min(bb_top + bb_height, float(video_height)))
            
            # Bounding box coordinate sanity check (xbr > xtl and ybr > ytl)
            if xbr <= xtl:
                xbr = min(xtl + 1.0, float(video_width))
            if ybr <= ytl:
                ybr = min(ytl + 1.0, float(video_height))
                
            box = MOTBox(
                frame=frame,
                track_id=track_id,
                xtl=round(xtl, 2),
                ytl=round(ytl, 2),
                xbr=round(xbr, 2),
                ybr=round(ybr, 2),
                confidence=conf,
                class_id=class_id,
                visibility=visibility
            )
            
            if track_id not in tracks:
                # Determine label from class_id
                label_name = None
                if labels_list and 0 < class_id <= len(labels_list):
                    label_name = labels_list[class_id - 1]
                if not label_name:
                    label_name = class_id_to_label.get(class_id)
                if not label_name:
                    label_name = default_label
                    
                tracks[track_id] = MOTTrack(
                    track_id=track_id,
                    label=label_name,
                    boxes=[]
                )
                
            tracks[track_id].boxes.append(box)
            
    # Sort boxes in each track by frame number
    for track in tracks.values():
        track.boxes.sort(key=lambda b: b.frame)
        
    return tracks
