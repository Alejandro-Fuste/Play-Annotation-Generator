# Specification: Final Four-Way Outside Zone + QB Zone Read Migration

## 1. Purpose

Update the existing migration implementation in:

```text
src/play_annotation_generator/outside_zone_qb_zone_read_migration.py
```

so it supports the final canonical reclassification of the legacy `OutsideZoneStretch` population into **four** destination play classes while preserving the existing `QB_ZoneRead` migration behavior.

This is an identity/taxonomy migration only. Do not redesign annotation timing, player-track mapping, action semantics, or tracking data.

The committed migration manifest must remain the single authoritative mapping for:

- tracking ZIP renames/moves;
- `DatasetSummary.output_file` updates;
- later renaming of the corresponding source video clips;
- provenance and rollback verification.

---

## 2. Final taxonomy decisions

The legacy source population in:

```text
data/tracking/OutsideZoneStretch/
```

contains clips that have now been manually reviewed and assigned to four canonical play classes:

```text
OutsideZoneStretch
OutsideZoneRead
SplitZone
InsideZoneStretch
```

The canonical destination is determined by the `Original ID` provenance stored in the current destination Key Actions CSVs.

Do **not** re-infer classification from action columns during migration.

The canonical destination CSVs are authoritative.

### Final expected legacy Outside Zone distribution

Require exactly:

```text
OutsideZoneStretch -> OutsideZoneStretch: 197
OutsideZoneStretch -> OutsideZoneRead:     96
OutsideZoneStretch -> SplitZone:           48
OutsideZoneStretch -> InsideZoneStretch:    6
------------------------------------------------
Total legacy OutsideZoneStretch sources:  347
```

Require:

```text
347 unique source identities
347 total assignments
0 duplicate source assignments
0 missing source assignments
```

If these counts do not match the checked-in CSVs, fail production validation rather than silently adjusting expectations.

---

## 3. QB_ZoneRead migration remains in scope

The existing `QB_ZoneRead` taxonomy decision remains unchanged.

Expected source population:

```text
198 total QB_ZoneRead clips

146 -> InsideZoneRead
46  -> OutsideZoneRead
6   -> HOLDOUT
```

Expected holdout legacy IDs:

```text
17
18
41
42
131
132
```

The six holdouts remain under their legacy identity and must not be migrated to `Counter` automatically.

`QB_ZoneRead` must not be added to `plays.json`.

`Keep` remains an action/outcome, not the play label.

---

## 4. Authoritative input files

Use the current checked-in repository versions of:

```text
data/key_actions/OutsideZoneStretch.csv
data/key_actions/OutsideZoneRead.csv
data/key_actions/SplitZone.csv
data/key_actions/InsideZoneStretch.csv
data/key_actions/InsideZoneRead.csv
data/key_actions/QB_ZoneRead.csv

data/DatasetSummary.csv
data/plays.json

data/tracking/OutsideZoneStretch/
data/tracking/QB_ZoneRead/
data/tracking/InsideZoneRead/
data/tracking/SplitZone/
```

`data/tracking/OutsideZoneRead/` and `data/tracking/InsideZoneStretch/` may not exist before apply. The migration must create destination directories only during `--apply`, never during dry-run.

---

## 5. Migration manifest

Continue using the permanent project artifact:

```text
data/migrations/outside_zone_qb_zone_read_migration_manifest.csv
```

Do not introduce a second mapping file.

The manifest must be regenerated after this implementation change.

### Required schema

Preserve the existing schema:

```csv
source_play,source_video_id,source_clip_name,destination_play,destination_video_id,destination_clip_name,status,source_key_actions_file,destination_key_actions_file,notes
```

Allowed statuses remain:

```text
MIGRATE
HOLDOUT
BLOCKED
```

---

## 6. Core implementation change: generic canonical provenance collection

Refactor only the manifest-building portion needed to support multiple canonical destination CSVs.

Do not hard-code the old assumption that an `OutsideZoneStretch_<id>` source may appear only in:

```text
OutsideZoneStretch.csv
OutsideZoneRead.csv
```

Instead, define the canonical destination files for the legacy Outside Zone source:

```python
OUTSIDE_ZONE_DESTINATION_FILES = {
    "OutsideZoneStretch": "OutsideZoneStretch.csv",
    "OutsideZoneRead": "OutsideZoneRead.csv",
    "SplitZone": "SplitZone.csv",
    "InsideZoneStretch": "InsideZoneStretch.csv",
}
```

For every row in each of those files:

1. read destination ID from `Video #`;
2. read provenance from `Original ID`;
3. parse `Original ID`;
4. if provenance is `OutsideZoneStretch_<source_id>`, create a source-to-destination mapping:
   - source play = `OutsideZoneStretch`
   - source ID = provenance ID
   - destination play = the canonical file's play name
   - destination ID = row `Video #`;
