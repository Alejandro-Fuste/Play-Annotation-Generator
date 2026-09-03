# TapeVision Annotation Enricher — Batch Processing Implementation Specification v2

**Recommended filename:** `batch_processing_spec_v2_stable_pipeline.md`

**Project:** `Combine_Tracks_and_Actions` / TapeVision Annotation Enricher  
**Implementation target:** Antigravity IDE  
**Purpose:** Add scalable, resumable, deterministic batch orchestration around the stabilized single-clip annotation/enrichment pipeline without changing annotation semantics.

---

# 1. Document Purpose

This specification supersedes earlier batch-processing specifications where they conflict with the current stabilized single-clip pipeline and current dataset organization.

The current single-clip pipeline is the source of truth for annotation behavior.

Batch processing must be implemented as an orchestration layer that:

1. discovers tracking clips;
2. resolves the correct per-play source files and shared metadata;
3. performs a preflight audit;
4. invokes the existing single-clip processing path;
5. writes outputs into isolated play/clip directories;
6. classifies each clip as `PASS`, `WARNING`, or `FAILED`;
7. isolates failures so one bad clip does not stop the run;
8. supports resumability and targeted reruns;
9. writes machine-readable and human-readable batch reports;
10. preserves the stabilized JetSweep_1 behavior exactly.

This task is **not** an annotation-engine redesign.

---

# 2. Authoritative Current-State Assumptions

Treat the following as fixed project requirements.

The stabilized single-clip pipeline correctly handles:

- player track ID → XML track ID mapping;
- football position mapping;
- offense/defense team-side mapping;
- `Action_PreSnap` expansion;
- sequential actions for the same player;
- full-timeline `Action_None` coverage;
- paired `Action_BallSnap` / `Action_SnapReceive` timing;
- cross-actor `Action_Toss` → `Action_BallCarry` timing;
- inclusive `End of OL Block` boundary timing;
- Center `Action_BallSnap` priority over `Action_ZoneBlock`;
- annotated frame roles such as `START`, `END`, and `BOUNDARY`;
- action definitions loaded from `actions.json`;
- play definitions loaded from `plays.json`;
- clip metadata loaded from `DatasetSummary.csv`;
- enriched CVAT XML generation;
- TapeVision JSON generation;
- Markdown review-report generation;
- validation;
- unknown/unassigned player-track detection.

The latest successful `JetSweep_1` output is the regression baseline.

The batch implementation must not intentionally change any of those behaviors.

---

# 3. Existing Architecture to Preserve

Before editing, Antigravity must inspect the current repository and locate the real single-clip execution path.

Earlier verified repository versions contained the following relevant modules:

```text
src/tapevision_enricher/
├── cli.py
├── pipeline_generate_and_enrich.py
├── enricher.py
├── mot_parser.py
├── player_track_sheet_parser.py
├── wide_action_csv_parser.py
├── action_event_normalizer.py
├── action_rules.py
├── cvat_xml_generator.py
├── cvat_xml_parser.py
├── validators.py
├── reviewer.py
├── config.py
├── models.py
└── writers/
```

A later refactor may also contain a shared output helper such as:

```text
output_pipeline.py
```

or equivalent.

Do not assume these names are unchanged. Inspect the current checkout.

The required architectural relationship is:

```text
batch discovery/resolution
        ↓
existing single-clip generate-and-enrich function/path
        ↓
existing output-writing path
        ↓
existing validation/review path
```

There must not be a second implementation of:

- action parsing;
- player mapping;
- action normalization;
- action timing;
- timeline completion;
- JSON generation;
- XML enrichment;
- review semantics;
- validation semantics.

---

# 4. Critical Architectural Principle

Batch mode is orchestration only.

Conceptually:

```text
tracking ZIP
+ Key Actions row(s)
+ Player Track assignment row(s)
+ DatasetSummary row
+ actions.json
+ plays.json
+ shared CVAT template
+ config
        ↓
EXISTING SINGLE-CLIP PIPELINE
        ↓
clip outputs
```

Batch mode performs:

```text
discover
   ↓
resolve
   ↓
preflight
   ↓
select/filter
   ↓
invoke existing worker
   ↓
write existing outputs
   ↓
classify status
   ↓
record manifest/summary
   ↓
continue
```

If batch implementation requires copying large blocks from `pipeline_generate_and_enrich.py`, `enricher.py`, `action_rules.py`, or the output writers, the architecture is wrong.

---

# 5. Non-Goals

Do not implement any of the following as part of batch processing:

- action timing redesign;
- endpoint-rule changes;
- new `START` / `END` / `BOUNDARY` semantics;
- player-position remapping;
- actor/XML ID remapping;
- automatic ID-switch repair;
- automatic ID-switch correction;
- missing-box interpolation;
- false-positive track deletion;
- referee-track deletion;
- automatic unknown-track assignment;
- football-track fabrication;
- automatic ball-track repair;
- duplicate-track merging;
- track renumbering;
- automatic player identity correction;
- automatic action correction;
- changes to JSON schema semantics;
- changes to XML action semantics;
- changes to existing validation severity rules except batch-level classification described here;
- aggressive multiprocessing before safety is demonstrated.

Batch mode may **report** tracking-quality signals already exposed by the current pipeline, but it must not repair them.

---

# 6. Source Folder Convention

The production tracking source tree is:

```text
data/
└── tracking/
    ├── JetSweep/
    │   ├── JetSweep_1_cvat_mot.zip
    │   ├── JetSweep_2_cvat_mot.zip
    │   └── ...
    ├── Counter/
    │   ├── Counter_1_cvat_mot.zip
    │   ├── Counter_2_cvat_mot.zip
    │   └── ...
    ├── InsideZone/
    ├── SplitZone/
    └── ... all 31 play types
```

Production tracking ZIPs are read-only source artifacts.

Do not:

- rename them;
- rewrite them;
- delete them;
- permanently unpack all of them;
- add generated files beside them.

The canonical production filename format is:

```text
<PlayName>_<VideoID>_cvat_mot.zip
```

