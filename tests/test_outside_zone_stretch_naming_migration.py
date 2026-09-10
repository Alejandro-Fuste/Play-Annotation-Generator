from pathlib import Path

from play_annotation_generator.outside_zone_stretch_naming_migration import apply_plan, build_plan


def _write_summary(path: Path, outputs: list[str]) -> None:
    path.write_text(
        "output_file,other\r\n" + "".join(f"{value},x\r\n" for value in outputs),
        encoding="utf-8",
    )


def _fixture(tmp_path: Path, ids: tuple[int, ...] = (1, 2)):
    tracking_root = tmp_path / "tracking"
    source_folder = tracking_root / "OutsideZone"
    source_folder.mkdir(parents=True)
    for clip_id in ids:
        (source_folder / f"OutsideZoneClosed_{clip_id}_cvat_mot.zip").write_bytes(f"zip-{clip_id}".encode())

    key_root = tmp_path / "key_actions"
    key_root.mkdir()
    (key_root / "OutsideZoneStretch.csv").write_text("Video Name:,Outside Zone Stretch\r\n", encoding="utf-8")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(summary, [f"OutsideZoneClosed_{clip_id}.mp4" for clip_id in ids])
    return tracking_root, key_root, summary


def test_build_plan_pairs_tracking_and_summary_ids(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 3))
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert [p.clip_id for p in plan.pairs] == [1, 3]
    assert [p.tracking_target.name for p in plan.pairs] == [
        "OutsideZoneStretch_1_cvat_mot.zip",
        "OutsideZoneStretch_3_cvat_mot.zip",
    ]
    assert [p.summary_target for p in plan.pairs] == [
        "OutsideZoneStretch_1.mp4",
        "OutsideZoneStretch_3.mp4",
    ]


def test_dry_run_planning_does_not_modify_files(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    before = summary.read_bytes()
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert summary.read_bytes() == before
    assert (tracking_root / "OutsideZone").is_dir()
    assert not (tracking_root / "OutsideZoneStretch").exists()
    assert (key_root / "OutsideZoneStretch.csv").exists()


def test_apply_updates_tracking_and_summary_but_not_key_actions(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    key_path = key_root / "OutsideZoneStretch.csv"
    key_before = key_path.read_bytes()
    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)

    assert not (tracking_root / "OutsideZone").exists()
    assert (tracking_root / "OutsideZoneStretch" / "OutsideZoneStretch_1_cvat_mot.zip").read_bytes() == b"zip-1"
    assert (tracking_root / "OutsideZoneStretch" / "OutsideZoneStretch_2_cvat_mot.zip").read_bytes() == b"zip-2"
    assert key_path.read_bytes() == key_before
    text = summary.read_text(encoding="utf-8")
    assert "OutsideZoneStretch_1.mp4" in text and "OutsideZoneStretch_2.mp4" in text
    assert "OutsideZoneClosed_" not in text


def test_tracking_folder_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "OutsideZoneStretch").mkdir()
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical tracking folder already exists" in error for error in plan.errors)


def test_missing_canonical_key_actions_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (key_root / "OutsideZoneStretch.csv").unlink()
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical Key Actions file not found" in error for error in plan.errors)


def test_id_mismatch_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    _write_summary(summary, ["OutsideZoneClosed_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("missing from DatasetSummary" in error for error in plan.errors)


def test_summary_target_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    _write_summary(summary, ["OutsideZoneClosed_1.mp4", "OutsideZoneStretch_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)


def test_unexpected_tracking_entry_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "OutsideZone" / "notes.txt").write_text("unexpected", encoding="utf-8")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("unexpected entries" in error for error in plan.errors)
