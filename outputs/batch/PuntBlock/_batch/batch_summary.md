# Play-Annotation-Generator Batch Processing Summary

## Run Overview

- Total discovered: 83
- Total preflight ready: 83
- Total preflight failed: 0
- Total selected after filters: 83
- Total attempted: 83
- PASS: 0
- WARNING: 78
- FAILED: 5
- SKIPPED: 0
- Total validation warnings: 10146
- Total validation errors: 5
- Total elapsed seconds: 287.589

## Dataset Quality Signals

- Total unknown/unassigned tracks: 1689 (across 81 clips)
- Total missing-box warnings: 6545 (across 81 clips)
- Clips with no ball track: 81

## Failure Reasons

| Failure Type | Count |
|---|---:|
| enrichment | 3 |
| unexpected_exception | 2 |

## Results By Play Type

| Play Type | Discovered | Selected | PASS | WARNING | FAILED | SKIPPED |
|---|---:|---:|---:|---:|---:|---:|
| PuntBlock | 83 | 83 | 0 | 78 | 5 | 0 |

## Failed Clips

| Clip Name | Play Name | Video ID | Failure Type | Message |
|---|---|---|---|---|
| PuntBlock_3 | PuntBlock | 3 | enrichment | Enriched with 1 validation error(s) |
| PuntBlock_14 | PuntBlock | 14 | enrichment | Enriched with 1 validation error(s) |
| PuntBlock_29 | PuntBlock | 29 | enrichment | Enriched with 1 validation error(s) |
| PuntBlock_80 | PuntBlock | 80 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| PuntBlock_81 | PuntBlock | 81 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
