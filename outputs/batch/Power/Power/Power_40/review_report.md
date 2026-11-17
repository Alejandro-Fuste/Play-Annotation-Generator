# Play-Annotation-Generator Annotation Review — Power_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_40`
- **Frame Range:** 0 to 839 (840 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 839
- **Player Tracks:** 34
- **Ball Tracks:** 2
- **Action Segments:** 94
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 329 | START | 11 | 643 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 329 | START | 11 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 329 | START | 11 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 329 | START | 11 | 641 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 329 | START | 36 | 633 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 329 | START | 11 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 329 | START | 11 | 626 |
| ✅ EXACT | `Action_DownBlock` | C | `11` | `11` | 627 | START | 627 | 652 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `13` | `13` | 627 | START | 627 | 646 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `8` | `8` | 627 | START | 627 | 637 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 11–686
- **Visible Samples:** 633

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 641 | 631 | inferred_complete_timeline |
| `Action_PreSnap` | 685 | 686 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 36–839
- **Visible Samples:** 788

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 633 | 598 | inferred_complete_timeline |
| `Action_PreSnap` | 641 | 671 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 681 | 839 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 11–729
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 178 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 637 | 458 | inferred_complete_timeline |
| `Action_PreSnap` | 643 | 654 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 667 | 676 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 681 | 699 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 707 | 729 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–782
- **Visible Samples:** 767

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 626 | 616 | inferred_complete_timeline |
| `Action_PullBlock` | 627 | 637 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 640 | 675 | 36 | inferred_complete_timeline |
| `Action_None` | 676 | 683 | 8 | inferred_complete_timeline |
| `Action_None` | 687 | 782 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–724
- **Visible Samples:** 657

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 72 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 626 | 533 | inferred_complete_timeline |
| `Action_DownBlock` | 627 | 652 | 26 | inferred_complete_timeline |
| `Action_None` | 686 | 687 | 2 | inferred_complete_timeline |
| `Action_None` | 693 | 724 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 11–665
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 141 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 155 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 171 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 180 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 193 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 273 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 297 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 322 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 399 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 407 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 420 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 430 | 432 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 440 | 495 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 626 | 130 | inferred_complete_timeline |
| `Action_DownBlock` | 627 | 646 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 661 | 665 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 11–822
- **Visible Samples:** 803

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 643 | 633 | inferred_complete_timeline |
| `Action_PreSnap` | 648 | 651 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 655 | 656 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 658 | 786 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 788 | 822 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–716
- **Visible Samples:** 706

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 716 | 706 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–737
- **Visible Samples:** 723

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 660 | 650 | inferred_complete_timeline |
| `Action_PreSnap` | 665 | 737 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 70–742
- **Visible Samples:** 667

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 70 | 87 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 742 | 649 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–721
- **Visible Samples:** 698

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 82 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 625 | 537 | inferred_complete_timeline |
| `Action_PreSnap` | 633 | 721 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–689
- **Visible Samples:** 679

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 689 | 679 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–812
- **Visible Samples:** 790

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 780 | 770 | inferred_complete_timeline |
| `Action_PreSnap` | 782 | 788 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 793 | 799 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 807 | 812 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 93–839
- **Visible Samples:** 747

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 93 | 839 | 747 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–839
- **Visible Samples:** 827

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 725 | 715 | inferred_complete_timeline |
| `Action_PreSnap` | 728 | 839 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 11–55 | 45 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 11–21 | 11 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 11–253 | 191 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 356–652 | 166 | 8 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 648–747 | 100 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 652–803 | 148 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 660–678 | 19 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 689–839 | 151 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 690–779 | 90 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 697–839 | 136 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 748–839 | 92 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 757–839 | 82 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 760–839 | 80 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 762–763 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 820–821 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 824–839 | 16 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 825–839 | 11 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 830–831 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 839–839 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 329 | 437 | 107 | 98.2% | 429, 435 |
| `20` | `25` | 503 | 619 | 92 | 78.6% | 514–530, 532, 535–536, 542–546 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 83 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [11-660] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [665-737] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-643] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [648-651] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [655-656] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [658-786] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [788-822] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-689] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-637] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [643-654] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [667-676] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [681-699] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [707-729] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-780] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [782-788] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [793-799] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [807-812] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-725] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [728-839] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-716] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [627-637] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [640-675] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-683] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-782] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [627-652] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-724] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-625] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [633-721] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-155] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-193] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-273] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-322] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-399] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-407] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-420] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-432] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-495] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [627-646] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [661-665] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-641] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [685-686] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-633] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [641-671] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-742] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-466] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-485] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-516] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-543] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [608-609] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [627-642] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [647-652] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [648-747] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [652-655] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [657-665] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [669-803] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [660-678] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [690-779] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [697-813] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [816-817] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [757-810] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [762-763] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [820-821] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [824-839] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [825-831] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [836-839] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [830-831] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>