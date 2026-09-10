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

LEGACY_FOLDER = "OutsideZone"
LEGACY_NAME = "OutsideZoneClosed"
CANONICAL_NAME = "OutsideZoneStretch"
TRACKING_PATTERN = re.compile(r"^OutsideZoneClosed_(?P<id>\d+)_cvat_mot\.zip$")
SUMMARY_PATTERN = re.compile(r"^OutsideZoneClosed_(?P<id>\d+)\.mp4$")


@dataclass(frozen=True)
class ClipPair:
    clip_id: int
    tracking_source: Path
    tracking_target: Path
    summary_row: int
    summary_source: str
    summary_target: str


@dataclass(frozen=True)
class MigrationPlan:
    source_folder: Path
    target_folder: Path
    key_actions_file: Path
    pairs: tuple[ClipPair, ...]
    errors: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.errors


def _extract_id(pattern: re.Pattern[str], value: str) -> int | None:
    match = pattern.fullmatch(value)
    return int(match.group("id")) if match else None


def _scan_summary(path: Path) -> tuple[list[tuple[int, str]], dict[str, list[int]]]:
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

    rows: list[tuple[int, str]] = []
    outputs: dict[str, list[int]] = {}
    for line_number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        parsed = next(csv.reader([line.rstrip("\r\n")]))
        if output_index >= len(parsed):
            raise ValueError(f"DatasetSummary row {line_number} has no output_file field")
        output_file = parsed[output_index].strip()
        rows.append((line_number, output_file))
        if output_file:
            outputs.setdefault(output_file, []).append(line_number)
    return rows, outputs


def build_plan(tracking_root: Path, dataset_summary: Path, key_actions_root: Path) -> MigrationPlan:
    tracking_root = tracking_root.resolve()
    dataset_summary = dataset_summary.resolve()
    key_actions_root = key_actions_root.resolve()

    source_folder = tracking_root / LEGACY_FOLDER
    target_folder = tracking_root / CANONICAL_NAME
    key_actions_file = key_actions_root / f"{CANONICAL_NAME}.csv"
    errors: list[str] = []

    if not tracking_root.is_dir():
        errors.append(f"Tracking root does not exist: {tracking_root}")
    if not dataset_summary.is_file():
        errors.append(f"DatasetSummary does not exist: {dataset_summary}")
    if not key_actions_root.is_dir():
        errors.append(f"Key Actions root does not exist: {key_actions_root}")
    if errors:
        return MigrationPlan(source_folder, target_folder, key_actions_file, (), tuple(errors))

    if not source_folder.is_dir():
        errors.append(f"[OutsideZoneStretch] legacy tracking folder not found: {source_folder}")
    if target_folder.exists():
        errors.append(f"[OutsideZoneStretch] canonical tracking folder already exists: {target_folder}")
    if not key_actions_file.is_file():
        errors.append(f"[OutsideZoneStretch] canonical Key Actions file not found: {key_actions_file}")
    if errors:
        return MigrationPlan(source_folder, target_folder, key_actions_file, (), tuple(errors))

    tracking_by_id: dict[int, Path] = {}
    unexpected: list[str] = []
    for path in sorted(source_folder.iterdir(), key=lambda p: p.name):
        if not path.is_file():
            unexpected.append(path.name)
            continue
        clip_id = _extract_id(TRACKING_PATTERN, path.name)
        if clip_id is None:
            unexpected.append(path.name)
            continue
        if clip_id in tracking_by_id:
            errors.append(f"[OutsideZoneStretch] duplicate legacy tracking ID {clip_id}")
        else:
            tracking_by_id[clip_id] = path
    if unexpected:
        errors.append(f"[OutsideZoneStretch] unexpected entries in legacy tracking folder: {unexpected}")

    try:
        summary_rows, all_outputs = _scan_summary(dataset_summary)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        errors.append(str(exc))
        return MigrationPlan(source_folder, target_folder, key_actions_file, (), tuple(errors))

    summary_by_id: dict[int, tuple[int, str]] = {}
    for row_number, output_file in summary_rows:
        clip_id = _extract_id(SUMMARY_PATTERN, output_file)
        if clip_id is None:
            continue
        if clip_id in summary_by_id:
            errors.append(f"[OutsideZoneStretch] duplicate legacy DatasetSummary ID {clip_id}")
        else:
            summary_by_id[clip_id] = (row_number, output_file)

    tracking_ids = set(tracking_by_id)
    summary_ids = set(summary_by_id)
    if not tracking_ids:
        errors.append("[OutsideZoneStretch] no legacy OutsideZoneClosed tracking files were found")
    if not summary_ids:
        errors.append("[OutsideZoneStretch] no legacy OutsideZoneClosed DatasetSummary rows were found")

    if tracking_ids != summary_ids:
        only_tracking = sorted(tracking_ids - summary_ids)
        only_summary = sorted(summary_ids - tracking_ids)
        if only_tracking:
            errors.append(f"[OutsideZoneStretch] IDs present in tracking but missing from DatasetSummary: {only_tracking}")
        if only_summary:
            errors.append(f"[OutsideZoneStretch] IDs present in DatasetSummary but missing from tracking: {only_summary}")

    pairs: list[ClipPair] = []
    for clip_id in sorted(tracking_ids & summary_ids):
        source = tracking_by_id[clip_id]
        target = target_folder / f"{CANONICAL_NAME}_{clip_id}_cvat_mot.zip"
        row_number, old_output = summary_by_id[clip_id]
        new_output = f"{CANONICAL_NAME}_{clip_id}.mp4"
        if all_outputs.get(new_output):
            errors.append(
                f"[OutsideZoneStretch] DatasetSummary target collision for ID {clip_id}: "
                f"{new_output} already appears on row(s) {all_outputs[new_output]}"
            )
        pairs.append(ClipPair(clip_id, source, target, row_number, old_output, new_output))

    return MigrationPlan(source_folder, target_folder, key_actions_file, tuple(pairs), tuple(errors))