Examples:

```text
JetSweep_1_cvat_mot.zip
JetSweep_137_cvat_mot.zip
Counter_12_cvat_mot.zip
```

---

# 7. Supporting Input Sources

The project uses:

- per-play Key Actions CSV files;
- per-play Player Track assignment CSV files;
- one shared CVAT XML template;
- shared `DatasetSummary.csv`;
- shared `actions.json`;
- shared `plays.json`;
- normal pipeline configuration.

Antigravity must inspect the current repository to determine the exact paths and filenames.

Do not move or rename these files solely for batch mode.

## 7.1 Required resolution model

Batch mode must be able to resolve, for every clip:

```text
play_name
video_id
clip_name
tracking_zip_path
key_actions_csv_path
player_tracks_csv_path
dataset_summary_path / matching row
actions_json_path
plays_json_path
template_xml_path
config
```

## 7.2 Per-play CSV resolution

The Key Actions and Player Track CSVs remain separate by play type.

Batch mode must support a dataset-root run across multiple play types by resolving the appropriate CSV pair for each `play_name`.

Preferred implementation order:

1. reuse an existing repository convention/config mapping if one already exists;
2. otherwise add a small batch-only resolver based on the current directory convention;
3. if the repository has no deterministic convention, add a batch configuration mapping such as:

```yaml
batch:
  play_sources:
    JetSweep:
      key_actions: ...
      player_tracks: ...
    Counter:
      key_actions: ...
      player_tracks: ...
```

Do **not** require the user to maintain a per-clip manifest.

A per-play mapping is acceptable if necessary; a 4,000-row manual manifest is not.

---

# 8. Output Directory Structure

Do not flatten output.

Required logical structure:

```text
<batch_output_root>/
├── JetSweep/
│   ├── JetSweep_1/
│   ├── JetSweep_2/
│   └── ...
├── Counter/
│   ├── Counter_1/
│   └── ...
└── ...
```

For example:

```text
data/tracking/JetSweep/JetSweep_137_cvat_mot.zip
```

maps to:

```text
<batch_output_root>/JetSweep/JetSweep_137/
```

Each clip directory must contain the **same standard outputs produced by the current single-clip pipeline**.

Do not force old filenames if the stabilized pipeline has renamed them.

Earlier repository versions used names such as:

```text
generated_base_cvat.xml
enriched_cvat.xml
tapevision_annotations.json
dense_actions.csv
normalized_action_events.csv
validation_report.md
validation_report.json
review_report.md
```

The current stabilized checkout may instead use final names such as:

```text
annotations.xml
annotations.json
```

Antigravity must inspect the current writer/output-finalization path and use its actual filenames as authoritative.

Batch mode must not invent alternate copies of the same semantic artifact.

---

# 9. Clip Discovery

Batch discovery starts from the configured tracking root, normally:

```text
data/tracking/
```

Discover production ZIPs under one play-level directory:

```text
data/tracking/<PlayFolder>/*.zip
```

The default production matcher should accept the canonical suffix:

```text
_cvat_mot.zip
```

Do not treat every arbitrary ZIP in the tree as a clip.

## 9.1 Parsed identity

For:

```text
JetSweep_137_cvat_mot.zip
```

resolve:

```text
play_name = JetSweep
video_id = 137
clip_name = JetSweep_137
```

Use the filename suffix as a fixed delimiter:

1. require `_cvat_mot.zip`;
2. remove that suffix;
3. split the remaining name on the **final underscore**;
4. final token = `video_id`;
5. preceding text = filename `play_name`;
6. canonical `clip_name = <play_name>_<video_id>`.

Preserve `video_id` as a string in metadata, while deriving a numeric sort key when it is an integer.

Do not perform fuzzy identity guessing.

## 9.2 Folder/filename consistency

Validate:

```text
tracking/JetSweep/JetSweep_137_cvat_mot.zip
```

as valid.

Flag:

```text
tracking/Counter/JetSweep_137_cvat_mot.zip
```

as a preflight failure:

```text
folder_play_mismatch
```

Comparison should use the repository's established canonical play-name convention.

Do not silently normalize two different play names into one.

---

# 10. Recognized Play Validation

The parsed play must be recognized by the project's authoritative play-definition source.

The stabilized pipeline loads play definitions from:

```text
plays.json
```

Batch preflight should use the same play-definition loader or current equivalent.

Do not maintain a separate hard-coded list of 31 plays in batch code if `plays.json` already defines them.

A folder or filename play not recognized by the authoritative play definitions should fail preflight:

```text
unrecognized_play
```

---

# 11. Deterministic Ordering

Processing order must be deterministic.

Default order:

```text
canonical play name
then numeric video ID
then clip name as stable fallback
```

Numeric IDs must sort numerically:

```text
1, 2, 3, 10, 11
```

not lexicographically:

```text
1, 10, 11, 2, 3
```

If a video ID is nonnumeric, sort it deterministically after/beside numeric IDs using a documented fallback.

Filesystem enumeration order must never determine batch order.

---

# 12. Input Preflight Audit

Preflight must occur **before enrichment begins**.

It should inspect all discovered clips and resolve required sources without running the annotation engine.

For each clip verify at minimum:

- canonical tracking ZIP name;
- readable ZIP;
- directory/filename play agreement;
- valid parsed video ID;
- play recognized by current `plays.json`;
- matching Key Actions source exists;
- exactly one logical Key Actions row/clip record resolves;
- matching Player Track assignment source exists;
- the logical player-assignment records for the video resolve;
- matching `DatasetSummary.csv` entry exists;
- no duplicate canonical clip identity exists;
- shared `actions.json` exists and parses through the existing loader;
- shared `plays.json` exists and parses through the existing loader;
- shared CVAT template exists;
- config can be loaded;
- output directory can be prepared safely.

Do not silently fall back to:

- first CSV row;
- nearest video ID;
- suffix-only row matching across the wrong play;
- a different play's CSV;
- missing metadata defaults when the stabilized single-clip path treats metadata as required.

## 12.1 Preflight failure examples

