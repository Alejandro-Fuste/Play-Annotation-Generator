# TapeVision v1.0 consolidation utility

This bundle adds one script and one test file, with the two current inventories provided for local use. Requires Python 3.9+ (pytest for tests). The production repository, Google Drive, and OneDrive are not included.

Extract the bundle into your local Play-Annotation-Generator checkout on a feature branch. The inventories contain Google Drive IDs; keep them and `dataset_plan.json` private and do not add them to the public repository. Only commit the script and tests. Commit them **before** previewing, because copy checks that the repository HEAD has not changed from the preview.

Run from the repository root:

```sh
python3 -m pytest -q tests/test_consolidate_dataset.py
python3 scripts/consolidate_dataset.py --preview
```

Read the 32 class boundaries and the local `dataset_plan.json` (including held clips, source metadata near each boundary, and summary counts). Inspect video content if view or identity is uncertain. A new preview can set a different boundary, e.g. `--boundary Counter=230 --plan dataset_plan_reviewed.json`; the number is the training count, not the last clip ID. The number is only an example. Use a fresh plan filename. Known batch failures, invalid annotations, and validation errors are held automatically. Warnings and missing validation reports remain provisional; review the plan summary and source reports before approving. No split is guaranteed leakage-free if paired or re-encoded videos cannot be identified.

When OneDrive is configured, use an empty dedicated version directory and a configured rclone Google Drive remote covering the source video files. Check free local space because this implementation downloads videos into the local OneDrive sync folder. Configure read-only Google Drive permission if available. Copy requires explicit approval of the plan and boundary reviews:

```sh
python3 scripts/consolidate_dataset.py --copy \
  --plan dataset_plan.json \
  --drive-remote 'gdrive:YOUR_VIDEO_FOLDER' \
  --destination '/ABSOLUTE/OneDrive/TapeVision_Dataset/v1.0' \
  --approve-boundaries
```

The remote name/folder and destination above are placeholders. Use `--local-videos /path/to/videos` instead of `--drive-remote` only if all eligible MP4s are already in a single local folder. If interrupted, repeat the same command with the same plan; the saved manifest locks the assignments and matching existing files are reused. No source file is deleted. The copy mode checks Drive file IDs and MD5 before accepting downloaded bytes, and verifies SHA-256 locally. A failed verification is not a completed dataset. Do not run concurrent copy processes for the same version. The manifest may exist with empty video hashes during copying; it is not a finished dataset until copy and verify succeed.

```sh
python3 scripts/consolidate_dataset.py --verify \
  --destination '/ABSOLUTE/OneDrive/TapeVision_Dataset/v1.0'
```

Check OneDrive sync status separately; local hash verification does not prove cloud upload. The script checks bytes, not video decoding or frame alignment. The destination contains train/, test/, README.md, and dataset_manifest.csv; the plan stays in the local repo. Never edit approved assignments in a partially copied version; resolve conflicts in a fresh version directory.
