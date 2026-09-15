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
    _parse_qb_new_id,
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
            "InsideZoneStretch",
            "OutsideZoneRead",
            "OutsideZoneStretch",
            "SplitZone",
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
    tmp_path.mkdir(parents=True, exist_ok=True)
    track_root = tmp_path / "tracking"
    ka_root = tmp_path / "key_actions"
    track_root.mkdir(parents=True, exist_ok=True)
    ka_root.mkdir(parents=True, exist_ok=True)

    # Tracking folders: OutsideZoneStretch, QB_ZoneRead, SplitZone, InsideZoneRead
    ozs_track = track_root / "OutsideZoneStretch"
    ozs_track.mkdir(parents=True, exist_ok=True)
    qb_track = track_root / "QB_ZoneRead"
    qb_track.mkdir(parents=True, exist_ok=True)
    split_track = track_root / "SplitZone"
    split_track.mkdir(parents=True, exist_ok=True)
    izr_track = track_root / "InsideZoneRead"
    izr_track.mkdir(parents=True, exist_ok=True)

    # OZS source zips: 1, 2, 3, 4, 5
    for i in (1, 2, 3, 4, 5):
        (ozs_track / f"OutsideZoneStretch_{i}_cvat_mot.zip").write_bytes(f"zip-ozs-{i}".encode())

    # QB source zips: 1, 3, 17
    for i in (1, 3, 17):
        (qb_track / f"QB_ZoneRead_{i}_cvat_mot.zip").write_bytes(f"zip-qb-{i}".encode())

    # Pre-existing SplitZone zip: 1
    (split_track / "SplitZone_1_cvat_mot.zip").write_bytes(b"zip-split-1")

    # Pre-existing IZR zip: 1
    (izr_track / "InsideZoneRead_1_cvat_mot.zip").write_bytes(b"zip-izr-1")

    # Key Actions:
    # OutsideZoneStretch.csv: 1 row (dest 1 <- orig 1)
    ozs_ka = ka_root / "OutsideZoneStretch.csv"
    ozs_ka.write_text(
        "Video Name:,Outside Zone Stretch\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,OL,Zone Block,Snap Receive,Press Edge,Read Edge Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,Original ID\r\n"
        '1,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,OutsideZoneStretch_1\r\n',
        encoding="utf-8",
    )

    # OutsideZoneRead.csv: 2 rows (dest 1 <- OZS 2, dest 2 <- QB 1)
    ozr_ka = ka_root / "OutsideZoneRead.csv"
    ozr_ka.write_text(
        "Video Name:,Outside Zone Read\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,OL,Zone Block,Snap Receive,Press Edge,Read Edge Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,Original ID\r\n"
        '1,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,OutsideZoneStretch_2\r\n'
        '2,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,OOB,QB_ZoneRead_1\r\n',
        encoding="utf-8",
    )

    # SplitZone.csv: 1 pre-existing row + 1 migrated OZS row (dest 271 <- OZS 3)
    split_ka = ka_root / "SplitZone.csv"
    split_ka.write_text(
        "Video Name:,Split Zone\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Split Block,Snap Receive,Handoff,Ball Carry,OL,Press Edge,Read Edge Defender,Block Second Level,End of OL Block,End of Play,Original ID\r\n"
        '1,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,Tac,SplitZone_1\r\n'
        '271,"0,ALL",-,-,-,-,-,-,-,-,-,-,-,TD,OutsideZoneStretch_3\r\n',
        encoding="utf-8",
    )

    # InsideZoneStretch.csv: 1 row (dest 1 <- OZS 5)
    izs_ka = ka_root / "InsideZoneStretch.csv"
    izs_ka.write_text(
        "Video Name:,Inside Zone Stretch\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,OL,Ball Snap,Zone Block,Snap Receive,Press Interior Gap,Handoff,Ball Carry,Block Second Level,End of Play,Original ID\r\n"
        '1,"0,ALL",-,-,-,-,-,-,-,-,Tac,OutsideZoneStretch_5\r\n',
        encoding="utf-8",
    )

    # QB_ZoneRead.csv: 3 rows using single New ID column format
    qb_ka = ka_root / "QB_ZoneRead.csv"
    qb_ka.write_text(
        "Video Name:,QB Zone Read\r\n"
        ",Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Snap Receive,Read Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,New ID\r\n"
        '1,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,OutsideZoneRead_2\r\n'
        '3,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,InsideZoneRead_236\r\n'
        '17,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,Counter_-\r\n',
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
            "OutsideZoneStretch_5.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "SplitZone_1.mp4",
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


def test_parse_qb_new_id_valid_and_invalid():
    # Valid
    assert _parse_qb_new_id("OutsideZoneRead_97") == ("OutsideZoneRead", 97)
    assert _parse_qb_new_id("InsideZoneRead_236") == ("InsideZoneRead", 236)
    assert _parse_qb_new_id("Counter_-") == ("Counter", None)

    # Invalid
    invalid_cases = [
        "OutsideZoneRead",
        "OutsideZoneRead_",
        "OutsideZoneRead_abc",
        "InsideZoneRead_-",
        "Counter_12",
        "QB_ZoneRead_97",
        "-",
        "",
        "   ",
        "SplitZone_10",
    ]
    for case in invalid_cases:
        with pytest.raises(ValueError, match="Malformed QB New ID"):
            _parse_qb_new_id(case)


def test_manifest_generation_four_way_mapping(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])

    assert len(rows) == 8  # OZS 1,2,3,4,5 + QB 1,3,17

    # 1. OutsideZoneStretch -> OutsideZoneStretch
    ozs_1 = next(r for r in rows if r.source_clip_name == "OutsideZoneStretch_1")
    assert ozs_1.status == STATUS_MIGRATE
    assert ozs_1.destination_play == "OutsideZoneStretch"
    assert ozs_1.destination_video_id == 1
    assert ozs_1.destination_clip_name == "OutsideZoneStretch_1"

    # 2. OutsideZoneStretch -> OutsideZoneRead
    ozs_2 = next(r for r in rows if r.source_clip_name == "OutsideZoneStretch_2")
    assert ozs_2.status == STATUS_MIGRATE
    assert ozs_2.destination_play == "OutsideZoneRead"
    assert ozs_2.destination_video_id == 1
    assert ozs_2.destination_clip_name == "OutsideZoneRead_1"

    # 3. OutsideZoneStretch -> SplitZone
    ozs_3 = next(r for r in rows if r.source_clip_name == "OutsideZoneStretch_3")
    assert ozs_3.status == STATUS_MIGRATE
    assert ozs_3.destination_play == "SplitZone"
    assert ozs_3.destination_video_id == 271
    assert ozs_3.destination_clip_name == "SplitZone_271"

    # 4. OutsideZoneStretch -> InsideZoneStretch
    ozs_5 = next(r for r in rows if r.source_clip_name == "OutsideZoneStretch_5")
    assert ozs_5.status == STATUS_MIGRATE
    assert ozs_5.destination_play == "InsideZoneStretch"
    assert ozs_5.destination_video_id == 1
    assert ozs_5.destination_clip_name == "InsideZoneStretch_1"

    # 5. OutsideZoneStretch unmapped source (OZS 4)
    ozs_4 = next(r for r in rows if r.source_clip_name == "OutsideZoneStretch_4")
    assert ozs_4.status == STATUS_BLOCKED
    assert ozs_4.destination_play == ""

    # 6. QB Holdout
    qb_17 = next(r for r in rows if r.source_clip_name == "QB_ZoneRead_17")
    assert qb_17.status == STATUS_HOLDOUT
    assert qb_17.destination_play == ""
    assert qb_17.destination_video_id is None
    assert qb_17.destination_clip_name == "QB_ZoneRead_17"

    # 7. QB -> OutsideZoneRead
    qb_1 = next(r for r in rows if r.source_clip_name == "QB_ZoneRead_1")
    assert qb_1.status == STATUS_MIGRATE
    assert qb_1.destination_play == "OutsideZoneRead"
    assert qb_1.destination_video_id == 2
    assert qb_1.destination_clip_name == "OutsideZoneRead_2"

    # 8. QB -> InsideZoneRead
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


