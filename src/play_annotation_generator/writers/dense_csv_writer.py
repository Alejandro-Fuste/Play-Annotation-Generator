import csv
from typing import List, Optional
from ..models import DenseActionAnnotation, ActionEvent

def write_dense_action_csv(
    output_path: str,
    dense_annotations: List[DenseActionAnnotation],
    video_name: str
) -> None:
    """
    Writes a frame-by-frame flat CSV of active actions and coordinates.
    """
    headers = [
        "video_name",
        "frame",
        "actor_track_id",
        "xml_track_id",
        "position",
        "team_side",
        "action",
        "xtl",
        "ytl",
        "xbr",
        "ybr",
        "w",
        "h",
        "source"
    ]
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for da in sorted(dense_annotations, key=lambda x: (x.frame, x.xml_track_id)):
            w = da.bbox_xywh[2]
            h = da.bbox_xywh[3]
            row = [
                video_name,
                da.frame,
                da.actor_track_id,
                da.xml_track_id,
                da.position,
                da.team_side,
                da.action,
                da.bbox_xyxy[0],
                da.bbox_xyxy[1],
                da.bbox_xyxy[2],
                da.bbox_xyxy[3],
                w,
                h,
                da.source
            ]
            writer.writerow(row)

def write_normalized_events_csv(
    output_path: str,
    events: List[ActionEvent],
    video_name: str
) -> None:
    """
    Writes a list of parsed/resolved ActionEvent records to CSV for debugging.
    """
    headers = [
        "video_name",
        "video_id",
        "source_column",
        "action",
        "start_frame",
        "annotated_frame_role",
        "actor_track_id",
        "target_kind",
        "play_tag",
        "result_tag",
        "result_frame",
        "notes"
    ]
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for ev in sorted(events, key=lambda x: (x.start_frame, x.action, str(x.actor_track_id))):
            row = [
                video_name,
                ev.video_id or "",
                ev.source_column,
                ev.action,
                ev.start_frame,
                ev.annotated_frame_role,
                ev.actor_track_id or "",
                ev.target_kind,
                ev.play_tag or "",
                ev.result_tag or "",
                ev.result_frame if ev.result_frame is not None else "",
                ev.notes or ""
            ]
            writer.writerow(row)
