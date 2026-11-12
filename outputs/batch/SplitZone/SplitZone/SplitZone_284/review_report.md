# Play-Annotation-Generator Annotation Review — SplitZone_284

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_284`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 749
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 43
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 515 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 515 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 538 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 526 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 526 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 515 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 515 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 515 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 526 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `8` | `Group` | 0 | START | 0 | 526 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 516 | START | 516 | 528 |
| ✅ EXACT | `Action_SplitBlock` | HB | `8` | `8` | 527 | START | 527 | 548 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `13` | 527 | START | 527 | 598 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 527 | START | 527 | 598 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 527 | START | 529 | 551 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 527 | START | 527 | 598 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 528 | END | 516 | 528 |
| ✅ EXACT | `Action_PressEdge` | RB | `11` | `11` | 539 | START | 539 | 557 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 546 | START | 546 | 560 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `20` | `20` | 552 | START | 552 | 576 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 558 | START | 558 | 634 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_SnapReceive` | 516 | 528 | 13 | inferred_complete_timeline |
| `Action_None` | 529 | 545 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 546 | 560 | 15 | inferred_complete_timeline |
| `Action_None` | 561 | 749 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–728
- **Visible Samples:** 693

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 538 | 539 | inferred_complete_timeline |
| `Action_PressEdge` | 539 | 557 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 558 | 634 | 77 | inferred_complete_timeline |
| `Action_BallCarry` | 641 | 645 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 648 | 658 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 686 | 725 | 40 | inferred_complete_timeline |
| `Action_BallCarry` | 727 | 728 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 526 | 527 | inferred_complete_timeline |
| `Action_SplitBlock` | 527 | 548 | 22 | inferred_complete_timeline |
| `Action_None` | 549 | 749 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–639
- **Visible Samples:** 640

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 639 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 749 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 749 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 526 | 527 | inferred_complete_timeline |
| `Action_ZoneBlock` | 527 | 598 | 72 | inferred_complete_timeline |
| `Action_None` | 599 | 749 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 526 | 527 | inferred_complete_timeline |
| `Action_ZoneBlock` | 527 | 598 | 72 | inferred_complete_timeline |
| `Action_None` | 599 | 749 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_BallSnap` | 516 | 528 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 529 | 551 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 552 | 576 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 577 | 598 | 22 | inferred_complete_timeline |
| `Action_None` | 599 | 749 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 526 | 527 | inferred_complete_timeline |
| `Action_ZoneBlock` | 527 | 598 | 72 | inferred_complete_timeline |
| `Action_None` | 599 | 749 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 748

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 541 | 26 | inferred_complete_timeline |
| `Action_None` | 544 | 749 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–574
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 574 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–545
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 545 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 749 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 744

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 563 | 48 | inferred_complete_timeline |
| `Action_None` | 570 | 749 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 748

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 742 | 227 | inferred_complete_timeline |
| `Action_None` | 745 | 749 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–686
- **Visible Samples:** 683

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 634 | 119 | inferred_complete_timeline |
| `Action_None` | 639 | 686 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 749 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 749 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–749
- **Visible Samples:** 739

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 656 | 141 | inferred_complete_timeline |
| `Action_None` | 660 | 670 | 11 | inferred_complete_timeline |
| `Action_None` | 678 | 683 | 6 | inferred_complete_timeline |
| `Action_None` | 685 | 749 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–727
- **Visible Samples:** 728

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |
| `Action_None` | 516 | 727 | 212 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–749 | 748 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 558–749 | 190 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 567–569 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 578–749 | 170 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 623–629 | 7 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 674–749 | 73 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 691–749 | 59 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 26 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 570: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [516–528], lower_priority='Action_ZoneBlock' annotated_start=527, effective_Action_ZoneBlock_start=529.
- ⚠️ Action 'Action_None' range [516-639] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-541] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-742] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-574] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-571] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-749] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-545] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [558-634] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [641-645] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [648-658] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [686-725] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [727-728] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [527-598] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-727] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-563] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-749] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-634] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-686] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-656] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-670] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-683] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-560] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-582] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-629] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-676] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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