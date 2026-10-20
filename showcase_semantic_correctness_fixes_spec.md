# Showcase Semantic Correctness Fixes — Antigravity Specification

## Goal

Fix the remaining semantic correctness issues in `Play-Annotation-Generator` before generating the employer-facing showcase dataset.

Repository:
`https://github.com/Alejandro-Fuste/Play-Annotation-Generator`

Use current `main`.

This task addresses six issues:

1. multi-player semicolon continuation cells are parsed incorrectly;
2. some showcase clips fall back to the wrong play label (`Play_Run_JetSweep`);
3. special-teams team-side assignment is wrong because normal football position heuristics are being used;
4. special-teams PreSnap timing can extend too far;
5. malformed required Key Action cells are treated as warnings instead of blockers;
6. approximate action aliases need an explicit semantic audit.

Do not create the public showcase repo.
Do not run the full dataset batch.
Do not generate all 51 showcase clips in this task.

---

## Frozen behavior

Do not modify:

- tracking ZIP contents;
- source Key Actions values;
- source PlayerTrack values;
- `plays.json` taxonomy;
- `actions.json` taxonomy unless separately approved;
- migration logic/manifests;
- actor_track_id ↔ xml_track_id behavior;
- explicit `start,end,track_id` semantics;
- Action_None complete-visible-timeline behavior;
- Ball Snap / Snap Receive semantics for normal plays;
- Toss → Ball Carry logic;
- Center priority logic;
- resume/overwrite semantics.

No unrelated refactors.

---

## 1. Fix multi-player semicolon continuation parsing

The source convention:

```text
52,19;14;20;18
```

means:

```text
frame 52 actor 19
frame 52 actor 14
frame 52 actor 20
frame 52 actor 18
```

The current parser incorrectly interprets the bare `14`, `20`, and `18` tokens as independent/global frame entries.

Update `parse_cell_entries()` so it correctly supports all of these formats:

```text
52,19
```

→ one event: frame 52, actor 19

```text
52,19;55,14
```

→ frame 52 actor 19; frame 55 actor 14

```text
52,19;14;20;18
```

→ frame 52 for actors 19,14,20,18

```text
361,11,18,21
```

→ frame 361 for actors 11,18,21

```text
191,261,OL
```

→ explicit range 191–261 for group OL

```text
20,30,4;40,50,7
```

→ actor 4 range 20–30; actor 7 range 40–50

### Parsing rule

For semicolon-separated entries:

- a complete tuple establishes the current frame/range context;
- a following bare numeric token inherits the most recent valid frame;
- a following full tuple starts a new context;
- malformed tokens never inherit a fabricated frame;
- bare continuation actor IDs must not become global events.

Preserve newline and pipe separators.

---

## 2. Duo_1 regression

The authoritative source row is now:

```text
Duo_1
Combo Blocks = 52,19;14;20;18
```

Expected parsed events:

```text
Action_ComboBlock frame 52 actor 19
Action_ComboBlock frame 52 actor 14
Action_ComboBlock frame 52 actor 20
Action_ComboBlock frame 52 actor 18
```

There must be zero global ComboBlock events at frames 14, 20, or 18.

Add both:
- a direct parser unit test;
- a Duo_1 regression test.

---

## 3. Fix canonical play-label resolution

Current bug: unrelated plays can fall back to:

```text
Play_Run_JetSweep
```

Examples previously observed:

```text
Duo_1
QuickScreens_1
FieldGoalBlock_3
```

Remove this fallback:

```python
p_tag = inferred_play if inferred_play else "Play_Run_JetSweep"
```

Resolve play tags from authoritative `data/plays.json`.

The logical play identity is already available from:
- showcase manifest;
- tracking folder/file;
- Key Actions metadata prefix;
- target video name.

Map the known play name to the exact formatted canonical play label from `plays.json`.

Do not hardcode run/pass prefixes when the formatted label already exists.

If a play cannot resolve:

```text
ERROR / BLOCKED
```

Never substitute JetSweep.

Add regression checks for:

```text
BootPass_1
Counter_1
Duo_1
QuickScreens_1
FieldGoalBlock_3
JetSweep_1
```

A non-JetSweep play must never receive the JetSweep play label.

---

## 4. Fix special-teams team-side assignment

