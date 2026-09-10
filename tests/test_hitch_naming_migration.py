from __future__ import annotations

from pathlib import Path

from play_annotation_generator.hitch_naming_migration import apply_plan, build_plan


def _write_summary(path: Path, ids: list[int]) -> None:
    rows = ["clip number,output_file,name\n"]
    rows.extend(f"{clip_id},Hitch9to15_{clip_id}.mp4,Hitch9to15_\n" for clip_id in ids)
    path.write_text("".join(rows), encoding="utf-8")


def _fixture(tmp_path: Path, ids: list[int] = [1, 2]) -> tuple[Path, Path, Path]:
    tracking_root = tmp_path / "tracking"
    legacy = tracking_root / "Hitch9to15"
    legacy.mkdir(parents=True)
    for clip_id in ids:
        (legacy / f"Hitch9to15_{clip_id}_cvat_mot.zip").write_bytes(
            f"zip-{clip_id}".encode()
        )

    dataset_summary = tmp_path / "DatasetSummary.csv"
    _write_summary(dataset_summary, ids)

    key_actions_root = tmp_path / "key_actions"
    key_actions_root.mkdir()
    (key_actions_root / "Hitch9to15.csv").write_text(
        "Video Name:,Hitch9to15\nVideo #,Pre Snap\n1,0\n",
        encoding="utf-8",
    )
    return tracking_root, dataset_summary, key_actions_root


def test_build_plan_pairs_tracking_and_summary_ids(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path, [1, 4, 9])
    plan = build_plan(tracking_root, summary, key_actions)

    assert plan.ready
    assert [pair.clip_id for pair in plan.pairs] == [1, 4, 9]
    assert plan.source_folder.name == "Hitch9to15"
    assert plan.target_folder.name == "Hitch"
    assert plan.key_actions_source.name == "Hitch9to15.csv"
    assert plan.key_actions_target.name == "Hitch.csv"


def test_dry_run_planning_does_not_modify_files(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path)
    before = summary.read_bytes()

    plan = build_plan(tracking_root, summary, key_actions)

    assert plan.ready
    assert (tracking_root / "Hitch9to15").is_dir()
    assert not (tracking_root / "Hitch").exists()
    assert (key_actions / "Hitch9to15.csv").is_file()
    assert not (key_actions / "Hitch.csv").exists()
    assert summary.read_bytes() == before


def test_apply_updates_all_identity_surfaces(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path)
    plan = build_plan(tracking_root, summary, key_actions)

    apply_plan(plan, summary)

    assert not (tracking_root / "Hitch9to15").exists()
    assert (tracking_root / "Hitch").is_dir()
    assert (tracking_root / "Hitch" / "Hitch_1_cvat_mot.zip").is_file()
    assert not (key_actions / "Hitch9to15.csv").exists()
    assert (key_actions / "Hitch.csv").is_file()
    text = summary.read_text(encoding="utf-8")
    assert "Hitch9to15_1.mp4" not in text
    assert "Hitch_1.mp4" in text
    assert "Hitch9to15_2.mp4" not in text
    assert "Hitch_2.mp4" in text


def test_tracking_folder_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path)
    (tracking_root / "Hitch").mkdir()

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("canonical tracking folder already exists" in e for e in plan.errors)


def test_key_actions_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path)
    (key_actions / "Hitch.csv").write_text("collision", encoding="utf-8")

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("canonical Key Actions target already exists" in e for e in plan.errors)


def test_id_mismatch_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path, [1, 2])
    _write_summary(summary, [1, 3])

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("missing from DatasetSummary" in e for e in plan.errors)
    assert any("missing from tracking" in e for e in plan.errors)


def test_summary_target_collision_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path, [1])
    summary.write_text(
        "clip number,output_file,name\n"
        "1,Hitch9to15_1.mp4,Hitch9to15_\n"
        "999,Hitch_1.mp4,Hitch_\n",
        encoding="utf-8",
    )

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("DatasetSummary target collision" in e for e in plan.errors)


def test_unexpected_tracking_entry_blocks_plan(tmp_path: Path) -> None:
    tracking_root, summary, key_actions = _fixture(tmp_path)
    (tracking_root / "Hitch9to15" / "notes.txt").write_text("unexpected")

    plan = build_plan(tracking_root, summary, key_actions)

    assert not plan.ready
    assert any("unexpected entries" in e for e in plan.errors)
