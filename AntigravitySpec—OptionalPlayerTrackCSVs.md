# Focused Implementation Specification: Make Player Track CSVs Optional in Batch Mode

## Project

**Repository:** `Play-Annotation-Generator` / TapeVision Annotation Enricher

## Objective

Update the current batch-processing implementation so that a missing per-play **Player Track / position CSV** does **not** cause the clip to fail preflight.

The correct behavior is:

```text
Player Track CSV exists
→ use current position/team assignment behavior

Player Track CSV missing
→ continue processing
→ preserve all MOT player tracks
→ leave unmatched players as unknown/unassigned
→ generate warnings
→ do NOT fabricate positions or team assignments
```

This is a **focused input-handling change only**.

Do not redesign the batch architecture or the annotation timing engine.

---

# 1. Current Problem

The current batch code treats Player Track CSVs as required.

In `batch_pipeline.py`, `resolve_per_play_sources(...)` currently emits:

```text
missing_player_tracks_source
```

when a per-play Player Track CSV cannot be found.

`resolve_clip_preflight(...)` then marks the clip:

```text
status = FAILED
```

and the clip never reaches:

```python
run_generate_and_enrich_pipeline(...)
```

This behavior is incorrect for the current dataset workflow.

Only some plays currently have Player Track CSVs, but all valid clips should still be enrichable from:

```text
tracking
+ Key Actions
+ DatasetSummary
+ actions.json
+ plays.json
+ template
```

without position assignments.

---

# 2. Authoritative Desired Behavior

Treat the Player Track CSV as **optional**.

## If Player Track CSV exists

Preserve current behavior exactly:

- parse assignments;
- map player track ID → football position;
- assign team side;
- generate current warnings/errors;
- preserve existing unknown-track behavior for tracks not assigned in the CSV.

## If Player Track CSV does not exist

The clip must still be preflight-ready.

Expected behavior:

```text
preflight_status = READY
player_tracks_resolved = false
```

The single-clip pipeline should run with:

```python
assignments = {}
```

or equivalent behavior.

Every MOT player that lacks assignment data must remain in the output.

Do not drop those tracks.

Their position/team values should follow the existing unknown/unassigned semantics, ultimately appearing as current equivalents of:

```text
Position_Unknown
Team_Unknown
```

or the existing intermediate `undefined` values that are later normalized to those outputs.

The clip should receive warnings, not a preflight failure.

---

# 3. Status Behavior

A missing Player Track CSV by itself must **not** cause:

```text
FAILED
```

Instead:

```text
missing Player Track CSV
→ warning
→ processing continues
```

Final semantic status should follow normal validation rules:

```text
PASS:
0 errors
0 warnings

WARNING:
0 errors
1+ warnings

FAILED:
1+ errors
```

Therefore, a clip with no Player Track CSV will normally become:

```text
WARNING
```

because position/team assignments are unavailable.

Do not hard-code `WARNING` at batch level; let the existing warning/validation flow produce it.

---

# 4. Inputs That Must Remain Required

Do not weaken required-input handling for other source files.

The following remain required:

```text
tracking ZIP / gt.txt
Key Actions CSV
DatasetSummary entry
actions.json
plays.json
CVAT template
valid config
```

Missing Key Actions must still fail preflight.

This specification applies only to Player Track / position assignment CSVs.

---

# 5. Files to Inspect

Before editing, inspect the current implementation of at least:

```text
src/play_annotation_generator/batch_pipeline.py
src/play_annotation_generator/cli.py
src/play_annotation_generator/pipeline_generate_and_enrich.py
src/play_annotation_generator/player_track_sheet_parser.py
src/play_annotation_generator/cvat_xml_generator.py
src/play_annotation_generator/enricher.py
src/play_annotation_generator/output_pipeline.py
tests/test_batch_pipeline.py
```

Also inspect any compatibility modules under:

```text
src/tapevision_enricher/
```

if they re-export or wrap the current implementation.

Use the current repository paths as authoritative.

---

