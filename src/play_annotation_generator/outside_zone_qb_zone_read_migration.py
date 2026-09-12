from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

STATUS_MIGRATE = "MIGRATE"
STATUS_HOLDOUT = "HOLDOUT"
STATUS_BLOCKED = "BLOCKED"
ALLOWED_STATUSES = {STATUS_MIGRATE, STATUS_HOLDOUT, STATUS_BLOCKED}

MANIFEST_COLUMNS = [
    "source_play",
    "source_video_id",
    "source_clip_name",
    "destination_play",
    "destination_video_id",
    "destination_clip_name",
    "status",
    "source_key_actions_file",
    "destination_key_actions_file",
    "notes",
]

DEFAULT_MANIFEST_PATH = Path("data/migrations/outside_zone_qb_zone_read_migration_manifest.csv")
DEFAULT_TRACKING_ROOT = Path("data/tracking")
DEFAULT_KEY_ACTIONS_ROOT = Path("data/key_actions")
DEFAULT_DATASET_SUMMARY = Path("data/DatasetSummary.csv")
DEFAULT_PLAYS_PATH = Path("data/plays.json")

EXPECTED_QB_HOLDOUTS = (17, 18, 41, 42, 131, 132)


@dataclass(frozen=True)
class ManifestRow:
    source_play: str
    source_video_id: int
    source_clip_name: str
    destination_play: str
    destination_video_id: int | None
    destination_clip_name: str
    status: str
    source_key_actions_file: str
    destination_key_actions_file: str
    notes: str

    def to_csv_dict(self) -> dict[str, str]:
        return {
            "source_play": self.source_play,
            "source_video_id": str(self.source_video_id),
            "source_clip_name": self.source_clip_name,
            "destination_play": self.destination_play,
            "destination_video_id": (
                str(self.destination_video_id) if self.destination_video_id is not None else ""
            ),
            "destination_clip_name": self.destination_clip_name,
            "status": self.status,
            "source_key_actions_file": self.source_key_actions_file,
            "destination_key_actions_file": self.destination_key_actions_file,
            "notes": self.notes,
        }

    @classmethod
    def from_csv_dict(cls, d: dict[str, str]) -> ManifestRow:
        status = d["status"].strip()
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"Invalid status '{status}' for {d.get('source_clip_name')}")
        dest_vid_raw = d.get("destination_video_id", "").strip()
        dest_vid = int(dest_vid_raw) if dest_vid_raw else None
        return cls(
            source_play=d["source_play"].strip(),
            source_video_id=int(d["source_video_id"].strip()),
            source_clip_name=d["source_clip_name"].strip(),
            destination_play=d.get("destination_play", "").strip(),
            destination_video_id=dest_vid,
            destination_clip_name=d.get("destination_clip_name", "").strip(),
            status=status,
            source_key_actions_file=d.get("source_key_actions_file", "").strip(),
            destination_key_actions_file=d.get("destination_key_actions_file", "").strip(),
            notes=d.get("notes", "").strip(),
        )


@dataclass(frozen=True)
class ValidationResult:
    rows: tuple[ManifestRow, ...]
    errors: tuple[str, ...]
    warnings: tuple[str, ...]
    ozs_to_ozs: int
    ozs_to_ozr: int
    ozs_blocked: int
    qb_to_izr: int
    qb_to_ozr: int
    qb_holdouts: int
    qb_blocked: int
    migrate_count: int
    holdout_count: int
    blocked_count: int
    dest_collisions: int
    summary_mismatches: int

    @property
    def ready(self) -> bool:
        return not self.errors and self.blocked_count == 0


def _parse_original_id(val: str) -> tuple[str, int]:
    val = val.strip()
    match = re.fullmatch(r"^(OutsideZoneStretch|QB_ZoneRead)_(\d+)$", val)
    if not match:
        raise ValueError(f"Malformed Original ID provenance: '{val}'")
    return match.group(1), int(match.group(2))


def _read_csv_rows(path: Path) -> list[list[str]]:
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    return list(csv.reader(text.splitlines()))


