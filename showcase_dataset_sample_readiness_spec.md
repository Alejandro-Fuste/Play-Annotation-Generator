# Showcase Dataset Sample Readiness — Antigravity Specification

## Goal

Prepare `Play-Annotation-Generator` to correctly generate annotation files for the curated 51-clip employer-facing showcase sample. This is a targeted readiness patch, not a full-dataset refactor.

Repository baseline:
`https://github.com/Alejandro-Fuste/Play-Annotation-Generator`

Current confirmed updates:
- `data/player_tracks/Draw.csv` now exists and includes Draw video #1.
- Duo tracking uses names like `Duo_clip1_cvat_mot.zip`.
- `Duo_clip1_cvat_mot.zip` is the physical tracking source for logical clip `Duo_1`.
- The canonical field-goal play name in the repo is `FieldGoalBlock`, not `FieldGoalBlocks`.

Do not change source annotation values, tracking ZIP contents, taxonomy, or migration history merely to make tests pass.

---

## Exact showcase set

Use exactly these 51 logical clips:

```text
BootPass_1
Counter_1
Counter_2
CrackToss_3
CrackToss_4
Dagger_1
DeepCross_1
Draw_1
Duo_1
FieldGoalBlock_3
FieldGoalBlock_4
Hitch_2
InsideZoneRead_1
InsideZoneRead_2
InsideZoneStretch_1
InsideZoneStretch_2
JetSweep_1
JetSweep_2
KickoffReturnTouchdown_5
KickoffReturnTouchdown_6
OnsideKickRecovery_1
OnsideKickRecovery_2
OutAndUp_1
OutRoutes_1
OutRoutes_2
OutsideZoneRead_1
OutsideZoneRead_2
OutsideZoneStretch_1
OutsideZoneStretch_2
PinAndPull_1
PinAndPull_2
Post10to15_1
Post10to15_2
Power_3
Power_4
PuntBlock_1
PuntBlock_2
PuntCoverage_1
PuntCoverage_2
PuntReturnTouchdown_1
PuntReturnTouchdown_2
QuickScreens_1
QuickScreens_2
RPO_1
Sack_1
Sack_2
SlantAndGo_1
Slants0to10_5
SplitZone_1
SplitZone_2
WRSlowScreens_1
```

Expected count: **51**.

---

## Primary defect to fix

`wide_action_csv_parser.py` only converts columns listed in `config["csv"]["action_columns"]` into `ActionEvent`s.

Many populated Key Actions columns used by this showcase set are currently not mapped, which means actions can be silently omitted.

This patch must make silent omission impossible for the showcase sample.

For every non-empty action column used by a showcase row:
1. normalize the header;
2. resolve it to one canonical `Action_*` label from `data/actions.json`;
3. parse it;
4. fail showcase readiness if no mapping exists.

Do not invent taxonomy labels when `actions.json` is authoritative.

---

## Required action coverage

Verify exact canonical names in `data/actions.json` and add mappings for all populated showcase columns.

At minimum cover these concepts in addition to already-supported actions:

### Passing / routes
```text
Pass Block
Pass Drop
Pump Fake
Clear Out Route
Dig Route
Run Deep Cross Route
Run Hitch Route
Run Out Route
Run Post Route
Run Slant Route
Sell Slant
Sell Out
Run Go Route
Release To Screen
Turn To Quarterback
Settle For Screen
Throw Screen Pass
Screen Block
Run After Catch
```

Expected naming pattern, subject to verification in `actions.json`:
```text
Action_PassBlock
Action_PassDrop
Action_PumpFake
Action_ClearOutRoute
Action_DigRoute
Action_RunDeepCrossRoute
Action_RunHitchRoute
Action_RunOutRoute
Action_RunPostRoute
Action_RunSlantRoute
Action_SellSlant
Action_SellOut
Action_RunGoRoute
Action_ReleaseToScreen
Action_TurnToQuarterback
Action_SettleForScreen
Action_ThrowScreenPass
Action_ScreenBlock
Action_RunAfterCatch
```

### Run concepts
```text
Handoff
Read Defender
Read Edge Defender
Keep
Pull Ball
Press Edge
Press Interior Gap
Crack Block
Combo Blocks
Split Block
Down Block / Down Blocks
Pull Block / Pull Blocks
Pull Lead Block
Play-side fake step
```

Expected naming pattern, subject to verification:
```text
Action_Handoff
Action_ReadDefender
Action_ReadEdgeDefender
Action_Keep
Action_PullBall
Action_PressEdge
Action_PressInteriorGap
Action_CrackBlock
Action_ComboBlock
Action_SplitBlock
Action_DownBlock
Action_PullBlock
Action_PullLeadBlock
Action_PlaySideFakeStep
```

### Special teams
```text
Kick Approach
Kick Ball
Catch Kick
Cross Goal Line
Onside Kick
Attempt Recovery
Secure Recovery
Long Snap
Place Ball
Attempt Block
Block Kick
Punt Ball
Block Punt
Catch Punt
Tackle
```

