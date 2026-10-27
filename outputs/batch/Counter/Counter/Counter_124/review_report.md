# Play-Annotation-Generator Annotation Review — Counter_124

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_124`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 40
- **Ball Tracks:** 2
- **Action Segments:** 97
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 8
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_PullBlock` | SAF1 | defense | `1` | `0` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `15` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 396 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 396 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 399 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 397 | START | 397 | 411 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `13` | `12` | 400 | START | 412 | 443 |
| ✅ EXACT | `Action_DownBlock` | RG | `7` | `6` | 400 | START | 400 | 443 |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | `20` | `19` | 400 | START | 400 | 441 |
| ✅ EXACT | `Action_PullBlock` | SAF1 | `1` | `0` | 400 | START | 400 | 443 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `22` | `21` | 400 | START | 400 | 443 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 411 | END | 397 | 411 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 417 | START | 417 | 441 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `20` | `19` | 442 | START | 442 | 506 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 443 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–504
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_SnapReceive` | 397 | 411 | 15 | inferred_complete_timeline |
| `Action_None` | 412 | 416 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 417 | 441 | 25 | inferred_complete_timeline |
| `Action_None` | 442 | 504 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–577
- **Visible Samples:** 578

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 577 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 396 | 372 | inferred_complete_timeline |
| `Action_BallSnap` | 397 | 411 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 412 | 443 | 32 | inferred_complete_timeline |
| `Action_None` | 444 | 629 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_DownBlock` | 400 | 443 | 44 | inferred_complete_timeline |
| `Action_None` | 444 | 520 | 77 | inferred_complete_timeline |
| `Action_None` | 526 | 629 | 104 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 586 | 190 | inferred_complete_timeline |
| `Action_None` | 590 | 596 | 7 | inferred_complete_timeline |
| `Action_None` | 598 | 629 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–486
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 458 | 62 | inferred_complete_timeline |
| `Action_None` | 464 | 466 | 3 | inferred_complete_timeline |
| `Action_None` | 469 | 480 | 12 | inferred_complete_timeline |
| `Action_None` | 482 | 486 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 419 | 23 | inferred_complete_timeline |
| `Action_None` | 424 | 629 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–473
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 431 | 35 | inferred_complete_timeline |
| `Action_None` | 443 | 450 | 8 | inferred_complete_timeline |
| `Action_None` | 463 | 464 | 2 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |
| `Action_None` | 471 | 473 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–457
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 457 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 522 | 126 | inferred_complete_timeline |
| `Action_None` | 524 | 629 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–557
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_PullBlock` | 400 | 443 | 44 | inferred_complete_timeline |
| `Action_None` | 444 | 451 | 8 | inferred_complete_timeline |
| `Action_None` | 453 | 557 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 396 | 397 | inferred_complete_timeline |
| `Action_None` | 397 | 478 | 82 | inferred_complete_timeline |
| `Action_None` | 491 | 493 | 3 | inferred_complete_timeline |
| `Action_None` | 495 | 629 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–289 | 290 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 28–47 | 15 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 96–115 | 20 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 244–629 | 386 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 247–506 | 260 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 343–474 | 122 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 359–628 | 269 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 447–629 | 166 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 451–629 | 179 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 468–492 | 21 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 479–629 | 151 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 483–629 | 136 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 489–514 | 21 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 503–629 | 127 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 507–508 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 509–629 | 121 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 511–550 | 40 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 517–629 | 113 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 521–579 | 57 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 540–541 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 550–629 | 80 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 552–629 | 78 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 570–625 | 13 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 578–629 | 49 | 3 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 590–602 | 13 | 1 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 615–617 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 7 | 7 | 1 | 100.0% | None |
| `20` | `21` | 288 | 288 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `13` (C): Annotated start 400 != Inferred start 412

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF3` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 250: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 250: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [397–411], lower_priority='Action_DownBlock' annotated_start=400, effective_Action_DownBlock_start=412.
- ⚠️ Action 'Action_None' range [444-451] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-557] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-577] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-478] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-629] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-504] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-458] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-480] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-399] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-520] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-522] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-586] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-596] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-431] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-450] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-473] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-457] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [442-506] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-460] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-491] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-628] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-470] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-487] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-629] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-477] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-482] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-492] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-599] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-625] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-493] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-514] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-550] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-572] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-579] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-573] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-625] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-586] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-602] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>