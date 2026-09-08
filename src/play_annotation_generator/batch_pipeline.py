import csv
import json
import os
import re
import sys
import time
import traceback
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from .annotation_metadata import load_play_definitions
from .config import DEFAULT_CONFIG, load_config
from .output_pipeline import write_single_clip_outputs
from .pipeline_generate_and_enrich import run_generate_and_enrich_pipeline
from .player_track_sheet_parser import parse_player_track_csv
from .wide_action_csv_parser import parse_wide_action_csv
from .writers.batch_report_writer import (
    write_batch_manifest_csv,
    write_batch_manifest_json,
    write_batch_summary_csv,
    write_batch_summary_json,
    write_batch_summary_markdown,
)


@dataclass
class TrackingInput:
    source_path: Path
    input_kind: str  # "GT_TXT" or "MOT_ZIP"
    relative_path: Path
    discovery_index: int
    folder_play_name: Optional[str] = None
    filename_play_name: Optional[str] = None
    video_id: Optional[str] = None
    clip_name: Optional[str] = None


@dataclass
class ResolvedClipIdentity:
    status: str  # "READY", "FAILED"
    failure_type: Optional[str] = None
    video_name: Optional[str] = None
    video_id: Optional[str] = None
    play_type: Optional[str] = None
    clip_key: Optional[str] = None
    message: Optional[str] = None
    key_actions_csv: Optional[Path] = None
    player_tracks_csv: Optional[Path] = None
    player_tracks_resolved: bool = True


@dataclass
class BatchClipJob:
    tracking_input: TrackingInput
    video_name: str
    video_id: str
    play_type: str
    clip_key: str
    output_dir: Path
    template_path: Path
    key_actions_csv: Path
    player_tracks_csv: Optional[Path] = None
    labels_path: Optional[Path] = None
    player_tracks_resolved: bool = True


def sanitize_filename_component(name: str) -> str:
    """
    Sanitizes a string for use as a filesystem directory component.
    """
    s = name.strip()
    s = re.sub(r'[\\/]', '_', s)
    s = re.sub(r'[\x00-\x1f\x7f]', '_', s)
    s = re.sub(r'_+', '_', s)
    if s in ('.', '..', ''):
        s = 'clip'
    return s


def parse_numeric_sort_key(video_id: Optional[str]) -> Tuple[int, str]:
    """
    Parses numeric sort key for video_id so 1, 2, 10 sort numerically.
    """
    if not video_id:
        return (999999999, "")
    try:
        val = int(video_id)
        return (val, str(video_id))
    except ValueError:
        return (999999999, str(video_id))


def discover_tracking_inputs(
    gt_dir: Path,
    output_root: Optional[Path] = None
) -> List[TrackingInput]:
    """
    Recursively discovers tracking inputs in gt_dir (gt.txt and .zip files).
    Ignores unpacked_mot subdirectories and anything inside output_root or _batch.
    Sorts deterministically by play name, numeric video ID, and relative POSIX path.
    """
    gt_dir = gt_dir.resolve()
    if output_root:
        output_root = output_root.resolve()

    candidates: List[Tuple[Path, str, Optional[str], Optional[str], Optional[str], Optional[str]]] = []

    for root, dirs, files in os.walk(gt_dir):
        current_path = Path(root).resolve()

        # Skip unpacked_mot or _batch directories
        if current_path.name.casefold() in ("unpacked_mot", "_batch", "_failures"):
            dirs.clear()
            continue

        # Skip output_root directory if inside gt_dir
        if output_root and (current_path == output_root or output_root in current_path.parents):
            dirs.clear()
            continue

        # Filter dirs in-place
        dirs[:] = [
            d for d in dirs
            if d.casefold() not in ("unpacked_mot", "_batch", "_failures") and not (output_root and (current_path / d).resolve() == output_root)
        ]

        for file in files:
            file_path = current_path / file
            kind = None
            if file.casefold() == "gt.txt":
                kind = "GT_TXT"
            elif file.casefold().endswith(".zip"):
                kind = "MOT_ZIP"

            if not kind:
                continue

            # Derive folder play name (first folder level under gt_dir)
            rel = file_path.relative_to(gt_dir)
            parts = rel.parts
            folder_play_name = parts[0] if len(parts) > 1 else None

            # Parse filename play name and video ID
            filename_play_name = None
            vid_id = None
            clip_name = None

            stem = file
            if stem.casefold().endswith("_cvat_mot.zip"):
                stem = stem[:-13]
            elif stem.casefold().endswith(".zip"):
                stem = stem[:-4]
            elif stem.casefold() == "gt.txt":
                stem = file_path.parent.name
                if stem.casefold() == "gt":
                    stem = file_path.parent.parent.name

            if "_" in stem:
                filename_play_name, vid_id = stem.rsplit("_", 1)
                filename_play_name = filename_play_name.strip()
                vid_id = vid_id.strip()
                clip_name = f"{filename_play_name}_{vid_id}"
            else:
                filename_play_name = stem.strip()
                clip_name = stem.strip()

            candidates.append((file_path, kind, folder_play_name, filename_play_name, vid_id, clip_name))

    # Sort deterministically: play name, numeric video ID, clip_name, relative path
    def sort_key(item):
        fpath, kind, folder_play, file_play, vid_id, clip_name = item
        p_name = (folder_play or file_play or "").casefold()
        num_key, str_key = parse_numeric_sort_key(vid_id)
        rel_posix = fpath.relative_to(gt_dir).as_posix()
        return (p_name, num_key, str_key, (clip_name or "").casefold(), rel_posix)

    candidates.sort(key=sort_key)

    results: List[TrackingInput] = []
    for idx, (path, kind, folder_play, file_play, vid_id, clip_name) in enumerate(candidates):
        rel_path = path.relative_to(gt_dir)
        results.append(
            TrackingInput(
                source_path=path,
                input_kind=kind,
                relative_path=rel_path,
                discovery_index=idx,
                folder_play_name=folder_play,
                filename_play_name=file_play,
                video_id=vid_id,
                clip_name=clip_name
            )
        )

    return results


