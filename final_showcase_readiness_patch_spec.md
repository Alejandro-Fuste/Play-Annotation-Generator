# Final Showcase Readiness Patch — Antigravity Implementation Specification

## Purpose

Finish the remaining showcase-dataset readiness work in `Play-Annotation-Generator` before generating the full curated employer-facing sample.

Repository:

`https://github.com/Alejandro-Fuste/Play-Annotation-Generator`

Use the current `main` branch as the baseline.

This task is intentionally narrow and contains only:

1. implement the already-configured Handoff termination rule;
2. support the intentionally non-temporal RPO `Route` notation such as `post,7`;
3. update the showcase manifest from 51 clips to 50 clips;
4. perform minor source-metadata cleanup that does not alter annotation semantics;
5. run a focused five-clip regression;
6. run the readiness audit after the focused regression.

Do **not** generate all 50 showcase clips in this task.
Do **not** run a full-dataset batch.
Do **not** create the public showcase GitHub repository in this task.

---

## 1. Current Confirmed Source State

### Counter_1

Authoritative PlayerTrack identities:

```text
C   = track 11
LB3 = track 17
```

Authoritative Key Actions:

```text
Ball Snap       = 348,11
Play-side step  = 358,12
Down Blocks     = 361,11,18,21
Pull Block      = 361,15
Pull Lead Block = 361,5
Snap Receive    = 361,16
Handoff         = 381,16
Ball Carry      = 388,12
End OL Block    = 438
```

Do not change these values.

### KickoffReturnTouchdown_6

The returner undergoes a real MOT ID switch.

Intended identities:

```text
Catch Kick       = 249–253, track 50
Ball Carry       = 283, track 61
Cross Goal Line  = 687–690, track 61
```

This is intentional. Do not force one track ID across the entire return.

### RPO_1

Current source notation:

```text
Route = post,7
```

This means:

```text
route_type = post
actor_track_id = 7
```

It intentionally does **not** contain a frame. Do not fabricate a frame.

### PlayerTrack `[?]`

The showcase may legitimately contain `[?]` PlayerTrack entries when the model never assigned a usable track ID. These remain review warnings, not blockers.

---

## 2. Frozen Behavior

Do not modify:

- tracking ZIP contents;
- source Key Actions frame values;
- source PlayerTrack values except the harmless Counter metadata-name correction specified below;
- `plays.json` taxonomy;
- `actions.json` taxonomy;
- migration code/manifests;
- actor_track_id ↔ xml_track_id behavior;
- explicit `start,end,track_id` semantics;
- semicolon continuation behavior already fixed;
- canonical play-label resolution already fixed;
- special-teams team-side row logic already fixed;
- special-teams PreSnap boundary logic already fixed;
- Long Snap timing behavior already fixed;
- Action_None complete-visible-frame coverage;
- Ball Snap / Snap Receive paired semantics;
- Toss → Ball Carry behavior;
- Center priority behavior;
- resume/overwrite behavior.

No unrelated refactors.

---

## 3. Implement Generic `ends_when_any_action_starts`

The configuration already contains:

```python
"Action_Handoff": {
    "ends_when_any_action_starts": [
        "Action_TakeHandoff",
        "Action_BallCarry"
    ]
}
```

The timing engine currently does not generally execute this configured rule.

Implement it in `infer_action_segments()`.

### Required semantics

For an action with:

```text
ends_when_any_action_starts = [A, B, ...]
```

and no explicit `end_frame`:

1. search all resolved events for the configured target action types;
2. consider only target events whose annotated/start frame is strictly greater than the current segment start;
3. find the earliest qualifying target frame;
4. set:

```text
segment_end = target_start - 1
```

This is a cross-actor rule. The target action does not need to belong to the same player.

### Precedence

Preserve this order:

```text
1. explicit source end_frame
2. existing hard/special cross-actor rule
3. configured ends_when_any_action_starts
4. terminal action rule
5. next same-actor explicit action - 1
6. applicable boundary
7. normal fallback
```

Do not let the new generic rule override explicit ranges.
Do not alter `Action_Toss` behavior.

---

## 4. Counter_1 Handoff Regression

For the authoritative Counter_1 source:

```text
Handoff starts    = 381
Ball Carry starts = 388
```

Expected generated result:

```text
Action_Handoff   381–387
Action_BallCarry 388–509
```

The Handoff actor is QB track 16.
The Ball Carry actor is RB track 12.

The rule must work even though the terminating Ball Carry belongs to a different actor.

Add a focused unit/regression test.

The generated Counter_1 review report must show:

```text
Action_Handoff | actor 16 | 381–387
Action_BallCarry | actor 12 | 388–...
```

---

## 5. Non-Temporal RPO Route Descriptor

`RPO.csv` contains values such as:

```text
post,7
slant,3
```

for the `Route` column.

These encode:

```text
route concept + actor track ID
```

They do **not** encode a start frame.

The current generic temporal parser treats `post` as a malformed frame. That behavior is incorrect for this column.

### Required design

Handle the `Route` column for RPO as a **non-temporal action descriptor**.

