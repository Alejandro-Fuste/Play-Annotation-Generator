# Migration data consistency — 2026-11-05

## Why the migration tests stopped matching the live repository

The historical `outside_zone_qb_zone_read_migration_manifest.csv` describes
source-to-destination renames, but current `data/tracking` and
`data/DatasetSummary.csv` already contain migrated names.

An audit of the checked-in text files found:

- **146** `QB_ZoneRead.csv` `New ID` values that disagree with the
  `InsideZoneRead.csv` `Original ID` provenance. Example: source
  `QB_ZoneRead_3` says `InsideZoneRead_236` in the source CSV, while
  `InsideZoneRead.csv` identifies video #237 as `QB_ZoneRead_3`.
- **343** legacy source clip names absent from the live DatasetSummary.
  The destinations corresponding to those rows exist in the summary.
- **343** destination ZIP collisions reported by the old preflight validator,
  which expects destinations not to exist *before* migration.

The first two migration tests now **assert that conflicting source data is
detected**, rather than asserting that a pre-migration manifest is READY after
the repository has changed. This is **not** a source-data reconciliation and
must not be treated as proof the migration artifacts are consistent.

## Required separate reconciliation

1. Cross-check the CVAT MOT ZIP identity and content, original video filenames,
   clip time offsets, and `DatasetSummary.csv` for the affected 146
   `QB_ZoneRead` sources. Determine whether the destination key-action
   `Video #`, source `New ID`, and DatasetSummary `output_file` disagree
   due to an indexing offset or an actual clip mismatch.
2. Reconcile and regenerate manifest data *only after* verifying clip identity.
   Never blanket-shift 146 IDs by one without this check.
3. Decide whether migration validation is running in preflight (sources exist,
   destinations absent) or post-migration audit (destinations exist, sources
   renamed), and add separate explicit modes if both workflows are needed.
4. Rerun `pytest -q` and a dedicated mapping audit after reconciliation.

No tracking ZIPs, key-action source CSVs, DatasetSummary entries, or historical
manifest records were modified in this PR.
