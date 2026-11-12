# Play-Annotation-Generator Annotation Review — SplitZone_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_102`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 689
- **Player Tracks:** 39
- **Ball Tracks:** 6
- **Action Segments:** 89
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | DT1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 12 | START | 13 | 497 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 12 | START | 13 | 489 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 12 | START | 13 | 492 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 12 | START | 13 | 492 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 12 | START | 13 | 492 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 12 | START | 13 | 492 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 12 | START | 13 | 518 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 490 | START | 490 | 504 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 493 | START | 505 | 586 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 493 | START | 493 | 583 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 493 | START | 493 | 514 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `6` | 493 | START | 493 | 568 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `7` | `7` | 493 | START | 493 | 610 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `1` | `1` | 498 | START | 498 | 522 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `13` | `13` | 504 | END | 490 | 504 |
| ✅ EXACT | `Action_Handoff` | DT1 | `13` | `13` | 508 | START | 508 | 518 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 519 | START | 519 | 529 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 610 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–582
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 518 | 506 | inferred_complete_timeline |
| `Action_BallCarry` | 519 | 529 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 573 | 574 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 576 | 582 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–592
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 497 | 485 | inferred_complete_timeline |
| `Action_SplitBlock` | 498 | 522 | 25 | inferred_complete_timeline |
| `Action_SplitBlock` | 579 | 592 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–622
- **Visible Samples:** 609

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 492 | 480 | inferred_complete_timeline |
| `Action_ZoneBlock` | 493 | 568 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 570 | 610 | 41 | inferred_complete_timeline |
| `Action_None` | 611 | 622 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–627
- **Visible Samples:** 607

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 492 | 480 | inferred_complete_timeline |
| `Action_ZoneBlock` | 493 | 583 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 586 | 589 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 596 | 610 | 15 | inferred_complete_timeline |
| `Action_None` | 611 | 627 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–624
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_BallSnap` | 490 | 504 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 505 | 586 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 589 | 610 | 22 | inferred_complete_timeline |
| `Action_None` | 611 | 624 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–635
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 492 | 480 | inferred_complete_timeline |
| `Action_ZoneBlock` | 493 | 610 | 118 | inferred_complete_timeline |
| `Action_None` | 611 | 635 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–517
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 492 | 480 | inferred_complete_timeline |
| `Action_ZoneBlock` | 493 | 514 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 516 | 517 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–631
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_None` | 490 | 631 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–689
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_None` | 490 | 689 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–546
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_SnapReceive` | 490 | 504 | 15 | inferred_complete_timeline |
| `Action_None` | 505 | 507 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 508 | 518 | 11 | inferred_complete_timeline |
| `Action_None` | 519 | 530 | 12 | inferred_complete_timeline |
| `Action_None` | 532 | 546 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–652
- **Visible Samples:** 640

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_None` | 490 | 652 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–628
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_None` | 490 | 628 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 27–655
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 489 | 463 | inferred_complete_timeline |
| `Action_None` | 490 | 655 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–689
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_None` | 490 | 689 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–517
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 489 | 477 | inferred_complete_timeline |
| `Action_None` | 490 | 517 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 13–546 | 534 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 116–173 | 58 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 186–305 | 94 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 219–227 | 8 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 456–674 | 190 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 523–529 | 7 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 528–548 | 21 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 537–579 | 34 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 540–689 | 150 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 543–657 | 98 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 546–607 | 58 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 556–601 | 45 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 563–666 | 101 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 591–689 | 94 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 591–689 | 97 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 592–689 | 98 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 594–689 | 96 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 595–597 | 3 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 599–601 | 3 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 603–644 | 42 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 608–640 | 33 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 614–623 | 9 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 678–689 | 12 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 685–689 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | 44 | 59 | 8 | 50.0% | 45–48, 50–51, 53, 55 |
| `17` | `19` | 94 | 167 | 59 | 79.7% | 95–96, 98–99, 101–102, 104, 106, 135, 146, 149, 158, 161–163 |
| `21` | `26` | 442 | 469 | 11 | 39.3% | 452–468 |
| `40` | `46` | 617 | 617 | 1 | 100.0% | None |
| `42` | `56` | 680 | 680 | 1 | 100.0% | None |
| `44` | `58` | 685 | 685 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 206: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [490–504], lower_priority='Action_ZoneBlock' annotated_start=493, effective_Action_ZoneBlock_start=505.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
- ⚠️ Action 'Action_SplitBlock' range [498-522] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [579-592] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [493-514] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [516-517] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-546] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-631] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-689] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [493-568] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-622] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-635] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-652] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [519-529] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [573-574] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [576-582] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [505-586] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [589-610] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-624] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-628] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [493-583] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [586-589] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-627] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-530] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-546] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-489] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-517] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-655] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-305] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-227] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-457] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-480] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-489] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 490, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [490-492] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-570] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-674] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-529] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-548] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-540] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-579] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-689] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-583] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-657] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-561] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-607] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-587] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-601] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-587] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-666] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-633] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-647] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-641] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-597] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-601] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-644] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-640] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-618] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-623] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>