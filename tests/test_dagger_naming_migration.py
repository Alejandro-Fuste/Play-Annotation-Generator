from pathlib import Path

from play_annotation_generator.dagger_naming_migration import (
    apply_plan,
    build_plan,
)


def _write_summary(path: Path, rows: list[str]) -> None:
    path.write_text(
        "clip number,start_time,end_time,play,view,fromYouTube,input_file,output_file,name,ext,date\n"
        + "\n".join(rows)
        + "\n",
        encoding="utf-8",
    )


def test_build_plan_pairs_tracking_and_summary_by_filename_id(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    dagger = tracking_root / "Dagger"
    dagger.mkdir(parents=True)
    (dagger / "DaggerConcept_1_cvat_mot.zip").write_bytes(b"1")
    (dagger / "DaggerConcept_2_cvat_mot.zip").write_bytes(b"2")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(
        summary,
        [
            "1,0,1,Pass,S,FALSE,x,DaggerConcept_1.mp4,DaggerConcept_,.mp4,2026-01-01",
            "2,0,1,Pass,E,FALSE,x,DaggerConcept_2.mp4,DaggerConcept_,.mp4,2026-01-01",
        ],
    )

    plan = build_plan(tracking_root, summary)

    assert plan.ready
    assert [item.clip_id for item in plan.tracking] == [1, 2]
    assert [item.target.name for item in plan.tracking] == [
        "Dagger_1_cvat_mot.zip",
        "Dagger_2_cvat_mot.zip",
    ]
    assert [item.target for item in plan.summary] == [
        "Dagger_1.mp4",
        "Dagger_2.mp4",
    ]


def test_dry_run_planning_does_not_modify_files(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    dagger = tracking_root / "Dagger"
    dagger.mkdir(parents=True)
    source = dagger / "DaggerConcept_1_cvat_mot.zip"
    source.write_bytes(b"zip")

    summary = tmp_path / "DatasetSummary.csv"
    original = (
        "clip number,start_time,end_time,play,view,fromYouTube,input_file,output_file,name,ext,date\n"
        "1,0,1,Pass,S,FALSE,x,DaggerConcept_1.mp4,DaggerConcept_,.mp4,2026-01-01\n"
    )
    summary.write_text(original, encoding="utf-8")

    plan = build_plan(tracking_root, summary)

    assert plan.ready
    assert source.exists()
    assert not (dagger / "Dagger_1_cvat_mot.zip").exists()
    assert summary.read_text(encoding="utf-8") == original


def test_apply_updates_tracking_and_only_output_file_tokens(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    dagger = tracking_root / "Dagger"
    dagger.mkdir(parents=True)
    source = dagger / "DaggerConcept_7_cvat_mot.zip"
    source.write_bytes(b"zipdata")

    summary = tmp_path / "DatasetSummary.csv"
    original = (
        "clip number,start_time,end_time,play,view,fromYouTube,input_file,output_file,name,ext,date\r\n"
        "7,0:00:04,0:00:17,Pass,S,FALSE,dagger-clip2_raw.mp4,DaggerConcept_7.mp4,DaggerConcept_,.mp4,2026-03-20\r\n"
    )
    summary.write_bytes(original.encode("utf-8"))

    plan = build_plan(tracking_root, summary)
    assert plan.ready
    apply_plan(plan, summary)

    assert not source.exists()
    target = dagger / "Dagger_7_cvat_mot.zip"
    assert target.read_bytes() == b"zipdata"

    updated = summary.read_text(encoding="utf-8")
    assert "Dagger_7.mp4" in updated
    assert "DaggerConcept_7.mp4" not in updated
    assert "dagger-clip2_raw.mp4" in updated
    assert "DaggerConcept_" in updated


def test_tracking_collision_blocks_entire_plan(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    dagger = tracking_root / "Dagger"
    dagger.mkdir(parents=True)
    (dagger / "DaggerConcept_1_cvat_mot.zip").write_bytes(b"legacy")
    (dagger / "Dagger_1_cvat_mot.zip").write_bytes(b"existing")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(
        summary,
        ["1,0,1,Pass,S,FALSE,x,DaggerConcept_1.mp4,DaggerConcept_,.mp4,2026-01-01"],
    )

    plan = build_plan(tracking_root, summary)

    assert not plan.ready
    assert any("tracking target collision" in error for error in plan.errors)


def test_id_mismatch_blocks_entire_plan(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    dagger = tracking_root / "Dagger"
    dagger.mkdir(parents=True)
    (dagger / "DaggerConcept_1_cvat_mot.zip").write_bytes(b"1")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(
        summary,
        ["2,0,1,Pass,S,FALSE,x,DaggerConcept_2.mp4,DaggerConcept_,.mp4,2026-01-01"],
    )

    plan = build_plan(tracking_root, summary)

    assert not plan.ready
    assert any("IDs present in tracking" in error for error in plan.errors)
    assert any("IDs present in DatasetSummary" in error for error in plan.errors)


def test_summary_target_collision_blocks_entire_plan(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    dagger = tracking_root / "Dagger"
    dagger.mkdir(parents=True)
    (dagger / "DaggerConcept_1_cvat_mot.zip").write_bytes(b"1")

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(
        summary,
        [
            "1,0,1,Pass,S,FALSE,x,DaggerConcept_1.mp4,DaggerConcept_,.mp4,2026-01-01",
            "99,0,1,Pass,S,FALSE,x,Dagger_1.mp4,Dagger_,.mp4,2026-01-01",
        ],
    )

    plan = build_plan(tracking_root, summary)

    assert not plan.ready
    assert any("DatasetSummary target collision" in error for error in plan.errors)


def test_no_legacy_dagger_rows_blocks_plan(tmp_path: Path):
    tracking_root = tmp_path / "tracking"
    (tracking_root / "Dagger").mkdir(parents=True)

    summary = tmp_path / "DatasetSummary.csv"
    _write_summary(
        summary,
        ["1,0,1,Pass,S,FALSE,x,Other_1.mp4,Other_,.mp4,2026-01-01"],
    )

    plan = build_plan(tracking_root, summary)

    assert not plan.ready
    assert any("no legacy DaggerConcept tracking files" in error for error in plan.errors)
    assert any("no legacy DaggerConcept DatasetSummary" in error for error in plan.errors)