Use explicit machine-readable failure types such as:

```text
malformed_filename
unreadable_zip
folder_play_mismatch
unrecognized_play
duplicate_clip_identity
missing_key_actions_source
missing_key_actions_row
ambiguous_key_actions_row
missing_player_tracks_source
missing_player_tracks_row
ambiguous_player_tracks_identity
missing_dataset_summary_entry
duplicate_dataset_summary_entry
missing_actions_definition
invalid_actions_definition
missing_plays_definition
invalid_plays_definition
missing_template
config_error
output_path_conflict
```

Exact enum names may follow current project style, but failures must be distinguishable.

---

# 13. Identity Resolution Safety

Earlier single-clip parsers used permissive compatibility matching such as name suffixes and historical JetSweep-specific fallbacks.

Batch mode must not use permissive matching as its authoritative clip resolver.

For batch:

```text
tracking filename identity
+ play folder identity
+ per-play CSV identity
+ DatasetSummary identity
```

must agree.

## 13.1 Key Actions

The resolver must identify the row(s) for the exact:

```text
play_name
video_id
```

using the current parser/data model.

If multiple physical rows legitimately belong to one logical clip, preserve current parser behavior.

Do not collapse semantically distinct rows accidentally.

## 13.2 Player Track assignments

The current player sheet may legitimately have multiple rows for the same video (for example offense and defense).

That is not automatically an ambiguity.

The batch resolver should verify that the existing single-clip parser can resolve the logical assignment set for the exact target video.

## 13.3 DatasetSummary

Resolve the exact DatasetSummary entry expected by the current single-clip metadata loader.

Verify the fields required by the stabilized pipeline, including the current source of:

- clip timing metadata;
- view;
- YouTube/source metadata;
- video/clip identity;
- any other fields now written into JSON/XML.

Do not duplicate DatasetSummary parsing in batch code if a current loader already exists.

---

# 14. Batch Manifest / Resolved Work Queue

Batch mode must generate its manifest automatically.

Recommended files:

```text
batch_manifest.csv
batch_manifest.json
```

The manifest represents discovery + preflight + selection state.

It is not a user-maintained input file.

## 14.1 Manifest fields

At minimum include:

```text
discovery_index
play_name
video_id
clip_name
tracking_zip
key_actions_source
key_actions_resolved
player_tracks_source
player_tracks_resolved
dataset_summary_resolved
template_resolved
actions_json_resolved
plays_json_resolved
preflight_status
preflight_failure_type
preflight_message
selected_for_run
output_directory
```

After processing, update/add:

```text
execution_state
status
warning_count
error_count
processing_error
traceback_file
started_at
finished_at
elapsed_seconds
```

Where practical also include existing metrics such as:

```text
num_tracks
num_player_tracks
num_ball_tracks
num_action_segments
num_mot_tracks
num_assignments
unknown_track_count
missing_box_warning_count
ball_track_count
```

Do not recompute these from scratch if they are already exposed by validation/review outputs.

## 14.2 Preflight status

Suggested values:

```text
READY
FAILED
FILTERED
```

This is separate from final validation status.

---

# 15. Batch Orchestration

Recommended control flow:

```python
load shared config/resources
discover clips
resolve per-play sources
run preflight for all clips
write initial manifest
apply deterministic filters
for each selected READY clip:
    evaluate resume/overwrite policy
    invoke existing single-clip worker
    invoke existing output finalization
    invoke existing review/validation output path
    classify result
    persist manifest/summary checkpoint
continue
write final aggregate summaries
```

The implementation should use small batch-specific dataclasses or equivalent typed records rather than large unstructured dictionaries if that matches the codebase style.

Potential concepts:

```text
DiscoveredClip
ResolvedClipInputs
BatchClipResult
BatchRunSummary
```

These are proposed names only.

---

# 16. Reuse of the Existing Single-Clip Pipeline

This is a hard requirement.

Locate the exact function currently used by the stabilized CLI command for one MOT ZIP + sources.

Earlier versions used:

```text
run_generate_and_enrich_pipeline(...)
```

plus output writing in the CLI.

Later versions may have a shared:

```text
output_pipeline.py
```

or equivalent.

Batch mode must call the same current worker/finalizer.

## 16.1 No duplicated writer path

If single-clip output writing is still embedded directly in `cli.py`, first extract that **existing writer sequence** into one backward-compatible helper that both single-clip and batch mode use.

If a shared output helper already exists, reuse it unchanged where possible.

The batch module must not separately reimplement:

- JSON writer invocation;
- XML writer invocation;
- dense CSV writer invocation;
- normalized-event CSV writer invocation;
- validation writer invocation;
- review-report invocation.

---

# 17. Frozen Single-Clip Semantics

Batch implementation must not intentionally modify:

```text
action_rules.py
action endpoint resolver modules
action_event_normalizer.py
sheet_group_resolver.py
player_track_sheet_parser.py
MOT ↔ XML mapping rules
complete timeline generation
Center action-priority logic
metadata meaning
review semantic classification
validation semantic rules
```

If a small change is genuinely required for reentrancy or dependency injection, it must be behavior-preserving and regression-tested.

Any newly discovered single-clip semantic bug must be:

1. documented;
2. excluded from the batch feature patch where possible;
3. handled in a separate issue/specification.

---

# 18. Processing Status Model

Final semantic clip status must use exactly:

```text
PASS
WARNING
FAILED
```

## 18.1 PASS

```text
validation.errors is empty
AND
validation.warnings is empty
AND
required processing/output generation completed
```

## 18.2 WARNING

```text
validation.errors is empty
AND
validation.warnings is nonempty
AND
required processing/output generation completed
```

Warnings do not prevent output generation.

Examples may include:

- unknown/unassigned player tracks;
- missing-box warnings;
- missing ball track;
- other current validation warnings.

## 18.3 FAILED

A clip is `FAILED` if any of the following is true:

```text
validation.errors is nonempty
```

**regardless of `validation.strict`**, or:

