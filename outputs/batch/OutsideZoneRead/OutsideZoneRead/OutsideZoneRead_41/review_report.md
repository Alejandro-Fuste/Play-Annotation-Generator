# Play-Annotation-Generator Annotation Review — OutsideZoneRead_41

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_41`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 689
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `2` | `2` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 28 | START | 28 | 480 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 28 | START | 28 | 480 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 28 | START | 28 | 480 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 28 | START | 28 | 484 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 28 | START | 28 | 689 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 28 | START | 28 | 480 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 28 | START | 28 | 480 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 28 | START | 28 | 249 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 481 | START | 481 | 523 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 481 | START | 481 | 523 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 481 | START | 481 | 523 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 481 | START | 481 | 523 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 481 | START | 481 | 523 |
| ✅ EXACT | `Action_PressEdge` | RB | `2` | `2` | 485 | START | 485 | 506 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 488 | START | 488 | 500 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 501 | START | 501 | 517 |

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
- **Visible Frames:** 28–566
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 249 | 222 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 487 | 233 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 488 | 500 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 501 | 517 | 17 | inferred_complete_timeline |
| `Action_None` | 518 | 566 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 28–506
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 484 | 457 | inferred_complete_timeline |
| `Action_PressEdge` | 485 | 506 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 28–689
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 689 | 662 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 28–689
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 480 | 453 | inferred_complete_timeline |
| `Action_ZoneBlock` | 481 | 523 | 43 | inferred_complete_timeline |
| `Action_None` | 524 | 570 | 47 | inferred_complete_timeline |
| `Action_None` | 575 | 605 | 31 | inferred_complete_timeline |
| `Action_None` | 608 | 689 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 28–689
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 480 | 453 | inferred_complete_timeline |
| `Action_ZoneBlock` | 481 | 523 | 43 | inferred_complete_timeline |
| `Action_None` | 524 | 565 | 42 | inferred_complete_timeline |
| `Action_None` | 569 | 689 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 28–660
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 480 | 453 | inferred_complete_timeline |
| `Action_ZoneBlock` | 481 | 523 | 43 | inferred_complete_timeline |
| `Action_None` | 524 | 559 | 36 | inferred_complete_timeline |
| `Action_None` | 564 | 660 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 28–689
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 480 | 453 | inferred_complete_timeline |
| `Action_ZoneBlock` | 481 | 523 | 43 | inferred_complete_timeline |
| `Action_None` | 524 | 689 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 28–689
- **Visible Samples:** 650

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 480 | 453 | inferred_complete_timeline |
| `Action_ZoneBlock` | 481 | 523 | 43 | inferred_complete_timeline |
| `Action_None` | 524 | 547 | 24 | inferred_complete_timeline |
| `Action_None` | 560 | 689 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 28–511
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 499 | 472 | inferred_complete_timeline |
| `Action_PreSnap` | 510 | 511 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 28–689
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 534 | 507 | inferred_complete_timeline |
| `Action_PreSnap` | 542 | 543 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 545 | 554 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 559 | 560 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 590 | 689 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 28–650
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 482 | 455 | inferred_complete_timeline |
| `Action_PreSnap` | 484 | 485 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 520 | 650 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 28–493
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 493 | 466 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 28–689
- **Visible Samples:** 662

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 689 | 662 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 28–521
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 521 | 494 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 505–590 | 81 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 510–689 | 179 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 528–689 | 162 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 530–689 | 160 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 543–689 | 146 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 544–689 | 138 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 544–689 | 138 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 548–689 | 142 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 568–689 | 122 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 575–689 | 107 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 603–604 | 2 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 603–642 | 40 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 613–615 | 3 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 622–639 | 8 | 3 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 624–639 | 16 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 624–687 | 39 | 5 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 650–689 | 37 | 3 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 657–689 | 30 | 3 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 671–689 | 19 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 674–689 | 16 | 1 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 675–681 | 7 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 679–689 | 11 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 680–683 | 4 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 680–688 | 9 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 682–686 | 5 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 685–686 | 2 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 686–688 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action 'Action_None' range [524-547] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-689] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [485-506] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-534] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [542-543] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [545-554] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [559-560] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-565] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-689] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-570] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-605] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-521] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-499] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-511] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-566] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-559] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-660] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-493] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-482] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-485] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-650] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-545] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [551-590] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-654] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-689] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [543-557] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-609] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [618-689] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-548] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-590] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-689] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [575-576] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [603-604] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [603-642] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [613-615] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [622-624] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [627-629] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [638-639] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [624-639] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [624-631] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [633-637] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [640-641] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [652-661] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [674-687] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [650-653] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [655-685] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [657-675] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [677-681] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [684-689] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [671-689] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [674-689] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [675-681] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [679-689] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [680-683] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [680-688] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [682-686] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [685-686] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [686-688] for track '40' has 1 frames without a visible bounding box.
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

</details>