# 6. Required Changes — Batch Source Resolution

Update:

```python
resolve_per_play_sources(...)
```

so that missing Player Track data is not added to the fatal `errors` list.

Current conceptual behavior:

```python
if player_track_file_missing:
    errors.append("missing_player_tracks_source: ...")
```

Required behavior:

```python
if player_track_file_missing:
    pt_path = None
```

and continue.

If useful, return a nonfatal warning/info list separately.

For example:

```python
return ka_path, pt_path, errors, warnings
```

or use the current project’s preferred structure.

Do not make missing Key Actions optional.

---

# 7. Required Changes — Resolved Types

Update any batch dataclasses/type hints that currently require:

```python
player_tracks_csv: Path
```

to permit:

```python
player_tracks_csv: Optional[Path]
```

This likely includes:

```text
ResolvedClipIdentity
BatchClipJob
```

or their current equivalents.

Do not use fake paths such as:

```text
Path("")
```

to represent absence.

Use `None`.

---

# 8. Required Changes — Preflight

Update:

```python
resolve_clip_preflight(...)
```

so missing Player Track CSV does not return:

```text
FAILED
missing_player_tracks_source
```

Instead, return:

```text
READY
```

with:

```text
player_tracks_csv = None
```

and preserve a nonfatal message such as:

```text
Player Track CSV not available for play 'Counter'; position/team assignments will remain unknown.
```

If the manifest supports resolved flags, set:

```text
player_tracks_resolved = false
```

For plays with a CSV:

```text
player_tracks_resolved = true
```

---

# 9. Required Changes — Single-Clip Worker Signature

The current worker:

```python
run_generate_and_enrich_pipeline(...)
```

accepts:

```python
player_tracks_csv: str
```

Change this to:

```python
player_tracks_csv: Optional[str]
```

or equivalent.

Preserve backward compatibility with existing callers.

Do not make the single-clip CLI optional unless required by this task; the primary requirement is batch behavior.

However, if making the worker optional requires updating the single-clip CLI type path, keep existing single-clip required CLI behavior unless there is a strong reason to change it.

---

# 10. Required Changes — Assignment Parsing

Current behavior should become conceptually:

```python
if player_tracks_csv:
    assignments, parse_warnings = parse_player_track_csv(...)
else:
    assignments = {}
    parse_warnings = [
        "No Player Track assignment CSV provided; position and team assignments will remain unknown."
    ]
```

Do not call:

```python
parse_player_track_csv(None, ...)
```

unless the parser is explicitly updated to safely accept `None`.

Prefer explicit handling in the orchestration layer.

Do not fabricate empty CSV files.

---

# 11. Preserve CVAT XML Behavior

The existing CVAT XML generator already supports missing assignments conceptually:

```python
position = assignment.position if assignment else "undefined"
team_side = assignment.team_side if assignment else "undefined"
```

Preserve that behavior.

Do not alter the identity mapping or tracking IDs.

When assignments are absent:

- MOT track remains present;
- original actor track ID remains present;
- XML track generation still works;
- position remains unknown;
- team side remains unknown.

Do not default unknown players to offense or defense.

---

# 12. Preserve Unknown-Track Detection

The existing downstream validation/review behavior that turns missing assignment information into dataset-quality findings must remain active.

Expected final output should continue surfacing values such as:

```text
Position_Unknown
Team_Unknown
```

and review warnings such as:

```text
undefined position
undefined team_side
```

Do not suppress these warnings.

Do not convert all unassigned tracks into successful known assignments.

The batch quality summary should continue to count them as:

```text
unknown_track_count
```

using unique tracks, not warning instances.

---

# 13. Manifest / Batch Summary Behavior

Update manifest fields so missing Player Track source is represented accurately.

Recommended fields:

```text
player_track_source
player_tracks_resolved
```

For a play with no CSV:

```text
player_track_source = ""
player_tracks_resolved = false
```

Do not write `"None"` or a fake filesystem path unless current serialization conventions require it.

The clip must not appear as:

