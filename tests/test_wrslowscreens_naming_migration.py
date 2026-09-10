from __future__ import annotations

from pathlib import Path

from play_annotation_generator.wrslowscreens_naming_migration import (
    build_plan,
    apply_plan,
)


def _write_summary(path: Path, ids: list[int]) -> None:
    rows = ["clip number,output_file,name\n"]
    rows.extend(f"{clip_id},WRSlowScreens_{clip_id}.mp4,WRSlowScreens_\n" for clip_id in ids)
    path.write_text("".join(rows), encoding="utf-8")


def _make_fixture(tmp_path: Path, ids: list[int] = [1, 2]) -> tuple[Path, Path, Path]:
    tracking_root = tmp_path / "tracking"
    legacy = tracking_root / "WR_SlowScreens"
    legacy.mkdir(parents=True)
    for clip_id in ids:
        (legacy / f"WRSlowScreens_{clip_id}_cvat_mot.zip").write_bytes(
            f"zip-{clip_id}".encode()
        )

    dataset_summary = tmp_path / "DatasetSummary.csv"
    _write_summary(dataset_summary, ids)

    key_actions_root = tmp_path / "key_actions"
    key_actions_root.mkdir()
    (key_actions_root / "WR_SlowScreens.csv").write_text(
        "Video Name:,WR Slow Screen\nVideo #,Pre Snap\n1,0\n",
        encoding="utf-8",
    )
    return tracking_root, dataset_summary, key_actions_root


def test_build_plan_pairs_tracking_and_dataset_summary_ids(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path, [1, 3, 8])
    plan = build_plan(tracking_root, summary, key_actions)

    assert plan.ready
    assert [pair.clip_id for pair in plan.pairs] == [1, 3, 8]
    assert plan.source_folder.name == "WR_SlowScreens"
    assert plan.target_folder.name == "WRSlowScreens"
    assert plan.key_actions_source.name == "WR_SlowScreens.csv"
    assert plan.key_actions_target.name == "WRSlowScreens.csv"


def test_dry_run_planning_does_not_modify_files(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    before = summary.read_bytes()

    plan = build_plan(tracking_root, summary, key_actions)

    assert plan.ready
    assert (tracking_root / "WR_SlowScreens").is_dir()
    assert not (tracking_root / "WRSlowScreens").exists()
    assert (key_actions / "WR_SlowScreens.csv").is_file()
    assert not (key_actions / "WRSlowScreens.csv").exists()
    assert summary.read_bytes() == before


def test_apply_renames_folder_and_key_actions_without_rewriting_summary(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    before = summary.read_bytes()
    plan = build_plan(tracking_root, summary, key_actions)

    apply_plan(plan)

    assert not (tracking_root / "WR_SlowScreens").exists()
    assert (tracking_root / "WRSlowScreens").is_dir()
    assert (tracking_root / "WRSlowScreens" / "WRSlowScreens_1_cvat_mot.zip").is_file()
    assert not (key_actions / "WR_SlowScreens.csv").exists()
    assert (key_actions / "WRSlowScreens.csv").is_file()
    assert summary.read_bytes() == before


def test_tracking_target_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    (tracking_root / "WRSlowScreens").mkdir()

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("canonical tracking folder already exists" in error for error in plan.errors)


def test_key_actions_target_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    (key_actions / "WRSlowScreens.csv").write_text("collision", encoding="utf-8")

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("canonical Key Actions target already exists" in error for error in plan.errors)


def test_id_mismatch_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path, [1, 2])
    _write_summary(summary, [1, 3])

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("missing from DatasetSummary" in error for error in plan.errors)
    assert any("missing from tracking" in error for error in plan.errors)


def test_unexpected_tracking_entry_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    (tracking_root / "WR_SlowScreens" / "notes.txt").write_text("unexpected")

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("unexpected entries" in error for error in plan.errors)
