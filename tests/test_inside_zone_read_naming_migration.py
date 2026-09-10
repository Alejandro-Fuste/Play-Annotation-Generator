import os
from pathlib import Path
import pytest

from play_annotation_generator.inside_zone_read_naming_migration import (
    ClipPair,
    MigrationPlan,
    apply_plan,
    build_plan,
    _render_updated_summary,
)


def _write_summary(
    path: Path,
    outputs: list[str],
    had_bom: bool = False,
    newline: str = "\r\n",
    custom_rows: list[str] | None = None,
) -> None:
    header = "clip number,start_time,end_time,play,view,fromYouTube,input_file,output_file,name,file extension,date,"
    if custom_rows is not None:
        body = newline.join(custom_rows) + newline
    else:
        rows = [
            f"{i},1:00:00,1:01:00,Run,E,FALSE,InsideZoneOpenFormations.mp4,{out},InsideZoneOpenFormations_,.mp4,2026-03-18,"
            for i, out in enumerate(outputs, start=1)
        ]
        body = newline.join(rows) + newline
    full_text = header + newline + body
    raw = full_text.encode("utf-8")
    if had_bom:
        raw = b"\xef\xbb\xbf" + raw
    path.write_bytes(raw)


def _fixture(
    tmp_path: Path,
    ids: tuple[int, ...] = (1, 2),
    had_bom: bool = False,
    newline: str = "\r\n",
):
    tracking_root = tmp_path / "tracking"
    source_folder = tracking_root / "InsideZone"
    source_folder.mkdir(parents=True)
    for clip_id in ids:
        (source_folder / f"InsideZoneOpenFormations_{clip_id}_cvat_mot.zip").write_bytes(
            f"zip-content-{clip_id}".encode()
        )

    key_root = tmp_path / "key_actions"
    key_root.mkdir()
    key_file = key_root / "InsideZone.csv"
    key_file.write_bytes(b"Video Name:,InsideZone_\r\n1,Play_Run,Result_Tackle\r\n")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(
        summary,
        [f"InsideZoneOpenFormations_{clip_id}.mp4" for clip_id in ids],
        had_bom=had_bom,
        newline=newline,
    )
    return tracking_root, key_root, summary


def test_build_plan_pairs_tracking_and_summary_ids(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 3))
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert [p.clip_id for p in plan.pairs] == [1, 3]
    assert [p.tracking_target.name for p in plan.pairs] == [
        "InsideZoneRead_1_cvat_mot.zip",
        "InsideZoneRead_3_cvat_mot.zip",
    ]
    assert [p.summary_target for p in plan.pairs] == [
        "InsideZoneRead_1.mp4",
        "InsideZoneRead_3.mp4",
    ]
    assert plan.key_actions_source == key_root / "InsideZone.csv"
    assert plan.key_actions_target == key_root / "InsideZoneRead.csv"


def test_non_contiguous_ids_are_valid(tmp_path):
    # IDs containing gap: (1, 134, 136, 235) - 135 missing
    ids = (1, 134, 136, 235)
    tracking_root, key_root, summary = _fixture(tmp_path, ids)
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert [p.clip_id for p in plan.pairs] == [1, 134, 136, 235]


def test_dry_run_planning_modifies_nothing(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    summary_before = summary.read_bytes()
    key_before = (key_root / "InsideZone.csv").read_bytes()
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert summary.read_bytes() == summary_before
    assert (tracking_root / "InsideZone").is_dir()
    assert not (tracking_root / "InsideZoneRead").exists()
    assert (key_root / "InsideZone.csv").read_bytes() == key_before
    assert not (key_root / "InsideZoneRead.csv").exists()


def test_apply_removes_legacy_folder_creates_canonical_and_renames(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    key_path = key_root / "InsideZone.csv"
    key_before = key_path.read_bytes()
    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)

    # Legacy folder removed
    assert not (tracking_root / "InsideZone").exists()
    # Canonical folder created
    assert (tracking_root / "InsideZoneRead").is_dir()
    # Tracking ZIP bytes preserved and renamed
    assert (tracking_root / "InsideZoneRead" / "InsideZoneRead_1_cvat_mot.zip").read_bytes() == b"zip-content-1"
    assert (tracking_root / "InsideZoneRead" / "InsideZoneRead_2_cvat_mot.zip").read_bytes() == b"zip-content-2"
    # Key actions renamed and bytes identical
    assert not key_path.exists()
    canonical_key = key_root / "InsideZoneRead.csv"
    assert canonical_key.exists()
    assert canonical_key.read_bytes() == key_before
    # DatasetSummary updated
    text = summary.read_text(encoding="utf-8")
    assert "InsideZoneRead_1.mp4" in text and "InsideZoneRead_2.mp4" in text
    assert "InsideZoneOpenFormations_1.mp4" not in text
    assert "InsideZoneOpenFormations_2.mp4" not in text


def test_canonical_tracking_folder_collision_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "InsideZoneRead").mkdir()
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical tracking folder already exists" in error for error in plan.errors)


def test_missing_legacy_key_actions_file_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (key_root / "InsideZone.csv").unlink()
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("legacy Key Actions file not found" in error for error in plan.errors)


def test_existing_canonical_key_actions_file_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (key_root / "InsideZoneRead.csv").write_bytes(b"existing")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical Key Actions target already exists" in error for error in plan.errors)