```text
preflight_status = FAILED
failure_type = missing_player_tracks_source
```

solely because the Player Track CSV is missing.

---

# 14. Warning Message

Generate one concise clip-level warning when no Player Track CSV is available.

Recommended wording:

```text
No Player Track assignment CSV available for play '<PlayName>'; player position and team-side assignments will remain unknown.
```

Do not generate one extra “missing CSV” warning for every individual track.

Existing per-track unknown-position/team warnings may still occur downstream.

---

# 15. CLI Behavior

Current batch CLI requires:

```text
--player-tracks
```

This may remain required as a **directory root argument**:

```text
--player-tracks data/player_tracks
```

even if some play-specific CSVs are missing inside that directory.

That is acceptable and minimizes CLI changes.

The important requirement is:

```text
missing <PlayName>.csv inside the directory
≠ batch preflight failure
```

Do not require one Player Track CSV per play.

If you choose to make the CLI argument itself optional, preserve backward compatibility and document the default directory. This is optional, not required.

---

# 16. Example Required Behavior

Given:

```text
data/tracking/Counter/Counter_1_cvat_mot.zip
data/key_actions/Counter.csv
data/DatasetSummary.csv
data/actions.json
data/plays.json
docs/JetSweepTemplate.xml
```

and no:

```text
data/player_tracks/Counter.csv
```

the batch should do:

```text
discover Counter_1
↓
resolve Key Actions successfully
↓
Player Track CSV unavailable
↓
preflight READY
↓
run existing single-clip pipeline
↓
assignments = {}
↓
generate all MOT player tracks
↓
positions/team sides remain unknown
↓
validation warnings generated
↓
clip status WARNING if no errors
↓
write normal clip outputs
```

It must not do:

```text
preflight FAILED
```

---

# 17. Existing Plays With Position CSVs Must Not Regress

Current repository has Player Track CSVs for at least:

```text
JetSweep
BootPass
```

These must continue using those assignment files exactly as before.

Do not bypass or ignore an existing Player Track CSV.

For:

```text
JetSweep_1
```

the stabilized position mappings and timeline behavior must remain unchanged.

---

# 18. JetSweep_1 Regression Requirement

Run the existing JetSweep_1 regression after implementation.

The required action timelines must remain unchanged:

```text
QB / actor 17
PreSnap      0–131
SnapReceive  132–144
Toss         145–159
Action_None  160–329
```

```text
WR / actor 19
PreSnap      0–95
JetMotion    96–159
BallCarry    160–329
```

```text
TE / actor 12
PreSnap      0–132
LeadBlock    133–192
Action_None  193–329
```

```text
RT / actor 13
PreSnap           0–132
ZoneBlock         133–164
BlockSecondLevel  165–192
Action_None       193–329
```

```text
Center / actor 7
PreSnap      0–131
BallSnap     132–144
ZoneBlock    145–192
Action_None  193–329
```

Also verify known JetSweep positions/team sides remain unchanged.

---

# 19. New Test Requirements

Add focused tests covering:

## 19.1 Missing per-play Player Track source

Set up:

```text
tracking exists
Key Actions exists
Player Track CSV missing
```

Assert:

```text
preflight_status == READY
```

not:

```text
FAILED
```

---

## 19.2 Batch processing without Player Track CSV

Run a real/minimal fixture with:

```text
player_tracks_csv = None
```

Assert:

- clip outputs are generated;
- processing does not throw;
- all MOT player tracks remain;
- assignment count is 0;
- warnings are nonempty;
- validation errors remain 0 if fixture is otherwise valid;
- semantic status is `WARNING`.

---

## 19.3 Unknown mapping output

Assert unassigned players are represented with existing unknown semantics, such as:

```text
Position_Unknown
Team_Unknown
```

or the exact stabilized output equivalents.

---

## 19.4 No fake assignment

Assert:

```text
actor_track_id
xml_track_id
```

remain tied to the original tracking/XML identity logic.

Do not allow fabricated football-position assignments.

