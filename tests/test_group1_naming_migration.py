from pathlib import Path

from play_annotation_generator.group1_naming_migration import (
    apply_plan,
    build_plan,
)


HEADER = (
    "clip number,start_time,end_time,play,view,fromYouTube,input_file,"
    "output_file,name,file extension,date,\n"
)


def _write_fixture(tmp_path: Path):
    tracking = tmp_path / "data" / "tracking"
    out_routes = tracking / "OutRoutes"
    pin_pull = tracking / "PinAndPull"
    out_routes.mkdir(parents=True)
    pin_pull.mkdir(parents=True)

    (out_routes / "OutRoutes1_cvat_mot.zip").write_bytes(b"one")
    (out_routes / "OutRoutes2_cvat_mot.zip").write_bytes(b"two")
    (pin_pull / "pinAndPull-clip1_cvat_mot.zip").write_bytes(b"three")

    summary = tmp_path / "data" / "DatasetSummary.csv"
    summary.write_text(
        HEADER
        + "1,0:00:01,0:00:02,Pass,S,FALSE,OutRoutes.mp4,OutRoutes1.mp4,OutRoutes,.mp4,2026-03-20,\n"
        + "2,0:00:03,0:00:04,Pass,E,FALSE,OutRoutes.mp4,OutRoutes2.mp4,OutRoutes,.mp4,2026-03-20,\n"
        + "23,00:00:00,00:00:04,Run,,,,pinAndPull-clip1.mp4,PinAndPull_,.mp4,2025-06-24,\n",
        encoding="utf-8",
    )
    return tracking, summary


def test_build_plan_pairs_tracking_and_summary_by_filename_id(tmp_path):
    tracking, summary = _write_fixture(tmp_path)

    plan = build_plan(tracking, summary)

    assert plan.ready
    assert len(plan.tracking) == 3
    assert len(plan.summary) == 3
    assert [item.clip_id for item in plan.tracking if item.family == "PinAndPull"] == [1]
    assert any(item.target.name == "OutRoutes_1_cvat_mot.zip" for item in plan.tracking)
    assert any(item.target == "PinAndPull_1.mp4" for item in plan.summary)


def test_dry_run_planning_does_not_modify_files(tmp_path):
    tracking, summary = _write_fixture(tmp_path)
    original_summary = summary.read_bytes()

    plan = build_plan(tracking, summary)

    assert plan.ready
    assert (tracking / "OutRoutes" / "OutRoutes1_cvat_mot.zip").exists()
    assert not (tracking / "OutRoutes" / "OutRoutes_1_cvat_mot.zip").exists()
    assert summary.read_bytes() == original_summary


def test_apply_updates_tracking_and_only_output_file_tokens(tmp_path):
    tracking, summary = _write_fixture(tmp_path)
    plan = build_plan(tracking, summary)

    apply_plan(plan, summary)

    assert not (tracking / "OutRoutes" / "OutRoutes1_cvat_mot.zip").exists()
    assert (tracking / "OutRoutes" / "OutRoutes_1_cvat_mot.zip").read_bytes() == b"one"
    assert (tracking / "OutRoutes" / "OutRoutes_2_cvat_mot.zip").read_bytes() == b"two"
    assert (tracking / "PinAndPull" / "PinAndPull_1_cvat_mot.zip").read_bytes() == b"three"

    text = summary.read_text(encoding="utf-8")
    assert "OutRoutes.mp4,OutRoutes_1.mp4,OutRoutes" in text
    assert "OutRoutes.mp4,OutRoutes_2.mp4,OutRoutes" in text
    assert ",PinAndPull_1.mp4,PinAndPull_" in text
    assert "pinAndPull-clip1.mp4" not in text


def test_collision_blocks_entire_plan(tmp_path):
    tracking, summary = _write_fixture(tmp_path)
    (tracking / "OutRoutes" / "OutRoutes_1_cvat_mot.zip").write_bytes(b"collision")

    plan = build_plan(tracking, summary)

    assert not plan.ready
    assert any("tracking target collision" in error for error in plan.errors)


def test_id_mismatch_blocks_entire_plan(tmp_path):
    tracking, summary = _write_fixture(tmp_path)
    (tracking / "PinAndPull" / "pinAndPull-clip1_cvat_mot.zip").unlink()

    plan = build_plan(tracking, summary)

    assert not plan.ready
    assert any(
        "IDs present in DatasetSummary legacy output_file values but missing from tracking"
        in error
        for error in plan.errors
    )


def test_summary_target_collision_blocks_entire_plan(tmp_path):
    tracking, summary = _write_fixture(tmp_path)
    with summary.open("a", encoding="utf-8") as fh:
        fh.write(
            "99,0:00:00,0:00:01,Pass,S,FALSE,other.mp4,"
            "OutRoutes_1.mp4,Other,.mp4,2026-01-01,\n"
        )

    plan = build_plan(tracking, summary)

    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)