5. if provenance is `QB_ZoneRead_<source_id>`, handle it only where explicitly valid under the QB migration rules;
6. reject malformed provenance.

The exact destination `Video #` values must come from the current CSVs. Do not assume historical ID ranges.

---

## 7. Provenance parsing

Preserve support for:

```text
OutsideZoneStretch_<integer>
QB_ZoneRead_<integer>
```

A provenance parser may continue to use a pattern equivalent to:

```python
r"^(OutsideZoneStretch|QB_ZoneRead)_(\d+)$"
```

Reject:

- missing `Original ID`;
- malformed values;
- unsupported source prefixes;
- duplicate source assignment across canonical destination files.

---

## 8. One-to-one Outside Zone source audit

The manifest generator must combine all four canonical destination files and assert:

```text
source = OutsideZoneStretch_1 ... OutsideZoneStretch_347
```

is represented exactly once.

A source appearing in two destination CSVs is a fatal error.

A source appearing in none of the destination CSVs but existing in tracking or DatasetSummary becomes:

```text
status = BLOCKED
```

Production validation must fail if any `BLOCKED` rows exist.

Do not silently:

- drop an unmapped source;
- duplicate a source;
- synthesize a classification;
- infer destination from action fields.

---

## 9. Final Outside Zone production counts

Update the production assertions and preflight reporting to these exact counts:

```text
ozs_to_ozs = 197
ozs_to_ozr = 96
ozs_to_split_zone = 48
ozs_to_inside_zone_stretch = 6
ozs_blocked = 0
```

Add fields to `ValidationResult` as needed, for example:

```python
ozs_to_split_zone: int
ozs_to_inside_zone_stretch: int
```

Remove or update old assertions that expect:

```text
228 OutsideZoneStretch
118 legacy OutsideZoneRead
```

Those counts are obsolete.

---

## 10. OutsideZoneRead population

The current canonical `OutsideZoneRead.csv` contains two source populations:

```text
96 rows sourced from OutsideZoneStretch
46 rows sourced from QB_ZoneRead
```

Expected total:

```text
142 OutsideZoneRead rows
```

Validate this by provenance, not by row-number ranges.

The manifest must therefore produce:

```text
96 OutsideZoneStretch -> OutsideZoneRead
46 QB_ZoneRead -> OutsideZoneRead
```

Do not assume the 46 QB-derived rows use any historical range such as `119-164` or `348-393`.

Their canonical destination IDs must be read directly from current `OutsideZoneRead.csv`.

---

## 11. SplitZone population

`SplitZone.csv` contains both pre-existing Split Zone annotations and legacy Outside Zone clips that were reclassified after manual review.

For every row whose:

```text
Original ID = OutsideZoneStretch_<id>
```

generate:

```text
OutsideZoneStretch_<source_id>
    ->
SplitZone_<Video #>
```

Expected migrated legacy Outside Zone count:

```text
48
```

Do not migrate or rename the pre-existing Split Zone clips.

Only rows with legacy Outside Zone provenance participate in this migration.

The newly added `Split Block` annotations are annotation data and must be preserved exactly. The migration code must not recompute or edit them.

---

## 12. InsideZoneStretch population

`InsideZoneStretch.csv` contains six manually reclassified legacy Outside Zone clips.

For every row:

```text
Original ID = OutsideZoneStretch_<id>
```

generate:

```text
OutsideZoneStretch_<source_id>
    ->
InsideZoneStretch_<Video #>
```

Expected count:

```text
6
```

Create:

```text
data/tracking/InsideZoneStretch/
```

during apply only if it does not already exist.

Do not modify the Inside Zone Stretch action annotations.

---

## 13. QB_ZoneRead canonical destination validation

The canonical destination CSVs, using `Original ID`, are authoritative.

For every `QB_ZoneRead` source classified as `OutsideZoneRead`:

- find the row in `OutsideZoneRead.csv` whose `Original ID` equals that QB source;
- use that row's current `Video #` as the destination ID.

For every `QB_ZoneRead` source classified as `InsideZoneRead`:

- validate it against the current `InsideZoneRead.csv` canonical mapping.

The `Classification` and `New ID` fields in `QB_ZoneRead.csv` should be checked for consistency, but stale `New ID` values must not override canonical provenance.

Recommended behavior:

- classification mismatch = ERROR;
- stale `New ID` = WARNING during dry-run;
- canonical destination mapping = destination CSV provenance.

Before final apply, update `QB_ZoneRead.csv` so its `New ID` values agree with the canonical manifest.

---

## 14. Manifest examples

Illustrative only; actual destination IDs must come from current CSVs.