- preflight required input is missing/ambiguous;
- source parsing fails;
- existing single-clip processing throws;
- required output cannot be written;
- output completion validation fails;
- required review/validation artifact generation fails if configured as required.

This batch-level classification rule is authoritative.

Do not change current single-clip strict/non-strict control flow merely to implement it.

---

# 19. Execution State vs Validation Status

Do not overload `PASS/WARNING/FAILED` with resume state.

Maintain a separate execution state, for example:

```text
PREFLIGHT_FAILED
PROCESSED
SKIPPED
INTERRUPTED
```

At minimum the summary must distinguish:

```text
status = PASS | WARNING | FAILED
execution_state = PROCESSED | SKIPPED | ...
```

A skipped clip retains its last known semantic status when available.

Example:

```text
execution_state = SKIPPED
status = WARNING
```

---

# 20. Failure Isolation

One failed clip must never terminate the whole batch unless the failure is truly batch-global.

Per clip:

```python
try:
    process_clip()
except Exception:
    record_failure()
    continue
```

Capture:

- exception type;
- concise exception message;
- clip identity;
- processing stage;
- traceback path.

## 20.1 Batch-global fatal failures

It is acceptable to abort before clip processing for failures such as:

- tracking root does not exist;
- shared `plays.json` cannot load;
- shared `actions.json` cannot load;
- shared template is missing;
- shared config is invalid;
- output root cannot be created;
- manifest cannot be initialized.

## 20.2 Per-clip tracebacks

Recommended:

```text
<batch_output_root>/_batch/failures/<clip_name>.traceback.txt
```

Do not dump full tracebacks into every CSV cell.

The summary should contain the path and concise error.

---

# 21. Warning Behavior

A warning does not make a clip unusable by definition.

If the existing single-clip pipeline completes and validation has:

```text
errors = []
warnings = [...]
```

then:

```text
status = WARNING
```

and all standard outputs should remain available.

Do not suppress unknown/unassigned tracks to make warnings disappear.

---

# 22. Unknown / Unassigned Player Tracks

Preserve current behavior exactly.

Unknown/unassigned tracks may appear as:

```text
Position_Unknown
Team_Unknown
```

or current equivalents.

Batch mode may aggregate counts such as:

```text
unknown_track_count
clips_with_unknown_tracks
```

but must not:

- assign a position;
- assign a team;
- change `actor_track_id`;
- change `xml_track_id`;
- remove the track;
- suppress the warning.

Unknown-track detection is a dataset-quality signal.

---

# 23. Tracking-Quality Signals

Batch reporting should aggregate quality information already available from current validation/review outputs.

Where reliably available, capture:

```text
unknown_track_count
missing_box_warning_count
ball_track_count
has_unknown_tracks
has_missing_box_warnings
has_no_ball_track
```

If existing validation exposes additional reliable categories, they may be summarized.

Do not claim automated detection of:

- true ID switches;
- referee false positives;
- duplicate physical-player tracks;

unless the current stabilized single-clip validation actually implements those checks.

If those checks are not currently implemented, do not fabricate status fields that imply they are.

---

# 24. Explicit Prohibition on Automatic Tracking Repair

Batch mode is audit/enrichment orchestration, not tracking correction.

Do not add:

```text
ID switch repair
box interpolation
false-positive deletion
referee deletion
track merging
unknown-track assignment
ball fabrication
player remapping
```

Any future cleanup pipeline should consume batch findings and rerun only affected clips afterward.

---

# 25. ZIP Handling

Production source ZIPs remain compressed.

Prefer the existing MOT importer behavior.

Earlier code accepted ZIP paths and extracted a clip into an output-local `unpacked_mot` directory.

Inspect current behavior.

Acceptable approaches:

1. direct ZIP reading, if already supported; or
2. controlled per-clip extraction.

Requirements:

- source ZIP is never modified;
- no common extraction path shared between clips;
- no permanent extraction of all 4,000 clips;
- temporary extraction is cleaned when safe;
- debugging artifacts may be retained only if current single-clip behavior intentionally retains them.

If the existing worker already handles ZIP extraction safely inside the clip output directory, batch code should simply pass the ZIP through.

---

# 26. Output Completion Definition

Resume logic must not use “one file exists” as completion.

A clip is **processing-complete** only when the expected output set for the current single-clip mode is present and parseable enough to prove the finalization stage completed.

Antigravity must derive the required output set from the current output finalizer.

At minimum, the semantic final outputs should include the current equivalents of:

```text
annotations XML
annotations JSON
validation_report.json
review_report.md   # if review generation is part of normal stabilized output
```

and any current required CSV/validation files.

## 26.1 Completion checks

Recommended checks:

- required files exist;
- JSON files parse;
- validation report has expected `warnings` and `errors` structures;
- annotation JSON has expected top-level schema marker/sections;
- XML parses;
- a persisted clip status/manifest record exists or can be reconstructed.

Do not rerun annotation inference just to check completion.

---

# 27. Resume Semantics

Provide behavior equivalent to:

```text
--resume
```

## 27.1 Default resume behavior

With `--resume`:

- if a clip has a semantically complete prior attempt, skip it;
- preserve its prior `PASS`, `WARNING`, or validation-derived `FAILED` status;
- record current execution state as `SKIPPED`;
- do not overwrite outputs.

This includes a clip whose prior processing completed but validation status was `FAILED`.

That preserves the previously established rule that a completed attempt is resumable regardless of validation outcome.

## 27.2 Incomplete prior output

If an output directory exists but is incomplete/corrupt:

- do not silently treat it as complete;
- classify the prior state as incomplete;
- either rerun safely under `--resume` using a temp/staging directory, or require `--overwrite` if current code cannot safely replace partial files.

Prefer safe automatic recovery when implementation is straightforward.

Document the chosen behavior.

---

# 28. Overwrite Semantics

Provide behavior equivalent to:

```text
--overwrite
```

`--overwrite` means deliberately regenerate selected clips even if a complete attempt exists.

Safety requirements:

