import os
from typing import Any, Dict, List, Optional

from .models import Track, ActionEvent, ActionSegment, DenseActionAnnotation
from .writers import (
    write_enriched_xml,
    write_tapevision_json,
    write_dense_action_csv,
    write_normalized_events_csv,
    write_validation_report
)


def write_single_clip_outputs(
    output_dir: str,
    input_xml_for_enrichment: str,
    csv_path: str,
    tracks: Dict[str, Track],
    metadata: Dict[str, Any],
    events: List[ActionEvent],
    segments: List[ActionSegment],
    dense_annotations: List[DenseActionAnnotation],
    metrics: Dict[str, Any],
    warnings: List[str],
    errors: List[str],
    config: Dict[str, Any],
    target_video_name: Optional[str] = None,
    review_enabled: bool = False,
    quiet: bool = False
) -> Dict[str, str]:
    """
    Writes all standard single-clip outputs for both Mode A, Mode B, and Batch processing.
    
    Returns a dictionary mapping output keys to file paths.
    """
    os.makedirs(output_dir, exist_ok=True)
    v_name = metadata.get("video_name", target_video_name or "play")

    # External Metadata & Taxonomy Resolution
    if config.get("metadata_enrichment", {}).get("enabled", True):
        from .annotation_metadata import (
            load_dataset_summary,
            resolve_clip_source_metadata,
            load_action_definitions,
            resolve_used_action_definitions,
            load_play_definitions,
            resolve_play_definition,
        )

        input_cfg = config.get("input", {})
        ds_csv = input_cfg.get("dataset_summary_csv", "data/DatasetSummary.csv")
        act_json = input_cfg.get("actions_json") or ("data/actions.json" if os.path.exists("data/actions.json") else "data/actions11.json")
        if not input_cfg.get("actions_json") and not os.path.exists(act_json) and os.path.exists("data/actions11.json"):
            act_json = "data/actions11.json"
        pl_json = input_cfg.get("plays_json", "data/plays.json")

        policy_cfg = config.get("metadata_enrichment", {})
        missing_file_policy = policy_cfg.get("missing_source_file_policy", "error")

        # 1. Dataset Summary
        ds_index, ds_err = load_dataset_summary(ds_csv)
        if ds_err:
            if missing_file_policy == "error":
                errors.append(ds_err)
            else:
                warnings.append(ds_err)

        clip_source, ds_warns, ds_errs = resolve_clip_source_metadata(ds_index, v_name)
        warnings.extend(ds_warns)
        errors.extend(ds_errs)

        # 2. Action Definitions
        c_to_h_act, act_defs_raw, act_err = load_action_definitions(act_json)
        if act_err:
            if missing_file_policy == "error":
                errors.append(act_err)
            else:
                warnings.append(act_err)

        seg_dicts = [{"action": s.action} for s in segments]
        resolved_action_defs, act_warns = resolve_used_action_definitions(seg_dicts, c_to_h_act, act_defs_raw)
        warnings.extend(act_warns)

        # 3. Play Definition
        c_to_h_play, play_defs_raw, play_err = load_play_definitions(pl_json)
        if play_err:
            if missing_file_policy == "error":
                errors.append(play_err)
            else:
                warnings.append(play_err)

        play_tag = metadata.get("play_tag")
        resolved_play_def, play_warns = resolve_play_definition(play_tag, c_to_h_play, play_defs_raw)
        warnings.extend(play_warns)

        # Attach resolved metadata to metadata dict for serialization
        metadata["clip_source"] = clip_source
        metadata["play_definition"] = resolved_play_def
        metadata["action_definitions"] = resolved_action_defs
        metadata["metadata_sources"] = {
            "dataset_summary": os.path.basename(ds_csv),
            "actions": os.path.basename(act_json),
            "plays": os.path.basename(pl_json)
        }

    annotations_xml_path = os.path.join(output_dir, "annotations.xml")
    annotations_json_path = os.path.join(output_dir, "annotations.json")
    dense_csv_path = os.path.join(output_dir, "dense_actions.csv")
    events_csv_path = os.path.join(output_dir, "normalized_action_events.csv")
    report_md_path = os.path.join(output_dir, "validation_report.md")
    report_json_path = os.path.join(output_dir, "validation_report.json")

    written_paths: Dict[str, str] = {}

    if not quiet:
        print(f"Writing outputs to directory: {output_dir}")

    # Enriched XML (annotations.xml)
    if config.get("output", {}).get("write_enriched_xml", True):
        write_enriched_xml(input_xml_for_enrichment, annotations_xml_path, segments, tracks, config, metadata=metadata)
        written_paths["annotations_xml"] = annotations_xml_path
        written_paths["enriched_xml"] = annotations_xml_path
        if not quiet:
            print(f"  Saved Annotations CVAT XML -> {annotations_xml_path}")

    # TapeVision JSON (annotations.json)
    if config.get("output", {}).get("write_tapevision_json", True):
        write_tapevision_json(
            annotations_json_path,
            tracks,
            metadata,
            segments,
            dense_annotations,
            config,
            input_xml_for_enrichment,
            csv_path
        )
        written_paths["annotations_json"] = annotations_json_path
        written_paths["tapevision_json"] = annotations_json_path
        if not quiet:
            print(f"  Saved TapeVision Annotations JSON -> {annotations_json_path}")

    # Dense Actions CSV
    write_dense = (
        config.get("output", {}).get("write_dense_csv", True) or
        config.get("output", {}).get("write_dense_actions_csv", True)
    )
    if write_dense:
        write_dense_action_csv(dense_csv_path, dense_annotations, v_name)
        write_normalized_events_csv(events_csv_path, events, v_name)
        written_paths["dense_actions_csv"] = dense_csv_path
        written_paths["normalized_events_csv"] = events_csv_path
        if not quiet:
            print(f"  Saved Dense Actions CSV -> {dense_csv_path}")
            print(f"  Saved Normalized Action Events CSV -> {events_csv_path}")

    # Validation Reports
    write_report = (
        config.get("output", {}).get("write_validation_report", True) or
        config.get("output", {}).get("write_validation_report_md", True) or
        config.get("output", {}).get("write_validation_report_json", True)
    )
    if write_report:
        write_validation_report(
            report_md_path,
            report_json_path,
            metrics,
            warnings,
            errors,
            input_xml_for_enrichment,
            csv_path,
            v_name
        )
        written_paths["validation_report_md"] = report_md_path
        written_paths["validation_report_json"] = report_json_path
        if not quiet:
            print(f"  Saved Validation Report Markdown -> {report_md_path}")
            print(f"  Saved Validation Report JSON -> {report_json_path}")

    # Review Report (Generated every single time clip outputs are written)
    write_review = config.get("output", {}).get("write_review_report", True)
    if write_review:
        try:
            from .reviewer import review_play_outputs
            report = review_play_outputs(output_dir)
            report_file = os.path.join(output_dir, "review_report.md")
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            written_paths["review_report"] = report_file
            if not quiet and review_enabled:
                print("\n" + report)
            if not quiet:
                print(f"  Saved Review Report -> {report_file}")
        except Exception as e:
            if not quiet:
                print(f"  Warning: Failed to generate review_report.md: {e}")

    return written_paths
