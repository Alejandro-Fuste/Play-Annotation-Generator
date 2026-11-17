# Play-Annotation-Generator Annotation Review — Power_322

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_322`
- **Frame Range:** 0 to 839 (840 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 839
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 177
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 20 | START | 20 | 505 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 20 | START | 20 | 308 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 20 | START | 20 | 348 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 20 | START | 20 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 20 | START | 215 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 20 | START | 20 | 550 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 20 | START | 20 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `1` | `1` | 506 | START | 506 | 535 |
| ✅ EXACT | `Action_DownBlock` | C | `10` | `10` | 506 | START | 506 | 567 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `12` | 506 | START | 506 | 510 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 215–216
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 215 | 216 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 20–148
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 148 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 20–737
- **Visible Samples:** 714

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 505 | 486 | inferred_complete_timeline |
| `Action_DownBlock` | 506 | 535 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 538 | 567 | 30 | inferred_complete_timeline |
| `Action_None` | 568 | 596 | 29 | inferred_complete_timeline |
| `Action_None` | 599 | 737 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–558
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 42 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 102 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 129 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 157 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 181 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 390 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 516 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 535 | 537 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 558 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 20–839
- **Visible Samples:** 784

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 308 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 357 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 505 | 147 | inferred_complete_timeline |
| `Action_DownBlock` | 506 | 567 | 62 | inferred_complete_timeline |
| `Action_None` | 568 | 650 | 83 | inferred_complete_timeline |
| `Action_None` | 675 | 798 | 124 | inferred_complete_timeline |
| `Action_None` | 801 | 839 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 20–839
- **Visible Samples:** 747

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 348 | 329 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 505 | 156 | inferred_complete_timeline |
| `Action_PullBlock` | 506 | 510 | 5 | inferred_complete_timeline |
| `Action_None` | 583 | 839 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 20–571
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 550 | 531 | inferred_complete_timeline |
| `Action_PreSnap` | 559 | 571 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–839
- **Visible Samples:** 787

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 548 | 529 | inferred_complete_timeline |
| `Action_PreSnap` | 561 | 572 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 576 | 587 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 596 | 762 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 773 | 839 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–589
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 582 | 563 | inferred_complete_timeline |
| `Action_PreSnap` | 585 | 589 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 142–550
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 142 | 239 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 281 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 285 | 550 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–532
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 109 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 532 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 20–839
- **Visible Samples:** 820

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 839 | 820 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–839
- **Visible Samples:** 817

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 585 | 566 | inferred_complete_timeline |
| `Action_PreSnap` | 589 | 839 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–839
- **Visible Samples:** 816

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 715 | 696 | inferred_complete_timeline |
| `Action_PreSnap` | 720 | 839 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 20–589 | 566 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 20–568 | 524 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 79–192 | 30 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 224–230 | 7 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 304–360 | 25 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 372–511 | 95 | 10 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 515–839 | 289 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 521–839 | 247 | 8 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 526–546 | 21 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 539–802 | 257 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 544–839 | 294 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 544–553 | 10 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 555–572 | 18 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 590–615 | 26 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 592–594 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 596–709 | 101 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 612–799 | 169 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 616–651 | 32 | 3 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 645–839 | 189 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 685–839 | 134 | 5 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 688–689 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 745–746 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 747–780 | 31 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 760–814 | 55 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 786–839 | 52 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 804–839 | 36 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 811–816 | 6 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 812–839 | 28 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 822–839 | 14 | 3 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 834–839 | 6 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 837–839 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 114 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-582] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [585-589] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [506-535] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-596] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-737] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-585] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [589-839] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-715] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [720-839] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-525] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-589] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-550] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [559-571] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-548] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-572] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [576-587] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [596-762] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-109] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-532] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-308] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-357] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [506-567] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-650] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-798] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [801-839] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-199] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-227] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-538] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [557-568] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-348] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [506-510] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-839] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-42] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-102] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-157] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-181] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-390] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-516] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-537] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-558] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-106] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-239] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-281] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-550] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-322] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-360] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-382] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-404] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-410] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-426] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-448] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-451] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-455] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-459] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-506] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-511] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-552] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-566] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [585-706] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [714-797] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-548] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [588-599] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [609-679] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [688-689] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [694-712] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [715-764] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [767-771] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [780-839] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [526-546] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-553] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-802] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-565] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [567-580] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-553] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-572] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [590-615] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [592-594] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [596-601] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [603-626] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [639-709] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [612-734] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [737-751] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [764-791] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [797-799] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [616-624] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [626-631] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [635-651] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [645-706] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [712-715] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [717-839] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [685-688] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [690-720] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [735-755] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [757-760] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [688-689] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [745-746] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [747-755] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [759-780] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [760-814] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [786-799] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [802-839] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [811-816] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [822-825] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [827-830] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>