- never recursively delete an arbitrary user-selected directory;
- only replace the known clip output directory under the configured batch root;
- preferably write to a temporary sibling directory and atomically replace known generated artifacts;
- if atomic directory replacement is impractical, remove/replace only known generated files.

`--resume` and `--overwrite` should be mutually exclusive unless the CLI has a clearly documented combined meaning.

---

# 29. Targeted Rerun / Filter Behavior

The batch runner should support targeted selection.

Required concepts:

```text
--play <PlayName>
--video-id <ID>
--status <PASS|WARNING|FAILED>
--resume
--overwrite
```

Also support a practical selection mechanism for several clips, such as one or more of:

```text
--video-id 1 --video-id 5 --video-id 9
--video-ids 1,5,9
--clip JetSweep_1
--clip-list path/to/list.txt
--start-video-id
--end-video-id
```

Do not add every possible flag if the current CLI has a cleaner established pattern.

## 29.1 Filter order

Recommended deterministic order:

```text
discover
→ preflight
→ sort
→ play filter
→ video/clip filter
→ prior-status filter
→ optional limit
→ resume/overwrite decision
→ process
```

## 29.2 Status filter source

For:

```text
--status FAILED
```

use the most recent compatible batch manifest/summary under the selected batch output root.

Do not infer historical status merely from directory names.

If there is no prior status record, the clip should not match a historical-status filter unless current outputs can be safely classified from `validation_report.json`.

## 29.3 Rerun failed clips

Recommended command concept:

```text
batch ... --status FAILED --overwrite
```

This reruns clips that were previously `FAILED`.

For validation-FAILED clips with complete outputs, `--overwrite` is necessary because normal `--resume` would skip them.

For prior execution failures with incomplete outputs, rerun may proceed after safe cleanup/staging according to the completion policy.

---

# 30. Batch Summary Outputs

Generate concise dataset-level outputs.

Recommended:

```text
<batch_output_root>/_batch/
├── batch_manifest.csv
├── batch_manifest.json
├── batch_summary.csv
├── batch_summary.json
├── batch_summary.md
└── failures/
```

If the current project convention prefers batch files directly under the output root, that is acceptable, but keep them separate from clip directories.

## 30.1 Per-clip summary fields

At minimum:

```text
play_name
video_id
clip_name
tracking_zip
execution_state
status
warning_count
error_count
output_directory
processing_error
failure_type
```

Where available:

```text
unknown_track_count
missing_box_warning_count
ball_track_count
action_segment_count
player_track_count
```

Do not duplicate the entire `review_report.md`.

## 30.2 Batch summary JSON

Recommended envelope:

```json
{
  "schema_version": "tapevision_batch_summary_v2",
  "generated_at": "...",
  "batch_root": "...",
  "selection": {},
  "aggregate": {},
  "plays": {},
  "clips": []
}
```

Use the project's existing JSON style if different.

---

# 31. Aggregate Dataset Statistics

At minimum report:

```text
total_discovered
total_preflight_ready
total_preflight_failed
total_selected
total_attempted
PASS
WARNING
FAILED
SKIPPED
```

Also summarize by play type.

For each play:

```text
discovered
attempted
PASS
WARNING
FAILED
SKIPPED
```

Where current data supports it, aggregate:

```text
clips_with_unknown_tracks
total_unknown_tracks
clips_with_missing_box_warnings
total_missing_box_warnings
clips_with_no_ball_track
clips_with_multiple_ball_tracks
```

Do not count one warning twice under multiple ambiguous categories unless documented.

---

# 32. Batch Markdown Summary

`batch_summary.md` should be concise.

Suggested structure:

```markdown
# TapeVision Batch Summary

## Run Overview
[compact totals table]

## Results by Play
[one row per play]

## Dataset Quality Signals
[aggregate quality counts]

## Failed Clips
[clip, failure type, concise message]

## Warning Clips
[optional compact count/list, not full per-clip diagnostics]
```

Do not embed every per-clip review report into the batch Markdown.

---

# 33. Manifest and Summary Checkpointing

For a 4,000-clip run, status must survive interruption.

After each clip finishes or fails:

1. update in-memory result;
2. atomically checkpoint machine-readable manifest/summary state.

Use a safe write pattern:

```text
write temp
fsync/close as practical
os.replace(temp, final)
```

The run should not lose hundreds of completed statuses because the process stopped near the end.

---

# 34. Logging

Logging should be clip-oriented.

At minimum log:

```text
batch start
discovery count
preflight totals
current clip
play
video ID
source resolution result
processing start
processing finish
PASS/WARNING/FAILED
warning/error counts
failure stage/reason
batch aggregate finish
```

Avoid:

- per-frame logging;
- every bounding box;
- entire JSON dumps;
- repeated stack traces in normal console output.

Full traceback belongs in the failure artifact; concise message belongs in console/summary.

Recommended progress line:

```text
[142/4032] JetSweep_137  WARNING  warnings=3 errors=0  1.8s
```

---

# 35. Concurrency Policy

V1 should be sequential unless Antigravity can prove the current stabilized worker is concurrency-safe.

Before adding concurrency, inspect:

- temporary extraction paths;
- shared global state;
- config mutation;
- shared writer paths;
- caches;
- logger handlers;
- current reviewer/output readers;
- any static filenames written outside the clip output directory.

If concurrency is not clearly safe:

```text
workers = 1
```

for V1.

The design should keep each clip job self-contained so parallelism can be added later without changing annotation semantics.

If concurrency is included:

- make it configurable;
- default conservatively;
- use per-clip temp directories;
- preserve deterministic final summary ordering;
- isolate exceptions;
- avoid shared mutable config;
- keep logs readable.

Correctness has priority over throughput.

---

# 36. CLI Design

Inspect current `argparse`/CLI architecture first.

Earlier versions had:

```text
generate-and-enrich
enrich-existing
review
```

Recommended new subcommand concept:

```text
batch-generate-and-enrich
```

or the closest naming consistent with the current CLI.

Suggested options:

```text
--tracking-root
--output
--template
--dataset-summary
--actions
--plays
--config
--play
--video-id / repeatable video IDs
--status
--resume
--overwrite
--limit
--review / --no-review if review is optional
--verbose
```

