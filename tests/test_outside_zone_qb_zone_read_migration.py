import csv
import json
import os
from pathlib import Path
import pytest

from play_annotation_generator.outside_zone_qb_zone_read_migration import (
    ManifestRow,
    STATUS_BLOCKED,
    STATUS_HOLDOUT,
    STATUS_MIGRATE,
    apply_migration,
    build_manifest,
    load_manifest,
    render_updated_summary,
    validate_manifest,
    write_manifest,
)


def _create_minimal_plays_json(path: Path) -> None:
    data = {
        "playLabels": [
            "InsideZoneRead",
            "OutsideZoneRead",
            "OutsideZoneStretch",
            "Counter",
            "Power",
        ]
    }
    path.write_text(json.dumps(data), encoding="utf-8")


def _create_minimal_summary(path: Path, output_files: list[str], had_bom: bool = False, newline: str = "\r\n") -> None:
    header = "clip number,start_time,end_time,play,view,fromYouTube,input_file,output_file,name,file extension,date,"
    rows = [header]
    for idx, out in enumerate(output_files, start=1):
        rows.append(
            f"{idx},1:00:00,1:01:00,Run,E,FALSE,source.mp4,{out},source_,.mp4,2026-03-18,"
        )
    text = newline.join(rows) + newline
    raw = text.encode("utf-8")
    if had_bom:
        raw = b"\xef\xbb\xbf" + raw
    path.write_bytes(raw)


def _setup_synthetic_dataset(tmp_path: Path):
    track_root = tmp_path / "tracking"
    ka_root = tmp_path / "key_actions"
    track_root.mkdir()
    ka_root.mkdir()

    # Tracking folders
    ozs_track = track_root / "OutsideZoneStretch"
    ozs_track.mkdir()
    qb_track = track_root / "QB_ZoneRead"
    qb_track.mkdir()
    izr_track = track_root / "InsideZoneRead"
    izr_track.mkdir()

    # OZS source zips: 1, 2, 3, 4
    for i in (1, 2, 3, 4):
        (ozs_track / f"OutsideZoneStretch_{i}_cvat_mot.zip").write_bytes(f"zip-ozs-{i}".encode())

    # QB source zips: 1, 3, 17
    for i in (1, 3, 17):
        (qb_track / f"QB_ZoneRead_{i}_cvat_mot.zip").write_bytes(f"zip-qb-{i}".encode())

    # Pre-existing IZR zip: 1
    (izr_track / "InsideZoneRead_1_cvat_mot.zip").write_bytes(b"zip-izr-1")

    # Key Actions:
    # OutsideZoneStretch.csv: 2 rows (dest 1 <- orig 1, dest 2 <- orig 2)
    ozs_ka = ka_root / "OutsideZoneStretch.csv"
    ozs_ka.write_text(
        "Video Name:,Outside Zone Stretch\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,OL,Zone Block,Snap Receive,Press Edge,Read Edge Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,Original ID\r\n"
        '1,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,OutsideZoneStretch_1\r\n'
        '2,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,OutsideZoneStretch_2\r\n',
        encoding="utf-8",
    )

    # OutsideZoneRead.csv: 2 rows (dest 1 <- OZS 3, dest 2 <- QB 1)
    ozr_ka = ka_root / "OutsideZoneRead.csv"
    ozr_ka.write_text(
        "Video Name:,Outside Zone Read\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,OL,Zone Block,Snap Receive,Press Edge,Read Edge Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,Original ID\r\n"
        '1,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,OutsideZoneStretch_3\r\n'
        '2,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,QB_ZoneRead_1\r\n',
        encoding="utf-8",
    )

    # QB_ZoneRead.csv: 3 rows (QB 1 -> OZR 2, QB 3 -> IZR 236, QB 17 -> HOLDOUT)
    qb_ka = ka_root / "QB_ZoneRead.csv"
    qb_ka.write_text(
        "Video Name:,QB Zone Read\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Snap Receive,Read Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,Classification,New ID\r\n"
        '1,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,OutsideZoneRead,348\r\n'
        '3,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,InsideZoneRead,236\r\n'
        '17,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,Counter,-\r\n',
        encoding="utf-8",
    )

    # InsideZoneRead.csv: 1 existing row + 1 QB row
    izr_ka = ka_root / "InsideZoneRead.csv"
    izr_ka.write_text(
        "Video Name:,Inside Zone Read\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Snap Receive,Read Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play\r\n"
        '1,"0,ALL",1,2,3,4,5,-,6,7,70,OOB\r\n'
        '236,"0,ALL",1,2,3,4,5,-,6,7,70,OOB\r\n',
        encoding="utf-8",
    )

    summary_file = tmp_path / "DatasetSummary.csv"
    _create_minimal_summary(
        summary_file,
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "OutsideZoneStretch_4.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "InsideZoneRead_1.mp4",
        ],
    )

    plays_file = tmp_path / "plays.json"
    _create_minimal_plays_json(plays_file)

    manifest_file = tmp_path / "manifest.csv"

    return {
        "track_root": track_root,
        "ka_root": ka_root,
        "summary": summary_file,
        "plays": plays_file,
        "manifest": manifest_file,
    }


