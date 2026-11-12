# Play-Annotation-Generator Annotation Review — SplitZone_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_141`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 659
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE1 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 12 | START | 13 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 12 | START | 13 | 453 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 12 | START | 13 | 426 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 12 | START | 13 | 429 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 12 | START | 13 | 426 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 12 | START | 13 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 12 | START | 13 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 12 | START | 17 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 12 | START | 13 | 426 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 12 | START | 13 | 426 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 12 | START | 13 | 464 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 427 | START | 427 | 439 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 430 | START | 430 | 578 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `16` | 430 | START | 440 | 578 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 430 | START | 430 | 507 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 430 | START | 430 | 458 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 430 | START | 430 | 528 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `0` | `0` | 433 | START | 433 | 551 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 439 | END | 427 | 439 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 446 | START | 446 | 464 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | TE1 | `1` | `1` | 454 | START | 454 | 480 |
| ✅ EXACT | `Action_BallCarry` | RB | `9` | `9` | 465 | START | 465 | 649 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 578 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–659
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_SnapReceive` | 427 | 439 | 13 | inferred_complete_timeline |
| `Action_None` | 440 | 445 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 446 | 464 | 19 | inferred_complete_timeline |
| `Action_None` | 465 | 659 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–649
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 464 | 452 | inferred_complete_timeline |
| `Action_BallCarry` | 465 | 649 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–543
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 543 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–659
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 659 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–659
- **Visible Samples:** 636

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 453 | 441 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 454 | 480 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 489 | 578 | 90 | inferred_complete_timeline |
| `Action_None` | 579 | 631 | 53 | inferred_complete_timeline |
| `Action_None` | 634 | 635 | 2 | inferred_complete_timeline |
| `Action_None` | 637 | 659 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–659
- **Visible Samples:** 645

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 432 | 420 | inferred_complete_timeline |
| `Action_SplitBlock` | 433 | 551 | 119 | inferred_complete_timeline |
| `Action_SplitBlock` | 554 | 578 | 25 | inferred_complete_timeline |
| `Action_None` | 579 | 659 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–659
- **Visible Samples:** 646

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 429 | 417 | inferred_complete_timeline |
| `Action_ZoneBlock` | 430 | 578 | 149 | inferred_complete_timeline |
| `Action_None` | 579 | 633 | 55 | inferred_complete_timeline |
| `Action_None` | 635 | 659 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 17–528
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 37 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 429 | 369 | inferred_complete_timeline |
| `Action_ZoneBlock` | 430 | 528 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–659
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_BallSnap` | 427 | 439 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 440 | 578 | 139 | inferred_complete_timeline |
| `Action_None` | 579 | 659 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–461
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 24 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 45 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 63 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 127 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 429 | 301 | inferred_complete_timeline |
| `Action_ZoneBlock` | 430 | 458 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 460 | 461 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–507
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 134 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 429 | 290 | inferred_complete_timeline |
| `Action_ZoneBlock` | 430 | 507 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–467
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 467 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 484 | 58 | inferred_complete_timeline |
| `Action_None` | 494 | 573 | 80 | inferred_complete_timeline |
| `Action_None` | 575 | 659 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 659 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–486
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 169 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 426 | 256 | inferred_complete_timeline |
| `Action_None` | 427 | 486 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 659 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 642

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 516 | 90 | inferred_complete_timeline |
| `Action_None` | 522 | 659 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 659 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 646

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 516 | 90 | inferred_complete_timeline |
| `Action_None` | 518 | 659 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 646

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 612 | 186 | inferred_complete_timeline |
| `Action_None` | 614 | 659 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–655
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 636 | 210 | inferred_complete_timeline |
| `Action_None` | 646 | 655 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–659
- **Visible Samples:** 643

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 426 | 414 | inferred_complete_timeline |
| `Action_None` | 427 | 561 | 135 | inferred_complete_timeline |
| `Action_None` | 566 | 659 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 121–123 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 195–197 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 237–313 | 61 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 456–586 | 130 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 475–659 | 181 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 484–515 | 23 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 522–659 | 138 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 533–659 | 127 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 536–539 | 4 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 543–659 | 111 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 557–659 | 103 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 560–659 | 58 | 8 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 573–592 | 8 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 586–659 | 74 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 596–597 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 608–653 | 31 | 8 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 611–621 | 9 | 2 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 624–626 | 3 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 625–645 | 8 | 3 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 644–647 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 430 != Inferred start 440
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '1' (TE1) duration 125 frames exceeds threshold 90 frames [start=454, end=578].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 149 frames exceeds threshold 90 frames [start=430, end=578].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 149 frames exceeds threshold 90 frames [start=430, end=578].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [427–439], lower_priority='Action_ZoneBlock' annotated_start=430, effective_Action_ZoneBlock_start=440.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 99 frames exceeds threshold 90 frames [start=430, end=528].
- ⚠️ Action 'Action_SplitBlock' range [433-551] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [454-480] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-631] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-484] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-573] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-659] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-636] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-655] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-612] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-659] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-467] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [465-649] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-516] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-543] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-561] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-659] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-633] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-659] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-516] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-659] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-486] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [430-507] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-24] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-63] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-76] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-87] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-127] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [430-458] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [460-461] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-429] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [430-528] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-259] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-313] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-475] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-586] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-491] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-515] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-539] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-607] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-565] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-578] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-583] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-620] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-632] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-597] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-616] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-621] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-632] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-653] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-621] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-626] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-628] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-635] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-647] for track '41' has 1 frames without a visible bounding box.
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