def build_manifest(
    tracking_root: Path | str = DEFAULT_TRACKING_ROOT,
    key_actions_root: Path | str = DEFAULT_KEY_ACTIONS_ROOT,
    dataset_summary: Path | str = DEFAULT_DATASET_SUMMARY,
) -> list[ManifestRow]:
    tracking_root = Path(tracking_root).resolve()
    key_actions_root = Path(key_actions_root).resolve()
    dataset_summary = Path(dataset_summary).resolve()

    ozs_file = key_actions_root / "OutsideZoneStretch.csv"
    ozr_file = key_actions_root / "OutsideZoneRead.csv"
    qb_file = key_actions_root / "QB_ZoneRead.csv"
    izr_file = key_actions_root / "InsideZoneRead.csv"

    if not ozs_file.is_file():
        raise FileNotFoundError(f"Missing OutsideZoneStretch Key Actions file: {ozs_file}")
    if not ozr_file.is_file():
        raise FileNotFoundError(f"Missing OutsideZoneRead Key Actions file: {ozr_file}")
    if not qb_file.is_file():
        raise FileNotFoundError(f"Missing QB_ZoneRead Key Actions file: {qb_file}")
    if not izr_file.is_file():
        raise FileNotFoundError(f"Missing InsideZoneRead Key Actions file: {izr_file}")

    ozs_csv = _read_csv_rows(ozs_file)
    ozr_csv = _read_csv_rows(ozr_file)
    qb_csv = _read_csv_rows(qb_file)
    izr_csv = _read_csv_rows(izr_file)

    ozs_headers = ozs_csv[2]
    ozs_vid_idx = ozs_headers.index("Video #")
    ozs_orig_idx = ozs_headers.index("Original ID")

    ozs_sources_mapped: dict[int, tuple[str, int, str]] = {}
    for row in ozs_csv[3:]:
        if not row or not row[0].strip():
            continue
        dest_id = int(row[ozs_vid_idx].strip())
        play, src_id = _parse_original_id(row[ozs_orig_idx])
        if play != "OutsideZoneStretch":
            raise ValueError(f"Expected OutsideZoneStretch Original ID, got {play}_{src_id}")
        if src_id in ozs_sources_mapped:
            raise ValueError(f"Duplicate OutsideZoneStretch source ID {src_id} in {ozs_file.name}")
        ozs_sources_mapped[src_id] = ("OutsideZoneStretch", dest_id, "Canonical stretch split")

    ozr_headers = ozr_csv[2]
    ozr_vid_idx = ozr_headers.index("Video #")
    ozr_orig_idx = ozr_headers.index("Original ID")

    qb_sources_mapped_ozr: dict[int, int] = {}
    for row in ozr_csv[3:]:
        if not row or not row[0].strip():
            continue
        dest_id = int(row[ozr_vid_idx].strip())
        play, src_id = _parse_original_id(row[ozr_orig_idx])
        if play == "OutsideZoneStretch":
            if src_id in ozs_sources_mapped:
                raise ValueError(
                    f"OutsideZoneStretch source ID {src_id} mapped in both OutsideZoneStretch and OutsideZoneRead"
                )
            ozs_sources_mapped[src_id] = ("OutsideZoneRead", dest_id, "Canonical read split")
        elif play == "QB_ZoneRead":
            if src_id in qb_sources_mapped_ozr:
                raise ValueError(f"Duplicate QB_ZoneRead source ID {src_id} in {ozr_file.name}")
            qb_sources_mapped_ozr[src_id] = dest_id
        else:
            raise ValueError(f"Unexpected source play in {ozr_file.name}: {play}")

    qb_headers = qb_csv[2]
    qb_vid_idx = qb_headers.index("Video #")
    qb_cls_idx = qb_headers.index("Classification")
    qb_new_id_idx = qb_headers.index("New ID") if "New ID" in qb_headers else -1

    holdout_set = set(EXPECTED_QB_HOLDOUTS)
    qb_rows: dict[int, ManifestRow] = {}

    for row in qb_csv[3:]:
        if not row or not row[0].strip():
            continue
        src_id = int(row[qb_vid_idx].strip())
        cls = row[qb_cls_idx].strip()
        new_id_str = (
            row[qb_new_id_idx].strip() if qb_new_id_idx >= 0 and len(row) > qb_new_id_idx else ""
        )

        if src_id in holdout_set or cls in ("Counter", "HOLDOUT", "Holdout"):
            if src_id not in holdout_set:
                raise ValueError(f"Unexpected QB holdout ID {src_id}")
            qb_rows[src_id] = ManifestRow(
                source_play="QB_ZoneRead",
                source_video_id=src_id,
                source_clip_name=f"QB_ZoneRead_{src_id}",
                destination_play="",
                destination_video_id=None,
                destination_clip_name=f"QB_ZoneRead_{src_id}",
                status=STATUS_HOLDOUT,
                source_key_actions_file="data/key_actions/QB_ZoneRead.csv",
                destination_key_actions_file="",
                notes="Unresolved Counter/gap taxonomy",
            )
        elif cls == "InsideZoneRead":
            if not new_id_str.isdigit():
                raise ValueError(f"QB_ZoneRead row {src_id} classified as InsideZoneRead missing valid New ID")
            dest_id = int(new_id_str)
            qb_rows[src_id] = ManifestRow(
                source_play="QB_ZoneRead",
                source_video_id=src_id,
                source_clip_name=f"QB_ZoneRead_{src_id}",
                destination_play="InsideZoneRead",
                destination_video_id=dest_id,
                destination_clip_name=f"InsideZoneRead_{dest_id}",
                status=STATUS_MIGRATE,
                source_key_actions_file="data/key_actions/QB_ZoneRead.csv",
                destination_key_actions_file="data/key_actions/InsideZoneRead.csv",
                notes="QB keep preserved as action",
            )
        elif cls == "OutsideZoneRead":
            if src_id not in qb_sources_mapped_ozr:
                raise ValueError(
                    f"QB_ZoneRead row {src_id} classified as OutsideZoneRead not found in OutsideZoneRead.csv"
                )
            dest_id = qb_sources_mapped_ozr[src_id]
            qb_rows[src_id] = ManifestRow(
                source_play="QB_ZoneRead",
                source_video_id=src_id,
                source_clip_name=f"QB_ZoneRead_{src_id}",
                destination_play="OutsideZoneRead",
                destination_video_id=dest_id,
                destination_clip_name=f"OutsideZoneRead_{dest_id}",
                status=STATUS_MIGRATE,
                source_key_actions_file="data/key_actions/QB_ZoneRead.csv",
                destination_key_actions_file="data/key_actions/OutsideZoneRead.csv",
                notes="QB keep preserved as action",
            )
        else:
            raise ValueError(f"Invalid QB_ZoneRead classification '{cls}' for video {src_id}")

    ozs_track_folder = tracking_root / "OutsideZoneStretch"
    ozs_source_ids = set(ozs_sources_mapped)
    if ozs_track_folder.is_dir():
        for p in ozs_track_folder.glob("OutsideZoneStretch_*_cvat_mot.zip"):
            m = re.match(r"^OutsideZoneStretch_(\d+)_cvat_mot\.zip$", p.name)
            if m:
                ozs_source_ids.add(int(m.group(1)))

    if dataset_summary.is_file():
        summary_lines = dataset_summary.read_text(encoding="utf-8-sig").splitlines()
        if summary_lines:
            header = next(csv.reader([summary_lines[0]]))
            if "output_file" in header:
                out_idx = header.index("output_file")
                for line in summary_lines[1:]:
                    parsed = next(csv.reader([line]))
                    if len(parsed) > out_idx:
                        m = re.match(r"^OutsideZoneStretch_(\d+)\.mp4$", parsed[out_idx].strip())
                        if m:
                            ozs_source_ids.add(int(m.group(1)))

    ozs_manifest_rows: list[ManifestRow] = []
    for src_id in sorted(ozs_source_ids):
        if src_id in ozs_sources_mapped:
            dest_play, dest_id, note = ozs_sources_mapped[src_id]
            dest_ka = f"data/key_actions/{dest_play}.csv"
            ozs_manifest_rows.append(
                ManifestRow(
                    source_play="OutsideZoneStretch",
                    source_video_id=src_id,
                    source_clip_name=f"OutsideZoneStretch_{src_id}",
                    destination_play=dest_play,
                    destination_video_id=dest_id,
                    destination_clip_name=f"{dest_play}_{dest_id}",
                    status=STATUS_MIGRATE,
                    source_key_actions_file="data/key_actions/OutsideZoneStretch.csv",
                    destination_key_actions_file=dest_ka,
                    notes=note,
                )
            )
        else:
            ozs_manifest_rows.append(
                ManifestRow(
                    source_play="OutsideZoneStretch",
                    source_video_id=src_id,
                    source_clip_name=f"OutsideZoneStretch_{src_id}",
                    destination_play="",
                    destination_video_id=None,
                    destination_clip_name=f"OutsideZoneStretch_{src_id}",
                    status=STATUS_BLOCKED,
                    source_key_actions_file="data/key_actions/OutsideZoneStretch.csv",
                    destination_key_actions_file="",
                    notes="Unmapped legacy source tracking clip without key action mapping",
                )
            )

    qb_manifest_rows = [qb_rows[src_id] for src_id in sorted(qb_rows)]
    return ozs_manifest_rows + qb_manifest_rows


