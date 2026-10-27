# Play-Annotation-Generator Annotation Review — Counter_239

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_239`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `28` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE1 | defense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `28` | `26` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 8 | START | 8 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 8 | START | 8 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 8 | START | 8 | 439 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 8 | START | 8 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 8 | START | 8 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 8 | START | 8 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 8 | START | 8 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `22` | `Group` | 8 | START | 8 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `26` | `Group` | 8 | START | 180 | 420 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `28` | `Group` | 8 | START | 282 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 8 | START | 8 | 267 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 421 | START | 421 | 434 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE1 | `16` | `15` | 423 | START | 423 | 467 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 423 | START | 423 | 445 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `19` | `18` | 423 | START | 435 | 478 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `28` | `26` | 423 | START | 423 | 500 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 434 | END | 421 | 434 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `10` | 440 | START | 440 | 483 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 449 | START | 449 | 569 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 517 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 8–569
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 267 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 420 | 147 | inferred_complete_timeline |
| `Action_SnapReceive` | 421 | 434 | 14 | inferred_complete_timeline |
| `Action_None` | 435 | 448 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 449 | 569 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 8–563
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 439 | 432 | inferred_complete_timeline |
| `Action_BallCarry` | 440 | 483 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 485 | 511 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 515 | 516 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 518 | 522 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 528 | 559 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 562 | 563 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–559
- **Visible Samples:** 550

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 549 | 129 | inferred_complete_timeline |
| `Action_None` | 552 | 559 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 569 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 8–569
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 475 | 55 | inferred_complete_timeline |
| `Action_None` | 506 | 569 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `28`</summary>

- **xml_track_id:** `26`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 282–569
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 422 | 135 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 423 | 500 | 78 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 502 | 505 | 4 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 508 | 517 | 10 | inferred_complete_timeline |
| `Action_None` | 518 | 569 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `26`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 180–569
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 180 | 420 | 241 | inferred_complete_timeline |
| `Action_None` | 421 | 458 | 38 | inferred_complete_timeline |
| `Action_None` | 478 | 497 | 20 | inferred_complete_timeline |
| `Action_None` | 510 | 569 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–569
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 504 | 84 | inferred_complete_timeline |
| `Action_None` | 514 | 569 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_BallSnap` | 421 | 434 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 435 | 478 | 44 | inferred_complete_timeline |
| `Action_PullBlock` | 482 | 514 | 33 | inferred_complete_timeline |
| `Action_PullBlock` | 516 | 517 | 2 | inferred_complete_timeline |
| `Action_None` | 518 | 569 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–569
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 135 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 422 | 283 | inferred_complete_timeline |
| `Action_DownBlock` | 423 | 445 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 450 | 454 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 457 | 464 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 466 | 507 | 42 | inferred_complete_timeline |
| `Action_None` | 528 | 569 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–450
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 135 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 420 | 280 | inferred_complete_timeline |
| `Action_None` | 421 | 450 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 545

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 422 | 415 | inferred_complete_timeline |
| `Action_DownBlock` | 423 | 467 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 485 | 517 | 33 | inferred_complete_timeline |
| `Action_None` | 518 | 569 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 8–493
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 467 | 47 | inferred_complete_timeline |
| `Action_None` | 491 | 493 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 451 | 31 | inferred_complete_timeline |
| `Action_None` | 460 | 468 | 9 | inferred_complete_timeline |
| `Action_None` | 517 | 518 | 2 | inferred_complete_timeline |
| `Action_None` | 521 | 569 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 440 | 20 | inferred_complete_timeline |
| `Action_None` | 449 | 569 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–566
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 483 | 63 | inferred_complete_timeline |
| `Action_None` | 485 | 486 | 2 | inferred_complete_timeline |
| `Action_None` | 488 | 527 | 40 | inferred_complete_timeline |
| `Action_None` | 529 | 537 | 9 | inferred_complete_timeline |
| `Action_None` | 547 | 566 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 569 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 569 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 510 | 90 | inferred_complete_timeline |
| `Action_None` | 513 | 519 | 7 | inferred_complete_timeline |
| `Action_None` | 531 | 569 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 569 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–478
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 244 | 237 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 420 | 174 | inferred_complete_timeline |
| `Action_None` | 421 | 478 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 420 | 413 | inferred_complete_timeline |
| `Action_None` | 421 | 569 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 8–274 | 267 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 8–125 | 105 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 147–156 | 10 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 151–156 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 226–391 | 143 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 453–454 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 488–569 | 36 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 508–558 | 43 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 560–562 | 3 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 567–568 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `28` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (DE1) duration 95 frames exceeds threshold 90 frames [start=423, end=517].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '18' (C) duration 95 frames exceeds threshold 90 frames [start=423, end=517].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [421–434], lower_priority='Action_PullBlock' annotated_start=423, effective_Action_PullBlock_start=435.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 95 frames exceeds threshold 90 frames [start=423, end=517].
- ⚠️ Action 'Action_PreSnap' range [8-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-478] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-510] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-519] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-569] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-467] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-569] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-549] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-559] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [440-483] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [485-511] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [515-516] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [518-522] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [528-559] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [562-563] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-440] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-450] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-483] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-527] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-537] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-566] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-451] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-468] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [423-467] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-125] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [435-478] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [482-514] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-504] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-569] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-422] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [423-445] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [450-454] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [457-464] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [466-507] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-569] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-475] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-458] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-497] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-391] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [423-500] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [502-505] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-497] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-569] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-543] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
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

</details>