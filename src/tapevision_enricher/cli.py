import argparse
import os
import sys
from .config import load_config
from .output_pipeline import write_single_clip_outputs

def parse_args():
    parser = argparse.ArgumentParser(
        description="Enrich CVAT XML files with action labels from wide-format CSVs using configurable rules."
    )
    
    # Backward compatible top-level arguments
    parser.add_argument(
        "--xml",
        default=None,
        help="Backward compatible path to input CVAT XML export file."
    )
    parser.add_argument(
        "--csv",
        default=None,
        help="Backward compatible path to wide-format action CSV file."
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Backward compatible path to optional YAML configuration file."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Backward compatible path to output directory. Defaults to outputs/<video_name>."
    )
    parser.add_argument(
        "--video-name",
        default=None,
        help="Backward compatible target video_name or video_id to filter CSV rows."
    )
    parser.add_argument(
        "--review",
        action="store_true",
        help="Automatically run and print interactive review report after completion."
    )
    
    # Metadata overrides (top-level)
    parser.add_argument("--dataset-summary", default=None, help="Path to Dataset Summary CSV")
    parser.add_argument("--actions-json", default=None, help="Path to actions11.json taxonomy file")
    parser.add_argument("--plays-json", default=None, help="Path to plays.json taxonomy file")
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")
    
    # generate-and-enrich subcommand
    gen_parser = subparsers.add_parser(
        "generate-and-enrich",
        help="Generate base CVAT XML directly from MOT tracks and sheets, and enrich it."
    )
    gen_parser.add_argument("--gt", required=True, help="Path to MOT gt.txt file or MOT zip file (e.g. data/tracking/JetSweep/JetSweep_1_cvat_mot.zip)")
    gen_parser.add_argument("--labels", default=None, help="Path to MOT labels.txt")
    gen_parser.add_argument("--template", required=True, help="Path to CVAT XML template file")
    gen_parser.add_argument("--key-actions", required=True, help="Path to wide Key Actions CSV")
    gen_parser.add_argument("--player-tracks", required=True, help="Path to Player Track ID CSV")
    gen_parser.add_argument("--config", default=None, help="Path to optional YAML configuration file")
    gen_parser.add_argument("--output", default=None, help="Path to output directory")
    gen_parser.add_argument("--video-name", default=None, help="Target video name filter")
    gen_parser.add_argument("--video-id", default=None, help="Target video ID filter")
    gen_parser.add_argument("--dataset-summary", default=None, help="Path to Dataset Summary CSV")
    gen_parser.add_argument("--actions-json", default=None, help="Path to actions11.json taxonomy file")
    gen_parser.add_argument("--plays-json", default=None, help="Path to plays.json taxonomy file")
    gen_parser.add_argument("--review", action="store_true", help="Automatically run review report after completion")
    
    # enrich-existing subcommand
    enrich_parser = subparsers.add_parser(
        "enrich-existing",
        help="Enrich an existing CVAT XML file with action labels."
    )
    enrich_parser.add_argument("--xml", required=True, help="Path to input CVAT XML export file")
    enrich_parser.add_argument("--csv", required=True, help="Path to wide-format action CSV file")
    enrich_parser.add_argument("--config", default=None, help="Path to optional YAML configuration file")
    enrich_parser.add_argument("--output", default=None, help="Path to output directory")
    enrich_parser.add_argument("--video-name", default=None, help="Target video name or video ID filter")
    enrich_parser.add_argument("--dataset-summary", default=None, help="Path to Dataset Summary CSV")
    enrich_parser.add_argument("--actions-json", default=None, help="Path to actions11.json taxonomy file")
    enrich_parser.add_argument("--plays-json", default=None, help="Path to plays.json taxonomy file")
    enrich_parser.add_argument("--review", action="store_true", help="Automatically run review report after completion")
    
    # review subcommand
    review_parser = subparsers.add_parser(
        "review",
        help="Interactively review generated play outputs (Options 1, 2, and 4)."
    )
    review_parser.add_argument("--dir", "--output", dest="dir", required=True, help="Path to output directory (e.g. outputs/JetSweep_1)")
    
    # batch-generate-and-enrich subcommand
    batch_parser = subparsers.add_parser(
        "batch-generate-and-enrich",
        help="Batch process multiple MOT tracking files sequentially."
    )
    batch_parser.add_argument("--gt-dir", "--tracking-root", dest="gt_dir", required=True, help="Directory containing MOT zips or gt.txt files")
    batch_parser.add_argument("--template", required=True, help="Path to CVAT XML template file")
    batch_parser.add_argument("--key-actions", required=True, help="Path to wide Key Actions CSV or directory")
    batch_parser.add_argument("--player-tracks", required=True, help="Path to Player Track ID CSV or directory")
    batch_parser.add_argument("--config", default=None, help="Path to optional YAML configuration file")
    batch_parser.add_argument("--output", default=None, help="Path to batch output directory")
    batch_parser.add_argument("--labels", default=None, help="Path to optional shared MOT labels.txt")
    batch_parser.add_argument("--limit", type=int, default=None, help="Limit number of matched jobs to process")
    batch_parser.add_argument("--play", default=None, help="Filter resolved clips by play type name/prefix")
    batch_parser.add_argument("--video-id", default=None, help="Filter resolved clips by video ID")
    batch_parser.add_argument("--status", default=None, help="Filter resolved clips by status (PASS, WARNING, FAILED)")
    batch_parser.add_argument("--dataset-summary", default=None, help="Path to Dataset Summary CSV")
    batch_parser.add_argument("--actions-json", default=None, help="Path to actions.json taxonomy file")
    batch_parser.add_argument("--plays-json", default=None, help="Path to plays.json taxonomy file")
    batch_parser.add_argument("--resume", "--skip-existing", dest="resume", action="store_true", help="Resume batch run by skipping complete existing outputs")
    batch_parser.add_argument("--overwrite", action="store_true", help="Overwrite existing clip output files")
    batch_parser.add_argument("--review", action="store_true", help="Generate review report for each clip")
    batch_parser.add_argument("--verbose", action="store_true", help="Print detailed diagnostic output")

    args = parser.parse_args()
    if hasattr(args, "resume"):
        args.skip_existing = args.resume
    return args

