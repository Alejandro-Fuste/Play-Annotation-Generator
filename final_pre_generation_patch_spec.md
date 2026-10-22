# Final Pre-Generation Patch — Antigravity Implementation Specification

## Purpose

Apply the last minimal changes required before generating the full 50-clip showcase annotation set in `Play-Annotation-Generator`.

Repository:

```text
https://github.com/Alejandro-Fuste/Play-Annotation-Generator
```

Use the current `main` branch.

This task is intentionally tiny.

Implement only:

1. three showcase manifest replacements;
2. the RPO-specific PreSnap end-frame rule;
3. focused regression tests;
4. a four-clip smoke/regression generation;
5. the final 50-clip readiness audit.

Do **not** make unrelated code changes.
Do **not** refactor existing working behavior.
Do **not** generate all 50 clips in this task.
Do **not** create the public showcase repository yet.

---

# 1. Frozen Existing Behavior

Preserve all currently working behavior, including:

- Duo semicolon continuation parsing;
- canonical play-tag resolution from `plays.json`;
- explicit `start,end,track_id` preservation;
- generic `ends_when_any_action_starts`;
- Counter_1 Handoff timing;
- special-teams offense/defense row-side logic;
- special-teams PreSnap fallbacks;
- Long Snap timing;
- non-temporal RPO Route descriptors;
- Action_None complete-visible-frame coverage;
- semantic alias audit;
- malformed temporal-cell blocking;
- `[?]` PlayerTrack values as warnings rather than blockers;
- batch resume/overwrite behavior;
- migration behavior.

Do not modify source tracking ZIPs.

---

# 2. Showcase Manifest Replacements

Update:

```text
data/showcase/showcase_clips.json
```

The manifest must remain exactly:

```text
50 clips
```

## Replace Punt Return TD sample

Remove:

```text
PuntReturnTouchdown_2
```

Add:

```json
{
  "logical_clip_name": "PuntReturnTouchdown_9",
  "play_name": "PuntReturnTouchdown",
  "video_id": "9",
  "tracking_source": "data/tracking/PuntReturnTouchdown/PuntReturnTouchdown_9_cvat_mot.zip",
  "key_actions_source": "data/key_actions/PuntReturnTouchdown.csv",
  "player_tracks_source": "data/player_tracks/PuntReturnTouchdown.csv"
}
```

Authoritative source row:

```text
PuntReturnTouchdown_9

Pre Snap        = 0,ALL
Long Snap       = 97,19
Snap Receive    = 128,1
Punt Ball       = 154,166,1
Catch Punt      = 276,283,27
Ball Carry      = 299,27
Cross Goal Line = 649,655,27
```

Relevant PlayerTrack identities:

```text
Long_Snapper = 19
Punter = 1
```

The returner actor `27` may be a later tracking identity not represented by the original pre-snap position row. Do not force another ID.

---

# 3. Replace Kickoff Return TD samples

Remove:

```text
KickoffReturnTouchdown_5
KickoffReturnTouchdown_6
```

Add:

```json
{
  "logical_clip_name": "KickoffReturnTouchdown_13",
  "play_name": "KickoffReturnTouchdown",
  "video_id": "13",
  "tracking_source": "data/tracking/KickoffReturnTouchdown/KickoffReturnTouchdown_13_cvat_mot.zip",
  "key_actions_source": "data/key_actions/KickoffReturnTouchdown.csv",
  "player_tracks_source": "data/player_tracks/KickoffReturnTouchdown.csv"
}
```

and:

```json
{
  "logical_clip_name": "KickoffReturnTouchdown_14",
  "play_name": "KickoffReturnTouchdown",
  "video_id": "14",
  "tracking_source": "data/tracking/KickoffReturnTouchdown/KickoffReturnTouchdown_14_cvat_mot.zip",
  "key_actions_source": "data/key_actions/KickoffReturnTouchdown.csv",
  "player_tracks_source": "data/player_tracks/KickoffReturnTouchdown.csv"
}
```

