# Play-Annotation-Generator Annotation Review — Power_100

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_100`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 629
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 0 | START | 0 | 629 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 471 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 263 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 288 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 506 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 451 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 322 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 447 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `13` | `13` | 452 | START | 452 | 460 |
| ✅ EXACT | `Action_DownBlock` | LT | `6` | `6` | 452 | START | 452 | 487 |
| ✅ EXACT | `Action_DownBlock` | RG | `9` | `9` | 452 | START | 452 | 488 |
| ✅ EXACT | `Action_PullBlock` | QB | `8` | `8` | 452 | START | 452 | 488 |

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
- **Visible Frames:** 0–532
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 322 | 323 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 451 | 120 | inferred_complete_timeline |
| `Action_PullBlock` | 452 | 488 | 37 | inferred_complete_timeline |
| `Action_None` | 489 | 532 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–555
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 471 | 472 | inferred_complete_timeline |
| `Action_PreSnap` | 554 | 555 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 629 | 630 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–506
- **Visible Samples:** 507

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 506 | 507 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–502
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 451 | 452 | inferred_complete_timeline |
| `Action_DownBlock` | 452 | 487 | 36 | inferred_complete_timeline |
| `Action_None` | 491 | 502 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–518
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 263 | 264 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 451 | 181 | inferred_complete_timeline |
| `Action_DownBlock` | 452 | 460 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 465 | 488 | 24 | inferred_complete_timeline |
| `Action_None` | 489 | 518 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–528
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 528 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–512
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 447 | 448 | inferred_complete_timeline |
| `Action_PreSnap` | 451 | 451 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 452 | 488 | 37 | inferred_complete_timeline |
| `Action_None` | 489 | 512 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 569 | 544 | inferred_complete_timeline |
| `Action_PreSnap` | 575 | 587 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 596 | 623 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 625 | 629 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–496
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 496 | 497 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–482
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 456 | 354 | inferred_complete_timeline |
| `Action_PreSnap` | 468 | 470 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 473 | 482 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 514 | 515 | inferred_complete_timeline |
| `Action_PreSnap` | 547 | 558 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 561 | 625 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 627 | 629 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 462 | 463 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 479 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 481 | 579 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 581 | 582 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 590 | 629 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–515
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 515 | 516 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 499 | 500 | inferred_complete_timeline |
| `Action_PreSnap` | 501 | 512 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 515 | 629 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–629 | 622 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–510 | 511 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 44–256 | 204 | 8 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 63–511 | 248 | 13 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 115–132 | 5 | 2 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 428–503 | 7 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 481–608 | 128 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 490–509 | 15 | 2 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 513–629 | 117 | 1 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 519–629 | 107 | 3 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 522–530 | 8 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 526–577 | 52 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 531–629 | 99 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 536–612 | 8 | 2 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 544–556 | 13 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 548–629 | 82 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 548–629 | 24 | 3 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 567–606 | 40 | 1 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 575–578 | 4 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 591–593 | 3 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 604–629 | 26 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 615–629 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 201: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 202: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-510] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [514-620] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-506] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-515] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-514] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [547-558] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-625] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-499] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-512] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [452-487] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-502] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-462] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-479] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-579] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [581-582] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-322] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [452-488] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-532] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-447] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-512] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-496] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-510] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-471] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [554-555] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [452-460] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-518] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-528] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-456] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-470] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-482] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-569] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [575-587] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [596-623] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-213] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-256] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-89] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-126] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-280] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-295] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-411] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-455] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-471] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-511] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-432] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [502-503] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-608] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [490-502] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-509] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-527] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-532] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [534-629] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [522-527] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [529-530] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [526-577] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-539] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [609-612] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-556] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-560] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-565] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [567-606] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [575-578] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [591-593] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [604-629] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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