def main():
    args = parse_args()

    if args.command == "batch-generate-and-enrich":
        from .batch_pipeline import run_batch_pipeline
        try:
            run_batch_pipeline(
                gt_dir=args.gt_dir,
                template_path=args.template,
                key_actions_csv=args.key_actions,
                player_tracks_csv=args.player_tracks,
                config_path=args.config,
                output_dir=args.output,
                labels_path=args.labels,
                dataset_summary_path=args.dataset_summary,
                actions_json_path=args.actions_json,
                plays_json_path=args.plays_json,
                limit=args.limit,
                play_filter=args.play,
                video_id_filter=args.video_id,
                status_filter=args.status,
                skip_existing=args.resume,
                overwrite=args.overwrite,
                review_enabled=args.review,
                verbose=args.verbose
            )
            sys.exit(0)
        except Exception as e:
            print(f"Batch execution failed: {e}", file=sys.stderr)
            sys.exit(1)

    if args.command == "review":
        from .reviewer import review_play_outputs
        out_dir = args.dir
        report = review_play_outputs(out_dir)
        print(report)
        
        # Also save copy to review_report.md in the output directory
        if os.path.exists(out_dir):
            report_file = os.path.join(out_dir, "review_report.md")
            with open(report_file, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\n[Saved Review Report -> {report_file}]")
        sys.exit(0)
    
    # Determine mode
    if args.command == "generate-and-enrich":
        mode = "generate_and_enrich_xml"
        config_path = args.config
        output_dir = args.output
        video_name = args.video_name
        video_id = args.video_id
    elif args.command == "enrich-existing":
        mode = "enrich_existing_xml"
        config_path = args.config
        output_dir = args.output
        video_name = args.video_name
        video_id = None
    else:
        # Fallback to backward compatible top-level args
        if args.xml and args.csv:
            mode = "enrich_existing_xml"
            config_path = args.config
            output_dir = args.output
            video_name = args.video_name
            video_id = None
        else:
            print("Error: Please provide a subcommand (generate-and-enrich or enrich-existing) or the backward compatible options (--xml and --csv).", file=sys.stderr)
            sys.exit(1)
            
    # 1. Load config
    config = load_config(config_path)
    config["mode"] = mode
    config.setdefault("input", {})

    if getattr(args, "dataset_summary", None):
        config["input"]["dataset_summary_csv"] = args.dataset_summary
    if getattr(args, "actions_json", None):
        config["input"]["actions_json"] = args.actions_json
    if getattr(args, "plays_json", None):
        config["input"]["plays_json"] = args.plays_json
    
    if mode == "generate_and_enrich_xml":
        # Override paths from CLI
        config.setdefault("input", {})
        config["input"]["gt_txt"] = args.gt
        config["input"]["labels_txt"] = args.labels
        config["input"]["xml_template"] = args.template
        config["input"]["key_actions_csv"] = args.key_actions
        config["input"]["player_track_csv"] = args.player_tracks
        
        gt_path = config["input"]["gt_txt"]
        labels_path = config["input"]["labels_txt"]
        template_path = config["input"]["xml_template"]
        key_actions_csv = config["input"]["key_actions_csv"]
        player_tracks_csv = config["input"]["player_track_csv"]
        
        # Validate existence
        for p_name, p_val in [("gt_txt", gt_path), ("xml_template", template_path), ("key_actions_csv", key_actions_csv), ("player_track_csv", player_tracks_csv)]:
            if not p_val or not os.path.exists(p_val):
                print(f"Error: {p_name} file does not exist: {p_val}", file=sys.stderr)
                sys.exit(1)
        if labels_path and not os.path.exists(labels_path):
            print(f"Error: labels_txt file does not exist: {labels_path}", file=sys.stderr)
            sys.exit(1)
            
        print("Running generate-and-enrich pipeline...")
        print(f"  MOT gt: {gt_path}")
        print(f"  MOT labels: {labels_path}")
        print(f"  XML Template: {template_path}")
        print(f"  Key Actions: {key_actions_csv}")
        print(f"  Player Tracks: {player_tracks_csv}")
        
        v_name = video_name
        if not v_name:
            if output_dir and os.path.basename(output_dir.rstrip("/\\")) not in ["outputs", "output", "."]:
                v_name = os.path.basename(output_dir.rstrip("/\\"))
            elif gt_path:
                base = os.path.basename(gt_path)
                for sfx in ["_cvat_mot.zip", "_mot.zip", ".zip", ".txt"]:
                    if base.endswith(sfx):
                        base = base[:-len(sfx)]
                        break
                v_name = base
            else:
                v_name = "generated_play"

        target_v_name = video_name or v_name
        out_dir = output_dir
        if not out_dir:
            out_dir = os.path.join(config.get("output", {}).get("output_dir", "outputs"), v_name)
            
        os.makedirs(out_dir, exist_ok=True)
        
        from .pipeline_generate_and_enrich import run_generate_and_enrich_pipeline
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
                gt_path=gt_path,
                labels_path=labels_path,
                template_path=template_path,
                key_actions_csv=key_actions_csv,
                player_tracks_csv=player_tracks_csv,
                config=config,
                output_dir=out_dir,
                target_video_name=target_v_name,
                target_video_id=video_id
            )
        except Exception as e:
            print(f"Pipeline execution failed with exception: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)
            
        xml_path = template_path
        csv_path = key_actions_csv
        input_xml_for_enrichment = os.path.join(out_dir, "generated_base_cvat.xml")
        
    else: # mode == "enrich_existing_xml"
        if args.command == "enrich-existing":
            xml_path = args.xml
            csv_path = args.csv
        else:
            xml_path = args.xml
            csv_path = args.csv
            
        config.setdefault("input", {})
        config["input"]["cvat_xml"] = xml_path
        config["input"]["action_csv"] = csv_path
        
        if not os.path.exists(xml_path):
            print(f"Error: XML file does not exist: {xml_path}", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists(csv_path):
            print(f"Error: CSV file does not exist: {csv_path}", file=sys.stderr)
            sys.exit(1)
            
        print("Running enrichment pipeline...")
        print(f"  Source XML: {xml_path}")
        print(f"  Source CSV: {csv_path}")
        
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
            ) = run_enrichment_pipeline(xml_path, csv_path, config, video_name)
        except Exception as e:
            print(f"Pipeline execution failed with exception: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)
            
        v_name = metadata.get("video_name", "enriched_play")
        out_dir = output_dir
        if not out_dir:
            out_dir = os.path.join(config.get("output", {}).get("output_dir", "outputs"), v_name)
            
        input_xml_for_enrichment = xml_path
        
    os.makedirs(out_dir, exist_ok=True)
    
    # Write outputs using shared helper
    write_single_clip_outputs(
        output_dir=out_dir,
        input_xml_for_enrichment=input_xml_for_enrichment,
        csv_path=csv_path,
        tracks=tracks,
        metadata=metadata,
        events=events,
        segments=segments,
        dense_annotations=dense_annotations,
        metrics=metrics,
        warnings=warnings,
        errors=errors,
        config=config,
        target_video_name=video_name,
        review_enabled=getattr(args, "review", False),
        quiet=False
    )
        
    # Print validation console summary
    print("\n" + "="*40)
    print("PIPELINE VALIDATION SUMMARY")
    print("="*40)
    print(f"Status: {'FAILED' if errors else 'SUCCESS'}")
    print(f"XML Tracks: {metrics.get('num_tracks', 0)} ({metrics.get('num_player_tracks', 0)} players, {metrics.get('num_ball_tracks', 0)} balls)")
    if mode == "generate_and_enrich_xml":
        print(f"MOT Rows Parsed: {metrics.get('num_mot_rows_parsed', 0)}")
        print(f"MOT Assignments: {metrics.get('num_assignments', 0)}")
    print(f"CSV Events Parsed: {metrics.get('num_events_parsed', 0)}")
    print(f"Action Segments Inferred: {metrics.get('num_action_segments', 0)}")
    print(f"Dense Frame-Level Annotations: {len(dense_annotations)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Errors: {len(errors)}")
    
    if warnings:
        print("\nWarnings:")
        for w in warnings[:5]:
            print(f"  - {w}")
        if len(warnings) > 5:
            print(f"  ... and {len(warnings) - 5} more warnings.")
            
    if errors:
        print("\nErrors:")
        for e in errors[:5]:
            print(f"  - {e}")
        if len(errors) > 5:
            print(f"  ... and {len(errors) - 5} more errors.")
            
    print("="*40)
    
    # Handle strict validation error exit code
    if errors and config.get("validation", {}).get("strict", False):
        print("Validation failed in strict mode. Exiting with error.", file=sys.stderr)
        sys.exit(1)
        
    print("Done!")

if __name__ == "__main__":
    main()