Per-play CSV source location should come from the established current repository convention or a batch source mapping, not from forcing one global Key Actions file.

Do not expose dozens of low-level annotation-engine options in batch mode if the single-clip config already owns them.

---

# 37. Shared Resources and Preloading

For efficiency, batch orchestration may load immutable shared resources once if doing so does not alter single-clip semantics.

Candidates:

```text
config
actions.json definitions
plays.json definitions
DatasetSummary index
per-play CSV indexes
```

However, prefer calling existing parsers/loaders rather than implementing second parsers.

A safe batch-only index may store lookup metadata but must feed the resolved source/identity into the same single-clip worker.

Do not mutate shared parsed structures across clips.

---

# 38. Review Report Integration

The stabilized pipeline generates `review_report.md`.

Batch mode should use the same current reviewer.

Do not create a batch-specific per-clip reviewer.

Per-clip reports remain under:

```text
<output_root>/<PlayName>/<ClipName>/review_report.md
```

Batch summary may extract compact issue counts already exposed by validation/review data, but should not replicate the full report.

Preserve the latest compact Markdown presentation and semantic classifications.

---

# 39. Validation Integration

Use the existing validator output as authoritative.

Batch classification:

```python
if errors:
    status = FAILED
elif warnings:
    status = WARNING
else:
    status = PASS
```

This rule applies even when:

```text
validation.strict = false
```

Do not reinterpret individual warnings/errors in batch code.

Batch code may categorize warning messages for aggregate counting only if the categorization is already stable or clearly isolated from validation severity.

---

# 40. Mandatory JetSweep_1 Regression Baseline

This is a blocking acceptance test.

After batch implementation:

1. run `JetSweep_1` using the existing single-clip path;
2. run `JetSweep_1` through batch mode;
3. compare semantic outputs.

The annotation timelines must remain functionally equivalent.

Required baseline timelines:

## QB / actor 17

```text
PreSnap      0–131
SnapReceive  132–144
Toss         145–159
Action_None  160–329
```

## WR / actor 19

```text
PreSnap      0–95
JetMotion    96–159
BallCarry    160–329
```

## TE / actor 12

```text
PreSnap      0–132
LeadBlock    133–192
Action_None  193–329
```

## RT / actor 13

```text
PreSnap           0–132
ZoneBlock         133–164
BlockSecondLevel  165–192
Action_None       193–329
```

## Center / actor 7

```text
PreSnap      0–131
BallSnap     132–144
ZoneBlock    145–192
Action_None  193–329
```

Also verify:

- `actor_track_id` values match;
- `xml_track_id` mapping matches;
- positions match;
- team sides match;
- play/result metadata matches;
- DatasetSummary metadata matches;
- unknown/unassigned-track detection matches;
- review-report semantic findings match;
- validation warnings/errors match.

---

# 41. Semantic Comparison Strategy

Do not require byte-for-byte equality for files containing:

- timestamps;
- source paths;
- generated-at fields;
- nondeterministic formatting that is semantically irrelevant.

Create test helpers that compare stable semantic content.

For annotation JSON compare at minimum:

```text
clip identity/metadata
play metadata/result
player identities
xml_track_id
actor_track_id
position
team_side
track samples/bounds as appropriate
action labels
action start/end frames
```

For XML compare the semantic track/action attributes and frame ranges, ignoring harmless serialization differences.

The expected result is:

```text
single_clip_semantics == batch_clip_semantics
```

---

# 42. Test Requirements

Add focused batch tests without weakening current single-clip tests.

At minimum cover:

1. canonical tracking discovery;
2. malformed filename;
3. folder/play mismatch;
4. deterministic numeric video sorting;
5. unrecognized play;
6. per-play Key Actions source resolution;
7. missing Key Actions row;
8. per-play Player Track source resolution;
9. missing Player Track row;
10. legitimate multi-row Player Track assignments;
11. DatasetSummary resolution;
12. missing DatasetSummary row;
13. duplicate clip identity;
14. preflight manifest generation;
15. one successful clip;
16. multi-clip sequential success;
17. one failed clip does not stop the next clip;
18. `PASS` classification;
19. `WARNING` classification;
20. `FAILED` when validation errors are nonempty even non-strict;
21. `FAILED` on processing exception;
22. play/clip output isolation;
23. resume skips complete PASS;
24. resume skips complete WARNING;
25. resume skips validation-FAILED-but-complete;
26. incomplete output is not considered complete;
27. overwrite reruns a completed clip;
28. status filter for FAILED;
29. play filter;
30. video ID filter;
31. multiple-clip/list selection if implemented;
32. limit/smoke-test behavior;
33. batch summary CSV/JSON;
34. aggregate by-play totals;
35. unknown-track aggregate count;
36. missing-box aggregate count;
37. no-ball aggregate count when available;
38. traceback/failure artifact;
39. ZIP source is not mutated;
40. existing single-clip Mode B regression;
41. existing Mode A regression if still supported;
42. full JetSweep_1 single-vs-batch semantic equivalence.

Run the complete suite:

```bash
pytest -q
```

All tests must pass.

---

# 43. Staged Rollout

Do not go directly from implementation to all ~4,000 clips.

## Stage 1 — JetSweep_1 only

Run batch mode for:

```text
JetSweep_1
```

Compare to the stable single-clip baseline.

Stop rollout if any semantic difference exists.

## Stage 2 — 5–10 Jet Sweep clips

Verify:

- discovery;
- deterministic order;
- source resolution;
- clip output directories;
- PASS/WARNING/FAILED classification;
- manifest checkpointing;
- resume behavior;
- overwrite behavior;
- warning aggregation.

## Stage 3 — Cross-play structural sample

Run a small set across structurally different categories, including where available:

- run play;
- pass play;
- special-teams play;
- sack-related play.

Confirm per-play CSV resolution and shared metadata handling.

## Stage 4 — One complete play type

Process all clips for one play.

Review:

