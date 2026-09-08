import csv
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

MANIFEST_CSV_FIELDS = [
    "discovery_index",
    "play_name",
    "video_id",
    "clip_name",
    "tracking_file",
    "tracking_kind",
    "key_actions_source",
    "player_track_source",
    "player_tracks_resolved",
    "template_source",
    "output_directory",
    "preflight_status",
    "preflight_failure_type",
    "execution_state",
    "status",
    "warning_count",
    "error_count",
    "unknown_track_count",
    "missing_box_warning_count",
    "ball_track_count",
    "has_unknown_tracks",
    "has_missing_box_warnings",
    "has_no_ball_track",
    "num_tracks",
    "num_player_tracks",
    "num_ball_tracks",
    "num_action_segments",
    "elapsed_seconds",
    "failure_type",
    "message",
    "traceback_file",
]

SUMMARY_CSV_FIELDS = [
    "play_name",
    "discovered",
    "selected",
    "attempted",
    "pass_count",
    "warning_count",
    "failed_count",
    "skipped_count",
    "total_unknown_tracks",
    "total_missing_box_warnings",
    "total_no_ball_tracks",
]


def write_batch_manifest_csv(manifest_csv_path: str, results: List[Dict[str, Any]]) -> None:
    """
    Atomically writes the batch manifest CSV file.
    """
    tmp_path = f"{manifest_csv_path}.tmp"
    os.makedirs(os.path.dirname(os.path.abspath(manifest_csv_path)), exist_ok=True)

    with open(tmp_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MANIFEST_CSV_FIELDS)
        writer.writeheader()
        for res in results:
            row = {}
            for field in MANIFEST_CSV_FIELDS:
                val = res.get(field)
                if val is None:
                    row[field] = ""
                else:
                    row[field] = val
            writer.writerow(row)

    os.replace(tmp_path, manifest_csv_path)


def write_batch_manifest_json(
    manifest_json_path: str,
    results: List[Dict[str, Any]],
    batch_root: str,
    arguments: Dict[str, Any]
) -> None:
    """
    Atomically writes the batch manifest JSON file.
    """
    tmp_path = f"{manifest_json_path}.tmp"
    os.makedirs(os.path.dirname(os.path.abspath(manifest_json_path)), exist_ok=True)

    data = {
        "schema_version": "tapevision_batch_manifest_v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "batch_root": batch_root,
        "arguments": arguments,
        "results": results
    }

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    os.replace(tmp_path, manifest_json_path)


def write_batch_summary_csv(summary_csv_path: str, play_stats: Dict[str, Dict[str, Any]]) -> None:
    """
    Atomically writes the batch summary CSV file (by play type).
    """
    tmp_path = f"{summary_csv_path}.tmp"
    os.makedirs(os.path.dirname(os.path.abspath(summary_csv_path)), exist_ok=True)

    with open(tmp_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_CSV_FIELDS)
        writer.writeheader()
        for play_name, stats in sorted(play_stats.items()):
            row = {
                "play_name": play_name,
                "discovered": stats.get("discovered", 0),
                "selected": stats.get("selected", 0),
                "attempted": stats.get("attempted", 0),
                "pass_count": stats.get("pass", 0),
                "warning_count": stats.get("warning", 0),
                "failed_count": stats.get("failed", 0),
                "skipped_count": stats.get("skipped", 0),
                "total_unknown_tracks": stats.get("unknown_tracks", 0),
                "total_missing_box_warnings": stats.get("missing_box_warnings", 0),
                "total_no_ball_tracks": stats.get("no_ball_tracks", 0),
            }
            writer.writerow(row)

    os.replace(tmp_path, summary_csv_path)


def write_batch_summary_json(
    summary_json_path: str,
    results: List[Dict[str, Any]],
    batch_root: str,
    totals: Dict[str, Any],
    play_stats: Dict[str, Dict[str, Any]]
) -> None:
    """
    Atomically writes the batch summary JSON file.
    """
    tmp_path = f"{summary_json_path}.tmp"
    os.makedirs(os.path.dirname(os.path.abspath(summary_json_path)), exist_ok=True)

    data = {
        "schema_version": "tapevision_batch_summary_v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "batch_root": batch_root,
        "totals": totals,
        "plays": play_stats,
        "clips": results
    }

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    os.replace(tmp_path, summary_json_path)


