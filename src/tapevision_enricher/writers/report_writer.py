import json
from typing import Any, Dict, List

def write_validation_report(
    md_output_path: str,
    json_output_path: str,
    metrics: Dict[str, Any],
    warnings: List[str],
    errors: List[str],
    xml_path: str,
    csv_path: str,
    video_name: str
) -> None:
    """
    Writes validation reports in Markdown and JSON formats.
    """
    # 1. Write JSON report
    report_dict = {
        "video_name": video_name,
        "input_xml": xml_path,
        "input_csv": csv_path,
        "metrics": metrics,
        "warnings": warnings,
        "errors": errors
    }
    
    with open(json_output_path, "w") as f:
        json.dump(report_dict, f, indent=2)
        
    # 2. Write Markdown report
    status = "SUCCESS" if not errors else "FAILED"
    
    lines = [
        f"# TapeVision Annotation Enrichment Validation Report",
        f"",
        f"## **Summary**",
        f"- **Status**: {status}",
        f"- **Video Name**: `{video_name}`",
        f"- **Input XML**: `{xml_path}`",
        f"- **Input CSV**: `{csv_path}`",
        f"",
        f"## **Key Metrics**",
        f"| Metric | Value |",
        f"| :--- | :--- |",
        f"| Total XML Tracks | {metrics.get('num_tracks', 0)} |",
        f"| Player Tracks | {metrics.get('num_player_tracks', 0)} |",
        f"| Ball Tracks | {metrics.get('num_ball_tracks', 0)} |",
        f"| CSV events parsed | {metrics.get('num_events_parsed', 0)} |",
        f"| Action Segments inferred | {metrics.get('num_action_segments', 0)} |",
        f"| Invalid XML Bounding Boxes | {metrics.get('num_invalid_boxes', 0)} |",
        f"| Video Start Frame | {metrics.get('start_frame', 0)} |",
        f"| Video Stop Frame | {metrics.get('stop_frame', 0)} |",
        f"",
    ]
    
    # Errors Section
    lines.append("## **Pipeline Errors**")
    if errors:
        lines.append(f"> [!CAUTION]")
        lines.append(f"> The following critical issues were encountered:")
        for err in errors:
            lines.append(f"> - {err}")
    else:
        lines.append("*No critical pipeline errors encountered.*")
    lines.append("")
    
    # Warnings Section
    lines.append("## **Pipeline Warnings**")
    if warnings:
        lines.append(f"> [!WARNING]")
        lines.append(f"> The following non-critical warnings were logged:")
        for warn in warnings:
            lines.append(f"> - {warn}")
    else:
        lines.append("*No validation warnings encountered.*")
    lines.append("")
    
    # Recommended Actions
    lines.append("## **Recommended Fixes / Action Items**")
    actions = []
    if errors:
        actions.append("- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.")
        actions.append("- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.")
    if metrics.get('num_invalid_boxes', 0) > 0:
        actions.append("- Re-interpolate or fix bounding boxes with negative coordinates/inverted bounds inside CVAT.")
    if warnings:
        actions.append("- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.")
        
    if not actions:
        actions.append("- None! The data pipeline enrichment successfully generated all outputs with clean validation metrics.")
        
    for act in actions:
        lines.append(act)
        
    markdown_content = "\n".join(lines)
    
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
