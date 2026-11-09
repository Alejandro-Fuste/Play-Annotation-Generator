# Play-Annotation-Generator Batch Processing Summary

## Run Overview

- Total discovered: 196
- Total preflight ready: 196
- Total preflight failed: 0
- Total selected after filters: 196
- Total attempted: 196
- PASS: 0
- WARNING: 190
- FAILED: 6
- SKIPPED: 0
- Total validation warnings: 23062
- Total validation errors: 6
- Total elapsed seconds: 859.508

## Dataset Quality Signals

- Total unknown/unassigned tracks: 3685 (across 192 clips)
- Total missing-box warnings: 15331 (across 192 clips)
- Clips with no ball track: 175

## Failure Reasons

| Failure Type | Count |
|---|---:|
| unexpected_exception | 4 |
| enrichment | 2 |

## Results By Play Type

| Play Type | Discovered | Selected | PASS | WARNING | FAILED | SKIPPED |
|---|---:|---:|---:|---:|---:|---:|
| OutsideZoneStretch | 196 | 196 | 0 | 190 | 6 | 0 |

## Failed Clips

| Clip Name | Play Name | Video ID | Failure Type | Message |
|---|---|---|---|---|
| OutsideZoneStretch_8 | OutsideZoneStretch | 8 | enrichment | Enriched with 1 validation error(s) |
| OutsideZoneStretch_131 | OutsideZoneStretch | 131 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| OutsideZoneStretch_132 | OutsideZoneStretch | 132 | unexpected_exception | Exception: UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9b in position 11: invalid start byte |
| OutsideZoneStretch_146 | OutsideZoneStretch | 146 | unexpected_exception | Exception: TimeoutError: [Errno 60] Operation timed out |
| OutsideZoneStretch_147 | OutsideZoneStretch | 147 | unexpected_exception | Exception: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xde in position 17: invalid continuation byte |
| OutsideZoneStretch_149 | OutsideZoneStretch | 149 | enrichment | Enriched with 1 validation error(s) |