def write_manifest(rows: Sequence[ManifestRow], manifest_path: Path | str = DEFAULT_MANIFEST_PATH) -> None:
    manifest_path = Path(manifest_path).resolve()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=MANIFEST_COLUMNS)
        writer.writeheader()
        for r in rows:
            writer.writerow(r.to_csv_dict())


def load_manifest(manifest_path: Path | str = DEFAULT_MANIFEST_PATH) -> list[ManifestRow]:
    manifest_path = Path(manifest_path).resolve()
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifest file not found: {manifest_path}")
    rows: list[ManifestRow] = []
    with manifest_path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for d in reader:
            rows.append(ManifestRow.from_csv_dict(d))
    return rows


def validate_manifest(
    manifest_rows: Sequence[ManifestRow],
    tracking_root: Path | str = DEFAULT_TRACKING_ROOT,
    dataset_summary: Path | str = DEFAULT_DATASET_SUMMARY,
    plays_path: Path | str = DEFAULT_PLAYS_PATH,
    key_actions_root: Path | str = DEFAULT_KEY_ACTIONS_ROOT,
    require_production_counts: bool = False,
) -> ValidationResult:
    tracking_root = Path(tracking_root).resolve()
    dataset_summary = Path(dataset_summary).resolve()
    plays_path = Path(plays_path).resolve()
    key_actions_root = Path(key_actions_root).resolve()

    errors: list[str] = []
    warnings: list[str] = []

    valid_play_labels: set[str] = set()
    if plays_path.is_file():
        try:
            plays_data = json.loads(plays_path.read_text(encoding="utf-8"))
            valid_play_labels = set(plays_data.get("playLabels", []))
        except Exception as exc:
            errors.append(f"Failed to load plays.json: {exc}")
    else:
        errors.append(f"plays.json does not exist: {plays_path}")

    summary_outputs: set[str] = set()
    summary_dupes: set[str] = set()
    if dataset_summary.is_file():
        try:
            summary_lines = dataset_summary.read_text(encoding="utf-8-sig").splitlines()
            if summary_lines:
                header = next(csv.reader([summary_lines[0]]))
                out_idx = header.index("output_file")
                for line in summary_lines[1:]:
                    if not line.strip():
                        continue
                    parsed = next(csv.reader([line]))
                    if len(parsed) > out_idx:
                        out_val = parsed[out_idx].strip()
                        if out_val in summary_outputs:
                            summary_dupes.add(out_val)
                        summary_outputs.add(out_val)
        except Exception as exc:
            errors.append(f"Failed to scan DatasetSummary: {exc}")
    else:
        errors.append(f"DatasetSummary does not exist: {dataset_summary}")

    if summary_dupes:
        errors.append(f"Duplicate output_file identities in DatasetSummary: {sorted(summary_dupes)}")

    qb_file = key_actions_root / "QB_ZoneRead.csv"
    if qb_file.is_file():
        try:
            qb_csv = _read_csv_rows(qb_file)
            qb_headers = qb_csv[2]
            qb_vid_idx = qb_headers.index("Video #")
            qb_cls_idx = qb_headers.index("Classification")
            qb_new_id_idx = qb_headers.index("New ID") if "New ID" in qb_headers else -1
            if qb_new_id_idx >= 0:
                for row in qb_csv[3:]:
                    if not row or not row[0].strip():
                        continue
                    v_id = int(row[qb_vid_idx].strip())
                    cls = row[qb_cls_idx].strip()
                    new_id_raw = row[qb_new_id_idx].strip() if len(row) > qb_new_id_idx else ""
                    if cls == "OutsideZoneRead" and new_id_raw.isdigit():
                        matching_row = next(
                            (
                                r
                                for r in manifest_rows
                                if r.source_play == "QB_ZoneRead" and r.source_video_id == v_id
                            ),
                            None,
                        )
                        if matching_row and matching_row.destination_video_id is not None:
                            if int(new_id_raw) != matching_row.destination_video_id:
                                warnings.append(
                                    f"Stale New ID detected in QB_ZoneRead.csv row {v_id}: "
                                    f"file has {new_id_raw}, canonical manifest has {matching_row.destination_video_id}"
                                )
        except Exception as exc:
            warnings.append(f"Could not check QB_ZoneRead.csv for stale New ID: {exc}")

    seen_sources: set[tuple[str, int]] = set()
    seen_destinations: set[tuple[str, int]] = set()

    ozs_to_ozs = 0
    ozs_to_ozr = 0
    ozs_blocked = 0
    qb_to_izr = 0
    qb_to_ozr = 0
    qb_holdouts = 0
    qb_blocked = 0

    dest_collisions = 0
    summary_mismatches = 0

    for r in manifest_rows:
        src_key = (r.source_play, r.source_video_id)
        if src_key in seen_sources:
            errors.append(f"Duplicate source identity in manifest: {r.source_play} #{r.source_video_id}")
        seen_sources.add(src_key)

        if r.status not in ALLOWED_STATUSES:
            errors.append(f"Invalid status '{r.status}' in row {r.source_clip_name}")

        if r.status == STATUS_MIGRATE:
            if not r.destination_play or r.destination_video_id is None:
                errors.append(f"MIGRATE row {r.source_clip_name} missing destination play or ID")
            else:
                dest_key = (r.destination_play, r.destination_video_id)
                if dest_key in seen_destinations:
                    errors.append(
                        f"Duplicate destination identity in manifest: {r.destination_play} #{r.destination_video_id}"
                    )
                seen_destinations.add(dest_key)

                if r.destination_play == "QB_ZoneRead":
                    errors.append(
                        f"QB_ZoneRead is not a canonical play and cannot be a destination (row {r.source_clip_name})"
                    )
                elif valid_play_labels and r.destination_play not in valid_play_labels:
                    errors.append(
                        f"Destination play '{r.destination_play}' not in plays.json (row {r.source_clip_name})"
                    )

            if r.source_play == "OutsideZoneStretch":
                if r.destination_play == "OutsideZoneStretch":
                    ozs_to_ozs += 1
                elif r.destination_play == "OutsideZoneRead":
                    ozs_to_ozr += 1
                else:
                    errors.append(
                        f"Unexpected destination play for OutsideZoneStretch: {r.destination_play} (row {r.source_clip_name})"
                    )
            elif r.source_play == "QB_ZoneRead":
                if r.destination_play == "InsideZoneRead":
                    qb_to_izr += 1
                elif r.destination_play == "OutsideZoneRead":
                    qb_to_ozr += 1
                else:
                    errors.append(
                        f"Unexpected destination play for QB_ZoneRead: {r.destination_play} (row {r.source_clip_name})"
                    )

        elif r.status == STATUS_HOLDOUT:
            if r.destination_play != "":
                errors.append(f"HOLDOUT row {r.source_clip_name} must have empty destination_play")
            if r.destination_video_id is not None:
                errors.append(f"HOLDOUT row {r.source_clip_name} must have empty destination_video_id")
            if r.destination_clip_name != r.source_clip_name:
                errors.append(
                    f"HOLDOUT row {r.source_clip_name} must have unchanged destination_clip_name"
                )
            if r.source_play == "QB_ZoneRead":
                qb_holdouts += 1
            else:
                errors.append(f"Unexpected HOLDOUT row for source play {r.source_play}")

        elif r.status == STATUS_BLOCKED:
            if r.source_play == "OutsideZoneStretch":
                ozs_blocked += 1
            elif r.source_play == "QB_ZoneRead":
                qb_blocked += 1

        src_zip = tracking_root / r.source_play / f"{r.source_clip_name}_cvat_mot.zip"
        if not src_zip.is_file():
            errors.append(f"Source tracking ZIP does not exist: {src_zip}")

        expected_summary_mp4 = f"{r.source_clip_name}.mp4"
        if expected_summary_mp4 not in summary_outputs:
            errors.append(f"Source clip {expected_summary_mp4} not found in DatasetSummary.csv")
            summary_mismatches += 1

        if r.status == STATUS_MIGRATE and r.destination_play:
            dest_zip = tracking_root / r.destination_play / f"{r.destination_clip_name}_cvat_mot.zip"
            if dest_zip.exists():
                if r.source_play == r.destination_play:
                    pass
                else:
                    errors.append(
                        f"Destination collision: unrelated file already exists at {dest_zip} (from {r.source_clip_name})"
                    )
                    dest_collisions += 1

    migrate_count = ozs_to_ozs + ozs_to_ozr + qb_to_izr + qb_to_ozr
    holdout_count = qb_holdouts
    blocked_count = ozs_blocked + qb_blocked

    if require_production_counts:
        if qb_to_izr != 146:
            errors.append(f"Expected exactly 146 QB -> InsideZoneRead MIGRATE clips, found {qb_to_izr}")
        if qb_to_ozr != 46:
            errors.append(f"Expected exactly 46 QB -> OutsideZoneRead MIGRATE clips, found {qb_to_ozr}")
        if qb_holdouts != 6:
            errors.append(f"Expected exactly 6 QB HOLDOUT clips, found {qb_holdouts}")
        if ozs_to_ozs != 228:
            errors.append(f"Expected exactly 228 OutsideZoneStretch -> OutsideZoneStretch clips, found {ozs_to_ozs}")
        if ozs_to_ozr != 118:
            errors.append(f"Expected exactly 118 OutsideZoneStretch -> OutsideZoneRead clips, found {ozs_to_ozr}")

    return ValidationResult(
        rows=tuple(manifest_rows),
        errors=tuple(errors),
        warnings=tuple(warnings),
        ozs_to_ozs=ozs_to_ozs,
        ozs_to_ozr=ozs_to_ozr,
        ozs_blocked=ozs_blocked,
        qb_to_izr=qb_to_izr,
        qb_to_ozr=qb_to_ozr,
        qb_holdouts=qb_holdouts,
        qb_blocked=qb_blocked,
        migrate_count=migrate_count,
        holdout_count=holdout_count,
        blocked_count=blocked_count,
        dest_collisions=dest_collisions,
        summary_mismatches=summary_mismatches,
    )


