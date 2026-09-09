from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DAGGER_FOLDER = "Dagger"
TRACKING_PATTERN = re.compile(r"^DaggerConcept_(?P<id>\d+)_cvat_mot\.zip$")
TRACKING_TARGET = "Dagger_{id}_cvat_mot.zip"
SUMMARY_PATTERN = re.compile(r"^DaggerConcept_(?P<id>\d+)\.mp4$")
SUMMARY_TARGET = "Dagger_{id}.mp4"


@dataclass(frozen=True)
class TrackingRename:
    clip_id: int
    source: Path
    target: Path


@dataclass(frozen=True)
class SummaryRename:
    clip_id: int
    row_number: int
    source: str
    target: str


@dataclass(frozen=True)
class MigrationPlan:
    tracking: tuple[TrackingRename, ...]
    summary: tuple[SummaryRename, ...]
    errors: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.errors


def _extract_id(pattern: re.Pattern[str], value: str) -> int | None:
    match = pattern.fullmatch(value)
    if not match:
        return None
    return int(match.group("id"))


def _read_dataset_summary_lines(path: Path) -> tuple[list[str], int]:
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    lines = text.splitlines(keepends=True)
    if not lines:
        raise ValueError(f"DatasetSummary is empty: {path}")

    header = next(csv.reader([lines[0].rstrip("\r\n")]))
    try:
        output_index = header.index("output_file")
    except ValueError as exc:
        raise ValueError("DatasetSummary is missing required 'output_file' column") from exc
    return lines, output_index


def _scan_summary(path: Path) -> tuple[list[tuple[int, str]], dict[str, list[int]]]:
    lines, output_index = _read_dataset_summary_lines(path)
    rows: list[tuple[int, str]] = []
    outputs: dict[str, list[int]] = {}

    for line_number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        parsed = next(csv.reader([line.rstrip("\r\n")]))
        if output_index >= len(parsed):
            raise ValueError(
                f"DatasetSummary row {line_number} has no output_file field"
            )
        output_file = parsed[output_index].strip()
        rows.append((line_number, output_file))
        if output_file:
            outputs.setdefault(output_file, []).append(line_number)
    return rows, outputs