---

## 19.5 Existing position CSV path

With a valid Player Track CSV:

- assignments still load;
- known positions remain known;
- behavior matches pre-change output.

---

## 19.6 Batch summary

For a missing Player Track CSV clip, assert:

```text
preflight_status = READY
status = WARNING
player_tracks_resolved = false
```

if that field is added.

Assert there is no:

```text
failure_type = missing_player_tracks_source
```

---

## 19.7 Mixed batch

Create a batch with:

```text
Play A → Player Track CSV exists
Play B → Player Track CSV missing
```

Assert both clips are attempted.

Expected:

```text
Play A → normal result
Play B → WARNING
FAILED due solely to Player Track absence = 0
```

---

# 20. Full Regression Suite

Run:

```bash
PYTHONPATH=src ./venv/bin/pytest -q
```

All existing and new tests must pass.

Do not modify existing tests simply to hide regressions.

---

# 21. Manual Smoke Test

After unit/integration tests pass, run one play that does **not** have a Player Track CSV.

Use an actual play in:

```text
data/tracking/
```

that has:

```text
tracking
Key Actions
DatasetSummary
```

but lacks:

```text
data/player_tracks/<PlayName>.csv
```

Run:

```bash
PYTHONPATH=src ./venv/bin/python -m play_annotation_generator.cli \
  batch-generate-and-enrich \
  --gt-dir data/tracking \
  --template docs/JetSweepTemplate.xml \
  --key-actions data/key_actions \
  --player-tracks data/player_tracks \
  --dataset-summary data/DatasetSummary.csv \
  --actions-json data/actions.json \
  --plays-json data/plays.json \
  --output outputs/batch_optional_player_tracks_test \
  --play <PlayName> \
  --limit 1
```

Expected batch result:

```text
Preflight: READY
Attempted: 1
FAILED: 0
WARNING: 1
```

assuming there are no unrelated validation errors.

Verify normal outputs are produced.

---

# 22. Do Not Change These Systems

Do not modify:

```text
action_rules.py
action endpoint logic
frame-role logic
PreSnap expansion
Action_None complete timeline behavior
BallSnap / SnapReceive pairing
Toss / BallCarry cross-actor timing
OL boundary logic
Center priority logic
JSON schema semantics
XML track identity semantics
unknown-track counting semantics
```

unless an import/type adjustment is strictly required.

This task is not an action-engine change.

---

# 23. Acceptance Criteria

The change is complete when all are true:

- [ ] Missing per-play Player Track CSV does not fail preflight.
- [ ] Missing Key Actions CSV still fails preflight.
- [ ] Batch job can carry `player_tracks_csv = None`.
- [ ] Single-clip worker can process without Player Track assignments.
- [ ] `assignments = {}` is used when no position CSV exists.
- [ ] All MOT player tracks remain in the output.
- [ ] No positions/team sides are fabricated.
- [ ] Unknown/unassigned semantics are preserved.
- [ ] Missing position CSV produces warnings.
- [ ] Clip normally becomes `WARNING`, not `FAILED`.
- [ ] Batch summary counts unknown tracks correctly.
- [ ] JetSweep still uses `JetSweep.csv`.
- [ ] BootPass still uses `BootPass.csv`.
- [ ] JetSweep_1 regression remains unchanged.
- [ ] Mixed batches can contain plays with and without Player Track CSVs.
- [ ] All tests pass.

---

# 24. Required Antigravity Final Response

When complete, report:

1. files modified;
2. exact functions changed;
3. how missing Player Track CSV is represented internally;
4. whether `--player-tracks` CLI remains required as a directory argument;
5. exact warning emitted for missing position assignment data;
6. how assignments are handled when the CSV is absent;
7. how unknown players appear in XML/JSON;
8. whether batch manifest includes a `player_tracks_resolved` field;
9. test results;
10. JetSweep_1 regression result;
11. result of one real no-position-CSV smoke test;
12. confirmation that no action-timing semantics changed.

Do not make unrelated refactors.