def print_preflight_report(res: ValidationResult) -> None:
    print("MIGRATION PREFLIGHT")
    print()
    print("Legacy Outside Zone source:")
    print(f"  OutsideZoneStretch -> OutsideZoneStretch: {res.ozs_to_ozs}")
    print(f"  OutsideZoneStretch -> OutsideZoneRead:    {res.ozs_to_ozr}")
    print(f"  Unmapped/BLOCKED:                          {res.ozs_blocked}")
    print()
    print("Legacy QB_ZoneRead source:")
    print(f"  -> InsideZoneRead:  {res.qb_to_izr}")
    print(f"  -> OutsideZoneRead: {res.qb_to_ozr}")
    print(f"  HOLDOUT:              {res.qb_holdouts}")
    if res.qb_blocked > 0:
        print(f"  BLOCKED:              {res.qb_blocked}")
    print()
    print(f"Manifest rows:        {len(res.rows)}")
    print(f"MIGRATE:              {res.migrate_count}")
    print(f"HOLDOUT:              {res.holdout_count}")
    print(f"BLOCKED:              {res.blocked_count}")
    print(f"Destination collisions: {res.dest_collisions}")
    print(f"DatasetSummary mismatches: {res.summary_mismatches}")
    print()
    if res.warnings:
        print("WARNINGS:")
        for w in res.warnings:
            print(f"  - {w}")
        print()
    if res.errors:
        print("VALIDATION ERRORS:")
        for err in res.errors:
            print(f"  - {err}")
        print()
    status_str = "READY" if res.ready else "FAILED"
    print(f"STATUS: {status_str}")