def test_manifest_generation_parses_provenance_and_holdouts(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])

    assert len(rows) == 7  # OZS 1,2,3,4 + QB 1,3,17

    ozs_4 = next(r for r in rows if r.source_clip_name == "OutsideZoneStretch_4")
    assert ozs_4.status == STATUS_BLOCKED
    assert ozs_4.destination_play == ""

    qb_17 = next(r for r in rows if r.source_clip_name == "QB_ZoneRead_17")
    assert qb_17.status == STATUS_HOLDOUT
    assert qb_17.destination_play == ""
    assert qb_17.destination_video_id is None
    assert qb_17.destination_clip_name == "QB_ZoneRead_17"

    qb_1 = next(r for r in rows if r.source_clip_name == "QB_ZoneRead_1")
    assert qb_1.status == STATUS_MIGRATE
    assert qb_1.destination_play == "OutsideZoneRead"
    assert qb_1.destination_video_id == 2
    assert qb_1.destination_clip_name == "OutsideZoneRead_2"

    qb_3 = next(r for r in rows if r.source_clip_name == "QB_ZoneRead_3")
    assert qb_3.status == STATUS_MIGRATE
    assert qb_3.destination_play == "InsideZoneRead"
    assert qb_3.destination_video_id == 236
    assert qb_3.destination_clip_name == "InsideZoneRead_236"


