# Play-Annotation-Generator Annotation Review — Power_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_39`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 31 | START | 31 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 31 | START | 31 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 31 | START | 31 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 31 | START | 31 | 429 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 31 | START | 31 | 429 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 31 | START | 31 | 429 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 31 | START | 31 | 474 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 31 | START | 31 | 492 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 31 | START | 31 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 31 | START | 31 | 495 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 31 | START | 31 | 477 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `14` | 430 | START | 430 | 440 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `15` | 430 | START | 430 | 440 |
| ✅ EXACT | `Action_PullBlock` | LG | `19` | `19` | 430 | START | 430 | 480 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 31–523
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 477 | 447 | inferred_complete_timeline |
| `Action_PreSnap` | 479 | 482 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 485 | 486 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 495 | 503 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 509 | 523 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 495 | 465 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 599 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 474 | 444 | inferred_complete_timeline |
| `Action_PreSnap` | 476 | 500 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 503 | 519 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 521 | 599 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 429 | 399 | inferred_complete_timeline |
| `Action_PullBlock` | 430 | 480 | 51 | inferred_complete_timeline |
| `Action_None` | 481 | 599 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 31–476
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 429 | 399 | inferred_complete_timeline |
| `Action_DownBlock` | 430 | 440 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 442 | 445 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 465 | 476 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 429 | 399 | inferred_complete_timeline |
| `Action_DownBlock` | 430 | 440 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 442 | 455 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 457 | 480 | 24 | inferred_complete_timeline |
| `Action_None` | 481 | 599 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 31–599
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 492 | 462 | inferred_complete_timeline |
| `Action_PreSnap` | 502 | 599 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 31–473
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 452 | 422 | inferred_complete_timeline |
| `Action_PreSnap` | 458 | 473 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 527 | 497 | inferred_complete_timeline |
| `Action_PreSnap` | 530 | 599 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 442 | 412 | inferred_complete_timeline |
| `Action_PreSnap` | 445 | 599 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 31–461
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 461 | 431 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 31–593
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 593 | 563 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 599 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 500 | 470 | inferred_complete_timeline |
| `Action_PreSnap` | 502 | 599 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 516 | 486 | inferred_complete_timeline |
| `Action_PreSnap` | 520 | 593 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 596 | 599 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 31–599
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 473 | 443 | inferred_complete_timeline |
| `Action_PreSnap` | 476 | 599 | 124 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 39–45 | 7 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 451–599 | 141 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 460–525 | 38 | 8 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 471–495 | 25 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 522–599 | 78 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 531–599 | 69 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 539–540 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 550–599 | 50 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 551–599 | 48 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 564–599 | 16 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 46 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [31-500] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-527] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-492] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-452] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-473] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-495] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-477] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-482] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-486] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-503] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-523] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-473] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [430-440] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [442-455] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [430-440] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [442-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [465-476] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-593] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-461] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-516] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-593] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-442] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-474] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-500] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [503-519] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-468] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-488] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-493] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-502] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-465] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-481] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-486] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-493] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-504] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [506-513] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [516-517] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-525] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-495] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [522-599] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-540] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [549-550] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [551-578] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [580-599] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [564-569] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [581-586] for track '32' has 2 frames without a visible bounding box.
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