def render_updated_summary(dataset_summary: Path, migrate_rows: Iterable[ManifestRow]) -> bytes:
    raw = dataset_summary.read_bytes()
    had_bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    lines = text.splitlines(keepends=True)
    if not lines:
        raise ValueError(f"DatasetSummary is empty: {dataset_summary}")

    header = next(csv.reader([lines[0].rstrip("\r\n")]))
    try:
        output_index = header.index("output_file")
    except ValueError as exc:
        raise ValueError("DatasetSummary missing required 'output_file' column") from exc

    row_index_by_source_mp4: dict[str, int] = {}
    for idx, line in enumerate(lines[1:], start=1):
        if not line.strip():
            continue
        parsed = next(csv.reader([line.rstrip("\r\n")]))
        if len(parsed) > output_index:
            out_val = parsed[output_index].strip()
            if out_val in row_index_by_source_mp4:
                raise ValueError(f"Duplicate output_file in DatasetSummary: {out_val}")
            row_index_by_source_mp4[out_val] = idx

    for r in migrate_rows:
        src_mp4 = f"{r.source_clip_name}.mp4"
        dest_mp4 = f"{r.destination_clip_name}.mp4"
        if src_mp4 == dest_mp4:
            continue
        if src_mp4 not in row_index_by_source_mp4:
            raise ValueError(f"Clip {src_mp4} not found in DatasetSummary during render")
        idx = row_index_by_source_mp4[src_mp4]
        line = lines[idx]
        if line.endswith("\r\n"):
            ending, body = "\r\n", line[:-2]
        elif line.endswith("\n") or line.endswith("\r"):
            ending, body = line[-1], line[:-1]
        else:
            ending, body = "", line

        if body.count(src_mp4) != 1:
            raise ValueError(
                f"Line {idx + 1} does not have exactly one occurrence of {src_mp4}; refusing non-surgical rewrite"
            )
        lines[idx] = body.replace(src_mp4, dest_mp4, 1) + ending

    updated = "".join(lines).encode("utf-8")
    return (b"\xef\xbb\xbf" + updated) if had_bom else updated


