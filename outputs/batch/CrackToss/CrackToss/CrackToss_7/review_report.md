# Play-Annotation-Generator Annotation Review — CrackToss_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_7`
- **Frame Range:** 0 to 448 (449 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 448
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `13` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `12` | `11` |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `24` | `19` |
| ⚠️ START CHANGED | `Action_Toss` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `1` | `Group` | 0 | START | 0 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 233 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `8` | `Group` | 0 | START | 0 | 233 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `15` | `13` | 234 | START | 234 | 241 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `12` | `11` | 241 | END | N/A | N/A |
| ✅ EXACT | `Action_CrackBlock` | Position_Unknown | `13` | `12` | 244 | START | 244 | 307 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `24` | `19` | 244 | START | 248 | 307 |
| ⚠️ START CHANGED | `Action_Toss` | Position_Unknown | `12` | `11` | 244 | START | 245 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `1` | `0` | 272 | START | 272 | 375 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 307 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–437
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 271 | 272 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 375 | 104 | inferred_complete_timeline |
| `Action_BallCarry` | 377 | 437 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 329 | 96 | inferred_complete_timeline |
| `Action_None` | 334 | 366 | 33 | inferred_complete_timeline |
| `Action_None` | 368 | 374 | 7 | inferred_complete_timeline |
| `Action_None` | 381 | 389 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 333 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 358 | 125 | inferred_complete_timeline |
| `Action_None` | 362 | 365 | 4 | inferred_complete_timeline |
| `Action_None` | 368 | 380 | 13 | inferred_complete_timeline |
| `Action_None` | 389 | 407 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 233 | 75 | inferred_complete_timeline |
| `Action_None` | 234 | 271 | 38 | inferred_complete_timeline |
| `Action_None` | 280 | 291 | 12 | inferred_complete_timeline |
| `Action_None` | 293 | 296 | 4 | inferred_complete_timeline |
| `Action_None` | 302 | 309 | 8 | inferred_complete_timeline |
| `Action_None` | 322 | 344 | 23 | inferred_complete_timeline |
| `Action_None` | 355 | 366 | 12 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 371 | 372 | 2 | inferred_complete_timeline |
| `Action_None` | 379 | 410 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 187 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 216 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 220 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 343 | 110 | inferred_complete_timeline |
| `Action_None` | 346 | 347 | 2 | inferred_complete_timeline |
| `Action_None` | 349 | 398 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 334 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 355 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–413
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_None` | 234 | 343 | 110 | inferred_complete_timeline |
| `Action_None` | 399 | 413 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–325 | 298 | 6 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 2–363 | 212 | 13 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 24–391 | 368 | 3 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 68–346 | 270 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 166–426 | 224 | 11 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 248–448 | 196 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 248–448 | 197 | 3 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 248–388 | 125 | 4 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 248–423 | 163 | 6 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 248–422 | 175 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 248–448 | 200 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 248–375 | 125 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 267–275 | 9 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 269–448 | 180 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 282–284 | 3 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 306–315 | 10 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 342–417 | 69 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 362–414 | 52 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 362–400 | 34 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 394–410 | 17 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 398–417 | 20 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 402–414 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `12` (Position_Unknown)
- ⚠️ `Action_PullBlock` for actor_track_id `24` (Position_Unknown): Annotated start 244 != Inferred start 248
- ⚠️ `Action_Toss` for actor_track_id `12` (Position_Unknown): Annotated start 244 != Inferred start 245
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 15: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 15: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 16: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 16: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 16: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [272-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [377-437] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-358] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-380] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-407] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-333] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-355] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-343] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-398] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-334] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-271] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-291] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-309] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-344] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-366] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-410] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-329] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-366] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-374] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-343] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-413] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-216] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-310] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-14] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-127] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [245-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-363] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-391] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-115] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-346] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-198] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-263] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-322] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-365] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-426] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-307] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-331] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-448] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-289] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-379] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-296] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-314] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-366] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-388] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-423] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-422] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-443] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-448] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-366] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-448] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-417] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-375] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-414] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-364] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-400] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-410] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-417] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-414] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>