Authoritative source rows:

## KickoffReturnTouchdown_13

```text
Pre Snap        = 0,ALL
Kick Approach   = 50,12
Kick Ball       = 116,121,12
Catch Kick      = 243,248,45
Ball Carry      = 257,45
Cross Goal Line = 646,658,45
```

PlayerTrack includes:

```text
Kicker = 12
Kick_Returner2 = 45
```

This is intentional.

## KickoffReturnTouchdown_14

```text
Pre Snap        = 0,ALL
Kick Approach   = 66,5
Kick Ball       = 129,133,5
Catch Kick      = 254,259,13
Ball Carry      = 270,13
Cross Goal Line = 658,677,13
```

PlayerTrack includes:

```text
Kicker = 5
Kick_Returner2 = 13
```

This is intentional.

---

# 4. Manifest Assertions

Add/update tests asserting:

```text
len(manifest) == 50
```

Present:

```text
PuntReturnTouchdown_9
KickoffReturnTouchdown_13
KickoffReturnTouchdown_14
```

Absent:

```text
PuntReturnTouchdown_2
KickoffReturnTouchdown_5
KickoffReturnTouchdown_6
```

Also verify all three replacement tracking ZIP paths exist.

---

# 5. RPO-Specific PreSnap Rule

## Required rule

For play:

```text
RPO
```

the PreSnap end frame must be:

```text
Run Block start frame - 2
```

This rule is specific to RPO.

Do not replace the normal Ball Snap fallback for other plays.
Do not make this a generic “earliest action minus two” rule.

## RPO_1 authoritative data

```text
Run Block start = 88
```

Therefore:

```text
PreSnap end = 86
```

For any player without an earlier explicit action:

```text
Action_PreSnap = 0–86
Action_None    = 87–...
```

subject to visible-frame gaps.

---

# 6. RPO Rule Precedence

For `RPO` only:

1. If the player has an explicit action earlier than the RPO global boundary, existing same-actor action logic still takes precedence.
2. Otherwise use:
   ```text
   RunBlockStart - 2
   ```
3. Do not alter the non-temporal Route descriptor behavior.
4. Do not fabricate Ball Snap.
5. Do not alter the Run Block source frame.

---

# 7. RPO_1 Regression Requirements

`RPO_1` must retain:

```text
Route = post,7
```

as:

```text
canonical_action = Action_RunPostRoute
actor_track_id = 7
temporal = false
```

No timed `Action_RunPostRoute` segment may be created.

Additionally:

```text
Run Block start = 88
Global RPO PreSnap end = 86
```

For players without an earlier explicit action, the timeline must not remain `Action_PreSnap` past frame 86.

Add a regression assertion for at least one player with no explicit post-snap action:

```text
Action_PreSnap 0–86
Action_None from 87 onward
```

subject to visibility.

---

# 8. Four-Clip Regression Generation

After implementation, generate only:

```text
RPO_1
PuntReturnTouchdown_9
KickoffReturnTouchdown_13
KickoffReturnTouchdown_14
```

Use a fresh output directory:

```text
output_showcase_pre_generation_check/
```

Recommended command:

```bash
PYTHONPATH=src ./venv/bin/python \
  -m play_annotation_generator.showcase \
  --manifest data/showcase/showcase_clips.json \
  --output output_showcase_pre_generation_check \
  --clips RPO_1,PuntReturnTouchdown_9,KickoffReturnTouchdown_13,KickoffReturnTouchdown_14 \
  --review
```

Do not overwrite previous regression directories.

---

# 9. Regression Acceptance Criteria

## RPO_1

Require:

```text
Play = canonical RPO play label
Route post,7 retained as non-temporal descriptor
0 fabricated timed RunPostRoute segments
Run Block starts at 88
PreSnap global fallback ends at 86
players without explicit action do not remain PreSnap after 86
0 validation errors
0 missing expected action segments
```