def resolve_per_play_sources(
    play_name: str,
    key_actions_arg: Path,
    player_tracks_arg: Path,
    config: Optional[Dict[str, Any]] = None
) -> Tuple[Optional[Path], Optional[Path], List[str]]:
    """
    Resolves the Key Actions CSV and Player Track CSV for a given play_name.
    Supports directory lookups (e.g. data/key_actions/<PlayName>.csv) and configuration mappings.
    """
    errors = []

    # 1. Check config overrides if available
    cfg_sources = (config or {}).get("batch", {}).get("play_sources", {}).get(play_name, {})
    cfg_ka = cfg_sources.get("key_actions")
    cfg_pt = cfg_sources.get("player_tracks")

    # 2. Key Actions CSV resolution
    ka_path: Optional[Path] = None
    if cfg_ka and Path(cfg_ka).exists():
        ka_path = Path(cfg_ka)
    elif key_actions_arg.is_file():
        ka_path = key_actions_arg
    elif key_actions_arg.is_dir():
        cand1 = key_actions_arg / f"{play_name}.csv"
        cand2 = key_actions_arg / play_name / "KeyActions_Sheet.csv"
        cand3 = key_actions_arg / play_name / f"{play_name}.csv"
        if cand1.exists():
            ka_path = cand1
        elif cand2.exists():
            ka_path = cand2
        elif cand3.exists():
            ka_path = cand3
        else:
            errors.append(f"missing_key_actions_source: Key Actions CSV not found for play '{play_name}' in directory '{key_actions_arg}'")
    else:
        if key_actions_arg.exists():
            ka_path = key_actions_arg
        else:
            errors.append(f"missing_key_actions_source: Key Actions source path does not exist: {key_actions_arg}")

    # 3. Player Tracks CSV resolution (optional per play)
    pt_path: Optional[Path] = None
    if cfg_pt and Path(cfg_pt).exists():
        pt_path = Path(cfg_pt)
    elif player_tracks_arg and player_tracks_arg.is_file():
        pt_path = player_tracks_arg
    elif player_tracks_arg and player_tracks_arg.is_dir():
        cand1 = player_tracks_arg / f"{play_name}.csv"
        cand2 = player_tracks_arg / play_name / "PlayerTrack_ID_Sheet.csv"
        cand3 = player_tracks_arg / play_name / f"{play_name}.csv"
        if cand1.exists():
            pt_path = cand1
        elif cand2.exists():
            pt_path = cand2
        elif cand3.exists():
            pt_path = cand3
        else:
            pt_path = None
    else:
        if player_tracks_arg and player_tracks_arg.exists():
            pt_path = player_tracks_arg
        else:
            pt_path = None

    return ka_path, pt_path, errors


def resolve_clip_preflight(
    tr_input: TrackingInput,
    key_actions_arg: Path,
    player_tracks_arg: Path,
    recognized_plays: Set[str],
    config: Optional[Dict[str, Any]] = None
) -> ResolvedClipIdentity:
    """
    Performs preflight validation for a discovered clip input.
    """
    f_play = tr_input.folder_play_name
    fn_play = tr_input.filename_play_name
    vid_id = tr_input.video_id
    clip_name = tr_input.clip_name

    if not fn_play or not vid_id or not clip_name:
        return ResolvedClipIdentity(
            status="FAILED",
            failure_type="malformed_filename",
            message=f"Could not parse play name or video ID from filename: {tr_input.relative_path.name}"
        )

    # Folder play vs filename play consistency check
    if f_play and f_play.casefold() != fn_play.casefold():
        return ResolvedClipIdentity(
            status="FAILED",
            failure_type="folder_play_mismatch",
            play_type=fn_play,
            video_id=vid_id,
            clip_key=clip_name,
            message=f"Folder play name '{f_play}' does not match filename play name '{fn_play}'"
        )

    play_type = fn_play

    # Recognized play validation against plays.json
    if recognized_plays:
        play_matched = False
        for rec in recognized_plays:
            if rec.casefold() == play_type.casefold() or rec.casefold() == f"play_run_{play_type}".casefold() or rec.casefold() == f"play_pass_{play_type}".casefold() or rec.casefold().endswith(f"_{play_type}".casefold()):
                play_matched = True
                break
        if not play_matched:
            return ResolvedClipIdentity(
                status="FAILED",
                failure_type="unrecognized_play",
                play_type=play_type,
                video_id=vid_id,
                clip_key=clip_name,
                message=f"Play type '{play_type}' is not recognized in plays.json definitions"
            )

    # Per-play CSV source resolution
    ka_csv, pt_csv, src_errors = resolve_per_play_sources(play_type, key_actions_arg, player_tracks_arg, config)
    if src_errors:
        fail_type = "missing_key_actions_source" if "key_actions" in src_errors[0] else "missing_player_tracks_source"
        return ResolvedClipIdentity(
            status="FAILED",
            failure_type=fail_type,
            play_type=play_type,
            video_id=vid_id,
            clip_key=clip_name,
            message="; ".join(src_errors),
            key_actions_csv=ka_csv,
            player_tracks_csv=pt_csv,
            player_tracks_resolved=False
        )

    pt_resolved = pt_csv is not None
    if pt_resolved:
        msg = "Preflight checks passed"
    else:
        msg = f"Player Track CSV not available for play '{play_type}'; position/team assignments will remain unknown."

    return ResolvedClipIdentity(
        status="READY",
        video_name=f"{play_type}_{vid_id}",
        video_id=vid_id,
        play_type=play_type,
        clip_key=clip_name,
        message=msg,
        key_actions_csv=ka_csv,
        player_tracks_csv=pt_csv,
        player_tracks_resolved=pt_resolved
    )


