# Play-Annotation-Generator Batch Processing Summary

## Run Overview

- Total discovered: 375
- Total preflight ready: 375
- Total preflight failed: 0
- Total selected after filters: 375
- Total attempted: 375
- PASS: 0
- WARNING: 368
- FAILED: 7
- SKIPPED: 0
- EXCLUDED: 0
- Total validation warnings: 32483
- Total validation errors: 7
- Total elapsed seconds: 1247.863

## Dataset Quality Signals

- Total unknown/unassigned tracks: 5173 (across 369 clips)
- Total missing-box warnings: 21351 (across 369 clips)
- Clips with no ball track: 349

## Failure Reasons

| Failure Type | Count |
|---|---:|
| unexpected_exception | 6 |
| enrichment | 1 |

## Results By Play Type

| Play Type | Discovered | Selected | PASS | WARNING | FAILED | SKIPPED | EXCLUDED |
|---|---:|---:|---:|---:|---:|---:|---:|
| Power | 375 | 375 | 0 | 368 | 7 | 0 | 0 |

## Failed Clips

| Clip Name | Play Name | Video ID | Failure Type | Message |
|---|---|---|---|---|
| Power_145 | Power | 145 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| Power_146 | Power | 146 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| Power_147 | Power | 147 | unexpected_exception | Exception: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa7 in position 11: invalid start byte |
| Power_335 | Power | 335 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| Power_336 | Power | 336 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| Power_337 | Power | 337 | unexpected_exception | Exception: UnicodeDecodeError: 'utf-8' codec can't decode byte 0x86 in position 10: invalid start byte |
| Power_357 | Power | 357 | enrichment | Enriched with 1 validation error(s) |
