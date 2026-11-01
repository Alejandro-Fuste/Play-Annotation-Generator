# Play-Annotation-Generator Batch Processing Summary

## Run Overview

- Total discovered: 382
- Total preflight ready: 381
- Total preflight failed: 1
- Total selected after filters: 381
- Total attempted: 381
- PASS: 0
- WARNING: 378
- FAILED: 4
- SKIPPED: 0
- Total validation warnings: 35370
- Total validation errors: 5
- Total elapsed seconds: 211.497

## Dataset Quality Signals

- Total unknown/unassigned tracks: 5601 (across 381 clips)
- Total missing-box warnings: 22863 (across 381 clips)
- Clips with no ball track: 354

## Failure Reasons

| Failure Type | Count |
|---|---:|
| enrichment | 3 |
| unrecognized_play | 1 |

## Results By Play Type

| Play Type | Discovered | Selected | PASS | WARNING | FAILED | SKIPPED |
|---|---:|---:|---:|---:|---:|---:|
| InsideZoneRead | 381 | 381 | 0 | 378 | 3 | 0 |
| InsideZoneRead_40_cvat | 1 | 0 | 0 | 0 | 1 | 0 |

## Failed Clips

| Clip Name | Play Name | Video ID | Failure Type | Message |
|---|---|---|---|---|
| InsideZoneRead_40_cvat_mot 2 | InsideZoneRead_40_cvat | mot 2 | unrecognized_play | Play type 'InsideZoneRead_40_cvat' is not recognized in plays.json definitions |
| InsideZoneRead_18 | InsideZoneRead | 18 | enrichment | Enriched with 1 validation error(s) |
| InsideZoneRead_225 | InsideZoneRead | 225 | enrichment | Enriched with 2 validation error(s) |
| InsideZoneRead_309 | InsideZoneRead | 309 | enrichment | Enriched with 1 validation error(s) |
