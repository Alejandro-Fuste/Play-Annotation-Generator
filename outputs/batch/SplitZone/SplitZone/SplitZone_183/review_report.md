# Play-Annotation-Generator Annotation Review — SplitZone_183

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_183`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_-`
- **Result Frame:** 569
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 165
- **Validation Warnings:** 185
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 309 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 309 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 309 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 306 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 161 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 307 | START | 307 | 318 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 310 | START | 310 | 331 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 310 | START | 323 | 333 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 310 | START | 310 | 399 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 310 | START | 310 | 315 |
| ✅ EXACT | `Action_SplitBlock` | TE | `2` | `2` | 312 | START | 312 | 399 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 322 | END | 307 | 322 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `8` | `8` | 331 | START | 331 | 399 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 331 | START | 331 | 338 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 339 | START | 339 | 405 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 399 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_SnapReceive` | 307 | 322 | 16 | inferred_complete_timeline |
| `Action_None` | 323 | 330 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 331 | 338 | 8 | inferred_complete_timeline |
| `Action_None` | 339 | 425 | 87 | inferred_complete_timeline |
| `Action_None` | 430 | 451 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–552
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 338 | 172 | inferred_complete_timeline |
| `Action_BallCarry` | 339 | 405 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 408 | 479 | 72 | inferred_complete_timeline |
| `Action_BallCarry` | 481 | 489 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 491 | 493 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 499 | 502 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 513 | 514 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 526 | 528 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 531 | 537 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 539 | 552 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 569 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 543 | 237 | inferred_complete_timeline |
| `Action_None` | 548 | 556 | 9 | inferred_complete_timeline |
| `Action_None` | 558 | 559 | 2 | inferred_complete_timeline |
| `Action_None` | 561 | 563 | 3 | inferred_complete_timeline |
| `Action_None` | 567 | 569 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–478
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 362 | 56 | inferred_complete_timeline |
| `Action_None` | 366 | 369 | 4 | inferred_complete_timeline |
| `Action_None` | 374 | 380 | 7 | inferred_complete_timeline |
| `Action_None` | 385 | 388 | 4 | inferred_complete_timeline |
| `Action_None` | 396 | 478 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 311 | 312 | inferred_complete_timeline |
| `Action_SplitBlock` | 312 | 399 | 88 | inferred_complete_timeline |
| `Action_None` | 400 | 424 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–484
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 309 | 310 | inferred_complete_timeline |
| `Action_ZoneBlock` | 310 | 331 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 361 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 365 | 399 | 35 | inferred_complete_timeline |
| `Action_None` | 400 | 430 | 31 | inferred_complete_timeline |
| `Action_None` | 436 | 458 | 23 | inferred_complete_timeline |
| `Action_None` | 463 | 464 | 2 | inferred_complete_timeline |
| `Action_None` | 480 | 484 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_BallSnap` | 307 | 318 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 323 | 333 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 399 | 65 | inferred_complete_timeline |
| `Action_None` | 400 | 482 | 83 | inferred_complete_timeline |
| `Action_None` | 484 | 485 | 2 | inferred_complete_timeline |
| `Action_None` | 487 | 498 | 12 | inferred_complete_timeline |
| `Action_None` | 501 | 506 | 6 | inferred_complete_timeline |
| `Action_None` | 510 | 539 | 30 | inferred_complete_timeline |
| `Action_None` | 542 | 563 | 22 | inferred_complete_timeline |
| `Action_None` | 565 | 569 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 309 | 310 | inferred_complete_timeline |
| `Action_ZoneBlock` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 332 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 334 | 356 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 359 | 399 | 41 | inferred_complete_timeline |
| `Action_None` | 400 | 569 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 309 | 310 | inferred_complete_timeline |
| `Action_ZoneBlock` | 310 | 399 | 90 | inferred_complete_timeline |
| `Action_None` | 400 | 401 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–524
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 397 | 91 | inferred_complete_timeline |
| `Action_None` | 401 | 458 | 58 | inferred_complete_timeline |
| `Action_None` | 460 | 464 | 5 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |
| `Action_None` | 473 | 474 | 2 | inferred_complete_timeline |
| `Action_None` | 489 | 491 | 3 | inferred_complete_timeline |
| `Action_None` | 517 | 524 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 329 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 334 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 475 | 169 | inferred_complete_timeline |
| `Action_None` | 478 | 479 | 2 | inferred_complete_timeline |
| `Action_None` | 486 | 488 | 3 | inferred_complete_timeline |
| `Action_None` | 492 | 494 | 3 | inferred_complete_timeline |
| `Action_None` | 499 | 500 | 2 | inferred_complete_timeline |
| `Action_None` | 502 | 558 | 57 | inferred_complete_timeline |
| `Action_None` | 561 | 569 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 358 | 52 | inferred_complete_timeline |
| `Action_None` | 362 | 388 | 27 | inferred_complete_timeline |
| `Action_None` | 390 | 432 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 403 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 569 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 562 | 256 | inferred_complete_timeline |
| `Action_None` | 564 | 569 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–535
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 466 | 160 | inferred_complete_timeline |
| `Action_None` | 468 | 473 | 6 | inferred_complete_timeline |
| `Action_None` | 477 | 478 | 2 | inferred_complete_timeline |
| `Action_None` | 504 | 506 | 3 | inferred_complete_timeline |
| `Action_None` | 517 | 519 | 3 | inferred_complete_timeline |
| `Action_None` | 524 | 535 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 569 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_None` | 307 | 440 | 134 | inferred_complete_timeline |
| `Action_None` | 445 | 569 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–461 | 461 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 335–434 | 100 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 339–569 | 216 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 364–569 | 168 | 3 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 402–438 | 37 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 412–425 | 14 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 428–438 | 11 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 437–569 | 122 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 439–473 | 29 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 449–568 | 111 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 464–465 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 469–494 | 19 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 477–569 | 82 | 5 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 481–557 | 37 | 6 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 485–486 | 2 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 487–492 | 6 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 497–499 | 3 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 501–569 | 66 | 4 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 510–568 | 57 | 2 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 512–516 | 5 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 518–519 | 2 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 523–524 | 2 | 1 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 526–569 | 28 | 4 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 542–544 | 3 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 556–569 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (9 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 368: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [307–322], lower_priority='Action_ZoneBlock' annotated_start=310, effective_Action_ZoneBlock_start=323.
- ⚠️ Action 'Action_None' range [307-569] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-543] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-556] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-424] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-334] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-362] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-478] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-569] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [339-405] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [408-479] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [481-489] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [491-493] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [499-502] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [513-514] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [526-528] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [531-537] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [539-552] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-397] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-458] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-464] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-491] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-524] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [331-399] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-456] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-475] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-494] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-558] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-440] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-358] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-388] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-432] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-425] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-451] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-569] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-562] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [310-331] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [335-361] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-430] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-458] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [307-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [323-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-482] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-498] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-506] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-539] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-563] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-466] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-473] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-506] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-535] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-403] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [310-399] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [310-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [318-332] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [334-356] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-434] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-446] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-504] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-569] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-390] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-438] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-425] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-438] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-475] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-501] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-519] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-465] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-453] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-533] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-559] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-568] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-475] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-494] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-496] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-518] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-546] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-558] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-569] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-488] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-514] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-544] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-554] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-492] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-508] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-534] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-569] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-543] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-568] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-516] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-519] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-530] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-547] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-569] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-544] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-563] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-569] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.

</details>