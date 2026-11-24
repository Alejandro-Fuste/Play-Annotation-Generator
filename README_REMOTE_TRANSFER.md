# TapeVision v1.0 — Rclone remote transfer patch

## Scope

Adds `--destination-remote`, `--pilot-per-split`, and `--state-file` to `scripts/consolidate_dataset.py`. Includes `scripts/remote_transfer.py` and remote-transfer tests. **Does not change your approved `dataset_plan_v1_final.json` or its assignments.**

This package is a patch to the `feature/dataset-consolidation` branch. It does not install software or authenticate Rclone. The source Google Drive remote should be configured with the video folder as its root; OneDrive remote should point to your target personal OneDrive.

## Install (from repository root)

```bash
unzip -o ~/Downloads/TapeVision_v1_remote_transfer_patch.zip -d "$PWD"
python3 -m pytest -q tests/test_consolidate_dataset.py tests/test_remote_transfer.py
python3 scripts/consolidate_dataset.py --help
```

## Four-pair cloud pilot (two train + two test)

```bash
python3 scripts/consolidate_dataset.py \
  --copy \
  --plan dataset_plan_v1_final.json \
  --drive-remote gdrive: \
  --destination-remote onedrive:TapeVision_Dataset/_pilot_v1 \
  --pilot-per-split 2 \
  --approve-boundaries
```

The pilot uploads only four pairs to the isolated `_pilot_v1/` destination. It does not touch the full `v1.0/` directory. You can rerun the same command to verify existing objects and resume. A local `dataset_plan_v1_final.json.pilot-state.json` checkpoint is created; do not edit or commit it.

Check pilot directory contents:

```bash
rclone lsf 'onedrive:TapeVision_Dataset/_pilot_v1' --recursive --files-only
rclone cat 'onedrive:TapeVision_Dataset/_pilot_v1/README.md'
```

Expect four `.mp4`, four clip `.json`, one `dataset_manifest.csv`, and one `README.md` (10 files).

## Full upload — ONLY after pilot approval

```bash
python3 scripts/consolidate_dataset.py \
  --copy \
  --plan dataset_plan_v1_final.json \
  --drive-remote gdrive: \
  --destination-remote onedrive:TapeVision_Dataset/v1.0 \
  --approve-boundaries
```

The full transfer will be considerably slower than preview: it downloads one MP4 to temporary local storage at a time, uploads it, reads back each uploaded file for SHA-256 verification, and writes a resumable checkpoint. The manifest and README are published **only when all planned pairs finish**. Restart after interruption with the same command and same plan/destination. Do not run another transfer simultaneously to the same destination.

**Important safeguards:**
- Never deletes or moves source files in Google Drive or your repository.
- Rejects conflicting existing remote objects instead of overwriting them.
- Performs source MD5 and remote SHA-256 checks; does not equate OneDrive's provider hash with SHA-256.
- Preserves `batch_status` for known failed clips. JSON schema and play/clip identity are still validated; known `validation_report.json` errors are accepted as requested.
- Uses approximately one video file's worth of local temporary disk storage at a time (plus Python JSON parsing memory).
- Plan is Git-commit pinned. If HEAD changed, regenerate and review preview rather than bypassing the guard.
- Remote operations require an authenticated Rclone installation on your Mac. Tests mock cloud transfers; they are **not** evidence of a successful live transfer.

Do not publish the `_pilot_v1` directory as the dataset release.