def build_plan(tracking_root: Path, dataset_summary: Path) -> MigrationPlan:
    tracking_root = tracking_root.resolve()
    dataset_summary = dataset_summary.resolve()
    errors: list[str] = []
    tracking_changes: list[TrackingRename] = []
    summary_changes: list[SummaryRename] = []

    if not tracking_root.is_dir():
        return MigrationPlan(
            (), (), (f"Tracking root does not exist or is not a directory: {tracking_root}",)
        )
    if not dataset_summary.is_file():
        return MigrationPlan((), (), (f"DatasetSummary does not exist: {dataset_summary}",))

    folder = tracking_root / DAGGER_FOLDER
    if not folder.is_dir():
        return MigrationPlan((), (), (f"[Dagger] tracking folder not found: {folder}",))

    try:
        summary_rows, all_outputs = _scan_summary(dataset_summary)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        return MigrationPlan((), (), (str(exc),))

    tracking_by_id: dict[int, Path] = {}
    for path in sorted(folder.iterdir(), key=lambda p: p.name):
        if not path.is_file():
            continue
        clip_id = _extract_id(TRACKING_PATTERN, path.name)
        if clip_id is None:
            continue
        if clip_id in tracking_by_id:
            errors.append(
                f"[Dagger] duplicate legacy tracking ID {clip_id}: "
                f"{tracking_by_id[clip_id].name}, {path.name}"
            )
            continue
        tracking_by_id[clip_id] = path

    summary_by_id: dict[int, tuple[int, str]] = {}
    for row_number, output_file in summary_rows:
        clip_id = _extract_id(SUMMARY_PATTERN, output_file)
        if clip_id is None:
            continue
        if clip_id in summary_by_id:
            previous_row, previous_value = summary_by_id[clip_id]
            errors.append(
                f"[Dagger] duplicate legacy DatasetSummary ID {clip_id}: "
                f"rows {previous_row} ({previous_value}) and {row_number} ({output_file})"
            )
            continue
        summary_by_id[clip_id] = (row_number, output_file)

    tracking_ids = set(tracking_by_id)
    summary_ids = set(summary_by_id)

    if not tracking_ids:
        errors.append("[Dagger] no legacy DaggerConcept tracking files were found")
    if not summary_ids:
        errors.append("[Dagger] no legacy DaggerConcept DatasetSummary output_file rows were found")

    if tracking_ids != summary_ids:
        only_tracking = sorted(tracking_ids - summary_ids)
        only_summary = sorted(summary_ids - tracking_ids)
        if only_tracking:
            errors.append(
                "[Dagger] IDs present in tracking but missing from DatasetSummary "
                f"legacy output_file values: {only_tracking}"
            )
        if only_summary:
            errors.append(
                "[Dagger] IDs present in DatasetSummary legacy output_file values "
                f"but missing from tracking: {only_summary}"
            )

    planned_tracking_targets: dict[Path, Path] = {}
    planned_summary_targets: dict[str, tuple[str, int]] = {}

    for clip_id in sorted(tracking_ids & summary_ids):
        source = tracking_by_id[clip_id]
        target = source.with_name(TRACKING_TARGET.format(id=clip_id))

        if target.exists() and target != source:
            errors.append(
                f"[Dagger] tracking target collision for ID {clip_id}: {target}"
            )
        previous_source = planned_tracking_targets.get(target)
        if previous_source is not None and previous_source != source:
            errors.append(
                f"Tracking target planned more than once: {target} "
                f"from {previous_source} and {source}"
            )
        planned_tracking_targets[target] = source

        row_number, old_output = summary_by_id[clip_id]
        new_output = SUMMARY_TARGET.format(id=clip_id)
        existing_rows = [
            row for row in all_outputs.get(new_output, []) if row != row_number
        ]
        if existing_rows:
            errors.append(
                f"[Dagger] DatasetSummary target collision for ID {clip_id}: "
                f"{new_output} already appears on row(s) {existing_rows}"
            )
        previous_summary = planned_summary_targets.get(new_output)
        if previous_summary is not None and previous_summary != (old_output, row_number):
            errors.append(f"DatasetSummary target planned more than once: {new_output}")
        planned_summary_targets[new_output] = (old_output, row_number)

        tracking_changes.append(TrackingRename(clip_id, source, target))
        summary_changes.append(
            SummaryRename(clip_id, row_number, old_output, new_output)
        )

    tracking_changes.sort(key=lambda item: item.clip_id)
    summary_changes.sort(key=lambda item: item.clip_id)
    return MigrationPlan(tuple(tracking_changes), tuple(summary_changes), tuple(errors))


def _render_updated_summary(
    dataset_summary: Path,
    changes: Iterable[SummaryRename],
) -> bytes:
    raw = dataset_summary.read_bytes()
    had_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    lines = text.splitlines(keepends=True)
    if not lines:
        raise ValueError("DatasetSummary is empty")

    header = next(csv.reader([lines[0].rstrip("\r\n")]))
    try:
        output_index = header.index("output_file")
    except ValueError as exc:
        raise ValueError("DatasetSummary is missing required 'output_file' column") from exc

    for change in changes:
        line_index = change.row_number - 1
        if line_index >= len(lines):
            raise ValueError(
                f"DatasetSummary row disappeared before apply: {change.row_number}"
            )

        line = lines[line_index]
        if line.endswith("\r\n"):
            ending, body = "\r\n", line[:-2]
        elif line.endswith("\n") or line.endswith("\r"):
            ending, body = line[-1], line[:-1]
        else:
            ending, body = "", line

        parsed = next(csv.reader([body]))
        if output_index >= len(parsed):
            raise ValueError(
                f"DatasetSummary row {change.row_number} has no output_file field"
            )
        current = parsed[output_index].strip()
        if current != change.source:
            raise ValueError(
                f"DatasetSummary row {change.row_number} changed since planning: "
                f"expected {change.source!r}, found {current!r}"
            )
        if body.count(change.source) != 1:
            raise ValueError(
                f"DatasetSummary row {change.row_number} does not contain exactly "
                f"one occurrence of {change.source!r}; refusing a non-surgical rewrite"
            )

        lines[line_index] = body.replace(change.source, change.target, 1) + ending

    updated = "".join(lines).encode("utf-8")
    return (b"\xef\xbb\xbf" + updated) if had_bom else updated


