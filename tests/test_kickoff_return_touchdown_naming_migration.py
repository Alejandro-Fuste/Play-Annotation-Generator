from __future__ import annotations

from pathlib import Path

from play_annotation_generator.kickoff_return_touchdown_naming_migration import (
    apply_plan,
    build_plan,
)


def _write_summary(path: Path, ids: list[int]) -> None:
    rows = ["clip number,output_file,name\n"]
    rows.extend(
        f"{clip_id},KickoffReturnTD_{clip_id}.mp4,KickoffReturnTouchdown_\n"
        for clip_id in ids
    )
    path.write_text("".join(rows), encoding="utf-8")


def _make_fixture(tmp_path: Path, ids: list[int] = [1, 2]) -> tuple[Path, Path, Path]:
    tracking_root = tmp_path / "tracking"
    legacy_folder = tracking_root / "KickoffReturnTDs"
    legacy_folder.mkdir(parents=True)
    for clip_id in ids:
        (legacy_folder / f"KickoffReturnTD_{clip_id}_cvat_mot.zip").write_bytes(
            f"zip-{clip_id}".encode()
        )

    dataset_summary = tmp_path / "DatasetSummary.csv"
    _write_summary(dataset_summary, ids)

    key_actions_root = tmp_path / "key_actions"
    key_actions_root.mkdir()
    (key_actions_root / "KickoffReturnTD.csv").write_text(
        "Video Name:,Kickoff Return TD\nVideo #,Pre Snap\n1,0\n",
        encoding="utf-8",
    )
    return tracking_root, dataset_summary, key_actions_root


def test_build_plan_pairs_tracking_and_summary_ids(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path, [1, 3, 8])
    plan = build_plan(tracking_root, summary, key_actions)

    assert plan.ready
    assert [pair.clip_id for pair in plan.pairs] == [1, 3, 8]
    assert plan.source_folder.name == "KickoffReturnTDs"
    assert plan.target_folder.name == "KickoffReturnTouchdown"
    assert plan.key_actions_source.name == "KickoffReturnTD.csv"
    assert plan.key_actions_target.name == "KickoffReturnTouchdown.csv"


def test_dry_run_planning_does_not_modify_files(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    before = summary.read_bytes()

    plan = build_plan(tracking_root, summary, key_actions)

    assert plan.ready
    assert (tracking_root / "KickoffReturnTDs").is_dir()
    assert not (tracking_root / "KickoffReturnTouchdown").exists()
    assert (key_actions / "KickoffReturnTD.csv").is_file()
    assert not (key_actions / "KickoffReturnTouchdown.csv").exists()
    assert summary.read_bytes() == before


def test_apply_updates_all_identity_surfaces(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path, [1, 2])
    plan = build_plan(tracking_root, summary, key_actions)

    apply_plan(plan, summary)

    assert not (tracking_root / "KickoffReturnTDs").exists()
    assert (tracking_root / "KickoffReturnTouchdown").is_dir()
    assert (
        tracking_root
        / "KickoffReturnTouchdown"
        / "KickoffReturnTouchdown_1_cvat_mot.zip"
    ).is_file()
    assert not (key_actions / "KickoffReturnTD.csv").exists()
    assert (key_actions / "KickoffReturnTouchdown.csv").is_file()
    text = summary.read_text(encoding="utf-8")
    assert "KickoffReturnTD_1.mp4" not in text
    assert "KickoffReturnTouchdown_1.mp4" in text
    assert "KickoffReturnTouchdown_2.mp4" in text


def test_tracking_folder_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    (tracking_root / "KickoffReturnTouchdown").mkdir()

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("canonical tracking folder already exists" in error for error in plan.errors)


def test_key_actions_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    (key_actions / "KickoffReturnTouchdown.csv").write_text("collision", encoding="utf-8")

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


def test_summary_target_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path, [1])
    summary.write_text(
        "clip number,output_file,name\n"
        "1,KickoffReturnTD_1.mp4,KickoffReturnTouchdown_\n"
        "999,KickoffReturnTouchdown_1.mp4,collision\n",
        encoding="utf-8",
    )

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)


def test_unexpected_tracking_entry_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _make_fixture(tmp_path)
    (tracking_root / "KickoffReturnTDs" / "notes.txt").write_text("unexpected")

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("unexpected entries" in error for error in plan.errors)
