# Play-Annotation-Generator Annotation Review — SplitZone_184

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_184`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_-`
- **Result Frame:** 329
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 4
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_SplitBlock` | TE | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 8 | START | 9 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 8 | START | 9 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 8 | START | 9 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 8 | START | 70 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 8 | START | 9 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 8 | START | 9 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 8 | START | 9 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 8 | START | 9 | 121 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 89 | START | 89 | 96 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `2` | `2` | 90 | START | 90 | 158 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `10` | 97 | START | 97 | 325 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 165 | START | 165 | 181 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 168 | START | 182 | 329 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 168 | START | 168 | 228 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `2` | `2` | 168 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 168 | START | 168 | 329 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `6` | `6` | 168 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SplitBlock` | TE | `15` | `15` | 171 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `5` | `5` | 181 | END | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–132
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 88 | 80 | inferred_complete_timeline |
| `Action_Handoff` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_None` | 97 | 132 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 9–325
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 96 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 325 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 70–77
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 70 | 77 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–158
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 89 | 81 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 90 | 158 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–121
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 121 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 164 | 156 | inferred_complete_timeline |
| `Action_BallSnap` | 165 | 181 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 71 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 130 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 167 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 329 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–228
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 167 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 228 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–111
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 111 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–103
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 103 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–130
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 105 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 42 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 47 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 162 | 113 | inferred_complete_timeline |
| `Action_None` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_None` | 175 | 329 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–307
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 140 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 198 | 34 | inferred_complete_timeline |
| `Action_None` | 200 | 307 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 164 | 156 | inferred_complete_timeline |
| `Action_None` | 165 | 329 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 111 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 164 | 49 | inferred_complete_timeline |
| `Action_None` | 165 | 329 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 164 | 156 | inferred_complete_timeline |
| `Action_None` | 165 | 329 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 86–87 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 93–285 | 146 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 101–329 | 229 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 121–182 | 59 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 134–227 | 86 | 6 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 137–295 | 158 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 155–277 | 120 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 162–167 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 165–301 | 137 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 183–329 | 147 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 185–329 | 145 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 187–329 | 143 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 194–270 | 73 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 247–287 | 41 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 274–324 | 25 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 281–286 | 6 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 298–324 | 23 | 3 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 309–324 | 12 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 312–314 | 3 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 314–325 | 6 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 168 != Inferred start 182
- ❌ Missing segment for action `Action_ZoneBlock` on target `2` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `6` (LG)
- ❌ Missing segment for action `Action_SplitBlock` on target `15` (TE)
- ❌ Missing segment for action `Action_SnapReceive` on target `5` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '2' has invalid range: start=168, end=158. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 162 frames exceeds threshold 90 frames [start=168, end=329].
- ⚠️ Segment 'Action_SnapReceive' for track '5' has invalid range: start=165, end=132. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=168, end=121. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 162 frames exceeds threshold 90 frames [start=168, end=329].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [165–181], lower_priority='Action_ZoneBlock' annotated_start=168, effective_Action_ZoneBlock_start=182.
- ⚠️ Segment 'Action_SplitBlock' for track '15' has invalid range: start=171, end=77. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [9-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [90-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-71] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-198] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-307] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-325] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-228] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-162] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-119] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-160] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-227] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-164] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-295] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-301] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-287] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-324] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-286] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-316] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-315] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>