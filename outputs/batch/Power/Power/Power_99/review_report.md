# Play-Annotation-Generator Annotation Review — Power_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_99`
- **Frame Range:** 0 to 869 (870 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 869
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 37
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 8 | START | 8 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 8 | START | 8 | 841 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 8 | START | 8 | 612 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 8 | START | 19 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 8 | START | 72 | 869 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 8 | START | 81 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 8 | START | 8 | 612 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 8 | START | 8 | 869 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 8 | START | 8 | 472 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `7` | `7` | 473 | START | 473 | 709 |
| ✅ EXACT | `Action_DownBlock` | LG | `15` | `15` | 613 | START | 613 | 720 |
| ✅ EXACT | `Action_DownBlock` | C | `4` | `4` | 613 | START | 613 | 720 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–841
- **Visible Samples:** 834

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 841 | 834 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–868
- **Visible Samples:** 824

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 804 | 771 | inferred_complete_timeline |
| `Action_PreSnap` | 809 | 815 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 833 | 836 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 841 | 865 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 867 | 868 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 72–869
- **Visible Samples:** 798

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 72 | 869 | 798 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 19–869
- **Visible Samples:** 824

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 31 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 771 | 709 | inferred_complete_timeline |
| `Action_PreSnap` | 773 | 855 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 857 | 869 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 81–506
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 124 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 506 | 380 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 8–869
- **Visible Samples:** 861

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 612 | 605 | inferred_complete_timeline |
| `Action_DownBlock` | 613 | 720 | 108 | inferred_complete_timeline |
| `Action_None` | 721 | 742 | 22 | inferred_complete_timeline |
| `Action_None` | 744 | 869 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–866
- **Visible Samples:** 859

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 612 | 605 | inferred_complete_timeline |
| `Action_DownBlock` | 613 | 720 | 108 | inferred_complete_timeline |
| `Action_None` | 721 | 866 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–723
- **Visible Samples:** 713

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 472 | 465 | inferred_complete_timeline |
| `Action_PullBlock` | 473 | 709 | 237 | inferred_complete_timeline |
| `Action_PullBlock` | 711 | 712 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 714 | 720 | 7 | inferred_complete_timeline |
| `Action_None` | 722 | 723 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 8–869
- **Visible Samples:** 862

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 869 | 862 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–869
- **Visible Samples:** 862

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 869 | 862 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 8–869
- **Visible Samples:** 856

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 753 | 746 | inferred_complete_timeline |
| `Action_PreSnap` | 760 | 869 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 8–750
- **Visible Samples:** 717

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 11 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 734 | 710 | inferred_complete_timeline |
| `Action_PreSnap` | 748 | 750 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 8–869
- **Visible Samples:** 848

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 45 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 869 | 810 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–760
- **Visible Samples:** 753

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 760 | 753 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–869
- **Visible Samples:** 862

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 869 | 862 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–869
- **Visible Samples:** 858

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 813 | 806 | inferred_complete_timeline |
| `Action_PreSnap` | 815 | 859 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 863 | 869 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 8–817
- **Visible Samples:** 807

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 745 | 738 | inferred_complete_timeline |
| `Action_PreSnap` | 747 | 761 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 764 | 817 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–869
- **Visible Samples:** 862

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 869 | 862 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–867
- **Visible Samples:** 855

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 815 | 808 | inferred_complete_timeline |
| `Action_PreSnap` | 821 | 867 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 8–826 | 803 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 8–869 | 858 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 8–869 | 858 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 517–869 | 346 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 724–869 | 146 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 760–843 | 84 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 772–852 | 81 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 199: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 869 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (C) duration 108 frames exceeds threshold 90 frames [start=613, end=720].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '7' (RG) duration 248 frames exceeds threshold 90 frames [start=473, end=720].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LG) duration 108 frames exceeds threshold 90 frames [start=613, end=720].
- ⚠️ Action 'Action_PreSnap' range [8-745] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [747-761] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [764-817] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-758] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [761-766] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [772-773] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [783-826] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-813] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [815-859] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [863-869] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-815] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [821-867] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-866] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-869] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-760] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [473-709] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [711-712] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [714-720] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [722-723] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-864] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-804] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [809-815] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [833-836] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [841-865] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [867-868] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-841] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-755] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [759-806] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-742] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [744-869] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-11] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-734] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [748-750] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-753] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-31] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-41] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-771] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [773-855] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-869] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-124] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-506] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-519] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-754] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [760-843] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [772-852] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>