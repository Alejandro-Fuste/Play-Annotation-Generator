# Play-Annotation-Generator Annotation Review — Duo_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_93`
- **Frame Range:** 0 to 568 (569 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 568
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `27` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `29` | `21` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | offense | `25` | `18` |
| ⚠️ START CHANGED | `Action_ComboBlock` | C | offense | `26` | `19` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | RT | offense | `25` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `12` | `Group` | 0 | START | 0 | 525 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `25` | `Group` | 0 | START | 15 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `26` | `Group` | 0 | START | 15 | 376 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `27` | `Group` | 0 | START | 17 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 461 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 568 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `17` | `17` | 384 | START | 384 | 393 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `29` | `21` | 384 | START | 384 | 426 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | `25` | `18` | 384 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ComboBlock` | C | `26` | `19` | 384 | START | 387 | 426 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | RT | `25` | `18` | 405 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 426 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `27`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `27`
- **team_side:** `offense`
- **Visible Frames:** 17–531
- **Visible Samples:** 506

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 49 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 531 | 468 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 461 | 462 | inferred_complete_timeline |
| `Action_PreSnap` | 463 | 468 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 471 | 502 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 507 | 508 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 514 | 527 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 541 | 568 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–524
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 333 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 435 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 455 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 523 | 524 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 568 | 569 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–496
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 427 | 428 | inferred_complete_timeline |
| `Action_PreSnap` | 429 | 430 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 443 | 479 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 481 | 493 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 495 | 496 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–546
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 525 | 526 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 534 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 541 | 542 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 544 | 546 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–568
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 37 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 45 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 89 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 568 | 448 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `26`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 15–568
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 376 | 362 | inferred_complete_timeline |
| `Action_ComboBlock` | 387 | 426 | 40 | inferred_complete_timeline |
| `Action_None` | 427 | 464 | 38 | inferred_complete_timeline |
| `Action_None` | 468 | 475 | 8 | inferred_complete_timeline |
| `Action_None` | 477 | 556 | 80 | inferred_complete_timeline |
| `Action_None` | 558 | 568 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 383 | 380 | inferred_complete_timeline |
| `Action_ComboBlock` | 384 | 393 | 10 | inferred_complete_timeline |
| `Action_ComboBlock` | 404 | 415 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `25`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 15–375
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 81 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 367 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 375 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–434
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 389 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 434 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 372 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 568 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–496
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 427 | 307 | inferred_complete_timeline |
| `Action_PreSnap` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 437 | 449 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 459 | 461 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 463 | 464 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 470 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 495 | 496 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 568 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–456
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 420 | 421 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 437 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 441 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 455 | 456 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 449 | 450 | inferred_complete_timeline |
| `Action_PreSnap` | 451 | 452 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 454 | 547 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 551 | 568 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 547 | 548 | inferred_complete_timeline |
| `Action_PreSnap` | 562 | 568 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 475 | 476 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 479 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 485 | 507 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 515 | 516 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 518 | 556 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 560 | 568 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–528
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 492 | 493 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 508 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 511 | 528 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 493 | 494 | inferred_complete_timeline |
| `Action_PreSnap` | 501 | 525 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 527 | 531 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 533 | 568 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–539 | 396 | 13 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 122–568 | 429 | 9 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 398–474 | 23 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 409–454 | 41 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 421–422 | 2 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 444–448 | 5 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 450–452 | 3 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 467–568 | 90 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 472–568 | 87 | 4 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 479–568 | 86 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 495–568 | 73 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 537–568 | 32 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 555–568 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_ComboBlock` on target `25` (RT)
- ⚠️ `Action_ComboBlock` for actor_track_id `26` (C): Annotated start 384 != Inferred start 387
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `25` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 130 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 568 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '18' has invalid range: start=384, end=375. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '18' has invalid range: start=405, end=375. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-333] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-435] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-455] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [523-524] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-475] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-479] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-507] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-516] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-556] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-452] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-547] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-492] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-508] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-528] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-461] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-468] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-502] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-508] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [514-527] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [541-568] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-420] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-437] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-441] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-453] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-456] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-493] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-525] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-531] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-81] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-434] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-425] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-427] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-461] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-464] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-470] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-547] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-525] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-534] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [541-542] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-546] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-372] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-568] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-45] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-89] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-568] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-427] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-430] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [443-479] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-493] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-371] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-423] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-433] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-466] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-491] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-506] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-528] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-539] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-383] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [384-393] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [404-415] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-81] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-367] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-375] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-376] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-464] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-475] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-556] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-531] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-371] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-460] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-480] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-519] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-528] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-542] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-400] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-466] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-474] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-415] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-421] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-454] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-422] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-448] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-452] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-540] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-479] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-485] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-488] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-513] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-542] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-556] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [559-568] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>