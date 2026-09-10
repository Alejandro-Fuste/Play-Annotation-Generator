from pathlib import Path

from play_annotation_generator.deepcross_naming_migration import apply_plan, build_plan


def _write_summary(path: Path, outputs: list[str]) -> None:
    path.write_text(
        "output_file,other\r\n" + "".join(f"{value},x\r\n" for value in outputs),
        encoding="utf-8",
    )


def _fixture(tmp_path: Path, ids: tuple[int, ...] = (1, 2)):
    tracking_root = tmp_path / "tracking"
    source_folder = tracking_root / "Crosses25+"
    source_folder.mkdir(parents=True)
    for clip_id in ids:
        (source_folder / f"Crosses25+_{clip_id}_cvat_mot.zip").write_bytes(f"zip-{clip_id}".encode())

    key_root = tmp_path / "key_actions"
    key_root.mkdir()
    (key_root / "Crosses25+.csv").write_text("Video Name:,Crosses25+ (Deep Cross)\r\n", encoding="utf-8")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(summary, [f"Crosses25+_{clip_id}.mp4" for clip_id in ids])
    return tracking_root, key_root, summary


def test_build_plan_pairs_tracking_and_summary_ids(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 3))
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert [p.clip_id for p in plan.pairs] == [1, 3]
    assert [p.tracking_target.name for p in plan.pairs] == [
        "DeepCross_1_cvat_mot.zip",
        "DeepCross_3_cvat_mot.zip",
    ]
    assert [p.summary_target for p in plan.pairs] == ["DeepCross_1.mp4", "DeepCross_3.mp4"]


def test_dry_run_planning_does_not_modify_files(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    before = summary.read_bytes()
    plan = build_plan(tracking_root, summary, key_root)
    assert plan.ready
    assert summary.read_bytes() == before
    assert (tracking_root / "Crosses25+").is_dir()
    assert not (tracking_root / "DeepCross").exists()
    assert (key_root / "Crosses25+.csv").exists()


def test_apply_updates_all_identity_surfaces(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    plan = build_plan(tracking_root, summary, key_root)
    apply_plan(plan, summary)
    assert not (tracking_root / "Crosses25+").exists()
    assert (tracking_root / "DeepCross" / "DeepCross_1_cvat_mot.zip").read_bytes() == b"zip-1"
    assert (tracking_root / "DeepCross" / "DeepCross_2_cvat_mot.zip").read_bytes() == b"zip-2"
    assert not (key_root / "Crosses25+.csv").exists()
    assert (key_root / "DeepCross.csv").exists()
    text = summary.read_text(encoding="utf-8")
    assert "DeepCross_1.mp4" in text and "DeepCross_2.mp4" in text
    assert "Crosses25+_" not in text


def test_tracking_folder_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "DeepCross").mkdir()
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical tracking folder already exists" in error for error in plan.errors)


def test_key_actions_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (key_root / "DeepCross.csv").write_text("collision", encoding="utf-8")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("canonical Key Actions target already exists" in error for error in plan.errors)


def test_id_mismatch_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1, 2))
    _write_summary(summary, ["Crosses25+_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("missing from DatasetSummary" in error for error in plan.errors)


def test_summary_target_collision_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path, (1,))
    _write_summary(summary, ["Crosses25+_1.mp4", "DeepCross_1.mp4"])
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)


def test_unexpected_tracking_entry_blocks_plan(tmp_path):
    tracking_root, key_root, summary = _fixture(tmp_path)
    (tracking_root / "Crosses25+" / "notes.txt").write_text("unexpected", encoding="utf-8")
    plan = build_plan(tracking_root, summary, key_root)
    assert not plan.ready
    assert any("unexpected entries" in error for error in plan.errors)