def _render_updated_summary(dataset_summary: Path, pairs: Iterable[ClipPair]) -> bytes:
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

    for pair in pairs:
        idx = pair.summary_row - 1
        if idx >= len(lines):
            raise ValueError(f"DatasetSummary row disappeared before apply: {pair.summary_row}")
        line = lines[idx]
        if line.endswith("\r\n"):
            ending, body = "\r\n", line[:-2]
        elif line.endswith("\n") or line.endswith("\r"):
            ending, body = line[-1], line[:-1]
        else:
            ending, body = "", line
        parsed = next(csv.reader([body]))
        if output_index >= len(parsed):
            raise ValueError(f"DatasetSummary row {pair.summary_row} has no output_file field")
        current = parsed[output_index].strip()
        if current != pair.summary_source:
            raise ValueError(
                f"DatasetSummary row {pair.summary_row} changed since planning: expected {pair.summary_source!r}, found {current!r}"
            )
        if body.count(pair.summary_source) != 1:
            raise ValueError(
                f"DatasetSummary row {pair.summary_row} does not contain exactly one occurrence of {pair.summary_source!r}; refusing a non-surgical rewrite"
            )
        lines[idx] = body.replace(pair.summary_source, pair.summary_target, 1) + ending

    updated = "".join(lines).encode("utf-8")
    return (b"\xef\xbb\xbf" + updated) if had_bom else updated