def test_manifest_generation_rejects_duplicate_source_across_destination_csvs(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    # OutsideZoneStretch_1 is already in OutsideZoneStretch.csv.
    # Put OutsideZoneStretch_1 also into SplitZone.csv.
    split_ka = env["ka_root"] / "SplitZone.csv"
    split_ka.write_text(
        "Video Name:,Split Zone\r\n,Key Actions\r\nVideo #,Original ID\r\n"
        "1,SplitZone_1\r\n271,OutsideZoneStretch_1\r\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Duplicate OutsideZoneStretch source ID"):
        build_manifest(env["track_root"], env["ka_root"], env["summary"])


def test_manifest_generation_rejects_duplicate_source_identity_in_same_file(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    bad_ozs = env["ka_root"] / "OutsideZoneStretch.csv"
    bad_ozs.write_text(
        "Video Name:,Outside Zone Stretch\r\n,Key Actions\r\nVideo #,Original ID\r\n"
        "1,OutsideZoneStretch_1\r\n2,OutsideZoneStretch_1\r\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Duplicate OutsideZoneStretch source ID"):
        build_manifest(env["track_root"], env["ka_root"], env["summary"])


def test_qb_destination_mismatch_against_canonical_csv_causes_error(tmp_path):
    # Case 1: OutsideZoneRead destination mismatch
    env = _setup_synthetic_dataset(tmp_path / "case1")
    qb_ka = env["ka_root"] / "QB_ZoneRead.csv"
    qb_ka.write_text(
        "Video Name:,QB Zone Read\r\n,Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Snap Receive,Read Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,New ID\r\n"
        '1,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,OutsideZoneRead_99\r\n'
        '3,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,InsideZoneRead_236\r\n'
        '17,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,Counter_-\r\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="does not match canonical OutsideZoneRead.csv destination"):
        build_manifest(env["track_root"], env["ka_root"], env["summary"])

    # Case 2: InsideZoneRead destination not found in InsideZoneRead.csv
    env2 = _setup_synthetic_dataset(tmp_path / "case2")
    qb_ka2 = env2["ka_root"] / "QB_ZoneRead.csv"
    qb_ka2.write_text(
        "Video Name:,QB Zone Read\r\n,Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Snap Receive,Read Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,New ID\r\n"
        '1,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,OutsideZoneRead_2\r\n'
        '3,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,InsideZoneRead_999\r\n'
        '17,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,Counter_-\r\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="destination InsideZoneRead_999 not found in InsideZoneRead.csv"):
        build_manifest(env2["track_root"], env2["ka_root"], env2["summary"])


def test_holdout_safety_and_exact_identities(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    # Attempt unauthorized holdout: row 1 (not in EXPECTED_QB_HOLDOUTS) with Counter_-
    qb_ka = env["ka_root"] / "QB_ZoneRead.csv"
    qb_ka.write_text(
        "Video Name:,QB Zone Read\r\n,Key Actions\r\n"
        "Video #,Pre Snap,Ball Snap,Zone Block,Snap Receive,Read Defender,Keep,Handoff,Ball Carry,Block Second Level,End of OL Block,End of Play,New ID\r\n"
        '1,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,Counter_-\r\n'
        '3,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,InsideZoneRead_236\r\n'
        '17,"0,ALL",1,2,3,4,5,-,6,7,70,OOB,Counter_-\r\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Unexpected QB holdout ID 1"):
        build_manifest(env["track_root"], env["ka_root"], env["summary"])


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
    assert not (env["track_root"] / "InsideZoneStretch").exists()


def test_apply_moves_tracking_zips_and_updates_summary(tmp_path):
    env = _setup_synthetic_dataset(tmp_path)
    # Remove OZS 4 (unmapped clip) so manifest has no BLOCKED clips
    (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_4_cvat_mot.zip").unlink()
    _create_minimal_summary(
        env["summary"],
        [
            "OutsideZoneStretch_1.mp4",
            "OutsideZoneStretch_2.mp4",
            "OutsideZoneStretch_3.mp4",
            "OutsideZoneStretch_5.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "SplitZone_1.mp4",
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
    assert (ozr_dir / "OutsideZoneRead_1_cvat_mot.zip").read_bytes() == b"zip-ozs-2"
    assert (ozr_dir / "OutsideZoneRead_2_cvat_mot.zip").read_bytes() == b"zip-qb-1"

    # Check InsideZoneStretch tracking folder created and populated
    izs_dir = env["track_root"] / "InsideZoneStretch"
    assert izs_dir.is_dir()
    assert (izs_dir / "InsideZoneStretch_1_cvat_mot.zip").read_bytes() == b"zip-ozs-5"

    # Check SplitZone tracking populated
    split_dir = env["track_root"] / "SplitZone"
    assert (split_dir / "SplitZone_1_cvat_mot.zip").read_bytes() == b"zip-split-1"
    assert (split_dir / "SplitZone_271_cvat_mot.zip").read_bytes() == b"zip-ozs-3"

    # Check InsideZoneRead tracking populated
    izr_dir = env["track_root"] / "InsideZoneRead"
    assert (izr_dir / "InsideZoneRead_1_cvat_mot.zip").read_bytes() == b"zip-izr-1"
    assert (izr_dir / "InsideZoneRead_236_cvat_mot.zip").read_bytes() == b"zip-qb-3"

    # Check holdout remains in QB_ZoneRead
    assert (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_17_cvat_mot.zip").read_bytes() == b"zip-qb-17"
    assert not (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_1_cvat_mot.zip").exists()
    assert not (env["track_root"] / "QB_ZoneRead" / "QB_ZoneRead_3_cvat_mot.zip").exists()

    # Check OutsideZoneStretch_1 remains in OutsideZoneStretch
    assert (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_1_cvat_mot.zip").read_bytes() == b"zip-ozs-1"

    # Check DatasetSummary surgical update
    raw_summary = env["summary"].read_bytes()
    assert raw_summary.startswith(b"\xef\xbb\xbf")  # BOM preserved
    summary_text = raw_summary.decode("utf-8-sig")
    assert "OutsideZoneStretch_1.mp4" in summary_text
    assert "OutsideZoneRead_1.mp4" in summary_text
    assert "OutsideZoneRead_2.mp4" in summary_text
    assert "SplitZone_271.mp4" in summary_text
    assert "InsideZoneStretch_1.mp4" in summary_text
    assert "InsideZoneRead_236.mp4" in summary_text
    assert "QB_ZoneRead_17.mp4" in summary_text
    assert "OutsideZoneStretch_2.mp4" not in summary_text
    assert "OutsideZoneStretch_3.mp4" not in summary_text
    assert "OutsideZoneStretch_5.mp4" not in summary_text
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
            "OutsideZoneStretch_5.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "SplitZone_1.mp4",
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
            "OutsideZoneStretch_5.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "SplitZone_1.mp4",
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
            "OutsideZoneStretch_5.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_1.mp4",  # Duplicate!
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "SplitZone_1.mp4",
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
            "OutsideZoneStretch_5.mp4",
            "QB_ZoneRead_1.mp4",
            "QB_ZoneRead_3.mp4",
            "QB_ZoneRead_17.mp4",
            "SplitZone_1.mp4",
            "InsideZoneRead_1.mp4",
        ],
    )

    rows = build_manifest(env["track_root"], env["ka_root"], env["summary"])
    summary_before = env["summary"].read_bytes()
    ozs_2_before = (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_2_cvat_mot.zip").read_bytes()

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
    assert (env["track_root"] / "OutsideZoneStretch" / "OutsideZoneStretch_2_cvat_mot.zip").read_bytes() == ozs_2_before
    assert not (env["track_root"] / "OutsideZoneRead" / "OutsideZoneRead_1_cvat_mot.zip").exists()
    # Verify DatasetSummary was untouched
    assert env["summary"].read_bytes() == summary_before


def test_outside_zone_read_mixed_provenance():
    ozr_file = Path("data/key_actions/OutsideZoneRead.csv")
    assert ozr_file.is_file()
    with ozr_file.open("r", encoding="utf-8-sig") as f:
        reader = list(csv.reader(f))
    headers = reader[2]
    orig_idx = headers.index("Original ID")
    ozs_prov = 0
    qb_prov = 0
    for row in reader[3:]:
        if not row or not row[0].strip():
            continue
        orig = row[orig_idx].strip()
        if orig.startswith("OutsideZoneStretch_"):
            ozs_prov += 1
        elif orig.startswith("QB_ZoneRead_"):
            qb_prov += 1

    assert ozs_prov == 96
    assert qb_prov == 46
    assert ozs_prov + qb_prov == 142


def test_strict_production_counts_rejects_alternate_197_48_counts():
    manifest_path = Path("data/migrations/outside_zone_qb_zone_read_migration_manifest.csv")
    assert manifest_path.is_file()
    rows = load_manifest(manifest_path)

    # Modify one row to simulate the 197 / 48 distribution (e.g. change one SplitZone clip to OutsideZoneStretch)
    modified_rows = []
    changed = False
    for r in rows:
        if not changed and r.source_play == "OutsideZoneStretch" and r.destination_play == "SplitZone":
            modified_rows.append(
                ManifestRow(
                    source_play=r.source_play,
                    source_video_id=r.source_video_id,
                    source_clip_name=r.source_clip_name,
                    destination_play="OutsideZoneStretch",
                    destination_video_id=999,
                    destination_clip_name="OutsideZoneStretch_999",
                    status=r.status,
                    source_key_actions_file=r.source_key_actions_file,
                    destination_key_actions_file="data/key_actions/OutsideZoneStretch.csv",
                    notes=r.notes,
                )
            )
            changed = True
        else:
            modified_rows.append(r)

    res = validate_manifest(
        modified_rows,
        tracking_root="data/tracking",
        dataset_summary="data/DatasetSummary.csv",
        plays_path="data/plays.json",
        key_actions_root="data/key_actions",
        require_production_counts=True,
    )
    assert not res.ready
    assert any("Expected exactly 196 OutsideZoneStretch -> OutsideZoneStretch clips, found 197" in e for e in res.errors)
    assert any("Expected exactly 49 OutsideZoneStretch -> SplitZone clips, found 48" in e for e in res.errors)


def test_canonical_manifest_generation_and_production_counts():
    rows = build_manifest(
        tracking_root="data/tracking",
        key_actions_root="data/key_actions",
        dataset_summary="data/DatasetSummary.csv",
    )
    res = validate_manifest(
        rows,
        tracking_root="data/tracking",
        dataset_summary="data/DatasetSummary.csv",
        plays_path="data/plays.json",
        key_actions_root="data/key_actions",
        require_production_counts=True,
    )

    # 1. Four-way Outside Zone strict counts
    assert res.ozs_to_ozs == 196
    assert res.ozs_to_ozr == 96
    assert res.ozs_to_split_zone == 49
    assert res.ozs_to_inside_zone_stretch == 6
    assert res.ozs_to_ozs + res.ozs_to_ozr + res.ozs_to_split_zone + res.ozs_to_inside_zone_stretch == 347

    # 2. Outside Zone source audit
    assert res.ozs_unique_sources == 347
    assert res.ozs_total_mappings == 347
    assert res.ozs_duplicates == 0
    assert res.ozs_missing == 0
    assert res.ozs_blocked == 0

    # 3. QB Zone Read counts
    assert res.qb_to_izr == 146
    assert res.qb_to_ozr == 46
    assert res.qb_holdouts == 6
    assert res.qb_blocked == 0

    # 4. Overall manifest counts
    assert res.migrate_count == 539
    assert res.holdout_count == 6
    assert res.blocked_count == 0
    assert len(res.rows) == 545

    # 5. Zero collisions, zero summary mismatches, zero warnings, ready status
    assert res.dest_collisions == 0
    assert res.summary_mismatches == 0
    assert len(res.warnings) == 0
    assert res.ready


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

    # Exact strict counts from canonical CSVs
    assert res.ozs_to_ozs == 196
    assert res.ozs_to_ozr == 96
    assert res.ozs_to_split_zone == 49
    assert res.ozs_to_inside_zone_stretch == 6
    assert res.ozs_unique_sources == 347
    assert res.ozs_total_mappings == 347
    assert res.ozs_duplicates == 0
    assert res.ozs_missing == 0
    assert res.ozs_blocked == 0

    assert res.qb_to_izr == 146
    assert res.qb_to_ozr == 46
    assert res.qb_holdouts == 6
    assert res.qb_blocked == 0

    assert res.migrate_count == 539
    assert res.holdout_count == 6
    assert res.blocked_count == 0
    assert res.dest_collisions == 0
    assert res.summary_mismatches == 0
    assert len(res.warnings) == 0

    # Check holdouts
    holdout_rows = [r for r in rows if r.status == STATUS_HOLDOUT]
    assert len(holdout_rows) == 6
    assert {r.source_video_id for r in holdout_rows} == {17, 18, 41, 42, 131, 132}

    # Status must be READY
    assert res.ready
