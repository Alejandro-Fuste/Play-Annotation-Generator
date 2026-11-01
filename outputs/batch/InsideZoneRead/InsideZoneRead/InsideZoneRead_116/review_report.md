# Play-Annotation-Generator Annotation Review — InsideZoneRead_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_116`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 689
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 125
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 397 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 2 | 542 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 7 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 363 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 541 | START | 541 | 555 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 543 | START | 556 | 622 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `10` | 543 | START | 543 | 574 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 543 | START | 543 | 555 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 543 | START | 543 | 559 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 543 | START | 556 | 622 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 555 | END | 541 | 555 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 558 | START | 558 | 567 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 568 | START | 568 | 568 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `7` | `6` | 579 | START | 643 | 689 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 622 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–664
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 140 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 405 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 410 | 540 | 131 | inferred_complete_timeline |
| `Action_SnapReceive` | 541 | 555 | 15 | inferred_complete_timeline |
| `Action_None` | 556 | 557 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 558 | 567 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 568 | 568 | 1 | inferred_complete_timeline |
| `Action_None` | 583 | 618 | 36 | inferred_complete_timeline |
| `Action_None` | 620 | 635 | 16 | inferred_complete_timeline |
| `Action_None` | 637 | 648 | 12 | inferred_complete_timeline |
| `Action_None` | 654 | 656 | 3 | inferred_complete_timeline |
| `Action_None` | 662 | 664 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 548 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 555 | 556 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 558 | 569 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 643 | 689 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–559
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 32 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 162 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 445 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 456 | 542 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 543 | 559 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–652
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 397 | 398 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 404 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 540 | 92 | inferred_complete_timeline |
| `Action_BallSnap` | 541 | 555 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 556 | 622 | 67 | inferred_complete_timeline |
| `Action_None` | 623 | 633 | 11 | inferred_complete_timeline |
| `Action_None` | 638 | 652 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–689
- **Visible Samples:** 661

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 542 | 541 | inferred_complete_timeline |
| `Action_ZoneBlock` | 543 | 555 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 568 | 605 | 38 | inferred_complete_timeline |
| `Action_ZoneBlock` | 607 | 608 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 610 | 622 | 13 | inferred_complete_timeline |
| `Action_None` | 623 | 634 | 12 | inferred_complete_timeline |
| `Action_None` | 639 | 652 | 14 | inferred_complete_timeline |
| `Action_None` | 662 | 689 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 680

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 542 | 537 | inferred_complete_timeline |
| `Action_ZoneBlock` | 543 | 574 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 583 | 622 | 40 | inferred_complete_timeline |
| `Action_None` | 623 | 625 | 3 | inferred_complete_timeline |
| `Action_None` | 627 | 689 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 663

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 540 | 101 | inferred_complete_timeline |
| `Action_None` | 541 | 620 | 80 | inferred_complete_timeline |
| `Action_None` | 635 | 644 | 10 | inferred_complete_timeline |
| `Action_None` | 648 | 671 | 24 | inferred_complete_timeline |
| `Action_None` | 673 | 674 | 2 | inferred_complete_timeline |
| `Action_None` | 676 | 681 | 6 | inferred_complete_timeline |
| `Action_None` | 683 | 689 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 540 | 541 | inferred_complete_timeline |
| `Action_None` | 541 | 689 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–685
- **Visible Samples:** 686

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 540 | 541 | inferred_complete_timeline |
| `Action_None` | 541 | 685 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 661

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 540 | 541 | inferred_complete_timeline |
| `Action_None` | 541 | 568 | 28 | inferred_complete_timeline |
| `Action_None` | 576 | 594 | 19 | inferred_complete_timeline |
| `Action_None` | 600 | 624 | 25 | inferred_complete_timeline |
| `Action_None` | 628 | 640 | 13 | inferred_complete_timeline |
| `Action_None` | 648 | 677 | 30 | inferred_complete_timeline |
| `Action_None` | 685 | 689 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 671

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 540 | 541 | inferred_complete_timeline |
| `Action_None` | 541 | 638 | 98 | inferred_complete_timeline |
| `Action_None` | 649 | 653 | 5 | inferred_complete_timeline |
| `Action_None` | 663 | 689 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 62–689 | 588 | 8 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 96–105 | 10 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 109–142 | 29 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 114–185 | 72 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 136–611 | 361 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 150–171 | 22 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 225–374 | 148 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 363–371 | 6 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 431–689 | 256 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 531–689 | 146 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 562–571 | 10 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 583–620 | 38 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 590–689 | 100 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 610–662 | 53 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 618–630 | 12 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 626–689 | 44 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 634–689 | 56 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 664–689 | 26 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 685–689 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 543 != Inferred start 556
- ⚠️ `Action_BallCarry` for actor_track_id `7` (RB): Annotated start 579 != Inferred start 643

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=543, end=74. Clamping end to start.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [541–555], lower_priority='Action_ZoneBlock' annotated_start=543, effective_Action_ZoneBlock_start=556.
- ⚠️ Action 'Action_PreSnap' range [0-162] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-540] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-685] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-568] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-594] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-624] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-640] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-677] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-432] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-620] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-644] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-671] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-674] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-681] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-638] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-653] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-363] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-548] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-556] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [558-569] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-405] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-540] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' for track '7' starts at frame 568, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Handoff' range [568-568] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-618] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-635] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-648] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-656] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-664] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-397] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-404] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-633] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-652] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [543-574] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-689] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-542] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [543-555] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [568-605] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [607-608] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [610-622] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-634] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-652] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-445] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [543-559] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-364] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-388] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-594] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-618] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-623] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-689] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-130] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-262] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-374] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-397] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-611] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-370] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-374] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-365] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-660] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-546] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-569] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-581] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-571] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-620] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-662] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-627] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-630] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-657] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-689] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>