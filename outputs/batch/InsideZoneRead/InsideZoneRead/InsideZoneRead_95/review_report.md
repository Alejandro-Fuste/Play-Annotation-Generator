# Play-Annotation-Generator Annotation Review — InsideZoneRead_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_95`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 80
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 4 | START | 4 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 4 | START | 4 | 373 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 4 | START | 4 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 4 | START | 4 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 4 | START | 4 | 330 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 4 | START | 4 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 4 | START | 4 | 330 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 4 | START | 4 | 330 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 4 | START | 4 | 330 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 4 | START | 4 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 4 | START | 4 | 328 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 329 | START | 329 | 343 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 331 | START | 353 | 355 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 331 | START | 331 | 362 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 331 | START | 331 | 442 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 331 | START | 331 | 356 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 331 | START | 331 | 351 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 345 | END | 329 | 345 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `16` | `15` | 351 | START | 351 | 362 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `22` | `21` | 352 | START | 352 | 442 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 367 | START | 367 | 373 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 374 | START | 374 | 493 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 442 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–485
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_SnapReceive` | 329 | 345 | 17 | inferred_complete_timeline |
| `Action_None` | 346 | 350 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 351 | 362 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 365 | 366 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 367 | 373 | 7 | inferred_complete_timeline |
| `Action_None` | 374 | 391 | 18 | inferred_complete_timeline |
| `Action_None` | 395 | 407 | 13 | inferred_complete_timeline |
| `Action_None` | 432 | 444 | 13 | inferred_complete_timeline |
| `Action_None` | 451 | 452 | 2 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |
| `Action_None` | 484 | 485 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–493
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 373 | 370 | inferred_complete_timeline |
| `Action_BallCarry` | 374 | 493 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–494
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 471 | 143 | inferred_complete_timeline |
| `Action_None` | 473 | 494 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 509 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–366
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 366 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 509 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 330 | 327 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 362 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 364 | 413 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 415 | 436 | 22 | inferred_complete_timeline |
| `Action_None` | 463 | 501 | 39 | inferred_complete_timeline |
| `Action_None` | 503 | 509 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 330 | 327 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 442 | 112 | inferred_complete_timeline |
| `Action_None` | 443 | 509 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_BallSnap` | 329 | 343 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 353 | 355 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 362 | 388 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 390 | 415 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 442 | 17 | inferred_complete_timeline |
| `Action_None` | 443 | 509 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 330 | 327 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 351 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 352 | 442 | 91 | inferred_complete_timeline |
| `Action_None` | 443 | 469 | 27 | inferred_complete_timeline |
| `Action_None` | 471 | 472 | 2 | inferred_complete_timeline |
| `Action_None` | 503 | 504 | 2 | inferred_complete_timeline |
| `Action_None` | 509 | 509 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–509
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 330 | 327 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 356 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 358 | 438 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 443 | 509 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 393 | 65 | inferred_complete_timeline |
| `Action_None` | 401 | 403 | 3 | inferred_complete_timeline |
| `Action_None` | 443 | 489 | 47 | inferred_complete_timeline |
| `Action_None` | 491 | 509 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–502
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 441 | 113 | inferred_complete_timeline |
| `Action_None` | 445 | 478 | 34 | inferred_complete_timeline |
| `Action_None` | 480 | 483 | 4 | inferred_complete_timeline |
| `Action_None` | 486 | 493 | 8 | inferred_complete_timeline |
| `Action_None` | 496 | 502 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 357 | 29 | inferred_complete_timeline |
| `Action_None` | 368 | 418 | 51 | inferred_complete_timeline |
| `Action_None` | 423 | 509 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 439 | 111 | inferred_complete_timeline |
| `Action_None` | 446 | 447 | 2 | inferred_complete_timeline |
| `Action_None` | 451 | 509 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 417 | 89 | inferred_complete_timeline |
| `Action_None` | 419 | 432 | 14 | inferred_complete_timeline |
| `Action_None` | 437 | 438 | 2 | inferred_complete_timeline |
| `Action_None` | 441 | 454 | 14 | inferred_complete_timeline |
| `Action_None` | 456 | 480 | 25 | inferred_complete_timeline |
| `Action_None` | 483 | 509 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 488 | 160 | inferred_complete_timeline |
| `Action_None` | 503 | 509 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–486
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 442 | 114 | inferred_complete_timeline |
| `Action_None` | 444 | 486 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 509 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–509
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 509 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–467
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 457 | 129 | inferred_complete_timeline |
| `Action_None` | 459 | 467 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–455
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 328 | 325 | inferred_complete_timeline |
| `Action_None` | 329 | 414 | 86 | inferred_complete_timeline |
| `Action_None` | 420 | 450 | 31 | inferred_complete_timeline |
| `Action_None` | 452 | 455 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 367–499 | 133 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 368–369 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 393–395 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 457–509 | 52 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 461–509 | 16 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 495–509 | 13 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 112 frames exceeds threshold 90 frames [start=331, end=442].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [329–345], lower_priority='Action_ZoneBlock' annotated_start=331, effective_Action_ZoneBlock_start=346.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LT) duration 112 frames exceeds threshold 90 frames [start=331, end=442].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 112 frames exceeds threshold 90 frames [start=331, end=442].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 112 frames exceeds threshold 90 frames [start=331, end=442].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '21' (RG) duration 91 frames exceeds threshold 90 frames [start=352, end=442].
- ⚠️ Action 'Action_None' range [329-366] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-471] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-494] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-393] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-489] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-414] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-450] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-455] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-442] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-486] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [374-493] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-417] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-432] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-454] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-480] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-439] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-441] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-478] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-483] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-493] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-502] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [329-343] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [353-355] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [362-388] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [390-415] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-488] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [351-362] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-391] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-407] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-444] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-457] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-467] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [331-362] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [364-413] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [415-436] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-501] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-357] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-418] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-509] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [331-356] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [358-438] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-469] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-499] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-509] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-486] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-501] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '27' has 1 frames without a visible bounding box.
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

</details>