- batch summary;
- failure distribution;
- unknown-track counts;
- missing-box counts;
- ball coverage signals;
- resume after intentional interruption.

## Stage 5 — All 31 play types

Only after Stages 1–4 pass should full dataset processing begin.

---

# 44. Long-Term Workflow Support

The batch output/status architecture should support:

```text
batch enrichment
        ↓
batch validation/audit
        ↓
identify tracking-quality problems
        ↓
manual/future cleanup
        ↓
rerun selected affected clips
        ↓
updated outputs
```

This means:

- stable clip identity;
- isolated clip output directory;
- persisted status;
- targeted rerun selection;
- overwrite;
- batch summary fields suitable for spreadsheet filtering.

Do not bind reruns to transient process memory.

---

# 45. Likely Files to Inspect Before Editing

Antigravity must inspect the current versions of at least:

```text
README.md
pyproject.toml
requirements.txt
configs/default_config.yaml
```

Core:

```text
src/tapevision_enricher/cli.py
src/tapevision_enricher/pipeline_generate_and_enrich.py
src/tapevision_enricher/enricher.py
src/tapevision_enricher/output_pipeline.py          # if present
src/tapevision_enricher/config.py
src/tapevision_enricher/models.py
```

Inputs/mapping:

```text
src/tapevision_enricher/mot_parser.py
src/tapevision_enricher/player_track_sheet_parser.py
src/tapevision_enricher/wide_action_csv_parser.py
src/tapevision_enricher/action_event_normalizer.py
src/tapevision_enricher/sheet_group_resolver.py
src/tapevision_enricher/cvat_xml_generator.py
src/tapevision_enricher/cvat_xml_parser.py
```

Timing — inspect, but do not redesign:

```text
src/tapevision_enricher/action_rules.py
any current action endpoint/frame-role resolver modules
any current complete-timeline helper
```

Metadata/definitions:

```text
current DatasetSummary loader/parser
current actions.json loader
current plays.json loader
```

Validation/review:

```text
src/tapevision_enricher/validators.py
src/tapevision_enricher/reviewer.py
```

Writers:

```text
src/tapevision_enricher/writers/*
```

Tests:

```text
tests/*
```

Actual data/source conventions:

```text
data/tracking/
current per-play Key Actions directories/files
current per-play Player Track assignment directories/files
DatasetSummary.csv
actions.json
plays.json
shared CVAT template
```

---

# 46. Recommended New/Changed Modules

Exact names must follow the current repository after inspection.

A clean design would likely add or reuse:

```text
src/tapevision_enricher/batch_pipeline.py
```

for orchestration.

Optionally:

```text
src/tapevision_enricher/batch_discovery.py
src/tapevision_enricher/batch_manifest.py
src/tapevision_enricher/writers/batch_report_writer.py
```

only if `batch_pipeline.py` would otherwise become too large.

Prefer a small number of cohesive modules.

If the current codebase already contains an earlier batch implementation or `output_pipeline.py`, extend/reuse it rather than creating parallel replacements.

Likely modifications:

```text
cli.py
README.md
config.py/default_config.yaml   # only for batch configuration if needed
writers/__init__.py             # only if adding writer exports
```

Do not modify timing modules for batch behavior.

---

# 47. Recommended Data Structures

Use current project conventions.

Suggested batch-only records:

## DiscoveredClip

```text
source_path
relative_path
folder_play_name
filename_play_name
video_id
clip_name
discovery_index
```

## ResolvedClipInputs

```text
play_name
video_id
clip_name
tracking_zip
key_actions_csv
player_tracks_csv
dataset_summary_identity
template
actions_json
plays_json
output_dir
preflight_status
preflight_messages
```

## BatchClipResult

```text
clip identity
execution_state
status
warnings/errors
metrics
quality counters
elapsed time
failure type
processing error
traceback path
```

Do not put core annotation objects into batch-specific models unless necessary.

---

# 48. Recommended Implementation Order

Antigravity should implement in this order.

## Phase 1 — Reconstruct current single-clip path

Document internally:

```text
CLI entry
→ worker
→ metadata/definition loaders
→ output finalizer
→ validation
→ review
```

Identify actual output filenames.

## Phase 2 — Verify JetSweep_1 baseline

Before batch changes, run current tests and preserve the stable baseline.

Create a semantic fixture/snapshot helper if one does not exist.

## Phase 3 — Shared output finalization

If writer calls are still embedded in CLI, extract a behavior-preserving reusable finalizer.

Run full regression tests.

If already shared, skip this phase.

## Phase 4 — Discovery and identity parsing

Implement:

- tracking-root discovery;
- filename parser;
- folder/play verification;
- deterministic sorting.

Test independently.

## Phase 5 — Per-play source resolver

Resolve:

- Key Actions CSV;
- Player Track CSV;
- DatasetSummary;
- shared definitions/template.

Reuse existing parsers.

## Phase 6 — Preflight + manifest

Create all resolved jobs before enrichment.

Write manifest.

## Phase 7 — Sequential batch orchestrator

Invoke the existing worker one clip at a time.

Add per-clip failure isolation.

## Phase 8 — Status classification

Implement `PASS/WARNING/FAILED` from existing validation results.

## Phase 9 — Resume/overwrite/status filters

Implement semantic completion checking and rerun controls.

## Phase 10 — Batch summaries

CSV/JSON/Markdown aggregate outputs.

## Phase 11 — CLI

Expose batch command and filters.

## Phase 12 — Tests

Run all focused tests and full suite.

## Phase 13 — Staged rollout

JetSweep_1 → 5–10 JetSweep → mixed plays → full play → dataset.

---

# 49. Acceptance Criteria

Implementation is accepted only when all are true.

## Architecture

- [ ] Batch mode calls the same single-clip annotation/enrichment path.
- [ ] No second timing engine exists.
- [ ] No duplicated JSON/XML writer pipeline exists.
- [ ] No automatic tracking repair exists.

## Discovery/preflight