def write_batch_summary_markdown(
    summary_md_path: str,
    results: List[Dict[str, Any]],
    total_discovered: int,
    total_preflight_ready: int,
    total_preflight_failed: int,
    total_selected: int,
    total_elapsed_seconds: float
) -> None:
    """
    Writes the batch summary Markdown file derived from results.
    """
    os.makedirs(os.path.dirname(os.path.abspath(summary_md_path)), exist_ok=True)

    attempted = [r for r in results if r.get("execution_state") == "PROCESSED"]
    pass_cnt = sum(1 for r in results if r.get("status") == "PASS")
    warning_cnt = sum(1 for r in results if r.get("status") == "WARNING")
    failed_cnt = sum(1 for r in results if r.get("status") == "FAILED")
    skipped_cnt = sum(1 for r in results if r.get("execution_state") == "SKIPPED")

    total_warnings = sum(int(r.get("warning_count") or 0) for r in results)
    total_errors = sum(int(r.get("error_count") or 0) for r in results)

    total_unknown_tracks = sum(int(r.get("unknown_track_count") or 0) for r in results)
    total_missing_box_warnings = sum(int(r.get("missing_box_warning_count") or 0) for r in results)
    clips_with_unknown_tracks = sum(1 for r in results if r.get("has_unknown_tracks"))
    clips_with_missing_boxes = sum(1 for r in results if r.get("has_missing_box_warnings"))
    clips_with_no_ball = sum(1 for r in results if r.get("has_no_ball_track"))

    # Failure type counts
    failure_counts: Dict[str, int] = {}
    for r in results:
        ft = r.get("failure_type")
        if ft:
            failure_counts[ft] = failure_counts.get(ft, 0) + 1

    # Play breakdown
    play_stats: Dict[str, Dict[str, int]] = {}
    for r in results:
        pt = r.get("play_name") or r.get("play_type") or "Unknown"
        if pt not in play_stats:
            play_stats[pt] = {
                "discovered": 0,
                "selected": 0,
                "attempted": 0,
                "pass": 0,
                "warning": 0,
                "failed": 0,
                "skipped": 0,
                "unknown_tracks": 0,
                "missing_box_warnings": 0,
                "no_ball_tracks": 0
            }

        play_stats[pt]["discovered"] += 1
        if r.get("execution_state") in ("PROCESSED", "SKIPPED"):
            play_stats[pt]["selected"] += 1
        if r.get("execution_state") == "PROCESSED":
            play_stats[pt]["attempted"] += 1

        st = r.get("status")
        ex = r.get("execution_state")

        if ex == "SKIPPED":
            play_stats[pt]["skipped"] += 1
        elif st == "PASS":
            play_stats[pt]["pass"] += 1
        elif st == "WARNING":
            play_stats[pt]["warning"] += 1
        elif st == "FAILED":
            play_stats[pt]["failed"] += 1

        play_stats[pt]["unknown_tracks"] += int(r.get("unknown_track_count") or 0)
        play_stats[pt]["missing_box_warnings"] += int(r.get("missing_box_warning_count") or 0)
        if r.get("has_no_ball_track"):
            play_stats[pt]["no_ball_tracks"] += 1

    lines = [
        "# Play-Annotation-Generator Batch Processing Summary",
        "",
        "## Run Overview",
        "",
        f"- Total discovered: {total_discovered}",
        f"- Total preflight ready: {total_preflight_ready}",
        f"- Total preflight failed: {total_preflight_failed}",
        f"- Total selected after filters: {total_selected}",
        f"- Total attempted: {len(attempted)}",
        f"- PASS: {pass_cnt}",
        f"- WARNING: {warning_cnt}",
        f"- FAILED: {failed_cnt}",
        f"- SKIPPED: {skipped_cnt}",
        f"- Total validation warnings: {total_warnings}",
        f"- Total validation errors: {total_errors}",
        f"- Total elapsed seconds: {total_elapsed_seconds:.3f}",
        "",
        "## Dataset Quality Signals",
        "",
        f"- Total unknown/unassigned tracks: {total_unknown_tracks} (across {clips_with_unknown_tracks} clips)",
        f"- Total missing-box warnings: {total_missing_box_warnings} (across {clips_with_missing_boxes} clips)",
        f"- Clips with no ball track: {clips_with_no_ball}",
        "",
    ]

    if failure_counts:
        lines.extend([
            "## Failure Reasons",
            "",
            "| Failure Type | Count |",
            "|---|---:|",
        ])
        for ft, cnt in sorted(failure_counts.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| {ft} | {cnt} |")
        lines.append("")

    if play_stats:
        lines.extend([
            "## Results By Play Type",
            "",
            "| Play Type | Discovered | Selected | PASS | WARNING | FAILED | SKIPPED |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ])
        for pt, stats in sorted(play_stats.items()):
            lines.append(
                f"| {pt} | {stats['discovered']} | {stats['selected']} | {stats['pass']} | "
                f"{stats['warning']} | {stats['failed']} | {stats['skipped']} |"
            )
        lines.append("")

    failed_clips = [r for r in results if r.get("status") == "FAILED"]
    if failed_clips:
        lines.extend([
            "## Failed Clips",
            "",
            "| Clip Name | Play Name | Video ID | Failure Type | Message |",
            "|---|---|---|---|---|",
        ])
        for fc in failed_clips:
            cn = fc.get("clip_name") or fc.get("clip_key") or "Unknown"
            pn = fc.get("play_name") or fc.get("play_type") or ""
            vid = fc.get("video_id") or ""
            ft = fc.get("failure_type") or "error"
            msg = (fc.get("message") or "").replace("\n", " ")
            lines.append(f"| {cn} | {pn} | {vid} | {ft} | {msg} |")
        lines.append("")

    with open(summary_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
