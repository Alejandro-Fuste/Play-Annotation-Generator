# Play-Annotation-Generator Annotation Review — InsideZoneRead_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_17`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Handoff` | LB2 | defense | `12` | `11` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 411 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 440 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 411 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 411 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 411 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 409 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 409 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 410 | START | 410 | 428 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 412 | START | 412 | 445 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 412 | START | 412 | 445 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 412 | START | 429 | 437 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 412 | START | 412 | 498 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 412 | START | 412 | 431 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 428 | END | 410 | 428 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `16` | 432 | START | 432 | 599 |
| ✅ EXACT | `Action_Handoff` | LB2 | `12` | `11` | 444 | START | 444 | 450 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | `20` | `19` | 449 | START | 492 | 498 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `18` | `17` | 451 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 498 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_SnapReceive` | 410 | 428 | 19 | inferred_complete_timeline |
| `Action_None` | 429 | 431 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 432 | 599 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–440
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 440 | 441 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 548 | 139 | inferred_complete_timeline |
| `Action_None` | 550 | 599 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–528
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 453 | 44 | inferred_complete_timeline |
| `Action_None` | 456 | 510 | 55 | inferred_complete_timeline |
| `Action_None` | 516 | 521 | 6 | inferred_complete_timeline |
| `Action_None` | 523 | 528 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 37 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 63 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 409 | 332 | inferred_complete_timeline |
| `Action_None` | 410 | 505 | 96 | inferred_complete_timeline |
| `Action_None` | 508 | 513 | 6 | inferred_complete_timeline |
| `Action_None` | 516 | 519 | 4 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |
| `Action_None` | 558 | 560 | 3 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |
| `Action_None` | 577 | 591 | 15 | inferred_complete_timeline |
| `Action_None` | 594 | 595 | 2 | inferred_complete_timeline |
| `Action_None` | 599 | 599 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 588 | 179 | inferred_complete_timeline |
| `Action_None` | 591 | 599 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |
| `Action_ZoneBlock` | 412 | 445 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 447 | 448 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 450 | 461 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 472 | 498 | 27 | inferred_complete_timeline |
| `Action_None` | 499 | 505 | 7 | inferred_complete_timeline |
| `Action_None` | 507 | 599 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |
| `Action_ZoneBlock` | 412 | 431 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 442 | 446 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 450 | 498 | 49 | inferred_complete_timeline |
| `Action_None` | 499 | 599 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–595
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_BallSnap` | 410 | 428 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 429 | 437 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 440 | 445 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 492 | 498 | 7 | inferred_complete_timeline |
| `Action_None` | 499 | 499 | 1 | inferred_complete_timeline |
| `Action_None` | 558 | 560 | 3 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |
| `Action_None` | 585 | 586 | 2 | inferred_complete_timeline |
| `Action_None` | 590 | 591 | 2 | inferred_complete_timeline |
| `Action_None` | 594 | 595 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–589
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |
| `Action_ZoneBlock` | 412 | 445 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 452 | 469 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 473 | 498 | 26 | inferred_complete_timeline |
| `Action_None` | 499 | 511 | 13 | inferred_complete_timeline |
| `Action_None` | 514 | 534 | 21 | inferred_complete_timeline |
| `Action_None` | 548 | 563 | 16 | inferred_complete_timeline |
| `Action_None` | 566 | 589 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–588
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 411 | 412 | inferred_complete_timeline |
| `Action_ZoneBlock` | 412 | 498 | 87 | inferred_complete_timeline |
| `Action_None` | 499 | 501 | 3 | inferred_complete_timeline |
| `Action_None` | 516 | 519 | 4 | inferred_complete_timeline |
| `Action_None` | 524 | 530 | 7 | inferred_complete_timeline |
| `Action_None` | 556 | 567 | 12 | inferred_complete_timeline |
| `Action_None` | 572 | 574 | 3 | inferred_complete_timeline |
| `Action_None` | 583 | 588 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 447 | 38 | inferred_complete_timeline |
| `Action_None` | 449 | 450 | 2 | inferred_complete_timeline |
| `Action_None` | 452 | 599 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–525
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 445 | 36 | inferred_complete_timeline |
| `Action_None` | 454 | 511 | 58 | inferred_complete_timeline |
| `Action_None` | 516 | 519 | 4 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–472
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 437 | 28 | inferred_complete_timeline |
| `Action_None` | 463 | 472 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–470
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 445 | 36 | inferred_complete_timeline |
| `Action_None` | 452 | 470 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–525
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 504 | 95 | inferred_complete_timeline |
| `Action_None` | 507 | 511 | 5 | inferred_complete_timeline |
| `Action_None` | 516 | 517 | 2 | inferred_complete_timeline |
| `Action_None` | 519 | 520 | 2 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–516
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 443 | 444 | inferred_complete_timeline |
| `Action_Handoff` | 444 | 450 | 7 | inferred_complete_timeline |
| `Action_None` | 451 | 499 | 49 | inferred_complete_timeline |
| `Action_None` | 505 | 516 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–586
- **Visible Samples:** 574

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 571 | 162 | inferred_complete_timeline |
| `Action_None` | 585 | 586 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 520 | 111 | inferred_complete_timeline |
| `Action_None` | 524 | 525 | 2 | inferred_complete_timeline |
| `Action_None` | 594 | 595 | 2 | inferred_complete_timeline |
| `Action_None` | 598 | 599 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 599 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–586
- **Visible Samples:** 550

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 545 | 136 | inferred_complete_timeline |
| `Action_None` | 559 | 560 | 2 | inferred_complete_timeline |
| `Action_None` | 585 | 586 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–567
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 409 | 410 | inferred_complete_timeline |
| `Action_None` | 410 | 521 | 112 | inferred_complete_timeline |
| `Action_None` | 524 | 529 | 6 | inferred_complete_timeline |
| `Action_None` | 533 | 539 | 7 | inferred_complete_timeline |
| `Action_None` | 566 | 567 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 445–473 | 29 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 453–599 | 147 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 467–529 | 38 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 534–543 | 10 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 557–562 | 6 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 557–587 | 12 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 559–560 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 573–574 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 599–599 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `20` (C): Annotated start 449 != Inferred start 492
- ❌ Missing segment for action `Action_BallCarry` on target `18` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '17' has invalid range: start=451, end=440. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [410–428], lower_priority='Action_ZoneBlock' annotated_start=412, effective_Action_ZoneBlock_start=429.
- ⚠️ Action 'Action_None' range [410-548] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-545] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-504] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-571] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-588] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-520] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-453] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-510] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-521] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-528] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-437] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-472] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-447] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [412-445] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [447-448] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [450-461] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-505] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-599] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-499] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-516] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-63] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-505] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-513] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-519] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-560] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-591] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-521] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-539] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-445] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-470] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-511] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-519] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-440] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [412-445] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [452-469] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [473-498] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-511] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-534] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-563] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-589] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [429-437] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [440-445] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [492-498] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 499, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [499-499] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-560] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-519] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-530] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-567] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-588] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [412-431] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [442-446] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [450-498] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-473] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-599] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-474] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-489] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-495] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-511] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-543] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-562] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-562] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-587] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '29' has 1 frames without a visible bounding box.
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

</details>