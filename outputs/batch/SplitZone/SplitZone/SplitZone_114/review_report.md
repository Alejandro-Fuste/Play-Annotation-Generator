# Play-Annotation-Generator Annotation Review — SplitZone_114

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_114`
- **Frame Range:** 0 to 809 (810 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 809
- **Player Tracks:** 32
- **Ball Tracks:** 6
- **Action Segments:** 116
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 13 | START | 14 | 654 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 13 | START | 14 | 651 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 13 | START | 14 | 654 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 13 | START | 14 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 13 | START | 14 | 651 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 13 | START | 14 | 654 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 13 | START | 14 | 466 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 13 | START | 14 | 654 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 652 | START | 652 | 667 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `15` | `15` | 653 | START | 653 | 687 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 655 | START | 655 | 725 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 655 | START | 668 | 716 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 655 | START | 655 | 698 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 655 | START | 655 | 725 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 655 | START | 655 | 675 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 667 | END | 652 | 667 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 670 | START | 670 | 677 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `7` | 678 | START | 678 | 706 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 725 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–809
- **Visible Samples:** 754

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 651 | 638 | inferred_complete_timeline |
| `Action_SnapReceive` | 652 | 667 | 16 | inferred_complete_timeline |
| `Action_None` | 668 | 669 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 670 | 677 | 8 | inferred_complete_timeline |
| `Action_None` | 678 | 691 | 14 | inferred_complete_timeline |
| `Action_None` | 734 | 809 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 14–706
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 466 | 453 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 677 | 206 | inferred_complete_timeline |
| `Action_BallCarry` | 678 | 706 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–809
- **Visible Samples:** 733

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 21 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 39 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 182 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 287 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 439 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 453 | 457 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 460 | 550 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 552 | 557 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 564 | 583 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 585 | 591 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 593 | 615 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 624 | 626 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 628 | 632 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 634 | 637 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 639 | 640 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 644 | 652 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 653 | 687 | 35 | inferred_complete_timeline |
| `Action_SplitBlock` | 689 | 708 | 20 | inferred_complete_timeline |
| `Action_SplitBlock` | 710 | 713 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 717 | 725 | 9 | inferred_complete_timeline |
| `Action_None` | 726 | 809 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–809
- **Visible Samples:** 796

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 654 | 641 | inferred_complete_timeline |
| `Action_ZoneBlock` | 655 | 725 | 71 | inferred_complete_timeline |
| `Action_None` | 726 | 809 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 14–758
- **Visible Samples:** 705

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 654 | 641 | inferred_complete_timeline |
| `Action_ZoneBlock` | 655 | 698 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 719 | 725 | 7 | inferred_complete_timeline |
| `Action_None` | 726 | 728 | 3 | inferred_complete_timeline |
| `Action_None` | 738 | 739 | 2 | inferred_complete_timeline |
| `Action_None` | 741 | 743 | 3 | inferred_complete_timeline |
| `Action_None` | 754 | 758 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–809
- **Visible Samples:** 787

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 651 | 638 | inferred_complete_timeline |
| `Action_BallSnap` | 652 | 667 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 668 | 716 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 724 | 725 | 2 | inferred_complete_timeline |
| `Action_None` | 726 | 754 | 29 | inferred_complete_timeline |
| `Action_None` | 757 | 809 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 14–770
- **Visible Samples:** 673

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 654 | 641 | inferred_complete_timeline |
| `Action_ZoneBlock` | 655 | 675 | 21 | inferred_complete_timeline |
| `Action_None` | 727 | 730 | 4 | inferred_complete_timeline |
| `Action_None` | 749 | 750 | 2 | inferred_complete_timeline |
| `Action_None` | 766 | 770 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–809
- **Visible Samples:** 775

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 654 | 641 | inferred_complete_timeline |
| `Action_ZoneBlock` | 655 | 725 | 71 | inferred_complete_timeline |
| `Action_None` | 726 | 755 | 30 | inferred_complete_timeline |
| `Action_None` | 763 | 769 | 7 | inferred_complete_timeline |
| `Action_None` | 784 | 809 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 14–809
- **Visible Samples:** 793

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 446 | 433 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 651 | 202 | inferred_complete_timeline |
| `Action_None` | 652 | 809 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–809
- **Visible Samples:** 792

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 35 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 651 | 612 | inferred_complete_timeline |
| `Action_None` | 652 | 809 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–809
- **Visible Samples:** 754

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 395 | 382 | inferred_complete_timeline |
| `Action_PreSnap` | 405 | 620 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 624 | 651 | 28 | inferred_complete_timeline |
| `Action_None` | 652 | 722 | 71 | inferred_complete_timeline |
| `Action_None` | 730 | 738 | 9 | inferred_complete_timeline |
| `Action_None` | 740 | 744 | 5 | inferred_complete_timeline |
| `Action_None` | 767 | 809 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–809
- **Visible Samples:** 768

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 651 | 638 | inferred_complete_timeline |
| `Action_None` | 652 | 704 | 53 | inferred_complete_timeline |
| `Action_None` | 713 | 725 | 13 | inferred_complete_timeline |
| `Action_None` | 738 | 747 | 10 | inferred_complete_timeline |
| `Action_None` | 755 | 804 | 50 | inferred_complete_timeline |
| `Action_None` | 806 | 809 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–809
- **Visible Samples:** 796

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 651 | 638 | inferred_complete_timeline |
| `Action_None` | 652 | 809 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–740
- **Visible Samples:** 714

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 41 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 651 | 609 | inferred_complete_timeline |
| `Action_None` | 652 | 719 | 68 | inferred_complete_timeline |
| `Action_None` | 722 | 724 | 3 | inferred_complete_timeline |
| `Action_None` | 734 | 737 | 4 | inferred_complete_timeline |
| `Action_None` | 739 | 740 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 14–83
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 83 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–800
- **Visible Samples:** 787

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 651 | 638 | inferred_complete_timeline |
| `Action_None` | 652 | 800 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 77–803 | 690 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 243–382 | 138 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 324–393 | 70 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 632–750 | 119 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 642–706 | 65 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 658–686 | 6 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 695–809 | 115 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 711–809 | 99 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 720–732 | 11 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 756–809 | 52 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 756–809 | 54 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 788–809 | 22 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 796–798 | 3 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 798–809 | 12 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 806–809 | 4 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 806–809 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | 35 | 123 | 39 | 43.8% | 36–42, 46–49, 54–57, 62–88, 102, 111–114, 117–119 |
| `20` | `21` | 523 | 539 | 13 | 76.5% | 528–529, 531, 535 |
| `23` | `25` | 645 | 651 | 7 | 100.0% | None |
| `27` | `34` | 718 | 809 | 64 | 69.6% | 719–746 |
| `29` | `36` | 720 | 720 | 1 | 100.0% | None |
| `30` | `38` | 725 | 725 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 809 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [652–667], lower_priority='Action_ZoneBlock' annotated_start=655, effective_Action_ZoneBlock_start=668.
- ⚠️ Action 'Action_PreSnap' range [14-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-691] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-800] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-446] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-755] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [763-769] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [784-809] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-704] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-725] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-747] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [755-804] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [806-809] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-466] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [678-706] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-654] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [655-675] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [727-730] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-750] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [766-770] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-809] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [668-716] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-754] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-719] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [722-724] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [734-737] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-740] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [655-698] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [726-728] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-739] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [741-743] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [754-758] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-395] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-620] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-722] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [730-738] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [740-744] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-21] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-39] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-182] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-287] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-439] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-457] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-550] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [552-557] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [564-583] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [585-591] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [593-615] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [624-626] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [628-632] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [634-637] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [639-640] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [653-687] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [689-708] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [710-713] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-730] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-746] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [782-785] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [787-803] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-344] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-382] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-393] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-750] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-706] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-682] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-686] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-809] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-722] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-728] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [730-732] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [756-757] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [756-809] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [796-798] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
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

</details>