## PuntReturnTouchdown_9

Require:

```text
Play = Play_SpecialTeams_PuntReturnTouchdown
Long Snap = actor 19
Snap Receive = actor 1
Punt Ball = actor 1
Catch Punt = actor 27
Ball Carry = actor 27
Cross Goal Line = actor 27
explicit ranges preserved
0 missing expected action segments
0 validation errors
```

Tracking-quality warnings may remain.

## KickoffReturnTouchdown_13

Require:

```text
Play = Play_SpecialTeams_KickoffReturnTouchdown
Kick Approach = actor 12
Kick Ball = actor 12
Catch Kick = actor 45
Ball Carry = actor 45
Cross Goal Line = actor 45
explicit ranges preserved
0 missing expected action segments
0 validation errors
```

`[?]` position assignments may remain warnings.

## KickoffReturnTouchdown_14

Require:

```text
Play = Play_SpecialTeams_KickoffReturnTouchdown
Kick Approach = actor 5
Kick Ball = actor 5
Catch Kick = actor 13
Ball Carry = actor 13
Cross Goal Line = actor 13
explicit ranges preserved
0 missing expected action segments
0 validation errors
```

---

# 10. Focused Tests

Add/update tests for:

### Manifest

```text
50 total clips
new three clips present
old three clips absent
replacement tracking ZIPs exist
```

### RPO PreSnap

Synthetic or fixture-based:

```text
play = RPO
RunBlock start = 88
```

Expected global fallback:

```text
PreSnap end = 86
```

Also assert:

```text
Action_None begins at 87
```

for a visible player with no explicit post-snap action.

### Regression-source identities

Assert current source rows contain:

```text
PuntReturnTouchdown_9:
Snap Receive actor 1
Catch Punt/Ball Carry/Cross Goal Line actor 27

KickoffReturnTouchdown_13:
Catch Kick/Ball Carry/Cross Goal Line actor 45

KickoffReturnTouchdown_14:
Catch Kick/Ball Carry/Cross Goal Line actor 13
```

---

# 11. Full Test Suite

Run focused tests first.

Then run:

```bash
PYTHONPATH=src ./venv/bin/pytest -q
```

The two already-known migration-state failures may remain only if they are exactly the same pre-existing failures in:

```text
tests/test_outside_zone_qb_zone_read_migration.py
```

No new failures are acceptable.

---

# 12. Final 50-Clip Readiness Audit

After the four-clip regression passes, run:

```bash
PYTHONPATH=src ./venv/bin/python \
  -m play_annotation_generator.showcase \
  --manifest data/showcase/showcase_clips.json \
  --audit
```

Required final gate:

```text
Showcase clips requested: 50
Tracking sources resolved: 50
Key Actions rows resolved: 50
PlayerTrack rows resolved: 50
Unmapped populated action columns: 0
BLOCKED: 0
```

`READY_WITH_REVIEW_WARNINGS` is acceptable for the known `[?]` PlayerTrack cases and ordinary tracking-quality warnings.

---

# 13. GO / NO-GO Decision

Antigravity must explicitly report one of:

```text
GO FOR FINAL 50-CLIP GENERATION
```

only if:

```text
BLOCKED = 0
0 validation errors across the four regression clips
0 missing expected action segments across the four regression clips
no new pytest failures
```

Otherwise report:

```text
NO-GO
```

and list the exact clip/reason.

---

# 14. Final Report

Report:

1. files changed;
2. manifest replacements;
3. final manifest count;
4. RPO PreSnap implementation;
5. RPO_1 generated PreSnap boundary;
6. focused test results;
7. full pytest result;
8. four-clip regression table with:
   - status
   - validation errors
   - warnings
   - missing expected action segments
9. final 50-clip readiness audit counts;
10. final GO / NO-GO statement.

Do not generate all 50 clips in this task.