def apply_plan(plan: MigrationPlan, dataset_summary: Path) -> None:
    if not plan.ready:
        raise RuntimeError("Cannot apply migration plan with validation errors")

    dataset_summary = dataset_summary.resolve()
    updated_summary = _render_updated_summary(dataset_summary, plan.summary)

    fd, temp_name = tempfile.mkstemp(
        prefix=f".{dataset_summary.name}.dagger.",
        suffix=".tmp",
        dir=str(dataset_summary.parent),
    )
    os.close(fd)
    temp_path = Path(temp_name)
    completed_renames: list[TrackingRename] = []

    try:
        temp_path.write_bytes(updated_summary)

        for change in plan.tracking:
            if not change.source.exists():
                raise FileNotFoundError(
                    f"Tracking source disappeared before apply: {change.source}"
                )
            if change.target.exists() and change.target != change.source:
                raise FileExistsError(
                    f"Tracking target appeared before apply: {change.target}"
                )

        for change in plan.tracking:
            os.replace(change.source, change.target)
            completed_renames.append(change)

        os.replace(temp_path, dataset_summary)

    except Exception:
        rollback_errors: list[str] = []
        for change in reversed(completed_renames):
            try:
                if change.target.exists() and not change.source.exists():
                    os.replace(change.target, change.source)
            except Exception as rollback_exc:  # pragma: no cover
                rollback_errors.append(
                    f"{change.target} -> {change.source}: {rollback_exc}"
                )
        if temp_path.exists():
            temp_path.unlink()
        if rollback_errors:
            raise RuntimeError(
                "Migration failed and one or more tracking renames could not be "
                "rolled back: " + "; ".join(rollback_errors)
            )
        raise
    finally:
        if temp_path.exists():
            temp_path.unlink()


def print_plan(plan: MigrationPlan) -> None:
    print("Dagger canonical naming migration")
    print("=" * 33)

    if plan.errors:
        print("\nVALIDATION ERRORS")
        for error in plan.errors:
            print(f"  - {error}")

    print(f"\nTracking renames ({len(plan.tracking)}):")
    for change in plan.tracking:
        print(f"  [Dagger #{change.clip_id}]")
        print(f"    {change.source} -> {change.target}")

    print(f"\nDatasetSummary.output_file updates ({len(plan.summary)}):")
    for change in plan.summary:
        print(
            f"  [Dagger #{change.clip_id}, row {change.row_number}] "
            f"{change.source} -> {change.target}"
        )

    print(
        f"\nStatus: {'READY' if plan.ready else 'BLOCKED'} | "
        f"paired clips: {len(plan.tracking)}"
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Plan or apply the Dagger canonical naming migration. "
            "Dry-run is the default."
        )
    )
    parser.add_argument(
        "--tracking-root",
        type=Path,
        default=Path("data/tracking"),
        help="Dataset tracking root (default: data/tracking)",
    )
    parser.add_argument(
        "--dataset-summary",
        type=Path,
        default=Path("data/DatasetSummary.csv"),
        help="DatasetSummary CSV (default: data/DatasetSummary.csv)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the validated plan without making changes (default).",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Apply the migration after all validation checks pass.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    plan = build_plan(args.tracking_root, args.dataset_summary)
    print_plan(plan)

    if not plan.ready:
        print("\nNo changes were made.", file=sys.stderr)
        return 2

    if not args.apply:
        print("\nDRY RUN: no changes were made.")
        print("Re-run with --apply only after reviewing every proposed change.")
        return 0

    try:
        apply_plan(plan, args.dataset_summary)
    except Exception as exc:
        print(f"\nAPPLY FAILED: {exc}", file=sys.stderr)
        return 1

    print("\nAPPLY COMPLETE: tracking filenames and DatasetSummary were updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
