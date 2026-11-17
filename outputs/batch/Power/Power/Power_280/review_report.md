# Play-Annotation-Generator Annotation Review — Power_280

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_280`
- **Frame Range:** 0 to 809 (810 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 809
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 26 | START | 26 | 260 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 26 | START | 26 | 282 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 26 | START | 26 | 637 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 26 | START | 26 | 637 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 26 | START | 26 | 748 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 26 | START | 26 | 669 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 26 | START | 26 | 689 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `11` | 638 | START | 638 | 646 |
| ✅ EXACT | `Action_DownBlock` | LG | `5` | `5` | 638 | START | 638 | 653 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `6` | 638 | START | 638 | 670 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `3` | 638 | START | 638 | 648 |

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
- **Visible Frames:** 26–799
- **Visible Samples:** 773

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 748 | 723 | inferred_complete_timeline |
| `Action_PreSnap` | 750 | 799 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 26–771
- **Visible Samples:** 738

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 669 | 644 | inferred_complete_timeline |
| `Action_PreSnap` | 675 | 710 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 713 | 714 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 716 | 771 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 26–795
- **Visible Samples:** 764

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 637 | 612 | inferred_complete_timeline |
| `Action_DownBlock` | 638 | 670 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 673 | 712 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 715 | 738 | 24 | inferred_complete_timeline |
| `Action_None` | 739 | 745 | 7 | inferred_complete_timeline |
| `Action_None` | 748 | 795 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 26–653
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 637 | 612 | inferred_complete_timeline |
| `Action_DownBlock` | 638 | 653 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 26–701
- **Visible Samples:** 665

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 260 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 294 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 637 | 338 | inferred_complete_timeline |
| `Action_DownBlock` | 638 | 646 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 648 | 651 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 655 | 701 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–809
- **Visible Samples:** 776

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 282 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 637 | 352 | inferred_complete_timeline |
| `Action_PullBlock` | 638 | 648 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 651 | 712 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 714 | 738 | 25 | inferred_complete_timeline |
| `Action_None` | 739 | 741 | 3 | inferred_complete_timeline |
| `Action_None` | 744 | 809 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 26–689
- **Visible Samples:** 664

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 689 | 664 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–675
- **Visible Samples:** 650

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 675 | 650 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 26–686
- **Visible Samples:** 661

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 686 | 661 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–696
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 647 | 622 | inferred_complete_timeline |
| `Action_PreSnap` | 650 | 651 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 660 | 665 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 669 | 672 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 675 | 696 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–648
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 648 | 623 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 26–809
- **Visible Samples:** 762

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 230 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 261 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 809 | 544 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–809
- **Visible Samples:** 777

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 690 | 665 | inferred_complete_timeline |
| `Action_PreSnap` | 692 | 703 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 707 | 708 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 710 | 724 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 727 | 809 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 26–55 | 30 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 26–809 | 758 | 7 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 184–250 | 59 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 389–427 | 27 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 639–704 | 57 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 639–809 | 159 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 647–697 | 48 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 675–676 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 679–750 | 72 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 687–737 | 38 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 731–763 | 31 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 740–741 | 2 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 770–809 | 40 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 770–771 | 2 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 772–809 | 38 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 788–809 | 22 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 797–805 | 9 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 798–809 | 12 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 800–809 | 10 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 805–809 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 809 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '3' (RG) duration 101 frames exceeds threshold 90 frames [start=638, end=738].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '6' (LT) duration 101 frames exceeds threshold 90 frames [start=638, end=738].
- ⚠️ Action 'Action_PreSnap' range [26-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-230] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-809] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-686] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [638-648] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [651-712] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-741] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-675] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-637] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [638-653] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [638-670] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [673-712] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [739-745] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-795] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-748] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [750-799] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-669] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [675-710] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [713-714] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [716-771] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-689] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-690] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [692-703] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [707-708] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [710-724] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [727-809] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [638-646] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [648-651] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [655-701] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-710] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [724-728] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [733-735] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [738-739] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [742-749] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [754-797] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-648] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-647] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [650-651] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [660-665] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [669-672] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [675-696] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-394] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-427] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [639-640] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [650-704] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [639-750] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [763-809] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [647-663] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [665-690] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [693-697] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [675-676] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [679-750] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [687-697] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [701-703] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [708-718] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [725-737] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [731-759] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [762-763] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [740-741] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [770-771] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [797-805] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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