- [ ] `data/tracking/<PlayName>/*_cvat_mot.zip` discovery works.
- [ ] folder/filename play mismatch is reported.
- [ ] filename identity is deterministic.
- [ ] per-play Key Actions resolve.
- [ ] per-play Player Track assignments resolve.
- [ ] DatasetSummary resolves.
- [ ] shared actions/plays/template/config resolve.
- [ ] preflight failures are explicit.

## Outputs

- [ ] Each clip writes to `<output>/<PlayName>/<ClipName>/`.
- [ ] Source ZIP is unchanged.
- [ ] Output filenames match the current single-clip pipeline.
- [ ] Review report remains the current `review_report.md`.

## Status

- [ ] zero errors/zero warnings → `PASS`.
- [ ] zero errors/nonzero warnings → `WARNING`.
- [ ] nonzero validation errors → `FAILED` regardless of strict mode.
- [ ] processing exception → `FAILED`.
- [ ] failed clip does not stop next clip.
- [ ] `SKIPPED` is execution state, not a replacement for semantic status.

## Resume/rerun

- [ ] completion requires the real required output set, not one file.
- [ ] `--resume` skips complete PASS.
- [ ] `--resume` skips complete WARNING.
- [ ] `--resume` skips complete validation-FAILED attempt.
- [ ] incomplete output is not treated as completed.
- [ ] `--overwrite` deliberately reruns selected completed clips.
- [ ] failed clips can be targeted by prior status.
- [ ] play/video selection works.

## Reporting

- [ ] generated manifest exists.
- [ ] machine-readable summary exists.
- [ ] human-readable batch summary exists.
- [ ] by-play totals exist.
- [ ] unknown-track aggregates exist where supported.
- [ ] missing-box aggregates exist where supported.
- [ ] ball-track aggregate exists where supported.
- [ ] failures include concise reason and traceback reference.

## Regression

- [ ] all preexisting tests pass.
- [ ] new batch tests pass.
- [ ] JetSweep_1 single-clip and batch semantic outputs are equivalent.
- [ ] mandatory JetSweep_1 timelines remain exactly as specified.
- [ ] unknown/unassigned-track behavior remains unchanged.

---

# 50. Required Antigravity Final Implementation Report

When Antigravity finishes implementation, it must report:

1. exact files added;
2. exact files modified;
3. the current single-clip function/path reused by batch mode;
4. actual output filenames used;
5. actual per-play source-resolution convention;
6. batch CLI command and all new options;
7. completion/resume rule;
8. overwrite rule;
9. status-filter behavior;
10. manifest and summary file locations;
11. concurrency policy implemented;
12. ZIP extraction/cleanup behavior;
13. how unknown-track/missing-box/ball counts are derived;
14. any deviations from this specification;
15. full `pytest -q` result;
16. JetSweep_1 single-vs-batch comparison result;
17. confirmation of each required JetSweep_1 timeline;
18. results of the Stage 2 small JetSweep batch if run;
19. any remaining risks before a 4,000-clip run.

Do not state the feature is ready for full dataset execution if the JetSweep_1 semantic comparison fails.

---

# 51. Conflicts With Earlier Batch Specifications

This v2 specification intentionally supersedes earlier batch guidance in the following areas.

## 51.1 Earlier one-play-per-invocation recommendation

Earlier guidance recommended one play type per batch invocation because Key Actions and Player Track CSVs are separate by play.

That is now superseded.

The current tracking tree is explicitly organized across all play folders under:

```text
data/tracking/
```

and batch processing should support a dataset-root run across multiple plays by resolving the proper per-play CSV pair.

`--play` remains a filter for one-play runs.

## 51.2 Earlier output filenames

Earlier repository versions used:

```text
enriched_cvat.xml
tapevision_annotations.json
review_report.txt
```

The stabilized project now has newer behavior, including Markdown review output, and may have finalized:

```text
annotations.xml
annotations.json
review_report.md
```

The current single-clip writer path is authoritative.

Do not restore older filenames merely because an older batch spec mentioned them.

## 51.3 Earlier action timing assumptions

Earlier batch work preceded the stabilized timing engine.

This specification freezes the current timing engine and the explicit JetSweep_1 baseline.

No older batch rule may override current:

- frame roles;
- paired/cross-actor endpoint behavior;
- Center priority;
- complete timeline behavior.

## 51.4 DatasetSummary/actions/plays integration

The current single-clip pipeline now loads:

```text
DatasetSummary.csv
actions.json
plays.json
```

These are required batch-resolved/shared sources.

Any earlier batch implementation that ignored them is incomplete.

## 51.5 Review report

The current report is:

```text
review_report.md
```

with current reviewer semantics/presentation.

Do not use older `review_report.txt` assumptions.

---

# 52. Decisions and Verification Still Needed Before Implementation

No major **product-level design decision** remains unresolved in this specification.

The required behavior is sufficiently defined for implementation.

However, Antigravity must verify the following **repository facts** in its current checkout before coding:

1. the exact current single-clip worker function(s);
2. whether shared output finalization already exists;
3. the exact final annotation XML/JSON filenames;
4. the exact current paths/naming convention of all per-play Key Actions CSVs;
5. the exact current paths/naming convention of all per-play Player Track CSVs;
6. the exact current DatasetSummary loader and unique lookup key;
7. the exact current `actions.json` and `plays.json` loaders/paths;
8. the exact shared CVAT template path;
9. whether review generation is mandatory or optional in the stabilized normal run;
10. whether the current MOT ZIP importer already cleans extraction directories.

These are implementation-discovery items, not reasons to redesign the feature.

If the current repository does **not** provide a deterministic per-play CSV path convention, the only implementation choice Antigravity may need to make is to introduce a small **per-play source mapping in batch configuration**. It must not introduce a manual per-clip manifest.

---

# 53. Final Directive

The success criterion is not merely:

```text
"4,000 files can be looped over."
```

The success criterion is:

> The exact stabilized single-clip TapeVision annotation pipeline can be applied deterministically, safely, audibly, and resumably across the complete dataset without changing annotation semantics.

When there is tension between batch convenience and semantic stability, preserve semantic stability.