Expected naming pattern, subject to verification:
```text
Action_KickApproach
Action_KickBall
Action_CatchKick
Action_CrossGoalLine
Action_OnsideKick
Action_AttemptRecovery
Action_SecureRecovery
Action_LongSnap
Action_PlaceBall
Action_AttemptBlock
Action_BlockKick
Action_PuntBall
Action_BlockPunt
Action_CatchPunt
Action_Tackle
```

---

## Header aliases

Normalize source-header variations without editing the CSV files.

At minimum handle:
```text
Down Block / Down Blocks
Pull Block / Pull Blocks
Ball Carry / Ball Carry<space>
Run Block / Run Block<space>
Turn To Quarterback / leading-space variant
Settle For Screen / trailing-space variant
Pass Block / Pass Block<space>
```

Do not parse the same physical column twice.

---

## Duo filename compatibility

Current physical source:
```text
data/tracking/Duo/Duo_clip1_cvat_mot.zip
```

Logical identity:
```text
play = Duo
video_id = 1
clip_key = Duo_1
```

Add narrow filename compatibility:

```regex
^Duo_clip(\d+)$
```

Required behavior:
```text
Duo_clip1_cvat_mot.zip   -> Duo / 1 / Duo_1
Duo_clip100_cvat_mot.zip -> Duo / 100 / Duo_100
```

Preserve the original physical source path in manifests/provenance.
Do not rename or move tracking ZIPs.
Do not broadly strip `clip` from unrelated play names.

---

## Timing rules

Preserve the existing precedence:

```text
1. explicit CSV end_frame
2. existing special cross-actor rule
3. existing terminal-action rule
4. next same-actor explicit action - 1
5. applicable boundary event
6. existing play-end / visible-track fallback
```

If a source cell is `start,end,track_id`, preserve that range unless existing visibility clamping or a documented higher-priority rule applies.

Do not replace explicit source end frames with inferred durations.

### Blocking families

When no explicit end or earlier same-actor transition exists, the following blocking families should be eligible for inclusive `End of OL Block` termination where semantically appropriate:

```text
Action_ZoneBlock
Action_ReachBlock
Action_DownBlock
Action_PullBlock
Action_PullLeadBlock
Action_LeadBlock
Action_BlockSecondLevel
Action_RunBlock
Action_PassBlock
Action_CrackBlock
Action_ComboBlock
Action_SplitBlock
Action_ScreenBlock
```

At minimum, ensure newly enabled `Action_PullLeadBlock` is not omitted from OL-boundary handling.

### Start-only transition actions

For actions such as:
```text
Action_PlaySideFakeStep
Action_PumpFake
Action_ReadDefender
Action_ReadEdgeDefender
Action_PullBall
Action_Keep
Action_TurnToQuarterback
Action_SettleForScreen
```

use next same-actor action minus one when no explicit end exists.
Do not invent fixed durations.

### Routes and special teams

Honor explicit ranges first.
If no explicit end exists, use the existing same-actor transition/fallback framework.
Do not fabricate frame values.

---

## Known source ambiguity policy

Do not auto-correct ambiguous source values.

Examples in the showcase sample include values like:
```text
?,51
?,20
[?]
```

Policy:
- `[?]` PlayerTrack assignments remain unknown/unassigned.
- unknown/non-numeric action frames must produce a visible readiness warning or failure;
- never invent a frame;
- never silently drop the event.

Classify clips as:
```text
READY_CLEAN
READY_WITH_REVIEW_WARNINGS
BLOCKED
```

or an equivalent explicit status.

---

## Play-specific requirements

### BootPass_1
Preserve:
```text
defense: Action_PreSnap through BallSnap-1
defense: Action_None from BallSnap onward on visible frames
```

### Counter_1 / Counter_2
Must parse:
```text
Play-side fake step
Down Blocks
Pull Block
Pull Lead Block
Handoff
```

### CrackToss_3 / CrackToss_4
Must parse:
```text
Crack Block
Pull Blocks
Toss
Ball Carry
```

### Draw_1
Confirm all three sources now resolve:
```text
tracking
data/key_actions/Draw.csv row 1
data/player_tracks/Draw.csv row 1
```

Must parse:
```text
Pass Block
Pass Drop
Handoff
Ball Carry
```

### Duo_1
Resolve:
```text
Duo_clip1_cvat_mot.zip -> logical Duo_1
```

Must parse:
```text
Combo Blocks
Handoff
Ball Carry
Block Second Level
End of OL Block
```

### FieldGoalBlock_3 / _4
Use canonical singular play name:
```text
FieldGoalBlock
```

Must parse:
```text
Long Snap
Place Ball
Kick Ball
Attempt Block
Block Kick
```

Do not introduce a duplicate `FieldGoalBlocks` taxonomy.

---

## Showcase manifest

Add one machine-readable manifest, recommended:

```text
data/showcase/showcase_clips.json
```