Current grid parsing infers offense/defense from position strings. This breaks special-team roles such as:

```text
Holder
Long_Snapper
Interior_Rusher
FG_Block_Support
```

Use the annotation sheet row structure instead.

For positional-grid PlayerTrack sheets:

```text
first row for a Video #  = offense / kicking or possession team
second row for a Video # = defense / return or block team
```

Assign `team_side` from row order.

Preserve explicit `team_side` values in normalized formats.

Use the old position-name heuristic only as fallback when neither explicit team_side nor paired-row structure is available.

Add representative tests for:

```text
FieldGoalBlock_3
PuntBlock_1
KickoffReturnTouchdown_6
```

For `FieldGoalBlock_3`, first-row roles such as Long_Snapper, Holder, Kicker must be offense; second-row rush/block roles must be defense.

---

## 5. Fix special-teams PreSnap termination

Normal scrimmage plays keep current Ball Snap fallback behavior.

Add a play-start boundary fallback for special teams.

### Punt family

```text
PuntBlock
PuntCoverage
PuntReturnTouchdown
```

Use:

```text
Long Snap start frame
```

Therefore:

```text
PreSnap end = LongSnap start - 1
```

for players with no earlier explicit action.

### Field goal family

```text
FieldGoalBlock
```

Use Long Snap start frame.

### Kickoff / onside family

```text
KickoffReturnTouchdown
OnsideKickRecovery
```

Use:

```text
Kick Approach start frame
```

If unavailable, fall back to:

```text
Kick Ball start frame
```

The existing primary rule remains:

```text
next same-actor explicit action - 1
```

The special-team event is only the global fallback.

---

## 6. Prevent Long Snap from stretching through the play

For `Action_LongSnap`:

1. preserve explicit range if source provides one;
2. otherwise use next same-actor explicit action - 1 if available;
3. otherwise stop at the first continuous visible-segment break after the start, or another existing defensible boundary;
4. do not stretch Long Snap automatically to play end.

If a safe end cannot be inferred, issue a review warning rather than fabricating a long segment.

Apply the same caution to other short special-team transition actions where appropriate.

Do not introduce arbitrary fixed frame durations.

---

## 7. Make malformed required action cells BLOCKED

The readiness audit currently treats parse failures as warnings.

These must be blockers:

```text
?,51
,17
,OL
,15
post,7
```

If a populated required action cell cannot produce at least one valid `ActionEvent`:

```text
BLOCKED
```

Do not invent frames.

For `RPO_1`, `post,7` can identify the route concept but does not provide a numeric frame, so the clip remains BLOCKED until source data is corrected.

Warnings may remain for tracking-quality issues such as:
- missing boxes;
- Position_Unknown from `[?]`;
- no ball track;
- fragmented tracking.

---

## 8. Readiness classification

Use:

```text
READY_CLEAN
READY_WITH_REVIEW_WARNINGS
BLOCKED
```

A clip is BLOCKED if any of these occur:

- missing tracking source;
- missing Key Actions row;
- missing PlayerTrack row;
- unmapped populated action column;
- mapped action missing from `actions.json`;
- malformed required action cell;
- canonical play label unresolved;
- generation validation errors.

---

## 9. Audit approximate semantic aliases

Review these mappings explicitly:

```text
Pass Drop -> Action_FakePassDroptoHandoff
Clear Out Route -> Action_ClearToEdge
Dig Route -> Action_BreakInside
Sell Slant -> Action_SellRoute
Run Go Route -> Action_VerticalStem
Press Interior Gap -> Action_PressGap
Onside Kick -> Action_KickBall
```

Create an explicit audit table in code/tests with:

```text
source header
mapped canonical action
classification
reason
```

Classification:

```text
EXACT
INTENTIONAL_ALIAS
NEEDS_SOURCE_REVIEW
```

Rules:
- true synonyms may remain;
- partial or meaning-changing substitutions must be `NEEDS_SOURCE_REVIEW`;
- showcase clips that depend on `NEEDS_SOURCE_REVIEW` mappings must be BLOCKED;
- do not add new taxonomy entries automatically.

The final report must explain each mapping decision.

---

## 10. Validate parsed event counts

For each populated action cell, readiness should record:

