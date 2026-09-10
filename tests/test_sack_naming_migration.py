from pathlib import Path

from play_annotation_generator.sack_naming_migration import apply_plan, build_plan


def _write_summary(path: Path, outputs: list[str]) -> None:
    path.write_text(
        "output_file,other\r\n" + "".join(f"{value},x\r\n" for value in outputs),
        encoding="utf-8",
    )


def _fixture(tmp_path: Path, ids: tuple[int, ...] = (1, 2)):
    tracking_root = tmp_path / "tracking"
    source_folder = tracking_root / "Sacks"
    source_folder.mkdir(parents=True)
    for clip_id in ids:
        (source_folder / f"sack_{clip_id}_cvat_mot.zip").write_bytes(f"zip-{clip_id}".encode())

    key_root = tmp_path / "key_actions"
    key_root.mkdir()
    (key_root / "Sacks.csv").write_text("Video Name:,Sacks\r\n", encoding="utf-8")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(summary, [f"sack_{clip_id}.mp4" for clip_id in ids])
    return tracking_root, key_root, summary


def test_build_plan_pairs_tracking_and_summary_ids(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 3))
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert [p.clip_id for p in plan.pairs] == [1, 3]
    assert [p.tracking_target.name for p in plan.pairs] == [
        "Sack_1_cvat_mot.zip",
        "Sack_3_cvat_mot.zip",
    ]
    assert [p.summary_target for p in plan.pairs] == ["Sack_1.mp4", "Sack_3.mp4"]


def test_dry_run_planning_does_not_modify_files(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    before = summary.read_bytes()
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert summary.read_bytes() == before
    assert (tracking_root / "Sacks").is_dir()
    assert not (tracking_root / "Sack").exists()
    assert (key_root / "Sacks.csv").exists()
    assert not (key_root / "Sack.csv").exists()


def test_apply_updates_all_identity_surfaces(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)
    assert not (tracking_root / "Sacks").exists()
    assert (tracking_root / "Sack" / "Sack_1_cvat_mot.zip").read_bytes() == b"zip-1"
    assert (tracking_root / "Sack" / "Sack_2_cvat_mot.zip").read_bytes() == b"zip-2"
    assert not (key_root / "Sacks.csv").exists()
    assert (key_root / "Sack.csv").exists()
    text = summary.read_text(encoding="utf-8")
    assert "Sack_1.mp4" in text and "Sack_2.mp4" in text
    assert "sack_" not in text


def test_tracking_folder_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "Sack").mkdir()
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical tracking folder already exists" in error for error in plan.errors)


def test_key_actions_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (key_root / "Sack.csv").write_text("collision", encoding="utf-8")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical Key Actions target already exists" in error for error in plan.errors)


def test_id_mismatch_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    _write_summary(summary, ["sack_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("missing from DatasetSummary" in error for error in plan.errors)


def test_summary_target_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    _write_summary(summary, ["sack_1.mp4", "Sack_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)


def test_unexpected_tracking_entry_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "Sacks" / "notes.txt").write_text("unexpected", encoding="utf-8")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("unexpected entries" in error for error in plan.errors)
