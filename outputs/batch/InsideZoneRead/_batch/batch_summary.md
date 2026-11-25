# Play-Annotation-Generator Batch Processing Summary

## Run Overview

- Total discovered: 382
- Total preflight ready: 381
- Total preflight failed: 1
- Total selected after filters: 381
- Total attempted: 381
- PASS: 0
- WARNING: 380
- FAILED: 2
- SKIPPED: 0
- EXCLUDED: 0
- Total validation warnings: 35917
- Total validation errors: 2
- Total elapsed seconds: 929.603

## Dataset Quality Signals

- Total unknown/unassigned tracks: 5601 (across 381 clips)
- Total missing-box warnings: 22851 (across 381 clips)
- Clips with no ball track: 354

## Failure Reasons

| Failure Type | Count |
|---|---:|
| unrecognized_play | 1 |
| enrichment | 1 |

## Results By Play Type

| Play Type | Discovered | Selected | PASS | WARNING | FAILED | SKIPPED | EXCLUDED |
|---|---:|---:|---:|---:|---:|---:|---:|
| InsideZoneRead | 381 | 381 | 0 | 380 | 1 | 0 | 0 |
| InsideZoneRead_40_cvat | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

## Failed Clips

| Clip Name | Play Name | Video ID | Failure Type | Message |
|---|---|---|---|---|
| InsideZoneRead_40_cvat_mot 2 | InsideZoneRead_40_cvat | mot 2 | unrecognized_play | Play type 'InsideZoneRead_40_cvat' is not recognized in plays.json definitions |
| InsideZoneRead_18 | InsideZoneRead | 18 | enrichment | Enriched with 1 validation error(s) |
