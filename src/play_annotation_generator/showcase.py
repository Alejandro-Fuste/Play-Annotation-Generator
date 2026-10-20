import argparse
import csv
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from .config import DEFAULT_CONFIG, load_config
from .models import ActionEvent, ActionSegment, DenseActionAnnotation, Track
from .output_pipeline import write_single_clip_outputs
from .pipeline_generate_and_enrich import run_generate_and_enrich_pipeline
from .player_track_sheet_parser import parse_player_track_csv
from .wide_action_csv_parser import normalize_column_name, parse_cell_entries, parse_wide_action_csv


@dataclass
class ClipReadinessResult:
    logical_clip_name: str
    play_name: str
    video_id: str
    tracking_source: str
    tracking_resolved: bool
    key_actions_source: str
    key_actions_resolved: bool
    key_actions_row_resolved: bool
    player_tracks_source: str
    player_tracks_resolved: bool
    player_tracks_row_resolved: bool
    play_in_plays_json: bool
    unmapped_columns: List[Tuple[str, str]] = field(default_factory=list)
    missing_action_defs: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    status: str = "READY_CLEAN"  # READY_CLEAN, READY_WITH_REVIEW_WARNINGS, BLOCKED


@dataclass
class ShowcaseReadinessSummary:
    clips_requested: int = 0
    tracking_resolved: int = 0
    key_actions_rows_resolved: int = 0
    player_tracks_rows_resolved: int = 0
    unmapped_action_columns_count: int = 0
    ready_clean_count: int = 0
    ready_with_warnings_count: int = 0
    blocked_count: int = 0
    results: List[ClipReadinessResult] = field(default_factory=list)

    def print_summary(self):
        print("========================================")
        print("SHOWCASE READINESS AUDIT SUMMARY")
        print("========================================")
        print(f"Showcase clips requested: {self.clips_requested}")
        print(f"Tracking sources resolved: {self.tracking_resolved}")
        print(f"Key Actions rows resolved: {self.key_actions_rows_resolved}")
        print(f"PlayerTrack rows resolved: {self.player_tracks_rows_resolved}")
        print(f"Unmapped populated action columns: {self.unmapped_action_columns_count}")
        print(f"READY_CLEAN: {self.ready_clean_count}")
        print(f"READY_WITH_REVIEW_WARNINGS: {self.ready_with_warnings_count}")
        print(f"BLOCKED: {self.blocked_count}")
        print("========================================")

        blocked_clips = [r for r in self.results if r.status == "BLOCKED"]
        if blocked_clips:
            print("\nBLOCKED CLIPS:")
            for b in blocked_clips:
                print(f"  - {b.logical_clip_name}: {', '.join(b.errors)}")

        warning_clips = [r for r in self.results if r.status == "READY_WITH_REVIEW_WARNINGS"]
        if warning_clips:
            print(f"\nREADY_WITH_REVIEW_WARNINGS CLIPS ({len(warning_clips)}):")
            for w in warning_clips:
                print(f"  - {w.logical_clip_name}: {'; '.join(w.warnings[:3])}")