def apply_migration(
    manifest_rows: Sequence[ManifestRow],
    tracking_root: Path | str = DEFAULT_TRACKING_ROOT,
    dataset_summary: Path | str = DEFAULT_DATASET_SUMMARY,
    plays_path: Path | str = DEFAULT_PLAYS_PATH,
    key_actions_root: Path | str = DEFAULT_KEY_ACTIONS_ROOT,
    require_production_counts: bool = False,
) -> None:
    res = validate_manifest(
        manifest_rows,
        tracking_root=tracking_root,
        dataset_summary=dataset_summary,
        plays_path=plays_path,
        key_actions_root=key_actions_root,
        require_production_counts=require_production_counts,
    )
    if not res.ready:
        reasons = list(res.errors)
        if res.blocked_count > 0:
            reasons.append(f"{res.blocked_count} clips are marked as BLOCKED")
        raise RuntimeError("Cannot apply migration: " + "; ".join(reasons))

    tracking_root = Path(tracking_root).resolve()
    dataset_summary = Path(dataset_summary).resolve()

    migrate_rows = [r for r in manifest_rows if r.status == STATUS_MIGRATE]
    updated_summary_bytes = render_updated_summary(dataset_summary, migrate_rows)

    fd, temp_summary_name = tempfile.mkstemp(
        prefix=f".{dataset_summary.name}.migration.", suffix=".tmp", dir=str(dataset_summary.parent)
    )
    os.close(fd)
    temp_summary_path = Path(temp_summary_name)

    journal: list[tuple[Path, Path]] = []
    created_directories: list[Path] = []

    try:
        temp_summary_path.write_bytes(updated_summary_bytes)

        cross_folder_moves: list[tuple[Path, Path]] = []
        intra_folder_moves: list[tuple[Path, Path]] = []

        for r in migrate_rows:
            src_path = tracking_root / r.source_play / f"{r.source_clip_name}_cvat_mot.zip"
            dest_dir = tracking_root / r.destination_play
            dest_path = dest_dir / f"{r.destination_clip_name}_cvat_mot.zip"
            if src_path == dest_path:
                continue
            if r.source_play != r.destination_play:
                cross_folder_moves.append((src_path, dest_path))
            else:
                intra_folder_moves.append((src_path, dest_path))

        dest_dirs = {dest.parent for _, dest in cross_folder_moves}
        for d in dest_dirs:
            if not d.exists():
                d.mkdir(parents=True, exist_ok=True)
                created_directories.append(d)

        for src, dest in cross_folder_moves:
            if dest.exists():
                raise FileExistsError(f"Cross-folder destination already exists: {dest}")
            os.replace(src, dest)
            journal.append((src, dest))

        staged_intra: list[tuple[Path, Path, Path]] = []
        for src, dest in intra_folder_moves:
            temp_intra = src.with_name(f".{src.name}.migrating.tmp")
            os.replace(src, temp_intra)
            journal.append((src, temp_intra))
            staged_intra.append((src, temp_intra, dest))

        for orig_src, temp_intra, final_dest in staged_intra:
            if final_dest.exists():
                raise FileExistsError(f"Intra-folder destination already exists: {final_dest}")
            os.replace(temp_intra, final_dest)
            journal.append((temp_intra, final_dest))

        os.replace(temp_summary_path, dataset_summary)

    except Exception as exc:
        rollback_errors: list[str] = []
        for orig, curr in reversed(journal):
            try:
                if curr.exists() and not orig.exists():
                    os.replace(curr, orig)
            except Exception as r_exc:  # pragma: no cover
                rollback_errors.append(f"Rollback {curr} -> {orig} failed: {r_exc}")

        for d in reversed(created_directories):
            try:
                if d.exists() and not any(d.iterdir()):
                    d.rmdir()
            except Exception as r_exc:  # pragma: no cover
                rollback_errors.append(f"Directory cleanup failed for {d}: {r_exc}")

        if temp_summary_path.exists():
            temp_summary_path.unlink()

        if rollback_errors:
            raise RuntimeError(
                f"Migration failed ({exc}) and rollback encountered errors: {'; '.join(rollback_errors)}"
            ) from exc
        raise
    finally:
        if temp_summary_path.exists():
            temp_summary_path.unlink()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Canonical Outside Zone Split and QB Zone Read Migration (Dry-run by default)."
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--tracking-root", type=Path, default=DEFAULT_TRACKING_ROOT)
    parser.add_argument("--key-actions-root", type=Path, default=DEFAULT_KEY_ACTIONS_ROOT)
    parser.add_argument("--dataset-summary", type=Path, default=DEFAULT_DATASET_SUMMARY)
    parser.add_argument("--plays-path", type=Path, default=DEFAULT_PLAYS_PATH)
    parser.add_argument("--generate-manifest", action="store_true", help="Generate or regenerate manifest file")
    parser.add_argument("--production-counts", action="store_true", help="Enforce exact production count assertions")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Perform preflight dry-run (default)")
    mode.add_argument("--apply", action="store_true", help="Apply migration modifications")
    args = parser.parse_args(argv)

    if args.generate_manifest or not args.manifest.is_file():
        rows = build_manifest(
            tracking_root=args.tracking_root,
            key_actions_root=args.key_actions_root,
            dataset_summary=args.dataset_summary,
        )
        write_manifest(rows, args.manifest)
        print(f"Manifest written to: {args.manifest} ({len(rows)} rows)")
    else:
        rows = load_manifest(args.manifest)

    res = validate_manifest(
        rows,
        tracking_root=args.tracking_root,
        dataset_summary=args.dataset_summary,
        plays_path=args.plays_path,
        key_actions_root=args.key_actions_root,
        require_production_counts=args.production_counts,
    )
    print_preflight_report(res)
    sys.stdout.flush()

    if not res.ready:
        print("\nPreflight check reported issues or BLOCKED clips. Migration cannot be applied.", file=sys.stderr)
        return 2

    if not args.apply:
        print("\nDRY RUN: zero filesystem or DatasetSummary mutations were made.")
        print("To apply changes once all conditions are resolved, run with --apply.")
        return 0

    try:
        apply_migration(
            rows,
            tracking_root=args.tracking_root,
            dataset_summary=args.dataset_summary,
            plays_path=args.plays_path,
            key_actions_root=args.key_actions_root,
            require_production_counts=args.production_counts,
        )
    except Exception as exc:
        print(f"\nAPPLY FAILED: {exc}", file=sys.stderr)
        return 1

    print("\nAPPLY COMPLETE: Tracking identities and DatasetSummary updated successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
