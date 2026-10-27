# Play-Annotation-Generator Annotation Review — Counter_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_50`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 659
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 117
- **Validation Warnings:** 143
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 37 | START | 37 | 52 |
| ✅ EXACT | `Action_DownBlock` | LG | `1` | `0` | 43 | START | 43 | 106 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `13` | `12` | 43 | START | 53 | 106 |
| ✅ EXACT | `Action_PullBlock` | RG | `11` | `10` | 43 | START | 43 | 106 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `3` | `2` | 43 | START | 43 | 106 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 52 | END | 37 | 52 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 58 | START | 58 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 73 | START | 73 | 366 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 106 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–574
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 52 | 16 | inferred_complete_timeline |
| `Action_None` | 53 | 57 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 73 | 294 | 222 | inferred_complete_timeline |
| `Action_None` | 297 | 304 | 8 | inferred_complete_timeline |
| `Action_None` | 306 | 497 | 192 | inferred_complete_timeline |
| `Action_None` | 505 | 574 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–567
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 366 | 294 | inferred_complete_timeline |
| `Action_BallCarry` | 405 | 521 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 525 | 567 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 298 | 262 | inferred_complete_timeline |
| `Action_None` | 300 | 543 | 244 | inferred_complete_timeline |
| `Action_None` | 545 | 550 | 6 | inferred_complete_timeline |
| `Action_None` | 553 | 659 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–623
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 623 | 587 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 645

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 600 | 564 | inferred_complete_timeline |
| `Action_None` | 612 | 620 | 9 | inferred_complete_timeline |
| `Action_None` | 625 | 659 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 636

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 106 | 64 | inferred_complete_timeline |
| `Action_None` | 107 | 536 | 430 | inferred_complete_timeline |
| `Action_None` | 546 | 584 | 39 | inferred_complete_timeline |
| `Action_None` | 597 | 645 | 49 | inferred_complete_timeline |
| `Action_None` | 649 | 659 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 52 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 53 | 106 | 54 | inferred_complete_timeline |
| `Action_None` | 107 | 118 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PullBlock` | 43 | 106 | 64 | inferred_complete_timeline |
| `Action_None` | 107 | 507 | 401 | inferred_complete_timeline |
| `Action_None` | 520 | 549 | 30 | inferred_complete_timeline |
| `Action_None` | 574 | 581 | 8 | inferred_complete_timeline |
| `Action_None` | 588 | 659 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–594
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 43 | 106 | 64 | inferred_complete_timeline |
| `Action_None` | 107 | 527 | 421 | inferred_complete_timeline |
| `Action_None` | 534 | 589 | 56 | inferred_complete_timeline |
| `Action_None` | 591 | 594 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–563
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 170 | 134 | inferred_complete_timeline |
| `Action_None` | 199 | 511 | 313 | inferred_complete_timeline |
| `Action_None` | 515 | 525 | 11 | inferred_complete_timeline |
| `Action_None` | 527 | 534 | 8 | inferred_complete_timeline |
| `Action_None` | 540 | 563 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 656

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 524 | 488 | inferred_complete_timeline |
| `Action_None` | 529 | 659 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–562
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 241 | 205 | inferred_complete_timeline |
| `Action_None` | 243 | 562 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_None` | 37 | 39 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–659 | 627 | 7 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–27 | 28 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 5–554 | 544 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 117–517 | 319 | 8 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 156–166 | 10 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 164–210 | 45 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 498–625 | 58 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 503–508 | 6 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 510–521 | 12 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 521–595 | 73 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 524–534 | 11 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 535–584 | 50 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 544–564 | 21 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 547–659 | 111 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 554–556 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 557–568 | 12 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 557–659 | 99 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 565–578 | 14 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 568–600 | 33 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 572–580 | 7 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 576–589 | 14 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 594–610 | 17 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 623–659 | 30 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 629–659 | 29 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 634–659 | 26 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 641–647 | 7 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 650–659 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `36` | `47` | 601 | 607 | 4 | 57.1% | 604–606 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `13` (C): Annotated start 43 != Inferred start 53
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [37–52], lower_priority='Action_DownBlock' annotated_start=43, effective_Action_DownBlock_start=53.
- ⚠️ Action 'Action_None' range [107-536] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-584] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-645] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-623] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-527] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-589] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-366] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [405-521] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [525-567] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-600] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-620] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-543] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-550] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-511] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-525] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-534] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-563] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-524] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-659] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-562] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-294] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-497] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-574] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-507] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-549] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-581] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-524] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-578] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-586] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-591] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-618] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-520] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-551] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-175] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-213] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-308] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-397] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-504] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-517] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-531] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-541] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-546] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-625] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-508] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-521] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-559] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-595] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-534] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-584] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-564] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-568] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-615] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-578] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-600] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-580] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-589] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-610] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-652] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-656] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-659] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-647] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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