# Play-Annotation-Generator Annotation Review — CrackToss_90

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_90`
- **Frame Range:** 0 to 499 (500 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 499
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 144
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | RB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `28` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `24` | `Group` | 0 | START | 48 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 138 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 322 | START | 322 | 334 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `7` | `6` | 325 | START | 325 | 389 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LB2 | `11` | `10` | 325 | START | 325 | 399 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `6` | `5` | 325 | START | 325 | 411 |
| ✅ EXACT | `Action_SnapReceive` | RB | `14` | `13` | 334 | END | 322 | 334 |
| ✅ EXACT | `Action_Toss` | RB | `14` | `13` | 336 | START | 336 | 352 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `28` | `26` | 353 | START | 353 | 414 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_SnapReceive` | 322 | 334 | 13 | inferred_complete_timeline |
| `Action_None` | 335 | 335 | 1 | inferred_complete_timeline |
| `Action_Toss` | 336 | 352 | 17 | inferred_complete_timeline |
| `Action_None` | 353 | 381 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–499
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 324 | 183 | inferred_complete_timeline |
| `Action_CrackBlock` | 325 | 389 | 65 | inferred_complete_timeline |
| `Action_CrackBlock` | 393 | 499 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `24`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 48–131
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 48 | 76 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 131 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_None` | 322 | 382 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_BallSnap` | 322 | 334 | 13 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_None` | 322 | 375 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_None` | 322 | 393 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–376
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_None` | 322 | 376 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–379
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 321 | 18 | inferred_complete_timeline |
| `Action_None` | 322 | 379 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_None` | 322 | 360 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 321 | 132 | inferred_complete_timeline |
| `Action_None` | 322 | 361 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 324 | 325 | inferred_complete_timeline |
| `Action_PullBlock` | 325 | 399 | 75 | inferred_complete_timeline |
| `Action_PullBlock` | 402 | 497 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–375
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 194 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 321 | 123 | inferred_complete_timeline |
| `Action_None` | 322 | 352 | 31 | inferred_complete_timeline |
| `Action_None` | 356 | 358 | 3 | inferred_complete_timeline |
| `Action_None` | 374 | 375 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–499
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 321 | 130 | inferred_complete_timeline |
| `Action_None` | 322 | 423 | 102 | inferred_complete_timeline |
| `Action_None` | 426 | 430 | 5 | inferred_complete_timeline |
| `Action_None` | 438 | 499 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_None` | 322 | 360 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–499 | 496 | 4 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–51 | 52 | 1 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–485 | 477 | 6 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–120 | 121 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–42 | 43 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 10–11 | 2 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 38–123 | 25 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 77–126 | 19 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 80–87 | 6 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 128–165 | 38 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 133–499 | 335 | 7 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 171–370 | 200 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 220–343 | 82 | 5 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 226–392 | 156 | 3 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 251–266 | 12 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 311–330 | 10 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 337–399 | 63 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 357–393 | 11 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 362–499 | 138 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 371–372 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 374–499 | 126 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 385–397 | 13 | 1 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 394–398 | 5 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 411–499 | 89 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 436–437 | 2 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 457–499 | 43 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 460–468 | 7 | 3 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 489–490 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `28` (6 segments found)

### Track Identity Issues

- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 319 targets track ID '423', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 182: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 182: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 499 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (Unknown) duration 161 frames exceeds threshold 90 frames [start=325, end=485].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '10' (LB2) duration 173 frames exceeds threshold 90 frames [start=325, end=497].
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-396] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-376] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-375] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-393] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-139] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [325-411] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [415-485] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [325-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-352] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-360] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [325-399] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [402-497] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-381] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-361] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-423] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-430] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-499] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-360] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-382] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-76] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-165] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-352] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [353-414] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [417-418] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [423-426] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [450-477] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [479-487] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-370] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-392] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-266] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-330] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-399] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-393] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-499] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-397] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-398] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-499] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>