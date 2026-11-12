# Play-Annotation-Generator Annotation Review — SplitZone_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_18`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 97
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | TE2 | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 399 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 355 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 261 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 356 | START | 356 | 368 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 359 | START | 359 | 373 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 359 | START | 359 | 436 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 359 | START | 369 | 374 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 359 | START | 359 | 373 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `7` | `7` | 359 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 368 | END | 356 | 368 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `5` | `5` | 368 | START | 368 | 373 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 384 | START | 384 | 399 |
| ✅ EXACT | `Action_BallCarry` | TE2 | `1` | `1` | 400 | START | 400 | 436 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `10` | `10` | 406 | START | 406 | 411 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 436 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 355 | 140 | inferred_complete_timeline |
| `Action_SnapReceive` | 356 | 368 | 13 | inferred_complete_timeline |
| `Action_None` | 369 | 373 | 5 | inferred_complete_timeline |
| `Action_None` | 377 | 383 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 384 | 399 | 16 | inferred_complete_timeline |
| `Action_None` | 400 | 436 | 37 | inferred_complete_timeline |
| `Action_None` | 438 | 539 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–452
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 441 | 86 | inferred_complete_timeline |
| `Action_None` | 451 | 452 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_SplitBlock` | 368 | 373 | 6 | inferred_complete_timeline |
| `Action_SplitBlock` | 378 | 411 | 34 | inferred_complete_timeline |
| `Action_SplitBlock` | 414 | 418 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_None` | 442 | 539 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–436
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_BallCarry` | 400 | 436 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |
| `Action_ZoneBlock` | 359 | 436 | 78 | inferred_complete_timeline |
| `Action_None` | 437 | 482 | 46 | inferred_complete_timeline |
| `Action_None` | 493 | 539 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 181 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 235 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 358 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 359 | 373 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 377 | 405 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 406 | 411 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 290 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 295 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 355 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 356 | 368 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 369 | 374 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 377 | 436 | 60 | inferred_complete_timeline |
| `Action_None` | 437 | 449 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |
| `Action_ZoneBlock` | 359 | 373 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 377 | 421 | 45 | inferred_complete_timeline |
| `Action_None` | 447 | 449 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 365 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–371
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 371 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–491
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 373 | 18 | inferred_complete_timeline |
| `Action_None` | 376 | 491 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–420
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 412 | 57 | inferred_complete_timeline |
| `Action_None` | 416 | 420 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–422
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 403 | 48 | inferred_complete_timeline |
| `Action_None` | 405 | 410 | 6 | inferred_complete_timeline |
| `Action_None` | 412 | 414 | 3 | inferred_complete_timeline |
| `Action_None` | 418 | 422 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–444
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 426 | 71 | inferred_complete_timeline |
| `Action_None` | 429 | 436 | 8 | inferred_complete_timeline |
| `Action_None` | 438 | 444 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 424 | 69 | inferred_complete_timeline |
| `Action_None` | 428 | 474 | 47 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 480 | 539 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–434
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 355 | 356 | inferred_complete_timeline |
| `Action_None` | 356 | 413 | 58 | inferred_complete_timeline |
| `Action_None` | 433 | 434 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 279–446 | 168 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 355–448 | 76 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 384–430 | 43 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 388–427 | 37 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 392–539 | 139 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 413–471 | 59 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 417–474 | 54 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 417–539 | 123 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 421–445 | 25 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 424–539 | 94 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 424–462 | 38 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 431–453 | 20 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 435–474 | 27 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 442–525 | 81 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 447–539 | 93 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 450–493 | 18 | 4 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 450–451 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 487–539 | 50 | 3 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 494–495 | 2 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 514–515 | 2 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 514–529 | 15 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 521–539 | 19 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 524–539 | 16 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 527–539 | 9 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 530–539 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (RT)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '7' has invalid range: start=359, end=261. Clamping end to start.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [356–368], lower_priority='Action_ZoneBlock' annotated_start=359, effective_Action_ZoneBlock_start=369.
- ⚠️ Action 'Action_None' range [356-413] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [400-436] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-403] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-410] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [359-373] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [377-421] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-449] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-373] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-491] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [368-373] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [378-411] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [414-418] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [432-433] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-424] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-474] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-426] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-436] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-444] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-412] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-358] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [359-373] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [377-405] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [406-411] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-441] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-371] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-355] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-365] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-482] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-290] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [369-374] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [377-436] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-355] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-436] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-446] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-371] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-448] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-430] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-422] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-417] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-477] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-501] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-471] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-474] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-445] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-438] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-488] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-501] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-430] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-462] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-443] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-453] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-474] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-520] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-539] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-485] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-493] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-496] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-507] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-525] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-539] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '42' has 1 frames without a visible bounding box.
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

</details>