def test_tracking_and_summary_id_mismatch_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    # Summary only has ID 1
    _write_summary(summary, ["InsideZoneOpenFormations_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("missing from DatasetSummary" in error for error in plan.errors)


def test_duplicate_summary_legacy_id_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    _write_summary(
        summary,
        ["InsideZoneOpenFormations_1.mp4", "InsideZoneOpenFormations_1.mp4"],
    )
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("duplicate legacy DatasetSummary ID 1" in error for error in plan.errors)


def test_duplicate_tracking_id_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    # Create duplicate tracking file with same ID via leading zeros or alternative
    (tracking_root / "InsideZone" / "InsideZoneOpenFormations_01_cvat_mot.zip").write_bytes(b"dup")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("duplicate legacy tracking ID 1" in error for error in plan.errors)


def test_summary_target_collision_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    _write_summary(
        summary,
        ["InsideZoneOpenFormations_1.mp4", "InsideZoneRead_1.mp4"],
    )
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)


def test_unexpected_tracking_entry_blocks_migration(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "InsideZone" / "random.txt").write_text("unexpected", encoding="utf-8")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("unexpected entries" in error for error in plan.errors)


def test_dataset_summary_bom_preserved(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,), had_bom=True)
    assert summary.read_bytes().startswith(b"\xef\xbb\xbf")
    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)
    raw_after = summary.read_bytes()
    assert raw_after.startswith(b"\xef\xbb\xbf")


def test_dataset_summary_crlf_lf_behavior_preserved(tmp_path):
    # Test CRLF
    tracking_root, key_root, summary_crlf = _fixture(tmp_path, (1,), newline="\r\n")
    plan = build_plan(tracking_root, summary_crlf, key_root)
    apply_plan(plan, summary_crlf)
    content_crlf = summary_crlf.read_bytes().decode("utf-8")
    assert "\r\n" in content_crlf
    assert "\n" not in content_crlf.replace("\r\n", "")

    # Test LF
    tracking_root_lf = tmp_path / "tracking_lf"
    (tracking_root_lf / "InsideZone").mkdir(parents=True)
    (tracking_root_lf / "InsideZone" / "InsideZoneOpenFormations_1_cvat_mot.zip").write_bytes(b"z")
    key_root_lf = tmp_path / "key_lf"
    key_root_lf.mkdir()
    (key_root_lf / "InsideZone.csv").write_bytes(b"k")
    summary_lf = tmp_path / "DatasetSummary_lf.csv"
    _write_summary(summary_lf, ["InsideZoneOpenFormations_1.mp4"], newline="\n")

    plan_lf = build_plan(tracking_root_lf, summary_lf, key_root_lf)
    apply_plan(plan_lf, summary_lf)
    raw_lf = summary_lf.read_bytes()
    assert b"\r" not in raw_lf


def test_apply_does_not_modify_unrelated_dataset_summary_fields(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    custom_row = "10,1:04:06,1:04:15,Run,E,FALSE,InsideZoneOpenFormations.mp4,InsideZoneOpenFormations_1.mp4,InsideZoneOpenFormations_,.mp4,2026-03-18,"
    _write_summary(summary, [], custom_rows=[custom_row])

    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)

    lines = summary.read_text(encoding="utf-8").splitlines()
    data_line = lines[1]
    expected = "10,1:04:06,1:04:15,Run,E,FALSE,InsideZoneOpenFormations.mp4,InsideZoneRead_1.mp4,InsideZoneOpenFormations_,.mp4,2026-03-18,"
    assert data_line == expected
    # Ensure input_file, name, etc. were not touched
    assert "InsideZoneOpenFormations.mp4" in data_line
    assert "InsideZoneOpenFormations_" in data_line
    assert "Run" in data_line
    assert "1:04:06" in data_line
    assert "2026-03-18" in data_line


def test_key_actions_byte_identical_before_and_after_apply(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    raw_key_content = b"Video Name:,InsideZone_\r\n1,Play_Run,Result_Tackle,10,20\r\n\xff\xfe random bytes\r\n"
    (key_root / "InsideZone.csv").write_bytes(raw_key_content)

    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)

    canonical_key = key_root / "InsideZoneRead.csv"
    assert canonical_key.read_bytes() == raw_key_content


def test_expected_count_check_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    plan = build_plan(tracking_root, summary, key_root, expected_count=234)
    assert not plan.ready
    assert any("expected exactly 234 paired clips, found 2" in error for error in plan.errors)


def test_rollback_restores_filesystem_on_failure(tmp_path, monkeypatch):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    key_before = (key_root / "InsideZone.csv").read_bytes()
    summary_before = summary.read_bytes()
    zip1_before = (tracking_root / "InsideZone" / "InsideZoneOpenFormations_1_cvat_mot.zip").read_bytes()

    plan = build_plan(tracking_root, summary, key_root)

    # Induce failure during atomic replace of DatasetSummary (after folder & key actions rename)
    real_replace = os.replace
    def fake_replace(src, dst):
        if Path(dst) == summary.resolve():
            raise OSError("Simulated disk error during DatasetSummary replace")
        return real_replace(src, dst)

    monkeypatch.setattr(os, "replace", fake_replace)

    with pytest.raises(OSError, match="Simulated disk error"):
        apply_plan(plan, summary)

    # Verify complete rollback
    assert (tracking_root / "InsideZone").is_dir()
    assert (tracking_root / "InsideZone" / "InsideZoneOpenFormations_1_cvat_mot.zip").read_bytes() == zip1_before
    assert (tracking_root / "InsideZone" / "InsideZoneOpenFormations_2_cvat_mot.zip").exists()
    assert not (tracking_root / "InsideZoneRead").exists()
    assert (key_root / "InsideZone.csv").read_bytes() == key_before
    assert not (key_root / "InsideZoneRead.csv").exists()
    assert summary.read_bytes() == summary_before
