# Play-Annotation-Generator Annotation Review — Power_301

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_301`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 115
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `23` | `22` |
| ✅ EXACT | `Action_PullBlock` | DE2 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 13 | START | 13 | 569 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 13 | START | 13 | 504 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 13 | START | 13 | 509 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 13 | START | 13 | 476 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 13 | START | 13 | 436 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 13 | START | 13 | 345 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 13 | START | 176 | 345 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 13 | START | 13 | 569 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 13 | START | 13 | 569 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `18` | 346 | START | 346 | 406 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `21` | `21` | 346 | START | 346 | 400 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `23` | `22` | 346 | START | 346 | 402 |
| ✅ EXACT | `Action_PullBlock` | DE2 | `5` | `5` | 346 | START | 346 | 439 |

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
- **Visible Frames:** 13–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 569 | 557 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–569
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 509 | 497 | inferred_complete_timeline |
| `Action_PreSnap` | 529 | 541 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 559 | 569 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 569 | 557 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 569 | 557 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–569
- **Visible Samples:** 550

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 476 | 464 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 487 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 489 | 507 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 509 | 569 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 436 | 424 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 439 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–569
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 504 | 492 | inferred_complete_timeline |
| `Action_PreSnap` | 511 | 569 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 13–569
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 345 | 333 | inferred_complete_timeline |
| `Action_DownBlock` | 346 | 406 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 413 | 414 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 417 | 439 | 23 | inferred_complete_timeline |
| `Action_None` | 440 | 455 | 16 | inferred_complete_timeline |
| `Action_None` | 472 | 569 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 176–569
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 176 | 345 | 170 | inferred_complete_timeline |
| `Action_DownBlock` | 346 | 402 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 405 | 439 | 35 | inferred_complete_timeline |
| `Action_None` | 440 | 569 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 526 | 514 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 569 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 191 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 345 | 152 | inferred_complete_timeline |
| `Action_PullBlock` | 346 | 439 | 94 | inferred_complete_timeline |
| `Action_None` | 440 | 569 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–436
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 425 | 413 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 432 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 436 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–531
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 420 | 408 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 516 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 520 | 531 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 436 | 424 | inferred_complete_timeline |
| `Action_PreSnap` | 448 | 450 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 454 | 457 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 463 | 465 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 471 | 472 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 544 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 546 | 569 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 448 | 436 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 569 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 569 | 557 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 490 | 478 | inferred_complete_timeline |
| `Action_PreSnap` | 492 | 569 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 569 | 557 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–558
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 531 | 519 | inferred_complete_timeline |
| `Action_PreSnap` | 540 | 558 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 13–472 | 460 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 13–521 | 501 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 13–66 | 15 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 15–455 | 390 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 178–211 | 17 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 242–249 | 6 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 408–420 | 5 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 439–500 | 40 | 5 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 452–569 | 118 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 453–454 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 468–478 | 10 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 481–569 | 88 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 500–532 | 27 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 507–562 | 51 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 527–564 | 18 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 529–558 | 30 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 543–569 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 602: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (DE2) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '18' (C) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (Unknown) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '22' (RG) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
- ⚠️ Action 'Action_PreSnap' range [13-504] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-490] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-569] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-526] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-569] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-531] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [540-558] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-509] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [529-541] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-476] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-487] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-507] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-569] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-436] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-439] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-420] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-516] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-531] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-472] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-32] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-521] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-425] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-432] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-436] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-448] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [346-406] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [413-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [417-439] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-455] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-66] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-436] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-450] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-457] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-465] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-472] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-544] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-345] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [346-400] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-455] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [346-402] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-245] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-409] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-420] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-449] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-455] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-463] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-481] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-500] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-569] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-454] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-470] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-478] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-482] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-569] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-504] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-527] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-532] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-533] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [537-543] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-562] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-532] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [542-543] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [549-554] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-564] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [529-558] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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