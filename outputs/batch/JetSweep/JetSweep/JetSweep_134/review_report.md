# Play-Annotation-Generator Annotation Review — JetSweep_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_134`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | offense | `2` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `18` | `17` | 30 | START | 30 | 76 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 46 | START | 46 | 64 |
| ✅ EXACT | `Action_LeadBlock` | RB | `7` | `6` | 47 | START | 47 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_SealBlock` | TE | `2` | `1` | 47 | START | 47 | 154 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 47 | START | 65 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 47 | START | 47 | 79 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `3` | 47 | START | 47 | 170 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 47 | START | 47 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 47 | START | 47 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 64 | END | 46 | 64 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 69 | START | 69 | 79 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `18` | `17` | 80 | START | 80 | 359 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `3` | `2` | 80 | START | 80 | 170 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_Toss` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 126 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_LeadBlock` | 47 | 170 | 124 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SealBlock` | 47 | 154 | 108 | inferred_complete_timeline |
| `Action_SealBlock` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 79 | 33 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 80 | 170 | 91 | inferred_complete_timeline |
| `Action_None` | 171 | 290 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 170 | 124 | inferred_complete_timeline |
| `Action_None` | 171 | 279 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 170 | 106 | inferred_complete_timeline |
| `Action_None` | 171 | 257 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 170 | 124 | inferred_complete_timeline |
| `Action_None` | 171 | 222 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 145 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 66 | 21 | inferred_complete_timeline |
| `Action_None` | 70 | 359 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 359 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 244 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 147 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 117 | 72 | inferred_complete_timeline |
| `Action_None` | 125 | 359 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 251 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 140 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 97 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 7–359 | 353 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 30–359 | 327 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 66–68 | 3 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 100–144 | 45 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 125–276 | 152 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 146–172 | 20 | 5 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 147–359 | 208 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 152–359 | 195 | 4 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 167–207 | 41 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 175–325 | 150 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 182–290 | 108 | 2 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 218–252 | 35 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 219–282 | 64 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 228–229 | 2 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 326–329 | 4 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 330–359 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SealBlock` and target `2` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 47 != Inferred start 65
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '2' (LT) duration 91 frames exceeds threshold 90 frames [start=80, end=170].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 99 frames exceeds threshold 90 frames [start=47, end=145].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '6' (RB) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 124 frames exceeds threshold 90 frames [start=47, end=170].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [46–64], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=65.
- ⚠️ Action 'Action_None' range [46-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [47-154] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [161-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-117] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-147] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [30-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-300] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-237] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-311] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-341] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-207] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-290] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '31' has 1 frames without a visible bounding box.
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

</details>