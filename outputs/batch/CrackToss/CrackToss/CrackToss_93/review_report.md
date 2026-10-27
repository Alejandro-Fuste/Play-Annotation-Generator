# Play-Annotation-Generator Annotation Review — CrackToss_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_93`
- **Frame Range:** 0 to 374 (375 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 374
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 46
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_CrackBlock` | WR1 | offense | `4` | `3` |
| ✅ EXACT | `Action_CrackBlock` | WR2 | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Toss` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `9` | `Group` | 0 | START | 0 | 303 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 274 | START | 274 | 284 |
| ✅ EXACT | `Action_CrackBlock` | WR1 | `4` | `3` | 277 | START | 277 | 316 |
| ✅ EXACT | `Action_CrackBlock` | WR2 | `6` | `5` | 277 | START | 277 | 316 |
| ✅ EXACT | `Action_PullBlock` | LT | `11` | `10` | 277 | START | 277 | 316 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 284 | END | 274 | 284 |
| ✅ EXACT | `Action_Toss` | QB | `8` | `7` | 288 | START | 288 | 303 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `9` | `8` | 304 | START | 304 | 356 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 316 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–331
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 273 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 274 | 284 | 11 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_Toss` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_None` | 304 | 331 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_BallCarry` | 304 | 356 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 374 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 273 | 227 | inferred_complete_timeline |
| `Action_None` | 274 | 337 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_CrackBlock` | 277 | 316 | 40 | inferred_complete_timeline |
| `Action_None` | 317 | 374 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_CrackBlock` | 277 | 316 | 40 | inferred_complete_timeline |
| `Action_None` | 317 | 374 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_PullBlock` | 277 | 316 | 40 | inferred_complete_timeline |
| `Action_None` | 317 | 374 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 304 | 31 | inferred_complete_timeline |
| `Action_None` | 308 | 355 | 48 | inferred_complete_timeline |
| `Action_None` | 367 | 374 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_BallSnap` | 274 | 284 | 11 | inferred_complete_timeline |
| `Action_None` | 285 | 374 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 300 | 27 | inferred_complete_timeline |
| `Action_None` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_None` | 313 | 374 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 273 | 263 | inferred_complete_timeline |
| `Action_None` | 274 | 328 | 55 | inferred_complete_timeline |
| `Action_None` | 332 | 374 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 374 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–357
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 273 | 182 | inferred_complete_timeline |
| `Action_None` | 274 | 357 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 86 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 273 | 164 | inferred_complete_timeline |
| `Action_None` | 274 | 339 | 66 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 352 | 356 | 5 | inferred_complete_timeline |
| `Action_None` | 358 | 371 | 14 | inferred_complete_timeline |
| `Action_None` | 374 | 374 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 374 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 273 | 6 | inferred_complete_timeline |
| `Action_None` | 274 | 363 | 90 | inferred_complete_timeline |
| `Action_None` | 371 | 374 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 273 | 208 | inferred_complete_timeline |
| `Action_None` | 274 | 306 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 374 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–358 | 349 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 75–374 | 198 | 5 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 308–374 | 67 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 324–328 | 5 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 342–374 | 28 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 35 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
- ⚠️ Action 'Action_None' range [274-300] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-374] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-337] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [304-356] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-355] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-363] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-357] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-374] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-86] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-108] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-339] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-371] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-358] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '21' has 1 frames without a visible bounding box.
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

</details>