def check_clip_completion(
    output_dir: Path,
    config: Dict[str, Any]
) -> Tuple[bool, bool, Optional[Dict[str, Any]]]:
    """
    Checks whether a clip output directory contains complete and parseable outputs.
    Returns (is_complete, is_partial, validation_report_data).
    """
    if not output_dir.exists() or not output_dir.is_dir():
        return False, False, None

    files = [f.name for f in output_dir.iterdir() if f.is_file()]
    if not files:
        return False, False, None

    json_path = output_dir / "annotations.json"
    report_json_path = output_dir / "validation_report.json"

    # Must have parseable annotations.json and validation_report.json
    if not json_path.exists() or not report_json_path.exists():
        return False, True, None

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            json.load(f)
    except Exception:
        return False, True, None

    report_data = None
    try:
        with open(report_json_path, "r", encoding="utf-8") as f:
            report_data = json.load(f)
        if not isinstance(report_data, dict):
            return False, True, None
        if "metrics" not in report_data or "warnings" not in report_data or "errors" not in report_data:
            return False, True, None
    except Exception:
        return False, True, None

    # Check remaining standard outputs enabled in config
    required_artifacts = []
    if config.get("output", {}).get("write_enriched_xml", True):
        required_artifacts.append("annotations.xml")

    write_dense = (
        config.get("output", {}).get("write_dense_csv", True) or
        config.get("output", {}).get("write_dense_actions_csv", True)
    )
    if write_dense:
        required_artifacts.append("dense_actions.csv")
        required_artifacts.append("normalized_action_events.csv")

    write_report = (
        config.get("output", {}).get("write_validation_report", True) or
        config.get("output", {}).get("write_validation_report_md", True) or
        config.get("output", {}).get("write_validation_report_json", True)
    )
    if write_report:
        required_artifacts.append("validation_report.md")

    # Base XML generated in Mode B
    required_artifacts.append("generated_base_cvat.xml")

    for artifact in required_artifacts:
        if not (output_dir / artifact).exists():
            return False, True, report_data

    return True, False, report_data


def clean_clip_outputs(output_dir: Path) -> None:
    """
    Removes known pipeline output files from output_dir for overwrite handling.
    """
    known_files = [
        "generated_base_cvat.xml",
        "annotations.xml",
        "annotations.json",
        "enriched_cvat.xml",
        "tapevision_annotations.json",
        "dense_actions.csv",
        "normalized_action_events.csv",
        "validation_report.md",
        "validation_report.json",
        "review_report.md",
        "review_report.txt",
    ]
    if output_dir.exists():
        for fname in known_files:
            fpath = output_dir / fname
            if fpath.exists():
                try:
                    fpath.unlink()
                except Exception:
                    pass

        unpacked = output_dir / "unpacked_mot"
        if unpacked.exists() and unpacked.is_dir():
            import shutil
            try:
                shutil.rmtree(unpacked)
            except Exception:
                pass