def apply_plan(plan: MigrationPlan, dataset_summary: Path) -> None:
    if not plan.ready:
        raise RuntimeError("Cannot apply migration plan with validation errors")

    dataset_summary = dataset_summary.resolve()
    updated_summary = _render_updated_summary(dataset_summary, plan.pairs)
    fd, temp_name = tempfile.mkstemp(
        prefix=f".{dataset_summary.name}.outside-zone-stretch.", suffix=".tmp", dir=str(dataset_summary.parent)
    )
    os.close(fd)
    temp_path = Path(temp_name)
    renamed_files: list[tuple[Path, Path]] = []
    target_created = False
    source_removed = False

    try:
        temp_path.write_bytes(updated_summary)
        if plan.target_folder.exists():
            raise FileExistsError(f"Canonical tracking folder appeared before apply: {plan.target_folder}")
        if not plan.key_actions_file.is_file():
            raise FileNotFoundError(f"Canonical Key Actions file disappeared before apply: {plan.key_actions_file}")

        plan.target_folder.mkdir()
        target_created = True
        for pair in plan.pairs:
            if not pair.tracking_source.exists():
                raise FileNotFoundError(f"Tracking source disappeared before apply: {pair.tracking_source}")
            if pair.tracking_target.exists():
                raise FileExistsError(f"Tracking target appeared before apply: {pair.tracking_target}")
            os.replace(pair.tracking_source, pair.tracking_target)
            renamed_files.append((pair.tracking_source, pair.tracking_target))

        if any(plan.source_folder.iterdir()):
            raise RuntimeError(f"Legacy tracking folder is not empty after planned renames: {plan.source_folder}")
        plan.source_folder.rmdir()
        source_removed = True
        os.replace(temp_path, dataset_summary)

    except Exception:
        rollback_errors: list[str] = []
        try:
            if source_removed and not plan.source_folder.exists():
                plan.source_folder.mkdir()
        except Exception as exc:  # pragma: no cover
            rollback_errors.append(f"Legacy folder recreation failed: {exc}")

        for source, target in reversed(renamed_files):
            try:
                if target.exists() and not source.exists():
                    os.replace(target, source)
            except Exception as exc:  # pragma: no cover
                rollback_errors.append(f"{target} -> {source}: {exc}")

        try:
            if target_created and plan.target_folder.exists() and not any(plan.target_folder.iterdir()):
                plan.target_folder.rmdir()
        except Exception as exc:  # pragma: no cover
            rollback_errors.append(f"Canonical folder cleanup failed: {exc}")

        if temp_path.exists():
            temp_path.unlink()
        if rollback_errors:
            raise RuntimeError("Migration failed and rollback was incomplete: " + "; ".join(rollback_errors))
        raise
    finally:
        if temp_path.exists():
            temp_path.unlink()


def print_plan(plan: MigrationPlan) -> None:
    print("OutsideZoneStretch canonical naming migration")
    print("=" * 44)
    if plan.errors:
        print("\nVALIDATION ERRORS")
        for error in plan.errors:
            print(f"  - {error}")
    print(f"\nTracking folder: {plan.source_folder} -> {plan.target_folder}")
    print(f"Key Actions: already canonical at {plan.key_actions_file} (no rename)")
    print(f"\nTracking + DatasetSummary pairs ({len(plan.pairs)}):")
    for pair in plan.pairs:
        print(f"  [OutsideZoneStretch #{pair.clip_id}, row {pair.summary_row}]")
        print(f"    {pair.tracking_source.name} -> {pair.tracking_target.name}")
        print(f"    {pair.summary_source} -> {pair.summary_target}")
    print(f"\nStatus: {'READY' if plan.ready else 'BLOCKED'} | paired clips: {len(plan.pairs)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Plan or apply the OutsideZoneClosed -> OutsideZoneStretch canonical naming migration. Dry-run is default.")
    parser.add_argument("--tracking-root", type=Path, default=Path("data/tracking"))
    parser.add_argument("--dataset-summary", type=Path, default=Path("data/DatasetSummary.csv"))
    parser.add_argument("--key-actions-root", type=Path, default=Path("data/key_actions"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

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
        apply_plan(plan, args.dataset_summary)
    except Exception as exc:
        print(f"\nAPPLY FAILED: {exc}", file=sys.stderr)
        return 1
    print("\nAPPLY COMPLETE: OutsideZoneStretch tracking identities and DatasetSummary were updated; Key Actions was unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
