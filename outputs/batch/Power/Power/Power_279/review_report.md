# Play-Annotation-Generator Annotation Review — Power_279

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_279`
- **Frame Range:** 0 to 839 (840 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 839
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `28` | `24` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 25 | START | 25 | 677 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 25 | START | 25 | 839 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 25 | START | 25 | 708 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 25 | START | 25 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 25 | START | 25 | 643 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 25 | START | 25 | 652 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 25 | START | 25 | 643 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 25 | START | 25 | 643 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 25 | START | 25 | 708 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 25 | START | 25 | 756 |
| ✅ EXACT | `Action_DownBlock` | C | `19` | `19` | 644 | START | 644 | 728 |
| ✅ EXACT | `Action_DownBlock` | LT | `20` | `20` | 644 | START | 644 | 728 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `28` | `24` | 644 | START | 644 | 647 |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `4` | 644 | START | 644 | 728 |

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
- **Visible Frames:** 25–719
- **Visible Samples:** 692

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 708 | 684 | inferred_complete_timeline |
| `Action_PreSnap` | 712 | 719 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–818
- **Visible Samples:** 788

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 756 | 732 | inferred_complete_timeline |
| `Action_PreSnap` | 762 | 763 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 765 | 818 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 25–708
- **Visible Samples:** 682

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 677 | 653 | inferred_complete_timeline |
| `Action_PreSnap` | 679 | 698 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 700 | 708 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 25–839
- **Visible Samples:** 815

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 839 | 815 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 25–751
- **Visible Samples:** 724

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 708 | 684 | inferred_complete_timeline |
| `Action_PreSnap` | 711 | 712 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 714 | 751 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 25–839
- **Visible Samples:** 814

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 643 | 619 | inferred_complete_timeline |
| `Action_DownBlock` | 644 | 728 | 85 | inferred_complete_timeline |
| `Action_None` | 729 | 794 | 66 | inferred_complete_timeline |
| `Action_None` | 796 | 839 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 25–174
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 167 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 174 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 25–839
- **Visible Samples:** 815

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 643 | 619 | inferred_complete_timeline |
| `Action_DownBlock` | 644 | 728 | 85 | inferred_complete_timeline |
| `Action_None` | 729 | 839 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 25–787
- **Visible Samples:** 752

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 643 | 619 | inferred_complete_timeline |
| `Action_PullBlock` | 644 | 728 | 85 | inferred_complete_timeline |
| `Action_None` | 729 | 768 | 40 | inferred_complete_timeline |
| `Action_None` | 770 | 774 | 5 | inferred_complete_timeline |
| `Action_None` | 785 | 787 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–839
- **Visible Samples:** 788

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 652 | 628 | inferred_complete_timeline |
| `Action_PreSnap` | 673 | 831 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 839 | 839 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 25–839
- **Visible Samples:** 806

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 706 | 682 | inferred_complete_timeline |
| `Action_PreSnap` | 708 | 723 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 732 | 839 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 25–750
- **Visible Samples:** 726

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 750 | 726 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 25–839
- **Visible Samples:** 797

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 650 | 626 | inferred_complete_timeline |
| `Action_PreSnap` | 663 | 690 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 692 | 703 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 709 | 839 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 25–839
- **Visible Samples:** 815

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 839 | 815 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–830
- **Visible Samples:** 771

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 668 | 644 | inferred_complete_timeline |
| `Action_PreSnap` | 672 | 674 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 676 | 682 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 693 | 695 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 697 | 754 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 759 | 762 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 768 | 788 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 800 | 830 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 25–839
- **Visible Samples:** 814

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 714 | 690 | inferred_complete_timeline |
| `Action_PreSnap` | 716 | 839 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 25–782
- **Visible Samples:** 756

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 732 | 708 | inferred_complete_timeline |
| `Action_PreSnap` | 734 | 763 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 765 | 782 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–837
- **Visible Samples:** 813

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 837 | 813 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 25–751
- **Visible Samples:** 727

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 751 | 727 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 25–839
- **Visible Samples:** 815

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 839 | 815 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 25–839
- **Visible Samples:** 807

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 710 | 686 | inferred_complete_timeline |
| `Action_PreSnap` | 715 | 778 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 782 | 784 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 786 | 839 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 25–839 | 815 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 43–71 | 8 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 279–670 | 376 | 7 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 679–839 | 161 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 707–714 | 8 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 717–733 | 11 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 724–839 | 73 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 767–773 | 7 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 778–780 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 784–839 | 55 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 801–839 | 39 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 811–812 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 817–839 | 15 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 824–839 | 16 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 825–839 | 14 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 825–839 | 15 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 832–839 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `28` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 558: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [25-677] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [679-698] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [700-708] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-750] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-652] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [673-831] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-732] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [734-763] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [765-782] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-768] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [770-774] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [785-787] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-708] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [711-712] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [714-751] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-706] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [708-723] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-756] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [762-763] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [765-818] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-714] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-837] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-668] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [672-674] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [676-682] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [693-695] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [697-754] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [759-762] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [768-788] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [800-830] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-710] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [715-778] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [782-784] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [786-839] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-650] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [663-690] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [692-703] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-751] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-708] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [712-719] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-167] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-794] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-839] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-293] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [644-647] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [650-670] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [707-714] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [717-721] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [728-733] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [724-751] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [776-778] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [767-773] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [778-780] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [784-785] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [811-812] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [817-818] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [820-822] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [826-829] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [825-833] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>