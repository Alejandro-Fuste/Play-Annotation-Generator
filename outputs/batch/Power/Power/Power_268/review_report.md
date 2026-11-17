# Play-Annotation-Generator Annotation Review — Power_268

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_268`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 689
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBlock` | TE | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 16 | START | 16 | 448 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 16 | START | 16 | 516 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 16 | START | 16 | 430 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 16 | START | 16 | 448 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 16 | START | 16 | 448 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 16 | START | 16 | 528 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `6` | 449 | START | 449 | 478 |
| ✅ EXACT | `Action_DownBlock` | C | `8` | `8` | 449 | START | 449 | 504 |
| ✅ EXACT | `Action_PullBlock` | TE | `0` | `0` | 449 | START | 449 | 504 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 16–528
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 528 | 513 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 16–689
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 448 | 433 | inferred_complete_timeline |
| `Action_PullBlock` | 449 | 504 | 56 | inferred_complete_timeline |
| `Action_None` | 505 | 522 | 18 | inferred_complete_timeline |
| `Action_None` | 527 | 536 | 10 | inferred_complete_timeline |
| `Action_None` | 550 | 553 | 4 | inferred_complete_timeline |
| `Action_None` | 555 | 689 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 16–541
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 448 | 433 | inferred_complete_timeline |
| `Action_DownBlock` | 449 | 478 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 481 | 504 | 24 | inferred_complete_timeline |
| `Action_None` | 505 | 541 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 16–523
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 448 | 433 | inferred_complete_timeline |
| `Action_DownBlock` | 449 | 504 | 56 | inferred_complete_timeline |
| `Action_None` | 505 | 523 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 16–549
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 430 | 415 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 485 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 549 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 16–516
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 516 | 501 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 16–582
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 582 | 567 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 16–689
- **Visible Samples:** 674

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 689 | 674 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 16–528
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 186 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 200 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 441 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 451 | 528 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 16–521
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 521 | 506 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 16–689
- **Visible Samples:** 669

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 505 | 490 | inferred_complete_timeline |
| `Action_PreSnap` | 511 | 689 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 16–536
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 536 | 521 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 16–521
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 16 | 20 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 220 | 199 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 521 | 300 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 16–532 | 517 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 16–73 | 56 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 16–689 | 674 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 495–680 | 186 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 504–523 | 18 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 542–689 | 148 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 547–689 | 143 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 592–594 | 3 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 596–665 | 17 | 4 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 604–606 | 3 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 609–611 | 3 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 615–672 | 23 | 5 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 619–689 | 71 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 622–623 | 2 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 641–644 | 4 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 643–677 | 21 | 6 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 644–658 | 7 | 2 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 645–674 | 27 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 646–689 | 15 | 5 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 646–647 | 2 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 646–649 | 4 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 667–689 | 9 | 4 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 669–689 | 21 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 674–689 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 536: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 536: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action 'Action_None' range [505-522] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-553] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-532] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-516] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-430] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-485] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-549] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-22] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-63] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [449-478] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-541] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-523] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-528] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-200] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-441] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-528] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-521] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-582] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-505] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-536] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-220] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-521] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-680] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-506] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-523] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [547-689] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [592-594] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [596-598] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [642-651] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [653-654] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [664-665] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [604-606] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [609-611] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [615-616] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [619-622] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [630-634] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [637-641] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [666-672] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [622-623] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [641-644] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [643-648] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [652-655] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [658-659] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [665-666] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [668-670] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [674-677] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [644-645] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [654-658] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [645-661] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [665-674] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [646-650] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [652-654] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [656-659] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [662-663] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [646-647] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [646-649] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [667-668] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [675-676] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [678-680] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>