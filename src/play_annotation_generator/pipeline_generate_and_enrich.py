import os
import zipfile
from typing import Any, Dict, List, Tuple, Optional

from .models import Track, ActionEvent, ActionSegment, DenseActionAnnotation
from .mot_parser import parse_mot_labels, parse_mot_gt, extract_mot_zip
from .player_track_sheet_parser import parse_player_track_csv
from .config import DEFAULT_CONFIG
from .cvat_xml_generator import generate_base_cvat_xml
from .enricher import run_enrichment_pipeline

def run_generate_and_enrich_pipeline(
    gt_path: str,
    labels_path: Optional[str],
    template_path: str,
    key_actions_csv: str,
    player_tracks_csv: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None,
    output_dir: str = "",
    target_video_name: Optional[str] = None,
    target_video_id: Optional[str] = None
) -> Tuple[Dict[str, Track], Dict[str, Any], List[ActionEvent], List[ActionSegment], List[DenseActionAnnotation], Dict[str, Any], List[str], List[str]]:
    """
    Orchestrates the generate_and_enrich_xml workflow (Mode B).
    
    1. Parses MOT tracking data (gt.txt and labels.txt or MOT zip).
    2. Parses Player Track ID CSV.
    3. Runs basic input validation checks.
    4. Generates a base CVAT XML in-memory and saves it.
    5. Calls the existing enrich_existing_xml pipeline on the generated base XML.
    """
    warnings: List[str] = []
    errors: List[str] = []
    if config is None:
        config = DEFAULT_CONFIG
    
    # 1. Parse MOT Labels and Tracking (supporting MOT zip archive)
    if gt_path and os.path.exists(gt_path) and zipfile.is_zipfile(gt_path):
        extracted_gt, extracted_labels = extract_mot_zip(gt_path, os.path.join(output_dir, "unpacked_mot"))
        gt_path = extracted_gt
        if not labels_path:
            labels_path = extracted_labels

    labels_list = parse_mot_labels(labels_path)
    mot_tracks = parse_mot_gt(gt_path, labels_list, config)
    
    # 2. Parse Player Track ID Assignments
    if player_tracks_csv:
        assignments, parse_warnings = parse_player_track_csv(player_tracks_csv, target_video_name, target_video_id)
        warnings.extend(parse_warnings)
    else:
        assignments = {}
        if target_video_name:
            play_name = target_video_name.rsplit("_", 1)[0] if "_" in target_video_name else target_video_name
            warn_msg = f"No Player Track assignment CSV available for play '{play_name}'; player position and team-side assignments will remain unknown."
        else:
            warn_msg = "No Player Track assignment CSV available; position and team-side assignments will remain unknown."
        warnings.append(warn_msg)
    
    # 3. Input Validation
    # Check: Every track ID in the Player Track ID sheet exists in gt.txt
    for tid_str in assignments.keys():
        try:
            tid = int(tid_str)
            if tid not in mot_tracks:
                msg = f"Track ID '{tid_str}' in Player Track ID sheet does not exist in MOT gt.txt."
                if config.get("validation", {}).get("strict", False):
                    errors.append(msg)
                else:
                    warnings.append(msg)
        except ValueError:
            msg = f"Invalid track ID '{tid_str}' in Player Track ID sheet. Must be an integer."
            if config.get("validation", {}).get("strict", False):
                errors.append(msg)
            else:
                warnings.append(msg)
                
    # Check if there are no player tracks found at all
    player_lbl = config.get("labels", {}).get("player_label", "player")
    num_players = sum(1 for t in mot_tracks.values() if t.label == player_lbl)
    if num_players == 0:
        errors.append("No player tracks found in MOT gt.txt.")
        
    # Check if we should fail or proceed
    if errors and config.get("validation", {}).get("strict", False):
        return {}, {}, [], [], [], {}, warnings, errors
        
    # 4. Generate Base XML
    os.makedirs(output_dir, exist_ok=True)
    generated_base_xml_path = os.path.join(output_dir, "generated_base_cvat.xml")
    
    try:
        generate_base_cvat_xml(
            template_path=template_path,
            output_xml_path=generated_base_xml_path,
            mot_tracks=mot_tracks,
            assignments=assignments,
            config=config
        )
    except Exception as e:
        errors.append(f"Failed to generate base CVAT XML: {e}")
        return {}, {}, [], [], [], {}, warnings, errors
        
    # 5. Invoke core enrichment pipeline on the newly created base XML
    target_video_filter = target_video_name or target_video_id
    
    try:
        (
            tracks,
            metadata,
            resolved_events,
            segments,
            dense_annotations,
            metrics,
            pipeline_warnings,
            pipeline_errors
        ) = run_enrichment_pipeline(
            xml_path=generated_base_xml_path,
            csv_path=key_actions_csv,
            config=config,
            target_video=target_video_filter
        )
    except Exception as e:
        errors.append(f"Core enrichment pipeline failed with exception: {e}")
        return {}, {}, [], [], [], {}, warnings, errors
        
    warnings.extend(pipeline_warnings)
    errors.extend(pipeline_errors)
    
    # 6. Additional Mode B Specific Validations
    start_frame = metadata.get("start_frame", 0)
    stop_frame = metadata.get("stop_frame", 0)
    
    # Check: Every action frame is within [start_frame, stop_frame]
    for ev in resolved_events:
        if ev.start_frame is not None and not (start_frame <= ev.start_frame <= stop_frame):
            msg = f"Action event '{ev.action}' has invalid start frame {ev.start_frame}. Video range is [{start_frame}, {stop_frame}]."
            if config.get("validation", {}).get("strict", False):
                errors.append(msg)
            else:
                warnings.append(msg)
                
    # Update metrics with MOT specific counts
    metrics["num_mot_rows_parsed"] = sum(len(t.boxes) for t in mot_tracks.values())
    metrics["num_mot_tracks"] = len(mot_tracks)
    metrics["num_assignments"] = len(assignments)
    
    return (
        tracks,
        metadata,
        resolved_events,
        segments,
        dense_annotations,
        metrics,
        warnings,
        errors
    )
