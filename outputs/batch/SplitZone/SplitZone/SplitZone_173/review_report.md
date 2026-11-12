# Play-Annotation-Generator Annotation Review — SplitZone_173

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_173`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | CB2 | defense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 367 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 408 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 368 | START | 368 | 372 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `12` | 371 | START | 371 | 394 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `16` | 371 | START | 373 | 385 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `17` | 371 | START | 371 | 527 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 371 | START | 371 | 381 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 371 | START | 371 | 415 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 372 | END | 368 | 372 |
| ✅ EXACT | `Action_SplitBlock` | CB2 | `10` | `10` | 378 | START | 378 | 527 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 404 | START | 404 | 408 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `8` | 409 | START | 409 | 474 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 527 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–438
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_SnapReceive` | 368 | 372 | 5 | inferred_complete_timeline |
| `Action_None` | 373 | 403 | 31 | inferred_complete_timeline |
| `Action_Handoff` | 404 | 408 | 5 | inferred_complete_timeline |
| `Action_None` | 409 | 438 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–474
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 408 | 409 | inferred_complete_timeline |
| `Action_BallCarry` | 409 | 474 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 599 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 599 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 414 | 47 | inferred_complete_timeline |
| `Action_None` | 417 | 539 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 599 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–478
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 415 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 419 | 478 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 381 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 386 | 389 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 392 | 423 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 438 | 455 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 457 | 527 | 71 | inferred_complete_timeline |
| `Action_None` | 528 | 599 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–441
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_BallSnap` | 368 | 372 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 373 | 385 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 389 | 427 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 432 | 435 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 440 | 441 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 527 | 157 | inferred_complete_timeline |
| `Action_None` | 528 | 599 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 394 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 404 | 405 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 411 | 412 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 414 | 506 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 508 | 527 | 20 | inferred_complete_timeline |
| `Action_None` | 528 | 599 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 430 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–442
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 442 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–450
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 396 | 29 | inferred_complete_timeline |
| `Action_None` | 399 | 450 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 417 | 50 | inferred_complete_timeline |
| `Action_None` | 419 | 448 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 583

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 420 | 53 | inferred_complete_timeline |
| `Action_None` | 432 | 543 | 112 | inferred_complete_timeline |
| `Action_None` | 546 | 571 | 26 | inferred_complete_timeline |
| `Action_None` | 576 | 599 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 468 | 101 | inferred_complete_timeline |
| `Action_None` | 470 | 599 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 498 | 131 | inferred_complete_timeline |
| `Action_None` | 500 | 519 | 20 | inferred_complete_timeline |
| `Action_None` | 521 | 523 | 3 | inferred_complete_timeline |
| `Action_None` | 526 | 543 | 18 | inferred_complete_timeline |
| `Action_None` | 546 | 599 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 377 | 378 | inferred_complete_timeline |
| `Action_SplitBlock` | 378 | 527 | 150 | inferred_complete_timeline |
| `Action_None` | 528 | 599 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 599 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–595
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 556 | 189 | inferred_complete_timeline |
| `Action_None` | 558 | 595 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–541
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 367 | 368 | inferred_complete_timeline |
| `Action_None` | 368 | 541 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 382–383 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 439–575 | 131 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 443–490 | 43 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 444–591 | 147 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 445–460 | 16 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 452–453 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 460–462 | 3 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 461–512 | 26 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 471–519 | 46 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 477–527 | 51 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 486–495 | 10 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 496–599 | 101 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 503–509 | 7 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 515–519 | 5 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 516–532 | 17 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 577–599 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 157 frames exceeds threshold 90 frames [start=371, end=527].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [368–372], lower_priority='Action_ZoneBlock' annotated_start=371, effective_Action_ZoneBlock_start=373.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RG) duration 157 frames exceeds threshold 90 frames [start=371, end=527].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 157 frames exceeds threshold 90 frames [start=371, end=527].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 108 frames exceeds threshold 90 frames [start=371, end=478].
- ⚠️ Action 'Action_None' range [368-417] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-448] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-396] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-450] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-430] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-442] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-420] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-543] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-571] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [409-474] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-556] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-595] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-599] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-468] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [371-394] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [404-405] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [411-412] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [414-506] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-599] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-541] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-498] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-519] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-523] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-543] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [373-385] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [389-427] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [432-435] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [440-441] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-539] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-438] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-370] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [371-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [383-384] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [386-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [392-423] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [438-455] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [371-415] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [419-478] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-486] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-509] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-575] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-472] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-490] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-481] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-591] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-460] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-512] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-508] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-519] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-527] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-495] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-590] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-519] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-532] for track '36' has 1 frames without a visible bounding box.
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

</details>