```csv
source_play,source_video_id,source_clip_name,destination_play,destination_video_id,destination_clip_name,status,source_key_actions_file,destination_key_actions_file,notes
OutsideZoneStretch,1,OutsideZoneStretch_1,OutsideZoneStretch,1,OutsideZoneStretch_1,MIGRATE,data/key_actions/OutsideZoneStretch.csv,data/key_actions/OutsideZoneStretch.csv,Canonical stretch classification
OutsideZoneStretch,121,OutsideZoneStretch_121,SplitZone,286,SplitZone_286,MIGRATE,data/key_actions/OutsideZoneStretch.csv,data/key_actions/SplitZone.csv,Reclassified from manual annotation review
OutsideZoneStretch,314,OutsideZoneStretch_314,InsideZoneStretch,1,InsideZoneStretch_1,MIGRATE,data/key_actions/OutsideZoneStretch.csv,data/key_actions/InsideZoneStretch.csv,Reclassified from manual annotation review
QB_ZoneRead,1,QB_ZoneRead_1,OutsideZoneRead,<canonical id>,OutsideZoneRead_<canonical id>,MIGRATE,data/key_actions/QB_ZoneRead.csv,data/key_actions/OutsideZoneRead.csv,QB keep preserved as action
QB_ZoneRead,17,QB_ZoneRead_17,,,QB_ZoneRead_17,HOLDOUT,data/key_actions/QB_ZoneRead.csv,,Unresolved Counter/gap taxonomy
```

Do not copy illustrative IDs unless they match the current checked-in files.

---

## 15. Tracking ZIP migration

The apply phase must continue to be manifest-driven.

For every `MIGRATE` row:

```text
data/tracking/<source_play>/<source_clip_name>_cvat_mot.zip
    ->
data/tracking/<destination_play>/<destination_clip_name>_cvat_mot.zip
```

Examples of the four-way Outside Zone migration:

```text
OutsideZoneStretch -> OutsideZoneStretch
OutsideZoneStretch -> OutsideZoneRead
OutsideZoneStretch -> SplitZone
OutsideZoneStretch -> InsideZoneStretch
```

Plus existing QB migrations:

```text
QB_ZoneRead -> InsideZoneRead
QB_ZoneRead -> OutsideZoneRead
```

Preserve the existing safe behavior:

- dry-run by default;
- `--apply` required;
- create missing destination directories only on apply;
- stage intra-folder renames to avoid filename collisions;
- use rollback journal;
- preserve ZIP bytes exactly;
- refuse to apply on validation errors or BLOCKED rows.

---

## 16. Destination collision rules

Because `SplitZone` and `InsideZoneRead` already contain canonical clips, collision validation is critical.

Before apply, verify every destination filename is either:

1. absent and safe to create; or
2. an expected in-place identity case where source and destination are the same exact path.

Any unrelated existing destination ZIP is a fatal error.

Do not overwrite an existing ZIP.

---

## 17. DatasetSummary migration

For every `MIGRATE` manifest row, update only:

```text
output_file
```

Example:

```text
OutsideZoneStretch_121.mp4
    ->
SplitZone_<canonical_id>.mp4
```

```text
OutsideZoneStretch_314.mp4
    ->
InsideZoneStretch_<canonical_id>.mp4
```

Preserve all other DatasetSummary fields exactly, including:

- input file;
- start/end time;
- view;
- fromYouTube;
- any source metadata;
- row order where practical;
- BOM/encoding;
- line-ending behavior.

HOLDOUT rows remain unchanged.

---

## 18. Permanent video rename support

The same committed manifest will later be used to rename actual video clips.

Do not add a second video mapping.

A future video rename utility must consume:

```text
source_clip_name
destination_clip_name
status
```

Only:

```text
status = MIGRATE
```

may be automatically renamed.

`HOLDOUT` and `BLOCKED` must never be renamed automatically.

---

## 19. Preflight report

Update the dry-run output so the four-way split is visible.

Expected format:

```text
MIGRATION PREFLIGHT

Legacy Outside Zone source:
  -> OutsideZoneStretch: 197
  -> OutsideZoneRead:     96
  -> SplitZone:           48
  -> InsideZoneStretch:    6
  Unmapped/BLOCKED:        0

Legacy QB_ZoneRead source:
  -> InsideZoneRead:      146
  -> OutsideZoneRead:      46
  HOLDOUT:                  6

Outside Zone source assignments:
  unique sources: 347
  total mappings: 347
  duplicates:       0
  missing:          0

Destination collisions:      0
DatasetSummary mismatches:   0
BLOCKED:                     0

STATUS: READY
```

Warnings such as stale `QB_ZoneRead.New ID` values may still be printed but must be clearly separated from fatal errors.

---

## 20. Expected manifest counts

With the current dataset state, the manifest should represent:

### Legacy Outside Zone

```text
347 MIGRATE
```

### Legacy QB_ZoneRead

```text
192 MIGRATE
6 HOLDOUT
```

### Overall

```text
MIGRATE: 539
HOLDOUT:   6
BLOCKED:   0
TOTAL:   545
```