def extract_quality_signals(report_data: Optional[Dict[str, Any]], tracks: Optional[Any] = None) -> Dict[str, Any]:
    """
    Extracts quality signals from validation report data and parsed tracks.
    Deduplicates unknown player tracks consistently by XML track ID so that multiple warnings or attributes
    for the same physical player track count as 1 unique unknown track.
    """
    metrics = report_data.get("metrics", {}) if report_data else {}
    warnings = report_data.get("warnings", []) if report_data else []

    unknown_track_ids: Set[str] = set()
    missing_box_warning_cnt = 0

    for w in warnings:
        w_str = str(w)
        if "Position_Unknown" in w_str or "Team_Unknown" in w_str or "undefined position" in w_str or "undefined team" in w_str:
            match = re.search(r"track '([^']+)'", w_str, re.IGNORECASE)
            if match:
                unknown_track_ids.add(match.group(1))
            else:
                unknown_track_ids.add(w_str)
        if "without a visible bounding box" in w_str or "missing_box" in w_str.lower():
            missing_box_warning_cnt += 1

    if tracks:
        track_values = tracks.values() if isinstance(tracks, dict) else tracks
        player_label = "player"
        for t in track_values:
            lbl = getattr(t, "label", "player") or "player"
            if lbl != player_label:
                continue

            t_pos = getattr(t, "position", "") or ""
            t_side = getattr(t, "team_side", "") or ""
            t_id = getattr(t, "xml_track_id", None) or getattr(t, "custom_track_id", None) or getattr(t, "track_id", None)

            if t_pos in ("Position_Unknown", "undefined", "") or t_side in ("Team_Unknown", "undefined", ""):
                if t_id is not None:
                    unknown_track_ids.add(str(t_id))

    unknown_track_cnt = len(unknown_track_ids)
    ball_track_cnt = int(metrics.get("num_ball_tracks") or 0)

    return {
        "unknown_track_count": unknown_track_cnt,
        "missing_box_warning_count": missing_box_warning_cnt,
        "ball_track_count": ball_track_cnt,
        "has_unknown_tracks": (unknown_track_cnt > 0),
        "has_missing_box_warnings": (missing_box_warning_cnt > 0),
        "has_no_ball_track": (ball_track_cnt == 0)
    }


