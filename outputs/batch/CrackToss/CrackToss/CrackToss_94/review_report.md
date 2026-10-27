# Play-Annotation-Generator Annotation Review — CrackToss_94

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_94`
- **Frame Range:** 0 to 374 (375 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 374
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 71
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | WR1 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | CB2 | defense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB1 | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `10` | `Group` | 0 | START | 0 | 308 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 276 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `4` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 279 |
| ✅ EXACT | `Action_BallSnap` | LG | `12` | `11` | 277 | START | 277 | 288 |
| ✅ EXACT | `Action_CrackBlock` | WR1 | `6` | `5` | 280 | START | 280 | 348 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `8` | `7` | 280 | START | 280 | 298 |
| ✅ EXACT | `Action_PullBlock` | CB2 | `1` | `0` | 280 | START | 280 | 348 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 288 | END | 277 | 288 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 293 | START | 293 | 308 |
| ✅ EXACT | `Action_BallCarry` | RB1 | `10` | `9` | 309 | START | 309 | 360 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 348 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_SnapReceive` | 277 | 288 | 12 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_Toss` | 293 | 308 | 16 | inferred_complete_timeline |
| `Action_None` | 309 | 334 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 308 | 309 | inferred_complete_timeline |
| `Action_BallCarry` | 309 | 360 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 258 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 276 | 17 | inferred_complete_timeline |
| `Action_None` | 277 | 374 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_CrackBlock` | 280 | 348 | 69 | inferred_complete_timeline |
| `Action_None` | 349 | 365 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–306
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_CrackBlock` | 280 | 298 | 19 | inferred_complete_timeline |
| `Action_CrackBlock` | 303 | 306 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 276 | 206 | inferred_complete_timeline |
| `Action_BallSnap` | 277 | 288 | 12 | inferred_complete_timeline |
| `Action_None` | 289 | 374 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 276 | 197 | inferred_complete_timeline |
| `Action_None` | 277 | 314 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_None` | 277 | 374 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_None` | 277 | 309 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_None` | 277 | 289 | 13 | inferred_complete_timeline |
| `Action_None` | 303 | 374 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 276 | 139 | inferred_complete_timeline |
| `Action_None` | 277 | 298 | 22 | inferred_complete_timeline |
| `Action_None` | 303 | 351 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_None` | 277 | 348 | 72 | inferred_complete_timeline |
| `Action_None` | 353 | 374 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_None` | 277 | 374 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 276 | 7 | inferred_complete_timeline |
| `Action_None` | 277 | 367 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_PullBlock` | 280 | 348 | 69 | inferred_complete_timeline |
| `Action_None` | 349 | 374 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 276 | 277 | inferred_complete_timeline |
| `Action_None` | 277 | 353 | 77 | inferred_complete_timeline |
| `Action_None` | 355 | 374 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–308 | 307 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–83 | 83 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 15–334 | 313 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 36–39 | 4 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 299–362 | 45 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 305–374 | 70 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 309–374 | 66 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 315–374 | 60 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 320–374 | 55 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 336–374 | 39 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 338–374 | 37 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | 224 | 226 | 2 | 66.7% | 225 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 190: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 190: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-374] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-258] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-308] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-365] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-353] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [280-298] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [303-306] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-374] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-276] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-367] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-309] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-83] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-276] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-298] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-351] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-321] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-321] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-331] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>