```text
source column
source cell
parsed event count
expected event count where determinable
```

Examples:

```text
52,19;14;20;18
expected = 4
```

```text
361,11,18,21
expected = 3
```

```text
191,261,OL
expected = 1
```

If a populated non-result action cell produces zero events:

```text
BLOCKED
```

---

## 11. Required tests

Add/update tests for:

### Parser
```text
52,19
52,19;55,14
52,19;14;20;18
361,11,18,21
191,261,OL
20,30,4;40,50,7
```

### Duo
Assert exactly four ComboBlock events at frame 52 for:
```text
19,14,20,18
```

and zero global ComboBlock artifacts.

### Play labels
Assert correct canonical play label for:
```text
BootPass_1
Counter_1
Duo_1
QuickScreens_1
FieldGoalBlock_3
JetSweep_1
```

### Special-team row-side assignment
Test:
```text
FieldGoalBlock_3
PuntBlock_1
KickoffReturnTouchdown_6
```

### Special-team PreSnap
Assert:
```text
PuntBlock -> Long Snap - 1
FieldGoalBlock -> Long Snap - 1
KickoffReturnTouchdown -> Kick Approach - 1
OnsideKickRecovery -> Kick Approach - 1
```

### Malformed cells
Assert BLOCKED for:
```text
?,51
,17
,OL
,15
post,7
```

### Alias audit
Assert every approximate alias has an explicit classification.

---

## 12. Validation sequence

### Stage A — focused tests

Run focused tests for:
- semicolon continuation;
- Duo_1;
- canonical play labels;
- special-team team-side assignment;
- special-team PreSnap timing;
- malformed-cell blocking;
- semantic alias audit.

### Stage B — full suite

Run:

```bash
PYTHONPATH=src ./venv/bin/pytest -q
```

The two known post-migration baseline failures may remain only if they are still the same pre-existing migration-state issue.

No new failures are acceptable.

### Stage C — readiness audit

Run:

```bash
PYTHONPATH=src ./venv/bin/python \
  -m play_annotation_generator.showcase \
  --audit
```

Confirm:
- zero unmapped populated action columns;
- malformed required cells are BLOCKED;
- play labels resolve canonically;
- no JetSweep fallback remains.

### Stage D — fresh focused smoke generation

Generate only:

```text
Duo_1
QuickScreens_1
FieldGoalBlock_3
PuntBlock_1
KickoffReturnTouchdown_6
Counter_1
```

Use a fresh output directory:

```text
output_showcase_semantic_fix/
```

Do not overwrite previous smoke evidence.

---

## 13. Acceptance criteria

### Duo_1
```text
4 ComboBlock events at frame 52
actors = 19,14,20,18
no global ComboBlock artifacts
correct canonical Duo play label
```

### QuickScreens_1
```text
correct QuickScreens canonical play label
not Play_Run_JetSweep
```

### FieldGoalBlock_3
```text
correct FieldGoalBlock canonical play label
first PlayerTrack row = offense/kicking team
second PlayerTrack row = defense/block team
PreSnap fallback ends at Long Snap - 1
Long Snap does not persist across unrelated later visibility fragments
```

### PuntBlock_1
```text
correct row-side team assignment
PreSnap fallback ends at Long Snap - 1
```

### KickoffReturnTouchdown_6
```text
correct team-side assignment
PreSnap fallback ends at Kick Approach - 1
```

### Showcase audit
```text
malformed required cells are BLOCKED
canonical play identity always resolves
no silent action omission
```

---

## 14. Final Antigravity report

Report:

1. files changed;
2. parser behavior before/after;
3. Duo_1 ComboBlock event list;
4. canonical play-label changes;
5. special-team team-side logic;
6. special-team PreSnap rules;
7. Long Snap timing behavior;
8. malformed-cell blocking behavior;
9. semantic alias audit table;
10. focused test results;
11. full pytest result;
12. updated showcase audit counts;
13. smoke-test results for:
   - Duo_1
   - QuickScreens_1
   - FieldGoalBlock_3
   - PuntBlock_1
   - KickoffReturnTouchdown_6
   - Counter_1
14. remaining BLOCKED showcase clips.

Do not generate all 51 showcase clips in this task.
Do not create the public showcase repository in this task.