If these production counts differ, fail production validation and report the discrepancy.

---

## 21. Tests to update/add

Update:

```text
tests/test_outside_zone_qb_zone_read_migration.py
```

### Required tests

#### Provenance / four-way mapping
- maps legacy source to `OutsideZoneStretch`;
- maps legacy source to `OutsideZoneRead`;
- maps legacy source to `SplitZone`;
- maps legacy source to `InsideZoneStretch`;
- rejects one source appearing in two destination CSVs;
- detects a source missing from all four destination CSVs;
- asserts 347 unique legacy Outside Zone sources.

#### Production counts
Assert exactly:

```text
197 OutsideZoneStretch
96 OutsideZoneRead
48 SplitZone
6 InsideZoneStretch
```

#### OutsideZoneRead mixed provenance
Assert:

```text
96 OutsideZoneStretch provenance
46 QB_ZoneRead provenance
142 total
```

#### QB migration
Assert:

```text
146 -> InsideZoneRead
46 -> OutsideZoneRead
6 HOLDOUT
```

#### Apply
Test creation/population of:

```text
data/tracking/OutsideZoneRead/
data/tracking/InsideZoneStretch/
```

and moves into existing:

```text
data/tracking/SplitZone/
data/tracking/InsideZoneRead/
```

#### Safety
Retain tests for:

- destination collisions;
- DatasetSummary mismatch;
- dry-run zero mutation;
- rollback after simulated failure;
- holdouts unchanged;
- byte-preserving ZIP moves;
- stale QB `New ID` warning;
- exact taxonomy validation against `plays.json`.

---

## 22. Full regression requirements

Run focused tests:

```bash
PYTHONPATH=src ./venv/bin/pytest -q tests/test_outside_zone_qb_zone_read_migration.py
```

Then run the full suite:

```bash
PYTHONPATH=src ./venv/bin/pytest -q
```

All tests must pass.

No unrelated code refactors.

---

## 23. Manifest regeneration

After the implementation is updated and tests pass, regenerate the manifest:

```bash
PYTHONPATH=src ./venv/bin/python \
  -m play_annotation_generator.outside_zone_qb_zone_read_migration \
  --generate-manifest \
  --production-counts
```

Then run dry-run validation:

```bash
PYTHONPATH=src ./venv/bin/python \
  -m play_annotation_generator.outside_zone_qb_zone_read_migration \
  --production-counts
```

Do **not** apply unless dry-run returns:

```text
STATUS: READY
BLOCKED: 0
Destination collisions: 0
DatasetSummary mismatches: 0
```

Review the regenerated manifest manually and commit it before applying.

---

## 24. Apply command

Only after the manifest is reviewed and committed:

```bash
PYTHONPATH=src ./venv/bin/python \
  -m play_annotation_generator.outside_zone_qb_zone_read_migration \
  --production-counts \
  --apply
```

The apply command must create missing destination tracking folders automatically.

---

## 25. Post-apply verification

After apply:

1. verify total tracking ZIP count is unchanged;
2. verify `OutsideZoneRead` tracking folder contains the expected canonical files;
3. verify `InsideZoneStretch` tracking folder contains 6 migrated files;
4. verify the relevant SplitZone files exist at their canonical IDs;
5. verify the relevant InsideZoneRead QB files exist at their canonical IDs;
6. verify only the six QB holdouts remain in `data/tracking/QB_ZoneRead/`;
7. verify no unresolved Outside Zone source remains in `data/tracking/OutsideZoneStretch/` under its old source identity;
8. run the normal batch preflight;
9. run the full test suite;
10. inspect for accidental macOS duplicates such as `* 2.zip`.

Do not delete any suspected duplicate without byte/hash verification.

---

## 26. Frozen semantics

This migration must not change:

- action timing;
- action definitions;
- `Keep` semantics;
- `Split Block` annotations;
- `Press Interior Gap` annotations;
- PreSnap behavior;
- `Action_None`;
- Ball Snap / Snap Receive semantics;
- actor/player track → XML mapping;
- position/team assignment;
- existing tracking boxes;
- ID switches;
- false positives;
- missing boxes;
- unknown/unassigned track behavior;
- review-report semantics.

This migration changes only canonical play/clip identity and corresponding storage location.

---

## 27. Non-goals

Do not:

- add `QB_ZoneRead` to canonical taxonomy;
- automatically resolve the six Counter/gap holdouts;
- infer play classification from actions during migration;
- regenerate action annotations;
- alter `plays.json` taxonomy as part of this migration;
- change `DatasetSummary` fields other than `output_file`;
- overwrite existing destination ZIPs;
- create a second manifest for video renaming;
- apply the migration automatically after implementation.

Implementation should stop after generating a clean manifest and successful dry-run unless the user explicitly runs `--apply`.