For:

```text
post,7
```

store:

```text
route_type = post
actor_track_id = 7
canonical_action = Action_RunPostRoute
```

For:

```text
slant,3
```

store:

```text
route_type = slant
actor_track_id = 3
canonical_action = Action_RunSlantRoute
```

If other currently supported RPO route strings exist, preserve the existing route-name mapping where valid.

### Critical constraint

Do **not** create a timed `ActionSegment` for a non-temporal Route descriptor.
Do **not** assign `frame = 0`.
Do **not** infer a frame.
Do **not** add it to the dense per-frame action timeline.

It is metadata describing the annotated receiver/route concept.

---

## 6. Representation of Non-Temporal Route Metadata

Prefer the smallest architecture change that cleanly preserves this information.

Acceptable approaches include:

- a dedicated non-temporal descriptor structure;
- row metadata carried into annotation JSON/review output;
- a separate list such as `non_temporal_action_descriptors`.

Do not misuse `ActionEvent.start_frame` with a fake value.

Minimum information that must survive:

```text
source_column: Route
raw_value: post,7
canonical_action: Action_RunPostRoute
actor_track_id: 7
temporal: false
```

The review report should make this visible, for example:

```text
Non-Temporal Action Descriptor:
Action_RunPostRoute | actor_track_id 7 | source Route | no temporal frame
```

Exact formatting may differ.

---

## 7. RPO Readiness Behavior

The readiness audit must special-case only the supported non-temporal RPO Route format.

For valid values such as:

```text
post,7
slant,3
```

the audit must:

- validate the route name;
- validate that the actor track ID is present and syntactically valid;
- accept the cell;
- not require a frame;
- not classify the clip as BLOCKED merely because the Route has no frame.

Invalid examples should still block:

```text
post
,7
unknownroute,7
post,[?]
```

unless an existing intentional policy explicitly allows them.

Do not loosen parsing for unrelated action columns.

---

## 8. RPO_1 Acceptance Criteria

`RPO_1` must no longer be BLOCKED because of:

```text
Route = post,7
```

The output/review must retain:

```text
canonical route = Action_RunPostRoute
actor_track_id = 7
temporal = false
```

It must create:

```text
0 fabricated timed Action_RunPostRoute segments
```

Existing temporal RPO actions must remain unchanged.

---

## 9. Showcase Manifest Cleanup

Update:

```text
data/showcase/showcase_clips.json
```

### Replace OutAndUp

Remove:

```text
OutAndUp_1
```

Add:

```text
OutAndUp_3
```

Use:

```json
{
  "logical_clip_name": "OutAndUp_3",
  "play_name": "OutAndUp",
  "video_id": "3",
  "tracking_source": "data/tracking/OutAndUp/OutAndUp_3_cvat_mot.zip",
  "key_actions_source": "data/key_actions/OutAndUp.csv",
  "player_tracks_source": "data/player_tracks/OutAndUp.csv"
}
```

Verify the tracking path exists before accepting the manifest.

### Remove Post10to15_2

Remove:

```text
Post10to15_2
```

Keep:

```text
Post10to15_1
```

No replacement Post10to15 clip is required.

### Expected final count

The manifest must contain exactly:

```text
50 clips
```

Add a test asserting:

```text
len(manifest) == 50
OutAndUp_3 present
OutAndUp_1 absent
Post10to15_1 present
Post10to15_2 absent
```

---

## 10. Minor Counter Metadata Cleanup

In:

```text
data/player_tracks/Counter.csv
```

change only:

```text
Video Name:,JetSweep_
```

to:

```text
Video Name:,Counter_
```

Do not alter Counter PlayerTrack rows or track IDs in this task.

---

## 11. PuntReturnTouchdown_2 Source Check

Before running regression/audit, verify that the user's corrected numeric `Cross Goal Line` value for:

```text
PuntReturnTouchdown_2
```

is present in `main`.

The final row must no longer contain:

```text
?,20
```

If the repository still contains `?,20`, do not guess the frame and do not modify it automatically.

Report:

```text
SOURCE UPDATE STILL REQUIRED
```

and leave `PuntReturnTouchdown_2` BLOCKED.

If the corrected numeric frame is present, proceed normally.

---

## 12. KickoffReturnTouchdown_6 ID-Switch Behavior

Do not require Catch Kick, Ball Carry, and Cross Goal Line to share one actor_track_id.

Expected source identity transition:

```text
Catch Kick       -> track 50
Ball Carry       -> track 61
Cross Goal Line  -> track 61
```

The regression must validate the events independently.

Required behavior:

```text
Catch Kick:
- action exists
- source range 249–253 preserved
- actor 50

Ball Carry:
- action exists
- begins at 283
- actor 61

Cross Goal Line:
- action exists
- source range 687–690 preserved
- actor 61
```

If track visibility prevents an explicit source action from becoming a segment, report that as a tracking/ID-switch continuity issue. Do not silently move the annotated start frame.

Do not shift an explicit range to the first visible frame and call it an exact match.

---

## 13. Five-Clip Regression Set

After implementation, generate only:

