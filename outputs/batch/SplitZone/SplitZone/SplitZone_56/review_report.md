# Play-Annotation-Generator Annotation Review — SplitZone_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_56`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 2 | START | 22 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 2 | START | 22 | 390 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 22 | 390 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 2 | START | 22 | 390 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 2 | START | 22 | 392 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 2 | START | 22 | 387 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 2 | START | 22 | 390 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 2 | START | 22 | 297 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 388 | START | 388 | 398 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 391 | START | 391 | 523 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 391 | START | 391 | 523 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 391 | START | 391 | 416 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 391 | START | 391 | 523 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `9` | `9` | 391 | START | 399 | 439 |
| ✅ EXACT | `Action_SplitBlock` | TE | `6` | `6` | 393 | START | 393 | 523 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 398 | END | 388 | 398 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 408 | START | 408 | 419 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `0` | `0` | 420 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RB | `0` | `0` | 420 | START | 420 | 504 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 523 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–490
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 387 | 366 | inferred_complete_timeline |
| `Action_SnapReceive` | 388 | 398 | 11 | inferred_complete_timeline |
| `Action_None` | 399 | 407 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 408 | 419 | 12 | inferred_complete_timeline |
| `Action_None` | 420 | 490 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–569
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 419 | 398 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 420 | 504 | 85 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 506 | 523 | 18 | inferred_complete_timeline |
| `Action_None` | 524 | 569 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 22–569
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 392 | 371 | inferred_complete_timeline |
| `Action_SplitBlock` | 393 | 523 | 131 | inferred_complete_timeline |
| `Action_None` | 524 | 569 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–569
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 390 | 369 | inferred_complete_timeline |
| `Action_ZoneBlock` | 391 | 523 | 133 | inferred_complete_timeline |
| `Action_None` | 524 | 569 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–569
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 390 | 369 | inferred_complete_timeline |
| `Action_ZoneBlock` | 391 | 416 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 419 | 523 | 105 | inferred_complete_timeline |
| `Action_None` | 524 | 569 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 22–569
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 297 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 387 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 388 | 398 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 399 | 439 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 445 | 451 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 459 | 523 | 65 | inferred_complete_timeline |
| `Action_None` | 524 | 536 | 13 | inferred_complete_timeline |
| `Action_None` | 543 | 569 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 22–554
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 390 | 369 | inferred_complete_timeline |
| `Action_ZoneBlock` | 391 | 523 | 133 | inferred_complete_timeline |
| `Action_None` | 524 | 554 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 22–569
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 390 | 369 | inferred_complete_timeline |
| `Action_ZoneBlock` | 391 | 523 | 133 | inferred_complete_timeline |
| `Action_None` | 524 | 569 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–569
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 387 | 366 | inferred_complete_timeline |
| `Action_None` | 388 | 452 | 65 | inferred_complete_timeline |
| `Action_None` | 455 | 569 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 22–450
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 355 | 334 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 387 | 28 | inferred_complete_timeline |
| `Action_None` | 388 | 409 | 22 | inferred_complete_timeline |
| `Action_None` | 412 | 415 | 4 | inferred_complete_timeline |
| `Action_None` | 434 | 436 | 3 | inferred_complete_timeline |
| `Action_None` | 438 | 443 | 6 | inferred_complete_timeline |
| `Action_None` | 446 | 450 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 22–569
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 387 | 366 | inferred_complete_timeline |
| `Action_None` | 388 | 409 | 22 | inferred_complete_timeline |
| `Action_None` | 411 | 455 | 45 | inferred_complete_timeline |
| `Action_None` | 458 | 464 | 7 | inferred_complete_timeline |
| `Action_None` | 470 | 477 | 8 | inferred_complete_timeline |
| `Action_None` | 479 | 483 | 5 | inferred_complete_timeline |
| `Action_None` | 486 | 569 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–569
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 387 | 366 | inferred_complete_timeline |
| `Action_None` | 388 | 409 | 22 | inferred_complete_timeline |
| `Action_None` | 419 | 420 | 2 | inferred_complete_timeline |
| `Action_None` | 432 | 483 | 52 | inferred_complete_timeline |
| `Action_None` | 486 | 569 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–561
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 387 | 366 | inferred_complete_timeline |
| `Action_None` | 388 | 561 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–569
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 387 | 366 | inferred_complete_timeline |
| `Action_None` | 388 | 569 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 296–302 | 7 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 408–569 | 161 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 447–569 | 121 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 447–543 | 96 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 456–569 | 113 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 519–569 | 51 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 527–569 | 43 | 1 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 544–569 | 26 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 548–549 | 2 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 557–561 | 5 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 567–569 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `0` (RB)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Overlapping action conflict at frame 420 for track '0': 'Action_BallCarry' vs 'Action_BlockSecondLevel'. Overriding with 'Action_BlockSecondLevel'.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '0' (RB) duration 104 frames exceeds threshold 90 frames [start=420, end=523].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [388–398], lower_priority='Action_ZoneBlock' annotated_start=391, effective_Action_ZoneBlock_start=399.
- ⚠️ Action 'Action_BlockSecondLevel' range [420-504] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [391-416] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-569] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-561] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-355] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-409] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-415] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-443] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-450] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-490] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-554] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-297] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [399-439] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [445-451] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-536] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-452] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-569] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-409] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-455] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-477] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-483] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-569] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-409] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-483] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-487] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-510] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-511] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-543] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-490] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-561] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '24' has 1 frames without a visible bounding box.
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

</details>