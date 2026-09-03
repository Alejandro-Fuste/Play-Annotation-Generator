import json
import os
from typing import Any, Dict, List
from ..models import Track, ActionSegment, DenseActionAnnotation

def write_play_annotation_json(
    output_path: str,
    tracks: Dict[str, Track],
    metadata: Dict[str, Any],
    segments: List[ActionSegment],
    dense_annotations: List[DenseActionAnnotation],
    config: Dict[str, Any],
    xml_path: str,
    csv_path: str
) -> None:
    """
    Writes the enriched annotations to a structured JSON file.
    """
    player_lbl = config.get("labels", {}).get("player_label", "player")
    ball_lbl = config.get("labels", {}).get("ball_label", "ball")
    
    # 1. Build players track lists
    players_json = []
    ball_json = []
    
    for xml_id, track in tracks.items():
        track_data = {
            "xml_track_id": xml_id,
            "actor_track_id": track.custom_track_id if track.custom_track_id else xml_id,
            "position": track.position if track.position and track.position != "undefined" else "Position_Unknown",
            "team_side": track.team_side if track.team_side and track.team_side != "undefined" else "Team_Unknown",
            "samples": []
        }
        
        for frame, box in sorted(track.boxes_by_frame.items()):
            w = box.xbr - box.xtl
            h = box.ybr - box.ytl
            track_data["samples"].append({
                "frame": frame,
                "bbox_xyxy": [box.xtl, box.ytl, box.xbr, box.ybr],
                "bbox_xywh": [box.xtl, box.ytl, w, h],
                "visible": not box.outside
            })
            
        if track.label == player_lbl:
            players_json.append(track_data)
        elif track.label == ball_lbl:
            # Ball doesn't need position/team_side typically, but let's follow the schema
            del track_data["position"]
            del track_data["team_side"]
            ball_json.append(track_data)
            
    # 2. Build actions JSON
    segments_json = []
    for seg in segments:
        segments_json.append({
            "actor_track_id": seg.actor_track_id,
            "xml_track_id": seg.xml_track_id,
            "position": seg.position if seg.position and seg.position != "undefined" else "Position_Unknown",
            "team_side": seg.team_side if seg.team_side and seg.team_side != "undefined" else "Team_Unknown",
            "action": seg.action,
            "start_frame": seg.start_frame,
            "end_frame": seg.end_frame,
            "source": seg.source
        })
        
    dense_json = []
    for da in dense_annotations:
        dense_json.append({
            "frame": da.frame,
            "actor_track_id": da.actor_track_id,
            "xml_track_id": da.xml_track_id,
            "position": da.position,
            "team_side": da.team_side,
            "action": da.action,
            "bbox_xyxy": da.bbox_xyxy,
            "bbox_xywh": da.bbox_xywh
        })
        
    # Read play-level fields from metadata
    play_tag = metadata.get("play_tag", "Play_Unknown")
    result_tag = metadata.get("result_tag", "Result_Unknown")
    result_frame = metadata.get("result_frame")
    if result_frame is None:
        result_frame = metadata.get("stop_frame", None)
    
    meta_sources = metadata.get("metadata_sources", {})
    clip_src = metadata.get("clip_source", {})
    
    out_dict = {
        "schema_version": "tapevision_annotation_enrichment_v1.1",
        "source": {
            "xml_file": os.path.basename(xml_path),
            "csv_file": os.path.basename(csv_path),
            "source_of_truth": "cvat_video_xml",
            "action_source": "key_actions_csv_plus_temporal_rules",
            "metadata_files": {
                "dataset_summary": os.path.basename(meta_sources.get("dataset_summary", "DatasetSummary.csv")),
                "actions": os.path.basename(meta_sources.get("actions", "actions.json")),
                "plays": os.path.basename(meta_sources.get("plays", "plays.json"))
            }
        },
        "clip": {
            "video_name": metadata.get("video_name", "Unknown"),
            "frame_start": metadata.get("start_frame", 0),
            "frame_end": metadata.get("stop_frame", 0),
            "num_frames": metadata.get("total_frames", 0),
            "source": {
                "start_time": clip_src.get("start_time"),
                "end_time": clip_src.get("end_time"),
                "clip_length": clip_src.get("clip_length"),
                "time_unit": "seconds",
                "view": clip_src.get("view"),
                "from_youtube": clip_src.get("from_youtube")
            }
        },
        "play": {
            "play_tag": play_tag,
            "definition": metadata.get("play_definition"),
            "result_tag": result_tag,
            "result_frame": result_frame
        },
        "tracks": {
            "players": players_json,
            "ball": ball_json
        },
        "actions": {
            "segments": segments_json,
            "dense_frame_annotations": dense_json
        },
        "definitions": {
            "actions": metadata.get("action_definitions", {})
        }
    }
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(out_dict, f, indent=2)


# Backward compatibility alias
write_tapevision_json = write_play_annotation_json
