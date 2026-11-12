# Play-Annotation-Generator Annotation Review — SplitZone_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_55`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 6 | START | 7 | 368 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 6 | START | 7 | 368 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 6 | START | 7 | 371 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 6 | START | 7 | 371 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 6 | START | 7 | 368 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 6 | START | 7 | 371 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 6 | START | 7 | 371 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 6 | START | 7 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 6 | START | 7 | 392 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 6 | START | 7 | 368 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 6 | START | 7 | 368 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 369 | START | 369 | 380 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 372 | START | 381 | 393 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `18` | 372 | START | 372 | 458 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `19` | 372 | START | 372 | 399 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 372 | START | 372 | 447 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 372 | START | 372 | 389 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 374 | START | 374 | 458 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 380 | END | 369 | 380 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 387 | START | 387 | 392 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `4` | `4` | 393 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `21` | `21` | 408 | START | 408 | 410 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 458 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_SnapReceive` | 369 | 380 | 12 | inferred_complete_timeline |
| `Action_None` | 381 | 386 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 387 | 392 | 6 | inferred_complete_timeline |
| `Action_None` | 393 | 569 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 7–392
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 392 | 386 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 557

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 500 | 132 | inferred_complete_timeline |
| `Action_None` | 507 | 569 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 557 | 189 | inferred_complete_timeline |
| `Action_None` | 561 | 569 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 569 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 373 | 367 | inferred_complete_timeline |
| `Action_SplitBlock` | 374 | 458 | 85 | inferred_complete_timeline |
| `Action_None` | 459 | 501 | 43 | inferred_complete_timeline |
| `Action_None` | 503 | 569 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 541

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 371 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 372 | 399 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 402 | 458 | 57 | inferred_complete_timeline |
| `Action_None` | 459 | 542 | 84 | inferred_complete_timeline |
| `Action_None` | 563 | 569 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 545

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 371 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 372 | 447 | 76 | inferred_complete_timeline |
| `Action_None` | 466 | 569 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_BallSnap` | 369 | 380 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 381 | 393 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 458 | 458 | 1 | inferred_complete_timeline |
| `Action_None` | 459 | 459 | 1 | inferred_complete_timeline |
| `Action_None` | 464 | 465 | 2 | inferred_complete_timeline |
| `Action_None` | 470 | 569 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 545

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 371 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 372 | 389 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 397 | 398 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 401 | 407 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 408 | 410 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 415 | 458 | 44 | inferred_complete_timeline |
| `Action_None` | 459 | 472 | 14 | inferred_complete_timeline |
| `Action_None` | 475 | 476 | 2 | inferred_complete_timeline |
| `Action_None` | 480 | 569 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 371 | 365 | inferred_complete_timeline |
| `Action_ZoneBlock` | 372 | 458 | 87 | inferred_complete_timeline |
| `Action_None` | 459 | 569 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 569 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 417 | 49 | inferred_complete_timeline |
| `Action_None` | 431 | 448 | 18 | inferred_complete_timeline |
| `Action_None` | 453 | 569 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–425
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 425 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–465
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 465 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–460
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 444 | 76 | inferred_complete_timeline |
| `Action_None` | 447 | 460 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 415 | 47 | inferred_complete_timeline |
| `Action_None` | 417 | 569 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 569 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 474 | 106 | inferred_complete_timeline |
| `Action_None` | 477 | 569 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 569 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 569 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 7–569
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 368 | 362 | inferred_complete_timeline |
| `Action_None` | 369 | 569 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 402–569 | 152 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 419–569 | 135 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 451–569 | 111 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 479–569 | 91 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 489–490 | 2 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 497–542 | 41 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 513–525 | 11 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 541–547 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (RB)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=393, end=392. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [369–380], lower_priority='Action_ZoneBlock' annotated_start=372, effective_Action_ZoneBlock_start=381.
- ⚠️ Action 'Action_None' range [369-417] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-448] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-500] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-557] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-569] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-501] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-392] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-465] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-474] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-569] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-444] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-460] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-415] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-569] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-569] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [381-393] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 459, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [459-459] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-425] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [372-399] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-542] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [372-447] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [372-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [397-398] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [408-410] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-472] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-487] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-510] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-431] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-471] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-510] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-534] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-516] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-525] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-547] for track '29' has 2 frames without a visible bounding box.
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

</details>