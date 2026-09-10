from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


LEGACY_FOLDER = "WR_SlowScreens"
CANONICAL_FOLDER = "WRSlowScreens"
TRACKING_PATTERN = re.compile(r"^WRSlowScreens_(?P<id>\d+)_cvat_mot\.zip$")
SUMMARY_PATTERN = re.compile(r"^WRSlowScreens_(?P<id>\d+)\.mp4$")
LEGACY_KEY_ACTIONS = "WR_SlowScreens.csv"
CANONICAL_KEY_ACTIONS = "WRSlowScreens.csv"


@dataclass(frozen=True)
class ClipPair:
    clip_id: int
    tracking_file: Path
    dataset_summary_row: int
    output_file: str


@dataclass(frozen=True)
class MigrationPlan:
    source_folder: Path
    target_folder: Path
    key_actions_source: Path
    key_actions_target: Path
    pairs: tuple[ClipPair, ...]
    errors: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.errors


def _extract_id(pattern: re.Pattern[str], value: str) -> int | None:
    match = pattern.fullmatch(value)
    return int(match.group("id")) if match else None


def _scan_dataset_summary(path: Path) -> tuple[dict[int, tuple[int, str]], dict[str, list[int]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "output_file" not in reader.fieldnames:
            raise ValueError("DatasetSummary is missing required 'output_file' column")

        by_id: dict[int, tuple[int, str]] = {}
        outputs: dict[str, list[int]] = {}
        for row_number, row in enumerate(reader, start=2):
            output_file = (row.get("output_file") or "").strip()
            if output_file:
                outputs.setdefault(output_file, []).append(row_number)
            clip_id = _extract_id(SUMMARY_PATTERN, output_file)
            if clip_id is None:
                continue
            if clip_id in by_id:
                prev_row, prev_value = by_id[clip_id]
                raise ValueError(
                    f"duplicate WRSlowScreens DatasetSummary ID {clip_id}: "
                    f"rows {prev_row} ({prev_value}) and {row_number} ({output_file})"
                )
            by_id[clip_id] = (row_number, output_file)
    return by_id, outputs


def build_plan(
    tracking_root: Path,
    dataset_summary: Path,
    key_actions_root: Path,
) -> MigrationPlan:
    tracking_root = tracking_root.resolve()
    dataset_summary = dataset_summary.resolve()
    key_actions_root = key_actions_root.resolve()

    source_folder = tracking_root / LEGACY_FOLDER
    target_folder = tracking_root / CANONICAL_FOLDER
    key_actions_source = key_actions_root / LEGACY_KEY_ACTIONS
    key_actions_target = key_actions_root / CANONICAL_KEY_ACTIONS
    errors: list[str] = []

    if not source_folder.is_dir():
        errors.append(f"legacy tracking folder not found: {source_folder}")
    if target_folder.exists():
        errors.append(f"canonical tracking folder already exists: {target_folder}")
    if not dataset_summary.is_file():
        errors.append(f"DatasetSummary does not exist: {dataset_summary}")
    if not key_actions_source.is_file():
        errors.append(f"legacy Key Actions source not found: {key_actions_source}")
    if key_actions_target.exists():
        errors.append(f"canonical Key Actions target already exists: {key_actions_target}")

    if errors:
        return MigrationPlan(
            source_folder,
            target_folder,
            key_actions_source,
            key_actions_target,
            (),
            tuple(errors),
        )

    tracking_by_id: dict[int, Path] = {}
    unexpected_tracking: list[str] = []
    for path in sorted(source_folder.iterdir(), key=lambda p: p.name):
        if not path.is_file():
            unexpected_tracking.append(path.name)
            continue
        clip_id = _extract_id(TRACKING_PATTERN, path.name)
        if clip_id is None:
            unexpected_tracking.append(path.name)
            continue
        if clip_id in tracking_by_id:
            errors.append(
                f"duplicate WRSlowScreens tracking ID {clip_id}: "
                f"{tracking_by_id[clip_id].name}, {path.name}"
            )
            continue
        tracking_by_id[clip_id] = path

    if unexpected_tracking:
        errors.append(
            "legacy tracking folder contains unexpected entries: "
            + ", ".join(unexpected_tracking)
        )
    if not tracking_by_id:
        errors.append("no WRSlowScreens tracking files found in legacy folder")

    try:
        summary_by_id, all_outputs = _scan_dataset_summary(dataset_summary)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        errors.append(str(exc))
        summary_by_id = {}
        all_outputs = {}

    tracking_ids = set(tracking_by_id)
    summary_ids = set(summary_by_id)
    if tracking_ids != summary_ids:
        only_tracking = sorted(tracking_ids - summary_ids)
        only_summary = sorted(summary_ids - tracking_ids)
        if only_tracking:
            errors.append(
                "IDs present in tracking but missing from DatasetSummary "
                f"WRSlowScreens output_file values: {only_tracking}"
            )
        if only_summary:
            errors.append(
                "IDs present in DatasetSummary WRSlowScreens output_file values "
                f"but missing from tracking: {only_summary}"
            )

    for clip_id, (_, output_file) in summary_by_id.items():
        rows = all_outputs.get(output_file, [])
        if len(rows) != 1:
            errors.append(
                f"DatasetSummary output collision for ID {clip_id}: "
                f"{output_file} appears on rows {rows}"
            )

    pairs = tuple(
        ClipPair(
            clip_id,
            tracking_by_id[clip_id],
            summary_by_id[clip_id][0],
            summary_by_id[clip_id][1],
        )
        for clip_id in sorted(tracking_ids & summary_ids)
    )

    return MigrationPlan(
        source_folder,
        target_folder,
        key_actions_source,
        key_actions_target,
        pairs,
        tuple(errors),
    )


def apply_plan(plan: MigrationPlan) -> None:
    if not plan.ready:
        raise RuntimeError("Cannot apply migration plan with validation errors")

    if not plan.source_folder.is_dir():
        raise FileNotFoundError(f"tracking source disappeared: {plan.source_folder}")
    if plan.target_folder.exists():
        raise FileExistsError(f"tracking target appeared: {plan.target_folder}")
    if not plan.key_actions_source.is_file():
        raise FileNotFoundError(
            f"Key Actions source disappeared: {plan.key_actions_source}"
        )
    if plan.key_actions_target.exists():
        raise FileExistsError(
            f"Key Actions target appeared: {plan.key_actions_target}"
        )

    folder_moved = False
    key_actions_moved = False
    try:
        os.replace(plan.source_folder, plan.target_folder)
        folder_moved = True
        os.replace(plan.key_actions_source, plan.key_actions_target)
        key_actions_moved = True
    except Exception:
        rollback_errors: list[str] = []
        if key_actions_moved:
            try:
                os.replace(plan.key_actions_target, plan.key_actions_source)
            except Exception as exc:  # pragma: no cover
                rollback_errors.append(f"Key Actions rollback failed: {exc}")
        if folder_moved:
            try:
                os.replace(plan.target_folder, plan.source_folder)
            except Exception as exc:  # pragma: no cover
                rollback_errors.append(f"tracking folder rollback failed: {exc}")
        if rollback_errors:
            raise RuntimeError(
                "Migration failed and rollback was incomplete: "
                + "; ".join(rollback_errors)
            )
        raise


def print_plan(plan: MigrationPlan) -> None:
    print("WRSlowScreens canonical naming migration")
    print("=" * 40)

    if plan.errors:
        print("\nVALIDATION ERRORS")
        for error in plan.errors:
            print(f"  - {error}")

    print("\nTracking folder rename:")
    print(f"  {plan.source_folder} -> {plan.target_folder}")

    print("\nKey Actions rename:")
    print(f"  {plan.key_actions_source} -> {plan.key_actions_target}")

    print(f"\nDatasetSummary pair verification ({len(plan.pairs)}):")
    for pair in plan.pairs:
        print(
            f"  [WRSlowScreens #{pair.clip_id}, row {pair.dataset_summary_row}] "
            f"{pair.tracking_file.name} <-> {pair.output_file}"
        )

    print(
        f"\nStatus: {'READY' if plan.ready else 'BLOCKED'} | "
        f"paired clips: {len(plan.pairs)}"
    )
    print("DatasetSummary.output_file values are already canonical; no CSV rewrite is planned.")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Plan or apply the WRSlowScreens canonical naming migration. "
            "Dry-run is the default."
        )
    )
    parser.add_argument(
        "--tracking-root",
        type=Path,
        default=Path("data/tracking"),
    )
    parser.add_argument(
        "--dataset-summary",
        type=Path,
        default=Path("data/DatasetSummary.csv"),
    )
    parser.add_argument(
        "--key-actions-root",
        type=Path,
        default=Path("data/key_actions"),
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    plan = build_plan(args.tracking_root, args.dataset_summary, args.key_actions_root)
    print_plan(plan)

    if not plan.ready:
        print("\nNo changes were made.", file=sys.stderr)
        return 2

    if not args.apply:
        print("\nDRY RUN: no changes were made.")
        print("Re-run with --apply only after reviewing every proposed change.")
        return 0

    try:
        apply_plan(plan)
    except Exception as exc:
        print(f"\nAPPLY FAILED: {exc}", file=sys.stderr)
        return 1

    print("\nAPPLY COMPLETE: tracking folder and Key Actions filename were updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