def test_manifest_write_and_load(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    write_manifest(rows, env["manifest"])
    loaded = load_manifest(env["manifest"])
    assert len(loaded) == len(rows)
    for orig, roundtrip in zip(rows, loaded):
        assert orig == roundtrip


def test_manifest_generation_rejects_malformed_original_id(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    bad_ozs = env["ka_root"] / "OutsideZoneStretch.csv"
    bad_ozs.write_text(
        "Video Name:,Outside Zone Stretch\r\n,Key Actions\r\nVideo #,Original ID\r\n1,InvalidID_1\r\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Malformed Original ID"):
        build_manifest(env["track_root"], env["ka_root"], env["summary"])


def test_manifest_generation_rejects_duplicate_source_identity(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    bad_ozs = env["ka_root"] / "OutsideZoneStretch.csv"
    bad_ozs.write_text(
        "Video Name:,Outside Zone Stretch\r\n,Key Actions\r\nVideo #,Original ID\r\n"
        "1,OutsideZoneStretch_1\r\n2,OutsideZoneStretch_1\r\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Duplicate OutsideZoneStretch source ID"):
        build_manifest(env["track_root"], env["ka_root"], env["summary"])


def test_stale_qb_new_id_reported_as_warning(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    res = validate_manifest(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )
    assert any("Stale New ID detected in QB_ZoneRead.csv row 1" in w for w in res.warnings)


def test_unmapped_source_causes_blocked_and_fails_validation(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    res = validate_manifest(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )
    assert res.blocked_count == 1
    assert not res.ready


def test_apply_refuses_to_run_when_blocked_exists(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    with pytest.raises(RuntimeError, match="1 clips are marked as BLOCKED"):
        apply_migration(
            rows,
            tracking_root=env["track_root"],
            dataset_summary=env["summary"],
            plays_path=env["plays"],
            key_actions_root=env["ka_root"],
        )


def test_dry_run_does_not_modify_filesystem_or_summary(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = [r for r in build_manifest(env["track_root"], env["ka_root"], env["summary"]) if r.status != STATUS_BLOCKED]
    summary_before = env["summary"].read_bytes()

    res = validate_manifest(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )
    assert res.ready
    assert env["summary"].read_bytes() == summary_before
    assert (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_1_cvat_mot.zip").exists()
    assert not (env["track_root"] / "OutsideZoneRead").exists()


def test_apply_moves_tracking_zips_and_updates_summary(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_4_cvat_mot.zip").unlink()
    _create_minimal_summary(
        env["summary"],
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "InsideZoneRead_1.mp4",
        ],
        had_bom=True,
    )

    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    assert all(r.status != STATUS_BLOCKED for r in rows)

    apply_migration(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )

    # Check OutsideZoneRead tracking folder created and populated
    ozr_dir = env["track_root"] / "OutsideZoneRead"
    assert ozr_dir.is_dir()
    assert (ozr_dir / "OutsideZoneRead_1_cvat_mot.zip").read_bytes() == b"zip-ozs-3"
    assert (ozr_dir / "OutsideZoneRead_2_cvat_mot.zip").read_bytes() == b"zip-qb-1"

    # Check InsideZoneRead tracking populated
    izr_dir = env["track_root"] / "InsideZoneRead"
    assert (izr_dir / "InsideZoneRead_236_cvat_mot.zip").read_bytes() == b"zip-qb-3"

    # Check holdout remains in QB_ZoneRead
    assert (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_17_cvat_mot.zip").read_bytes() == b"zip-qb-17"
    assert not (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_1_cvat_mot.zip").exists()
    assert not (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_3_cvat_mot.zip").exists()

    # Check DatasetSummary surgical update
    raw_summary = env["summary"].read_bytes()
    assert raw_summary.startswith(b"\xef\xbb\xbf")  # BOM preserved
    summary_text = raw_summary.decode("utf-8-sig")
    assert "OutsideZoneRead_1.mp4" in summary_text
    assert "OutsideZoneRead_2.mp4" in summary_text
    assert "InsideZoneRead_236.mp4" in summary_text
    assert "QB_ZoneRead_17.mp4" in summary_text
    assert "OutsideZoneStretch_3.mp4" not in summary_text
    assert "QB_ZoneRead_1.mp4" not in summary_text
    assert "QB_ZoneRead_3.mp4" not in summary_text


def test_destination_collision_blocks_migration(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_4_cvat_mot.zip").unlink()
    _create_minimal_summary(
        env["summary"],
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "InsideZoneRead_1.mp4",
        ],
    )
    # Simulate pre-existing collision at destination
    ozr_dir = env["track_root"] / "OutsideZoneRead"
    ozr_dir.mkdir()
    (ozr_dir / "OutsideZoneRead_1_cvat_mot.zip").write_bytes(b"collision")

    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    res = validate_manifest(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )
    assert not res.ready
    assert res.dest_collisions == 1
    assert any("Destination collision" in err for err in res.errors)


def test_missing_summary_row_blocks_migration(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_4_cvat_mot.zip").unlink()
    # Write summary missing QB_ZoneRead_1.mp4
    _create_minimal_summary(
        env["summary"],
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "InsideZoneRead_1.mp4",
        ],
    )

    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    res = validate_manifest(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )
    assert not res.ready
    assert any("QB_ZoneRead_1.mp4 not found in DatasetSummary.csv" in err for err in res.errors)


def test_duplicate_summary_row_blocks_migration(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_4_cvat_mot.zip").unlink()
    _create_minimal_summary(
        env["summary"],
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_1.mp4",  # Duplicate!
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "InsideZoneRead_1.mp4",
        ],
    )

    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    res = validate_manifest(
        rows,
        tracking_root=env["track_root"],
        dataset_summary=env["summary"],
        plays_path=env["plays"],
        key_actions_root=env["ka_root"],
    )
    assert not res.ready
    assert any("Duplicate output_file identities in DatasetSummary" in err for err in res.errors)


def test_rollback_on_apply_failure(tmp_path, monkeypatch):
    env = _setup_synthetic_dataset(tmp_path)
    (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_4_cvat_mot.zip").unlink()
    _create_minimal_summary(
        env["summary"],
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "InsideZoneRead_1.mp4",
        ],
    )

    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    summary_before = env["summary"].read_bytes()
    ozs_3_before = (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_3_cvat_mot.zip").read_bytes()

    # Induce an error during DatasetSummary atomic replace
    real_replace = os.replace

    def mock_replace(src, dest):
        if str(dest) == str(env["summary"]):
            raise IOError("Simulated disk error replacing DatasetSummary")
        return real_replace(src, dest)

    monkeypatch.setattr(os, "replace", mock_replace)

    with pytest.raises(IOError, match="Simulated disk error"):
        apply_migration(
            rows,
            tracking_root=env["track_root"],
            dataset_summary=env["summary"],
            plays_path=env["plays"],
            key_actions_root=env["ka_root"],
        )

    # Verify tracking file was restored to original location
    assert (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_3_cvat_mot.zip").read_bytes() == ozs_3_before
    assert not (env["track_root"] / "OutsideZoneRead" / "OutsideZoneRead_1_cvat_mot.zip").exists()
    # Verify DatasetSummary was untouched
    assert env["summary"].read_bytes() == summary_before


def test_committed_manifest_against_live_repository():
    manifest_path = Path("data/migrations/outside_zone_qb_zone_read_migration_manifest.csv")
    assert manifest_path.is_file(), "Committed manifest file must exist in data/migrations/"

    rows = load_manifest(manifest_path)
    assert len(rows) == 545

    res = validate_manifest(
        rows,
        tracking_root="data/tracking",
        dataset_summary="data/DatasetSummary.csv",
        plays_path="data/plays.json",
        key_actions_root="data/key_actions",
        require_production_counts=True,
    )

    # 1. Check exact counts
    assert res.ozs_to_ozs == 228
    assert res.ozs_to_ozr == 118
    assert res.qb_to_izr == 146
    assert res.qb_to_ozr == 46
    assert res.qb_holdouts == 6
    assert res.migrate_count == 538
    assert res.holdout_count == 6
    assert res.blocked_count == 1
    assert res.ozs_blocked == 1
    assert res.qb_blocked == 0
    assert res.dest_collisions == 0
    assert res.summary_mismatches == 0

    # 2. Check blocked row is specifically OutsideZoneStretch_213
    blocked_rows = [r for r in rows if r.status == STATUS_BLOCKED]
    assert len(blocked_rows) == 1
    assert blocked_rows[0].source_clip_name == "OutsideZoneStretch_213"

    # 3. Check holdout clips
    holdout_rows = [r for r in rows if r.status == STATUS_HOLDOUT]
    assert len(holdout_rows) == 6
    assert {r.source_video_id for r in holdout_rows} == {17, 18, 41, 42, 131, 132}

    # 4. Status must be FAILED because of the BLOCKED row
    assert not res.ready