def run_batch_pipeline(
    gt_dir: str,
    template_path: str,
    key_actions_csv: str,
    player_tracks_csv: str,
    config_path: Optional[str] = None,
    output_dir: Optional[str] = None,
    labels_path: Optional[str] = None,
    dataset_summary_path: Optional[str] = None,
    actions_json_path: Optional[str] = None,
    plays_json_path: Optional[str] = None,
    limit: Optional[int] = None,
    play_filter: Optional[str] = None,
    video_id_filter: Optional[str] = None,
    status_filter: Optional[str] = None,
    skip_existing: bool = False,
    overwrite: bool = False,
    review_enabled: bool = True,
    verbose: bool = False
) -> Dict[str, Any]:
    """
    Main batch processing entry point adhering to Batch Processing Spec v2.
    """
    batch_start_time = time.time()

    if skip_existing and overwrite:
        raise ValueError("Flags --resume/--skip-existing and --overwrite are mutually exclusive.")

    if limit is not None and limit <= 0:
        raise ValueError("--limit must be a positive integer.")

    if status_filter:
        status_filter = status_filter.upper()
        if status_filter not in ("PASS", "WARNING", "FAILED"):
            raise ValueError("--status filter must be one of PASS, WARNING, FAILED.")

    # Validate root paths
    gt_dir_path = Path(gt_dir)
    if not gt_dir_path.exists() or not gt_dir_path.is_dir():
        raise FileNotFoundError(f"Tracking root directory does not exist: {gt_dir}")

    template_p = Path(template_path)
    if not template_p.exists():
        raise FileNotFoundError(f"--template file does not exist: {template_path}")

    key_actions_p = Path(key_actions_csv)
    player_tracks_p = Path(player_tracks_csv)

    # 2. Load Config & Taxonomies
    config = load_config(config_path)
    config["mode"] = "generate_and_enrich_xml"

    if dataset_summary_path:
        config.setdefault("input", {})["dataset_summary_csv"] = dataset_summary_path
    if actions_json_path:
        config.setdefault("input", {})["actions_json"] = actions_json_path
    if plays_json_path:
        config.setdefault("input", {})["plays_json"] = plays_json_path

    # Verify shared plays.json
    pl_path = config.get("input", {}).get("plays_json", "data/plays.json")
    canonical_plays, play_defs, pl_err = load_play_definitions(pl_path)
    if pl_err:
        raise FileNotFoundError(f"Authoritative plays.json load error: {pl_err}")

    recognized_play_labels = set(canonical_plays.keys()) | set(play_defs.keys())

    # 3. Output Root Setup
    if output_dir:
        batch_root = Path(output_dir)
    else:
        cfg_out = config.get("output", {}).get("output_dir", "outputs")
        batch_root = Path(cfg_out) / "batch"

    batch_root.mkdir(parents=True, exist_ok=True)
    meta_batch_dir = batch_root / "_batch"
    meta_batch_dir.mkdir(parents=True, exist_ok=True)
    failures_dir = meta_batch_dir / "failures"

    manifest_csv_path = str(meta_batch_dir / "batch_manifest.csv")
    manifest_json_path = str(meta_batch_dir / "batch_manifest.json")
    summary_csv_path = str(meta_batch_dir / "batch_summary.csv")
    summary_json_path = str(meta_batch_dir / "batch_summary.json")
    summary_md_path = str(meta_batch_dir / "batch_summary.md")

    cli_arguments = {
        "gt_dir": str(gt_dir_path.resolve()),
        "template": str(template_p.resolve()),
        "key_actions": str(key_actions_p.resolve()),
        "player_tracks": str(player_tracks_p.resolve()),
        "config": str(Path(config_path).resolve()) if config_path else None,
        "output": str(batch_root.resolve()),
        "play": play_filter,
        "video_id": video_id_filter,
        "status": status_filter,
        "limit": limit,
        "skip_existing": skip_existing,
        "overwrite": overwrite,
        "review": review_enabled,
        "verbose": verbose
    }

    # 4. Discovery
    discovered_inputs = discover_tracking_inputs(gt_dir_path, batch_root)
    total_discovered = len(discovered_inputs)

    # 5. Preflight Input Resolution
    resolved_jobs: List[Tuple[TrackingInput, ResolvedClipIdentity]] = []
    matched_jobs: List[BatchClipJob] = []

    total_preflight_ready = 0
    total_preflight_failed = 0

    for tr_input in discovered_inputs:
        identity = resolve_clip_preflight(
            tr_input=tr_input,
            key_actions_arg=key_actions_p,
            player_tracks_arg=player_tracks_p,
            recognized_plays=recognized_play_labels,
            config=config
        )
        resolved_jobs.append((tr_input, identity))

        if identity.status == "READY":
            total_preflight_ready += 1
            # Structured output path: <batch_output_root>/<PlayName>/<ClipName>/
            job_out_dir = batch_root / identity.play_type / identity.clip_key
            matched_jobs.append(
                BatchClipJob(
                    tracking_input=tr_input,
                    video_name=identity.video_name,
                    video_id=identity.video_id,
                    play_type=identity.play_type,
                    clip_key=identity.clip_key,
                    output_dir=job_out_dir,
                    template_path=template_p,
                    key_actions_csv=identity.key_actions_csv,
                    player_tracks_csv=identity.player_tracks_csv,
                    labels_path=Path(labels_path) if labels_path else None,
                    player_tracks_resolved=identity.player_tracks_resolved
                )
            )
        else:
            total_preflight_failed += 1

    # 6. Apply Selection Filters & Collision Check
    selected_jobs: List[BatchClipJob] = []
    seen_clip_keys: Dict[str, BatchClipJob] = {}
    collided_keys: Set[str] = set()

    # Parse video_id filters (support comma separated)
    vid_id_set: Optional[Set[str]] = None
    if video_id_filter:
        vid_id_set = {v.strip() for v in video_id_filter.split(",") if v.strip()}

    for job in matched_jobs:
        if play_filter and job.play_type.casefold() != play_filter.casefold():
            continue
        if vid_id_set and job.video_id not in vid_id_set:
            continue

        if job.clip_key in seen_clip_keys:
            collided_keys.add(job.clip_key)
        else:
            seen_clip_keys[job.clip_key] = job
            selected_jobs.append(job)

    # Sort selected jobs deterministically
    def job_sort_key(j: BatchClipJob):
        num_key, str_key = parse_numeric_sort_key(j.video_id)
        return (j.play_type.casefold(), num_key, str_key, j.clip_key.casefold())

    selected_jobs.sort(key=job_sort_key)
    total_selected = len(selected_jobs)

    if limit is not None:
        selected_jobs = selected_jobs[:limit]

    # Initial Results List for Manifest
    results: List[Dict[str, Any]] = []

    # Record preflight failure items in results list
    for tr_input, identity in resolved_jobs:
        if identity.status != "READY":
            p_name = identity.play_type or tr_input.filename_play_name or tr_input.folder_play_name or "Unknown"
            v_id = identity.video_id or tr_input.video_id or ""
            c_key = identity.clip_key or tr_input.clip_name or sanitize_filename_component(tr_input.relative_path.stem)
            results.append({
                "discovery_index": tr_input.discovery_index,
                "play_name": p_name,
                "video_id": v_id,
                "clip_name": c_key,
                "tracking_file": tr_input.relative_path.as_posix(),
                "tracking_kind": tr_input.input_kind,
                "key_actions_source": str(key_actions_p),
                "player_track_source": str(identity.player_tracks_csv) if identity.player_tracks_csv else "",
                "player_tracks_resolved": getattr(identity, "player_tracks_resolved", False),
                "template_source": str(template_p),
                "output_directory": "",
                "preflight_status": "FAILED",
                "preflight_failure_type": identity.failure_type or "preflight_error",
                "execution_state": "PREFLIGHT_FAILED",
                "status": "FAILED",
                "warning_count": 0,
                "error_count": 1,
                "unknown_track_count": 0,
                "missing_box_warning_count": 0,
                "ball_track_count": 0,
                "has_unknown_tracks": False,
                "has_missing_box_warnings": False,
                "has_no_ball_track": True,
                "num_tracks": None,
                "num_player_tracks": None,
                "num_ball_tracks": None,
                "num_action_segments": None,
                "elapsed_seconds": 0.0,
                "failure_type": identity.failure_type or "preflight_error",
                "message": identity.message or f"Preflight status: {identity.status}",
                "traceback_file": None
            })

    # Initial checkpoint write
    write_batch_manifest_csv(manifest_csv_path, results)
    write_batch_manifest_json(manifest_json_path, results, str(batch_root.resolve()), cli_arguments)

    print(f"Discovered {total_discovered} tracking inputs ({total_preflight_ready} preflight ready, {total_preflight_failed} preflight failed).")
    print(f"Processing {len(selected_jobs)} selected jobs...")

    # 7. Sequential Orchestration Loop
    for idx, job in enumerate(selected_jobs, start=1):
        job_start = time.time()
        job_out_dir = job.output_dir

        # Check collision
        if job.clip_key in collided_keys:
            res = {
                "discovery_index": job.tracking_input.discovery_index,
                "play_name": job.play_type,
                "video_id": job.video_id,
                "clip_name": job.clip_key,
                "tracking_file": job.tracking_input.relative_path.as_posix(),
                "tracking_kind": job.tracking_input.input_kind,
                "key_actions_source": str(job.key_actions_csv),
                "player_track_source": str(job.player_tracks_csv) if job.player_tracks_csv else "",
                "player_tracks_resolved": job.player_tracks_resolved,
                "template_source": str(job.template_path),
                "output_directory": str(job_out_dir),
                "preflight_status": "FAILED",
                "preflight_failure_type": "duplicate_clip_identity",
                "execution_state": "PREFLIGHT_FAILED",
                "status": "FAILED",
                "warning_count": 0,
                "error_count": 1,
                "unknown_track_count": 0,
                "missing_box_warning_count": 0,
                "ball_track_count": 0,
                "has_unknown_tracks": False,
                "has_missing_box_warnings": False,
                "has_no_ball_track": True,
                "num_tracks": None,
                "num_player_tracks": None,
                "num_ball_tracks": None,
                "num_action_segments": None,
                "elapsed_seconds": round(time.time() - job_start, 3),
                "failure_type": "duplicate_clip_identity",
                "message": f"Multiple tracking inputs resolved to the same clip key '{job.clip_key}'",
                "traceback_file": None
            }
            results.append(res)
            write_batch_manifest_csv(manifest_csv_path, results)
            write_batch_manifest_json(manifest_json_path, results, str(batch_root.resolve()), cli_arguments)
            print(f"[{idx}/{len(selected_jobs)}] {job.play_type}/{job.clip_key} .... FAILED (duplicate_clip_identity)")
            continue

        # Check existing completion state for resume
        is_complete, is_partial, report_data = check_clip_completion(job_out_dir, config)

        if is_complete and (skip_existing or not overwrite):
            warn_cnt = len(report_data.get("warnings", [])) if report_data else 0
            err_cnt = len(report_data.get("errors", [])) if report_data else 0
            metrics = report_data.get("metrics", {}) if report_data else {}
            
            # Map semantic status
            if err_cnt > 0:
                sem_stat = "FAILED"
            elif warn_cnt > 0:
                sem_stat = "WARNING"
            else:
                sem_stat = "PASS"

            # Apply status filter if set
            if status_filter and sem_stat != status_filter:
                continue

            q_signals = extract_quality_signals(report_data)

            res = {
                "discovery_index": job.tracking_input.discovery_index,
                "play_name": job.play_type,
                "video_id": job.video_id,
                "clip_name": job.clip_key,
                "tracking_file": job.tracking_input.relative_path.as_posix(),
                "tracking_kind": job.tracking_input.input_kind,
                "key_actions_source": str(job.key_actions_csv),
                "player_track_source": str(job.player_tracks_csv) if job.player_tracks_csv else "",
                "player_tracks_resolved": job.player_tracks_resolved,
                "template_source": str(job.template_path),
                "output_directory": str(job_out_dir),
                "preflight_status": "READY",
                "preflight_failure_type": None,
                "execution_state": "SKIPPED",
                "status": sem_stat,
                "warning_count": warn_cnt,
                "error_count": err_cnt,
                "unknown_track_count": q_signals["unknown_track_count"],
                "missing_box_warning_count": q_signals["missing_box_warning_count"],
                "ball_track_count": q_signals["ball_track_count"],
                "has_unknown_tracks": q_signals["has_unknown_tracks"],
                "has_missing_box_warnings": q_signals["has_missing_box_warnings"],
                "has_no_ball_track": q_signals["has_no_ball_track"],
                "num_tracks": metrics.get("num_tracks"),
                "num_player_tracks": metrics.get("num_player_tracks"),
                "num_ball_tracks": metrics.get("num_ball_tracks"),
                "num_action_segments": metrics.get("num_action_segments"),
                "elapsed_seconds": round(time.time() - job_start, 3),
                "failure_type": None,
                "message": "Complete existing output",
                "traceback_file": None
            }
            results.append(res)
            write_batch_manifest_csv(manifest_csv_path, results)
            write_batch_manifest_json(manifest_json_path, results, str(batch_root.resolve()), cli_arguments)
            print(f"[{idx}/{len(selected_jobs)}] {job.play_type}/{job.clip_key} .... SKIPPED ({sem_stat})")
            continue

        if is_partial and not overwrite and skip_existing:
            res = {
                "discovery_index": job.tracking_input.discovery_index,
                "play_name": job.play_type,
                "video_id": job.video_id,
                "clip_name": job.clip_key,
                "tracking_file": job.tracking_input.relative_path.as_posix(),
                "tracking_kind": job.tracking_input.input_kind,
                "key_actions_source": str(job.key_actions_csv),
                "player_track_source": str(job.player_tracks_csv) if job.player_tracks_csv else "",
                "player_tracks_resolved": job.player_tracks_resolved,
                "template_source": str(job.template_path),
                "output_directory": str(job_out_dir),
                "preflight_status": "READY",
                "preflight_failure_type": None,
                "execution_state": "PREFLIGHT_FAILED",
                "status": "FAILED",
                "warning_count": 0,
                "error_count": 1,
                "unknown_track_count": 0,
                "missing_box_warning_count": 0,
                "ball_track_count": 0,
                "has_unknown_tracks": False,
                "has_missing_box_warnings": False,
                "has_no_ball_track": True,
                "num_tracks": None,
                "num_player_tracks": None,
                "num_ball_tracks": None,
                "num_action_segments": None,
                "elapsed_seconds": round(time.time() - job_start, 3),
                "failure_type": "partial_existing_output",
                "message": "Partial output requires --overwrite",
                "traceback_file": None
            }
            results.append(res)
            write_batch_manifest_csv(manifest_csv_path, results)
            write_batch_manifest_json(manifest_json_path, results, str(batch_root.resolve()), cli_arguments)
            print(f"[{idx}/{len(selected_jobs)}] {job.play_type}/{job.clip_key} .... FAILED (partial_existing_output)")
            continue

        # Clean prior output if overwrite
        if overwrite:
            clean_clip_outputs(job_out_dir)

        # Execute single-clip worker path
        job_out_dir.mkdir(parents=True, exist_ok=True)
        tb_file_path = None

        try:
            (
                tracks,
                metadata,
                events,
                segments,
                dense_annotations,
                metrics,
                warnings,
                errors
            ) = run_generate_and_enrich_pipeline(
                gt_path=str(job.tracking_input.source_path),
                labels_path=str(job.labels_path) if job.labels_path else None,
                template_path=str(job.template_path),
                key_actions_csv=str(job.key_actions_csv),
                player_tracks_csv=str(job.player_tracks_csv) if job.player_tracks_csv else None,
                config=config,
                output_dir=str(job_out_dir),
                target_video_name=job.video_name,
                target_video_id=job.video_id
            )

            generated_base_xml = os.path.join(job_out_dir, "generated_base_cvat.xml")

            write_single_clip_outputs(
                output_dir=str(job_out_dir),
                input_xml_for_enrichment=generated_base_xml,
                csv_path=str(job.key_actions_csv),
                tracks=tracks,
                metadata=metadata,
                events=events,
                segments=segments,
                dense_annotations=dense_annotations,
                metrics=metrics,
                warnings=warnings,
                errors=errors,
                config=config,
                target_video_name=job.video_name,
                review_enabled=review_enabled,
                quiet=True
            )

            err_cnt = len(errors)
            warn_cnt = len(warnings)

            # Determine semantic status:
            # PASS (0 errors, 0 warnings), WARNING (0 errors, >0 warnings), FAILED (>0 errors)
            if err_cnt > 0:
                sem_stat = "FAILED"
                fail_type = "enrichment"
                msg = f"Enriched with {err_cnt} validation error(s)"
            elif warn_cnt > 0:
                sem_stat = "WARNING"
                fail_type = None
                msg = f"Processed with {warn_cnt} warning(s)"
            else:
                sem_stat = "PASS"
                fail_type = None
                msg = "Processed successfully"

            # Apply status filter if set
            if status_filter and sem_stat != status_filter:
                continue

            q_signals = extract_quality_signals({"metrics": metrics, "warnings": warnings}, tracks)

            res = {
                "discovery_index": job.tracking_input.discovery_index,
                "play_name": job.play_type,
                "video_id": job.video_id,
                "clip_name": job.clip_key,
                "tracking_file": job.tracking_input.relative_path.as_posix(),
                "tracking_kind": job.tracking_input.input_kind,
                "key_actions_source": str(job.key_actions_csv),
                "player_track_source": str(job.player_tracks_csv) if job.player_tracks_csv else "",
                "player_tracks_resolved": job.player_tracks_resolved,
                "template_source": str(job.template_path),
                "output_directory": str(job_out_dir),
                "preflight_status": "READY",
                "preflight_failure_type": None,
                "execution_state": "PROCESSED",
                "status": sem_stat,
                "warning_count": warn_cnt,
                "error_count": err_cnt,
                "unknown_track_count": q_signals["unknown_track_count"],
                "missing_box_warning_count": q_signals["missing_box_warning_count"],
                "ball_track_count": q_signals["ball_track_count"],
                "has_unknown_tracks": q_signals["has_unknown_tracks"],
                "has_missing_box_warnings": q_signals["has_missing_box_warnings"],
                "has_no_ball_track": q_signals["has_no_ball_track"],
                "num_tracks": metrics.get("num_tracks"),
                "num_player_tracks": metrics.get("num_player_tracks"),
                "num_ball_tracks": metrics.get("num_ball_tracks"),
                "num_action_segments": metrics.get("num_action_segments"),
                "elapsed_seconds": round(time.time() - job_start, 3),
                "failure_type": fail_type,
                "message": msg,
                "traceback_file": None
            }

        except Exception as e:
            failures_dir.mkdir(parents=True, exist_ok=True)
            tb_file = failures_dir / f"{job.clip_key}.traceback.txt"
            with open(tb_file, "w", encoding="utf-8") as f:
                f.write(f"Clip Key: {job.clip_key}\n")
                f.write(f"Play Name: {job.play_type}\n")
                f.write(f"Tracking File: {job.tracking_input.source_path}\n")
                f.write(f"Exception Type: {type(e).__name__}\n")
                f.write(f"Exception Message: {e}\n\n")
                f.write(traceback.format_exc())

            tb_file_path = str(tb_file)

            if status_filter and status_filter != "FAILED":
                continue

            res = {
                "discovery_index": job.tracking_input.discovery_index,
                "play_name": job.play_type,
                "video_id": job.video_id,
                "clip_name": job.clip_key,
                "tracking_file": job.tracking_input.relative_path.as_posix(),
                "tracking_kind": job.tracking_input.input_kind,
                "key_actions_source": str(job.key_actions_csv),
                "player_track_source": str(job.player_tracks_csv) if job.player_tracks_csv else "",
                "player_tracks_resolved": job.player_tracks_resolved,
                "template_source": str(job.template_path),
                "output_directory": str(job_out_dir),
                "preflight_status": "READY",
                "preflight_failure_type": None,
                "execution_state": "PROCESSED",
                "status": "FAILED",
                "warning_count": 0,
                "error_count": 1,
                "unknown_track_count": 0,
                "missing_box_warning_count": 0,
                "ball_track_count": 0,
                "has_unknown_tracks": False,
                "has_missing_box_warnings": False,
                "has_no_ball_track": True,
                "num_tracks": None,
                "num_player_tracks": None,
                "num_ball_tracks": None,
                "num_action_segments": None,
                "elapsed_seconds": round(time.time() - job_start, 3),
                "failure_type": "unexpected_exception",
                "message": f"Exception: {type(e).__name__}: {e}",
                "traceback_file": tb_file_path
            }

        results.append(res)
        write_batch_manifest_csv(manifest_csv_path, results)
        write_batch_manifest_json(manifest_json_path, results, str(batch_root.resolve()), cli_arguments)

        st_label = res["status"]
        if st_label == "WARNING":
            st_label += f" ({res['warning_count']} warnings)"
        elif st_label == "FAILED":
            st_label += f" ({res.get('failure_type') or 'error'})"

        print(f"[{idx}/{len(selected_jobs)}] {job.play_type}/{job.clip_key} .... {st_label}")

    total_elapsed = round(time.time() - batch_start_time, 3)

    # 8. Compute Play Statistics & Write Summary Reports
    play_stats: Dict[str, Dict[str, Any]] = {}
    for r in results:
        pt = r.get("play_name") or "Unknown"
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

    totals_data = {
        "total_discovered": total_discovered,
        "total_preflight_ready": total_preflight_ready,
        "total_preflight_failed": total_preflight_failed,
        "total_selected": total_selected,
        "total_attempted": sum(1 for r in results if r.get("execution_state") == "PROCESSED"),
        "pass_count": sum(1 for r in results if r.get("status") == "PASS"),
        "warning_count": sum(1 for r in results if r.get("status") == "WARNING"),
        "failed_count": sum(1 for r in results if r.get("status") == "FAILED"),
        "skipped_count": sum(1 for r in results if r.get("execution_state") == "SKIPPED"),
        "total_elapsed_seconds": total_elapsed
    }

    write_batch_summary_csv(summary_csv_path, play_stats)
    write_batch_summary_json(summary_json_path, results, str(batch_root.resolve()), totals_data, play_stats)
    write_batch_summary_markdown(
        summary_md_path=summary_md_path,
        results=results,
        total_discovered=total_discovered,
        total_preflight_ready=total_preflight_ready,
        total_preflight_failed=total_preflight_failed,
        total_selected=total_selected,
        total_elapsed_seconds=total_elapsed
    )

    pass_cnt = totals_data["pass_count"]
    warning_cnt = totals_data["warning_count"]
    fail_cnt = totals_data["failed_count"]
    skip_cnt = totals_data["skipped_count"]

    print("\n" + "=" * 40)
    print("BATCH PROCESSING COMPLETE")
    print("=" * 40)
    print(f"Manifest CSV: {manifest_csv_path}")
    print(f"Manifest JSON: {manifest_json_path}")
    print(f"Summary CSV: {summary_csv_path}")
    print(f"Summary JSON: {summary_json_path}")
    print(f"Summary Markdown: {summary_md_path}")
    print(f"PASS: {pass_cnt}")
    print(f"WARNING: {warning_cnt}")
    print(f"FAILED: {fail_cnt}")
    print(f"SKIPPED: {skip_cnt}")
    print(f"Total Time: {total_elapsed:.3f}s")
    print("=" * 40)

    return {
        "manifest_csv": manifest_csv_path,
        "manifest_json": manifest_json_path,
        "summary_csv": summary_csv_path,
        "summary_json": summary_json_path,
        "summary_md": summary_md_path,
        "total_discovered": total_discovered,
        "total_preflight_ready": total_preflight_ready,
        "total_selected": total_selected,
        "results": results
    }
