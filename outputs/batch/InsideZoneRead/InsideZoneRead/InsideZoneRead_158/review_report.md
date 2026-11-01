# Play-Annotation-Generator Annotation Review — InsideZoneRead_158

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_158`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `26` | `22` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 2 | START | 2 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `10` | `Group` | 2 | START | 2 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 2 | START | 2 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 2 | START | 2 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 2 | START | 2 | 326 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 2 | START | 2 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 2 | START | 2 | 326 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 2 | START | 2 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `26` | `Group` | 2 | START | 36 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 2 | START | 2 | 323 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `21` | `19` | 324 | START | 324 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 327 | START | 327 | 371 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 327 | START | 327 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 327 | START | 327 | 347 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `19` | 327 | START | 340 | 341 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `26` | `22` | 327 | START | 327 | 335 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 337 | END | 324 | 337 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `10` | 343 | START | 343 | 361 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 362 | START | 362 | 529 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 391 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 2–529
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 65 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 323 | 250 | inferred_complete_timeline |
| `Action_SnapReceive` | 324 | 337 | 14 | inferred_complete_timeline |
| `Action_None` | 338 | 342 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 343 | 361 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 529 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 53 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 142 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 210 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 323 | 100 | inferred_complete_timeline |
| `Action_None` | 324 | 341 | 18 | inferred_complete_timeline |
| `Action_None` | 352 | 382 | 31 | inferred_complete_timeline |
| `Action_None` | 384 | 539 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 2–478
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 478 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 539 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–457
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 457 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 2–499
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 326 | 325 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 371 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_None` | 402 | 499 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 9 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 20 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 137 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 298 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 321 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 326 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 329 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 387 | 391 | 5 | inferred_complete_timeline |
| `Action_None` | 392 | 539 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_BallSnap` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 340 | 341 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 353 | 359 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 368 | 383 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_None` | 392 | 539 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `26`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 36–539
- **Visible Samples:** 484

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 53 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 326 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 335 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 355 | 391 | 37 | inferred_complete_timeline |
| `Action_None` | 392 | 539 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 2–367
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 326 | 325 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 347 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 367 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 350 | 27 | inferred_complete_timeline |
| `Action_None` | 353 | 425 | 73 | inferred_complete_timeline |
| `Action_None` | 427 | 539 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 12–352
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 126 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 323 | 178 | inferred_complete_timeline |
| `Action_None` | 324 | 352 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 2–439
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 49 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 323 | 249 | inferred_complete_timeline |
| `Action_None` | 324 | 338 | 15 | inferred_complete_timeline |
| `Action_None` | 348 | 405 | 58 | inferred_complete_timeline |
| `Action_None` | 408 | 411 | 4 | inferred_complete_timeline |
| `Action_None` | 415 | 434 | 20 | inferred_complete_timeline |
| `Action_None` | 436 | 439 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 2–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 443 | 120 | inferred_complete_timeline |
| `Action_None` | 445 | 539 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 2–520
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 520 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–473
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 468 | 145 | inferred_complete_timeline |
| `Action_None` | 472 | 473 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 2–395
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 395 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–520
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 504 | 181 | inferred_complete_timeline |
| `Action_None` | 509 | 520 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 539 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–529
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 323 | 322 | inferred_complete_timeline |
| `Action_None` | 324 | 529 | 206 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 2–539 | 535 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 2–344 | 343 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 12–16 | 5 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 59–66 | 8 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 369–371 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 381–539 | 159 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 387–539 | 153 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 394–539 | 146 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 438–444 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 442–539 | 98 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 466–539 | 62 | 4 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 469–509 | 30 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 475–539 | 65 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 508–509 | 2 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 513–514 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `26` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 316: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 316: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [324–337], lower_priority='Action_ZoneBlock' annotated_start=327, effective_Action_ZoneBlock_start=338.
- ⚠️ Action 'Action_None' range [324-478] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-350] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-468] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-350] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-425] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-520] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-504] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-520] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-395] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-457] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [362-529] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-529] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-341] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-382] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-443] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-344] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-371] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [376-377] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-499] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-9] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-137] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-298] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-321] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-338] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-405] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-434] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-347] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [363-367] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-323] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [324-326] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [328-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [335-336] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [340-341] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [353-359] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [368-383] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-126] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-335] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-66] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-444] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-471] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-495] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-509] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-539] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-491] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>