```text
Counter_1
KickoffReturnTouchdown_6
OutAndUp_3
PuntReturnTouchdown_2
RPO_1
```

Use a fresh output root:

```text
output_showcase_final_regression/
```

Recommended command:

```bash
PYTHONPATH=src ./venv/bin/python   -m play_annotation_generator.showcase   --manifest data/showcase/showcase_clips.json   --output output_showcase_final_regression   --clips Counter_1,KickoffReturnTouchdown_6,OutAndUp_3,PuntReturnTouchdown_2,RPO_1   --review
```

If `PuntReturnTouchdown_2` is still source-blocked, skip generation for that clip after clearly reporting the blocker, or run the other four and report it as not generated.

Do not fabricate the missing source frame.

---

## 14. Regression Acceptance Criteria

### Counter_1

Require:

```text
Play = Play_Run_Counter
Center = track 11
LB3 = track 17
Ball Snap = actor 11
Handoff = actor 16, frames 381–387
Ball Carry = actor 12, starts 388
no duplicate assignment warning for track 11
0 validation errors
```

### KickoffReturnTouchdown_6

Require:

```text
Play = Play_SpecialTeams_KickoffReturnTouchdown
Catch Kick = actor 50, explicit 249–253
Ball Carry = actor 61, starts 283
Cross Goal Line = actor 61, explicit 687–690
no missing expected action for those three source annotations
0 validation errors
```

Tracking-quality warnings may remain.

### OutAndUp_3

Require:

```text
Play = canonical OutAndUp play label
Ball Snap parses
Pass Block parses
Snap Receive parses
Throw Pass explicit 103–113 preserved
Sell Out explicit 51–80 preserved
Run Go Route parses
0 malformed required-action errors
0 validation errors
```

### PuntReturnTouchdown_2

If corrected source exists:

```text
Cross Goal Line has numeric frame/range
event parses
expected segment exists
0 malformed required-action errors
0 validation errors
```

If source still says `?,20`:

```text
BLOCKED
```

and report source correction is still required.

### RPO_1

Require:

```text
Play = canonical RPO play label
Route post,7 accepted
route descriptor canonical action = Action_RunPostRoute
route descriptor actor = 7
temporal = false
0 fabricated RunPostRoute timed segments
clip not BLOCKED because Route lacks a frame
0 validation errors
```

---

## 15. Tests

Add/update focused tests for:

### Handoff generic configured termination

Synthetic:

```text
Action_Handoff start 100 actor A
Action_BallCarry start 120 actor B
```

Expected:

```text
Handoff = 100–119
```

Also test that an explicit Handoff end takes precedence.

### Counter regression

Use Counter_1 data and assert:

```text
Handoff 381–387
BallCarry starts 388
```

### Non-temporal RPO Route

Assert:

```text
post,7 -> valid non-temporal Action_RunPostRoute descriptor for actor 7
slant,3 -> valid non-temporal Action_RunSlantRoute descriptor for actor 3
```

Assert no timed segment is generated.

Assert malformed route descriptors still block.

### Manifest

Assert exactly 50 entries and correct inclusion/exclusion.

### KRT ID switch

Assert independent actor IDs are retained for:

```text
CatchKick actor 50
BallCarry actor 61
CrossGoalLine actor 61
```

Do not require one continuous actor ID.

---

## 16. Readiness Audit After Regression

After the five-clip regression, run:

```bash
PYTHONPATH=src ./venv/bin/python   -m play_annotation_generator.showcase   --manifest data/showcase/showcase_clips.json   --audit
```

Expected manifest count:

```text
50
```

Expected policy:

- `[?]` PlayerTrack values remain review warnings;
- valid RPO non-temporal Route does not block;
- malformed required temporal actions still block;
- no unmapped populated action columns;
- no unresolved canonical play labels.

Do not generate all 50 clips yet.

---

## 17. Full Test Suite

Run focused tests first.

Then run:

```bash
PYTHONPATH=src ./venv/bin/pytest -q
```

The two known pre-existing migration-state failures may remain only if they are exactly the same previously documented failures in:

```text
test_outside_zone_qb_zone_read_migration.py
```

No new failures are acceptable.

---

## 18. Final Antigravity Report

Report:

1. files changed;
2. implementation of generic `ends_when_any_action_starts`;
3. Counter_1 generated Handoff and Ball Carry ranges;
4. RPO non-temporal descriptor representation;
5. RPO_1 route descriptor output;
6. manifest changes and final count;
7. confirmation that `OutAndUp_3` replaced `OutAndUp_1`;
8. confirmation that `Post10to15_2` was removed;
9. Counter metadata-prefix cleanup;
10. whether `PuntReturnTouchdown_2` source correction is present;
11. focused test results;
12. full pytest results;
13. five-clip regression table with status, validation errors, warnings, and expected-action audit status;
14. updated 50-clip readiness audit counts;
15. remaining BLOCKED clips, if any;
16. whether the 50-clip showcase is ready for the final generation run.

Do not run the 50-clip generation yet.
Do not create the public showcase GitHub repository yet.