def audit_showcase_readiness(
    manifest_path: str = "data/showcase/showcase_clips.json",
    actions_json_path: str = "data/actions.json",
    plays_json_path: str = "data/plays.json",
    config: Optional[Dict[str, Any]] = None
) -> ShowcaseReadinessSummary:
    """
    Read-only audit of all showcase clips in the manifest.
    Does NOT generate per-clip annotation outputs.
    """
    if config is None:
        config = load_config()

    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Showcase manifest not found: {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # Load canonical actions
    with open(actions_json_path, "r", encoding="utf-8") as f:
        actions_data = json.load(f)
    canonical_actions: Set[str] = set(actions_data.get("formattedActionLabels", []))

    # Load canonical plays
    with open(plays_json_path, "r", encoding="utf-8") as f:
        plays_data = json.load(f)
    canonical_plays: Set[str] = set(plays_data.get("playLabels", []))
    canonical_plays.update(plays_data.get("formattedPlayLabels", []))
    defs = plays_data.get("defintions") or plays_data.get("definitions") or {}
    canonical_plays.update(defs.keys())

    action_cols_map = config.get("csv", {}).get("action_columns", {})
    norm_action_cols = {normalize_column_name(k): v for k, v in action_cols_map.items()}

    non_action_norm = {
        "videoname", "videoid", "video", "originalid", "coverage", "ol",
        "result", "notes", "playtag", "resulttag", "resultframe", "play", "endofplay", "endplay"
    }

    summary = ShowcaseReadinessSummary(clips_requested=len(manifest))

    for item in manifest:
        clip_name = item["logical_clip_name"]
        play_name = item["play_name"]
        vid_id = str(item["video_id"]).strip()
        tracking_src = item["tracking_source"]
        ka_src = item["key_actions_source"]
        pt_src = item["player_tracks_source"]

        res = ClipReadinessResult(
            logical_clip_name=clip_name,
            play_name=play_name,
            video_id=vid_id,
            tracking_source=tracking_src,
            tracking_resolved=os.path.exists(tracking_src),
            key_actions_source=ka_src,
            key_actions_resolved=os.path.exists(ka_src),
            key_actions_row_resolved=False,
            player_tracks_source=pt_src,
            player_tracks_resolved=os.path.exists(pt_src),
            player_tracks_row_resolved=False,
            play_in_plays_json=(play_name in canonical_plays)
        )

        if res.tracking_resolved:
            summary.tracking_resolved += 1
        else:
            res.errors.append(f"Tracking source not found: {tracking_src}")

        if not res.play_in_plays_json:
            res.errors.append(f"Play '{play_name}' not defined in plays.json")

        # Check Key Actions file & matching row
        row_dict: Optional[Dict[str, str]] = None
        if res.key_actions_resolved:
            with open(ka_src, "r", encoding="utf-8") as f:
                lines = f.readlines()
            header_idx = -1
            for i, line in enumerate(lines):
                parts = [p.strip().strip('"').strip("'") for p in line.split(",")]
                if parts and parts[0] in ["Video #", "video_name", "video_id", "video #", "Video#"]:
                    header_idx = i
                    break
            if header_idx >= 0:
                reader = csv.DictReader(lines[header_idx:])
                reader.fieldnames = [name.strip().strip('"').strip("'") for name in reader.fieldnames if name]
                for r in reader:
                    r_id = r.get("Video #", r.get("Video ID", r.get("video_id", "")))
                    if r_id and str(r_id).strip() == vid_id:
                        row_dict = {k: (v.strip() if v else "") for k, v in r.items() if k}
                        res.key_actions_row_resolved = True
                        summary.key_actions_rows_resolved += 1
                        break
            if not res.key_actions_row_resolved:
                res.errors.append(f"Row for video_id {vid_id} not found in {ka_src}")
        else:
            res.errors.append(f"Key Actions file not found: {ka_src}")

        # Check PlayerTrack file & matching row
        if res.player_tracks_resolved:
            with open(pt_src, "r", encoding="utf-8") as f:
                pt_lines = f.readlines()
            for line in pt_lines:
                parts = line.split(",")
                if parts and parts[0].strip().strip('"').strip("'") == vid_id:
                    res.player_tracks_row_resolved = True
                    summary.player_tracks_rows_resolved += 1
                    if "[?]" in line or "?" in line:
                        res.warnings.append("PlayerTrack has unassigned/unknown positions ([?])")
                    break
            if not res.player_tracks_row_resolved:
                res.errors.append(f"Row for video_id {vid_id} not found in {pt_src}")
        else:
            res.errors.append(f"PlayerTrack file not found: {pt_src}")

        # Verify populated action columns in Key Actions row
        if row_dict:
            for col_name, cell_val in row_dict.items():
                if not col_name or not cell_val:
                    continue
                if cell_val in ["-", "--", "N/A", "n/a", "none", "None"]:
                    continue
                norm_c = normalize_column_name(col_name)
                if norm_c in non_action_norm:
                    continue

                if norm_c not in norm_action_cols:
                    res.unmapped_columns.append((col_name, cell_val))
                    summary.unmapped_action_columns_count += 1
                    res.errors.append(
                        f"UNMAPPED_ACTION_COLUMN: play={play_name} video_id={vid_id} column={col_name} value={cell_val}"
                    )
                else:
                    action_label = norm_action_cols[norm_c]
                    if action_label != "Action_None" and action_label != "Action_PlayEnd":
                        if action_label not in canonical_actions:
                            res.missing_action_defs.append(action_label)
                            res.errors.append(
                                f"Mapped action '{action_label}' for column '{col_name}' does not exist in actions.json"
                            )

                    # Check semantic alias audit classification
                    from .semantic_audit import get_alias_audit_map
                    alias_audit = get_alias_audit_map()
                    if norm_c in alias_audit:
                        audit_entry = alias_audit[norm_c]
                        if audit_entry["classification"] == "NEEDS_SOURCE_REVIEW":
                            res.errors.append(
                                f"Action column '{col_name}' is classified as NEEDS_SOURCE_REVIEW: {audit_entry['reason']}"
                            )

                    # Check cell entries parsing
                    entries = parse_cell_entries(cell_val)
                    valid_entries = [e for e in entries if e[0] is not None]
                    for e in entries:
                        frame, actor, err = e
                        if err:
                            res.errors.append(f"Malformed action cell in column '{col_name}' value '{cell_val}': {err}")
                    if not valid_entries:
                        res.errors.append(f"Action cell in column '{col_name}' value '{cell_val}' produced 0 valid events")

        # Classify status
        if res.errors:
            res.status = "BLOCKED"
            summary.blocked_count += 1
        elif res.warnings:
            res.status = "READY_WITH_REVIEW_WARNINGS"
            summary.ready_with_warnings_count += 1
        else:
            res.status = "READY_CLEAN"
            summary.ready_clean_count += 1

        summary.results.append(res)

    return summary


def generate_showcase(
    manifest_path: str = "data/showcase/showcase_clips.json",
    output_dir: str = "output_showcase",
    subset_clips: Optional[List[str]] = None,
    review: bool = True,
    template_path: str = "docs/JetSweepTemplate.xml",
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Executes showcase generation for manifest clips (or an explicit subset).
    """
    if config is None:
        config = load_config()

    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Showcase manifest not found: {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    if subset_clips:
        subset_set = {c.strip() for c in subset_clips if c.strip()}
        manifest = [item for item in manifest if item["logical_clip_name"] in subset_set]

    os.makedirs(output_dir, exist_ok=True)

    summary_records = []
    print(f"Generating {len(manifest)} showcase clips to '{output_dir}'...")

    for idx, item in enumerate(manifest, 1):
        clip_name = item["logical_clip_name"]
        play_name = item["play_name"]
        vid_id = str(item["video_id"]).strip()
        tracking_src = item["tracking_source"]
        ka_src = item["key_actions_source"]
        pt_src = item["player_tracks_source"]

        clip_out_dir = os.path.join(output_dir, play_name, clip_name)
        os.makedirs(clip_out_dir, exist_ok=True)

        print(f"[{idx}/{len(manifest)}] Generating {clip_name}...")

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
                gt_path=tracking_src,
                labels_path=None,
                template_path=template_path,
                key_actions_csv=ka_src,
                player_tracks_csv=pt_src if os.path.exists(pt_src) else None,
                config=config,
                output_dir=clip_out_dir,
                target_video_name=clip_name,
                target_video_id=vid_id
            )

            input_xml_for_enrichment = os.path.join(clip_out_dir, "generated_base_cvat.xml")

            write_single_clip_outputs(
                output_dir=clip_out_dir,
                input_xml_for_enrichment=input_xml_for_enrichment,
                csv_path=ka_src,
                tracks=tracks,
                metadata=metadata,
                events=events,
                segments=segments,
                dense_annotations=dense_annotations,
                metrics=metrics,
                warnings=warnings,
                errors=errors,
                config=config,
                target_video_name=clip_name,
                review_enabled=review,
                quiet=True
            )

            status = "FAILED" if errors else ("WARNING" if warnings else "PASS")
            print(f"  -> {status} (Errors: {len(errors)}, Warnings: {len(warnings)})")

            summary_records.append({
                "clip_name": clip_name,
                "play_name": play_name,
                "video_id": vid_id,
                "status": status,
                "errors_count": len(errors),
                "warnings_count": len(warnings),
                "tracks_count": metrics.get("num_tracks", 0),
                "segments_count": len(segments),
                "dense_count": len(dense_annotations),
                "errors": errors,
                "warnings": warnings[:5]
            })

        except Exception as e:
            print(f"  -> ERROR: {e}")
            summary_records.append({
                "clip_name": clip_name,
                "play_name": play_name,
                "video_id": vid_id,
                "status": "EXCEPTION",
                "errors_count": 1,
                "warnings_count": 0,
                "errors": [str(e)]
            })

    # Write aggregate summary
    summary_path_json = os.path.join(output_dir, "showcase_summary.json")
    with open(summary_path_json, "w", encoding="utf-8") as f:
        json.dump(summary_records, f, indent=2)

    summary_path_md = os.path.join(output_dir, "showcase_summary.md")
    with open(summary_path_md, "w", encoding="utf-8") as f:
        f.write("# Showcase Dataset Generation Summary\n\n")
        f.write(f"- **Clips Generated:** {len(summary_records)}\n")
        pass_count = sum(1 for r in summary_records if r["status"] == "PASS")
        warn_count = sum(1 for r in summary_records if r["status"] == "WARNING")
        fail_count = sum(1 for r in summary_records if r["status"] in ("FAILED", "EXCEPTION"))
        f.write(f"- **PASS:** {pass_count}\n")
        f.write(f"- **WARNING:** {warn_count}\n")
        f.write(f"- **FAILED:** {fail_count}\n\n")

        f.write("| Clip | Play | Status | Segments | Dense Frames | Errors | Warnings |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for r in summary_records:
            f.write(f"| {r['clip_name']} | {r['play_name']} | {r['status']} | {r.get('segments_count', 0)} | {r.get('dense_count', 0)} | {r['errors_count']} | {r['warnings_count']} |\n")

    print(f"\nShowcase generation complete. Summary written to {summary_path_md}")
    return {"records": summary_records, "summary_md": summary_path_md, "summary_json": summary_path_json}


def main():
    parser = argparse.ArgumentParser(description="Showcase Dataset Sample Readiness & Generation")
    parser.add_argument("--manifest", default="data/showcase/showcase_clips.json", help="Path to showcase clips manifest JSON")
    parser.add_argument("--output", default="output_showcase", help="Output directory for showcase artifacts")
    parser.add_argument("--template", default="docs/JetSweepTemplate.xml", help="Path to CVAT XML template")
    parser.add_argument("--actions-json", default="data/actions.json", help="Path to actions taxonomy JSON")
    parser.add_argument("--plays-json", default="data/plays.json", help="Path to plays taxonomy JSON")
    parser.add_argument("--review", action="store_true", default=True, help="Generate review report markdown artifacts")
    parser.add_argument("--audit", action="store_true", help="Run read-only showcase readiness audit without generating artifacts")
    parser.add_argument("--clips", default=None, help="Comma-separated subset of clips to run (e.g. smoke test subset)")

    args = parser.parse_args()

    if args.audit:
        res = audit_showcase_readiness(
            manifest_path=args.manifest,
            actions_json_path=args.actions_json,
            plays_json_path=args.plays_json
        )
        res.print_summary()
        if res.blocked_count > 0:
            sys.exit(1)
        sys.exit(0)

    subset = [c.strip() for c in args.clips.split(",")] if args.clips else None
    generate_showcase(
        manifest_path=args.manifest,
        output_dir=args.output,
        subset_clips=subset,
        review=args.review,
        template_path=args.template
    )


if __name__ == "__main__":
    main()
