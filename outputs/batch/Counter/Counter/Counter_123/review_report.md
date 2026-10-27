# Play-Annotation-Generator Annotation Review — Counter_123

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_123`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | WR3 | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `20` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 291 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 292 | START | 292 | 307 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 300 | START | 300 | 331 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `8` | `7` | 300 | START | 308 | 321 |
| ✅ EXACT | `Action_PlaySideFakeStep` | Position_Unknown | `3` | `2` | 300 | START | 300 | 332 |
| ✅ EXACT | `Action_PullBlock` | LG | `19` | `18` | 300 | START | 300 | 381 |
| ✅ EXACT | `Action_PullLeadBlock` | WR3 | `5` | `4` | 300 | START | 300 | 336 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 307 | END | 292 | 307 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 318 | START | 318 | 332 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `3` | `2` | 333 | START | 333 | 465 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 381 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_SnapReceive` | 292 | 307 | 16 | inferred_complete_timeline |
| `Action_None` | 308 | 317 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 318 | 332 | 15 | inferred_complete_timeline |
| `Action_None` | 333 | 499 | 167 | inferred_complete_timeline |
| `Action_None` | 502 | 539 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 539 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–524
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 524 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 300 | 336 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–463
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 361 | 70 | inferred_complete_timeline |
| `Action_None` | 363 | 463 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–432
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_PullBlock` | 300 | 381 | 82 | inferred_complete_timeline |
| `Action_None` | 382 | 432 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_BallSnap` | 292 | 307 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 308 | 321 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |
| `Action_DownBlock` | 300 | 331 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 342 | 343 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–527
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 527 | 236 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–363
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 363 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–454
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 346 | 55 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |
| `Action_None` | 358 | 360 | 3 | inferred_complete_timeline |
| `Action_None` | 409 | 454 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 325 | 34 | inferred_complete_timeline |
| `Action_None` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_None` | 343 | 346 | 4 | inferred_complete_timeline |
| `Action_None` | 368 | 371 | 4 | inferred_complete_timeline |
| `Action_None` | 374 | 509 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–489
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 359 | 68 | inferred_complete_timeline |
| `Action_None` | 361 | 489 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 539 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 413 | 122 | inferred_complete_timeline |
| `Action_None` | 425 | 446 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 539 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 539 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 517 | 226 | inferred_complete_timeline |
| `Action_None` | 521 | 539 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 502 | 211 | inferred_complete_timeline |
| `Action_None` | 534 | 539 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 539 | 248 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–539 | 540 | 2 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–491 | 476 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 330–485 | 156 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 338–437 | 99 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 358–482 | 125 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 359–384 | 25 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 361–456 | 96 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 406–408 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 412–479 | 48 | 3 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 491–494 | 4 | 1 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 500–502 | 3 | 1 | Undefined position; Undefined team |
| `31` | `55` | Position_Unknown | Team_Unknown | 515–518 | 4 | 1 | Undefined position; Undefined team |
| `32` | `59` | Position_Unknown | Team_Unknown | 523–525 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `8` (C): Annotated start 300 != Inferred start 308
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 248: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [292–307], lower_priority='Action_DownBlock' annotated_start=300, effective_Action_DownBlock_start=308.
- ⚠️ Action 'Action_None' range [292-527] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [333-465] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [467-469] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [476-477] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [484-486] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [490-491] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-413] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-446] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [300-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-363] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [308-321] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-489] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-517] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-524] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-499] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-346] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-454] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-502] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-371] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-509] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-432] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [300-331] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [342-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-361] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-463] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-485] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-437] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-482] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-384] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-456] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-454] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-479] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-494] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-502] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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