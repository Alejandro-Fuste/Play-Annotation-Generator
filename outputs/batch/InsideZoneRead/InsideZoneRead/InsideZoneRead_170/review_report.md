# Play-Annotation-Generator Annotation Review — InsideZoneRead_170

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_170`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 407 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 407 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 436 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 407 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `7` | `Group` | 0 | START | 0 | 407 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 408 | START | 408 | 422 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 410 | START | 410 | 431 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 410 | START | 423 | 430 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 410 | START | 410 | 505 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 410 | START | 410 | 505 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `20` | 410 | START | 410 | 464 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 422 | END | 408 | 422 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `11` | 425 | START | 425 | 439 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 440 | START | 440 | 452 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `12` | 453 | START | 453 | 629 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 505 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_SnapReceive` | 408 | 422 | 15 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 425 | 439 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 440 | 452 | 13 | inferred_complete_timeline |
| `Action_None` | 453 | 622 | 170 | inferred_complete_timeline |
| `Action_None` | 625 | 629 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 436 | 437 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 452 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 453 | 629 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 629 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–618
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 449 | 42 | inferred_complete_timeline |
| `Action_None` | 459 | 464 | 6 | inferred_complete_timeline |
| `Action_None` | 469 | 470 | 2 | inferred_complete_timeline |
| `Action_None` | 474 | 487 | 14 | inferred_complete_timeline |
| `Action_None` | 495 | 504 | 10 | inferred_complete_timeline |
| `Action_None` | 535 | 563 | 29 | inferred_complete_timeline |
| `Action_None` | 598 | 599 | 2 | inferred_complete_timeline |
| `Action_None` | 602 | 618 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–611
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 611 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–431
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_ZoneBlock` | 410 | 431 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–464
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_ZoneBlock` | 410 | 464 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–590
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 407 | 181 | inferred_complete_timeline |
| `Action_BallSnap` | 408 | 422 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 423 | 430 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 445 | 505 | 61 | inferred_complete_timeline |
| `Action_None` | 506 | 581 | 76 | inferred_complete_timeline |
| `Action_None` | 583 | 584 | 2 | inferred_complete_timeline |
| `Action_None` | 588 | 590 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 280 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 409 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 410 | 505 | 96 | inferred_complete_timeline |
| `Action_None` | 506 | 520 | 15 | inferred_complete_timeline |
| `Action_None` | 522 | 629 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–613
- **Visible Samples:** 614

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_ZoneBlock` | 410 | 505 | 96 | inferred_complete_timeline |
| `Action_None` | 506 | 613 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–616
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 459 | 52 | inferred_complete_timeline |
| `Action_None` | 461 | 501 | 41 | inferred_complete_timeline |
| `Action_None` | 508 | 616 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 562 | 155 | inferred_complete_timeline |
| `Action_None` | 566 | 629 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–481
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 22 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 407 | 382 | inferred_complete_timeline |
| `Action_None` | 408 | 481 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 549 | 142 | inferred_complete_timeline |
| `Action_None` | 553 | 559 | 7 | inferred_complete_timeline |
| `Action_None` | 562 | 588 | 27 | inferred_complete_timeline |
| `Action_None` | 590 | 629 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–500
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 500 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 610 | 203 | inferred_complete_timeline |
| `Action_None` | 612 | 629 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 594 | 187 | inferred_complete_timeline |
| `Action_None` | 599 | 629 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 607 | 200 | inferred_complete_timeline |
| `Action_None` | 610 | 613 | 4 | inferred_complete_timeline |
| `Action_None` | 616 | 618 | 3 | inferred_complete_timeline |
| `Action_None` | 623 | 629 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–526
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 487 | 80 | inferred_complete_timeline |
| `Action_None` | 512 | 513 | 2 | inferred_complete_timeline |
| `Action_None` | 515 | 517 | 3 | inferred_complete_timeline |
| `Action_None` | 523 | 526 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–508
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |
| `Action_None` | 408 | 492 | 85 | inferred_complete_timeline |
| `Action_None` | 495 | 497 | 3 | inferred_complete_timeline |
| `Action_None` | 506 | 508 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–629 | 630 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 6–28 | 8 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 76–430 | 328 | 8 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 129–629 | 442 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 440–482 | 39 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 440–606 | 91 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 443–489 | 25 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 466–613 | 139 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 507–629 | 107 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 507–629 | 122 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 508–629 | 120 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 524–526 | 3 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 539–629 | 91 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 571–614 | 43 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 573–575 | 3 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 597–629 | 33 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 340: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 340: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 96 frames exceeds threshold 90 frames [start=410, end=505].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [408–422], lower_priority='Action_ZoneBlock' annotated_start=410, effective_Action_ZoneBlock_start=423.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 96 frames exceeds threshold 90 frames [start=410, end=505].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 96 frames exceeds threshold 90 frames [start=410, end=505].
- ⚠️ Action 'Action_None' range [408-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-610] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-487] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-449] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-464] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-487] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-504] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-563] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-599] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-618] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-594] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-607] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-613] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-618] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-611] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-492] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-508] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [410-431] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-459] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-501] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-616] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-622] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-436] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [423-430] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-581] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-590] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-562] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-407] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-549] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-559] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-588] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-629] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [410-505] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-613] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-280] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-520] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-500] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-22] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-481] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [410-464] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-328] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-334] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-340] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-388] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-396] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-407] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-430] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-441] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-462] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-482] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-537] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-543] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-606] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-451] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-478] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-551] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-603] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-604] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-537] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-604] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-614] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-575] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>