It must contain exactly the 51 logical clips.

Each entry should include:
```text
logical_clip_name
play_name
video_id
tracking_source
key_actions_source
player_tracks_source
```

Duo example:
```json
{
  "logical_clip_name": "Duo_1",
  "play_name": "Duo",
  "video_id": "1",
  "tracking_source": "data/tracking/Duo/Duo_clip1_cvat_mot.zip",
  "key_actions_source": "data/key_actions/Duo.csv",
  "player_tracks_source": "data/player_tracks/Duo.csv"
}
```

The manifest should be the authoritative showcase selection list.
Do not use broad filesystem discovery to decide showcase membership.

---

## Readiness audit

Add a read-only showcase readiness workflow.

It must verify, for every manifest clip:
```text
tracking source exists
Key Actions source exists
matching Key Actions row exists
PlayerTrack source exists
matching PlayerTrack row exists
play exists in plays.json
every populated action column is mapped
mapped Action_* exists in actions.json
required cells parse
```

Expected summary shape:
```text
Showcase clips requested: 51
Tracking sources resolved: 51
Key Actions rows resolved: 51
PlayerTrack rows resolved: 51
Unmapped populated action columns: 0
READY_CLEAN: <count>
READY_WITH_REVIEW_WARNINGS: <count>
BLOCKED: <count>
```

Readiness mode must not generate per-clip annotation outputs.

A populated unmapped action column must be a hard readiness failure, for example:
```text
UNMAPPED_ACTION_COLUMN:
play=Counter
video_id=1
column=Pull Lead Block
value=361,5
```

---

## Showcase generation workflow

Provide a deterministic way to generate exactly the 51 manifest clips.

A small dedicated script/module is preferred, for example:
```text
python -m play_annotation_generator.showcase   --manifest data/showcase/showcase_clips.json   --output output_showcase   --review
```

Exact CLI shape may differ.

Requirements:
- process only manifest clips;
- never trigger the 4,000+ clip batch;
- preserve normal per-clip artifacts;
- write one aggregate showcase summary.

Normal outputs should include, where enabled:
```text
generated_base_cvat.xml
annotations.xml
annotations.json
dense_actions.csv
normalized_action_events.csv
validation_report.json
validation_report.md
review_report.md
```

---

## Tests

Add focused tests for:

1. every unique populated showcase action header maps to a canonical action;
2. every mapped `Action_*` exists in `actions.json`;
3. `Duo_clip1` -> `Duo_1`;
4. `Duo_clip100` -> `Duo_100`;
5. normal filenames such as `BootPass_1` and `JetSweep_2` are unchanged;
6. Draw_1 resolves tracking + Key Actions + PlayerTrack inputs;
7. FieldGoalBlock naming remains singular;
8. explicit `start,end,track_id` ranges retain the explicit end;
9. newly enabled blocking actions honor End-of-OL-Block logic where appropriate;
10. an unknown populated action column fails readiness rather than being ignored;
11. existing BootPass and JetSweep tests remain green.

---

## Validation sequence

Do not immediately generate all 51 clips.

### Stage A
Run focused tests.

### Stage B
Run full suite:
```bash
PYTHONPATH=src ./venv/bin/pytest -q
```

### Stage C
Run readiness-only audit for all 51.

Target:
```text
51 evaluated
51 tracking resolved
51 Key Actions rows resolved
51 PlayerTrack rows resolved
0 unmapped populated action columns
```

Any source ambiguity must be listed explicitly.

### Stage D
Generate this representative smoke subset only:
```text
BootPass_1
Counter_1
Draw_1
Duo_1
FieldGoalBlock_3
JetSweep_1
PuntBlock_1
QuickScreens_1
SplitZone_1
```

Verify:
```text
no validation errors
expected actions appear in Action Annotation Audit
explicit ranges preserved
defensive Action_None behavior preserved
special-team position labels preserved
no populated action silently omitted
```

### Stage E
Only if Stage D is acceptable, generate all 51 showcase clips.

Do not run any other clips.

---

## Frozen behavior

Do not modify:
```text
tracking ZIP contents
source Key Actions values
PlayerTrack source values
plays.json taxonomy
migration code/manifests
actor_track_id <-> xml_track_id logic
Action_None complete-timeline policy
Ball Snap / Snap Receive semantics
Toss -> Ball Carry semantics
Center priority behavior
resume/overwrite semantics
```

No unrelated refactors.

---

## Final Antigravity report

Report:
```text
files changed
new action-column mappings
new/changed timing rules
Duo filename normalization behavior
showcase manifest path
focused test results
full pytest result
51-clip readiness summary
representative smoke-test results
BLOCKED clips
READY_WITH_REVIEW_WARNINGS clips
whether all 51 are safe to generate
```

Do not create the new public showcase GitHub repository in this task.

This task ends when the existing `Play-Annotation-Generator` is demonstrably ready to generate the curated 51-clip sample without silent action omission.
