# Play-Annotation-Generator Annotation Review — SplitZone_165

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_165`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 569
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 170
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 138
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 8 | START | 9 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 8 | START | 9 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `12` | `Group` | 8 | START | 9 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 8 | START | 9 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 8 | START | 9 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 8 | START | 9 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 8 | START | 9 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 8 | START | 9 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 8 | START | 9 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 8 | START | 9 | 292 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 293 | START | 293 | 306 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `19` | `19` | 296 | START | 307 | 421 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 296 | START | 296 | 421 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 296 | START | 296 | 421 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 296 | START | 296 | 421 |
| ✅ EXACT | `Action_SplitBlock` | HB | `12` | `12` | 304 | START | 304 | 408 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 306 | END | 293 | 306 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 312 | START | 312 | 324 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 325 | START | 325 | 567 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 421 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–529
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_SnapReceive` | 293 | 306 | 14 | inferred_complete_timeline |
| `Action_None` | 307 | 311 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 312 | 324 | 13 | inferred_complete_timeline |
| `Action_None` | 325 | 529 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 324 | 316 | inferred_complete_timeline |
| `Action_BallCarry` | 325 | 567 | 243 | inferred_complete_timeline |
| `Action_BallCarry` | 569 | 569 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–408
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 303 | 295 | inferred_complete_timeline |
| `Action_SplitBlock` | 304 | 408 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–537
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 505 | 213 | inferred_complete_timeline |
| `Action_None` | 507 | 515 | 9 | inferred_complete_timeline |
| `Action_None` | 517 | 518 | 2 | inferred_complete_timeline |
| `Action_None` | 523 | 525 | 3 | inferred_complete_timeline |
| `Action_None` | 527 | 528 | 2 | inferred_complete_timeline |
| `Action_None` | 530 | 537 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 569 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 9–388
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 332 | 40 | inferred_complete_timeline |
| `Action_None` | 352 | 355 | 4 | inferred_complete_timeline |
| `Action_None` | 358 | 388 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–473
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 295 | 287 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 421 | 126 | inferred_complete_timeline |
| `Action_None` | 422 | 432 | 11 | inferred_complete_timeline |
| `Action_None` | 436 | 447 | 12 | inferred_complete_timeline |
| `Action_None` | 456 | 473 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 9–569
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_BallSnap` | 293 | 306 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 307 | 421 | 115 | inferred_complete_timeline |
| `Action_None` | 422 | 515 | 94 | inferred_complete_timeline |
| `Action_None` | 521 | 522 | 2 | inferred_complete_timeline |
| `Action_None` | 525 | 526 | 2 | inferred_complete_timeline |
| `Action_None` | 533 | 540 | 8 | inferred_complete_timeline |
| `Action_None` | 546 | 549 | 4 | inferred_complete_timeline |
| `Action_None` | 552 | 554 | 3 | inferred_complete_timeline |
| `Action_None` | 558 | 561 | 4 | inferred_complete_timeline |
| `Action_None` | 567 | 569 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 9–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 295 | 287 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 421 | 126 | inferred_complete_timeline |
| `Action_None` | 422 | 569 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–555
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 295 | 287 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 421 | 126 | inferred_complete_timeline |
| `Action_None` | 422 | 500 | 79 | inferred_complete_timeline |
| `Action_None` | 502 | 508 | 7 | inferred_complete_timeline |
| `Action_None` | 512 | 516 | 5 | inferred_complete_timeline |
| `Action_None` | 521 | 532 | 12 | inferred_complete_timeline |
| `Action_None` | 543 | 544 | 2 | inferred_complete_timeline |
| `Action_None` | 550 | 555 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–569
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 318 | 26 | inferred_complete_timeline |
| `Action_None` | 320 | 324 | 5 | inferred_complete_timeline |
| `Action_None` | 328 | 333 | 6 | inferred_complete_timeline |
| `Action_None` | 335 | 358 | 24 | inferred_complete_timeline |
| `Action_None` | 367 | 369 | 3 | inferred_complete_timeline |
| `Action_None` | 376 | 384 | 9 | inferred_complete_timeline |
| `Action_None` | 388 | 569 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–361
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 342 | 50 | inferred_complete_timeline |
| `Action_None` | 360 | 361 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 9–561
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 331 | 39 | inferred_complete_timeline |
| `Action_None` | 336 | 342 | 7 | inferred_complete_timeline |
| `Action_None` | 344 | 351 | 8 | inferred_complete_timeline |
| `Action_None` | 368 | 369 | 2 | inferred_complete_timeline |
| `Action_None` | 381 | 388 | 8 | inferred_complete_timeline |
| `Action_None` | 411 | 530 | 120 | inferred_complete_timeline |
| `Action_None` | 532 | 550 | 19 | inferred_complete_timeline |
| `Action_None` | 558 | 561 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 9–325
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 325 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–569
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 542 | 250 | inferred_complete_timeline |
| `Action_None` | 547 | 563 | 17 | inferred_complete_timeline |
| `Action_None` | 569 | 569 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–367
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 334 | 42 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |
| `Action_None` | 361 | 367 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–565
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 337 | 45 | inferred_complete_timeline |
| `Action_None` | 339 | 411 | 73 | inferred_complete_timeline |
| `Action_None` | 417 | 518 | 102 | inferred_complete_timeline |
| `Action_None` | 520 | 556 | 37 | inferred_complete_timeline |
| `Action_None` | 559 | 562 | 4 | inferred_complete_timeline |
| `Action_None` | 564 | 565 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 9–554
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 522 | 230 | inferred_complete_timeline |
| `Action_None` | 532 | 554 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–505
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 327 | 35 | inferred_complete_timeline |
| `Action_None` | 331 | 467 | 137 | inferred_complete_timeline |
| `Action_None` | 477 | 496 | 20 | inferred_complete_timeline |
| `Action_None` | 499 | 500 | 2 | inferred_complete_timeline |
| `Action_None` | 503 | 505 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–569
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 333 | 41 | inferred_complete_timeline |
| `Action_None` | 337 | 347 | 11 | inferred_complete_timeline |
| `Action_None` | 349 | 371 | 23 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_None` | 406 | 408 | 3 | inferred_complete_timeline |
| `Action_None` | 410 | 521 | 112 | inferred_complete_timeline |
| `Action_None` | 526 | 540 | 15 | inferred_complete_timeline |
| `Action_None` | 568 | 569 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 9–548
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 292 | 284 | inferred_complete_timeline |
| `Action_None` | 293 | 390 | 98 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_None` | 402 | 404 | 3 | inferred_complete_timeline |
| `Action_None` | 406 | 516 | 111 | inferred_complete_timeline |
| `Action_None` | 520 | 527 | 8 | inferred_complete_timeline |
| `Action_None` | 547 | 548 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 9–321 | 313 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 330–336 | 7 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 347–392 | 32 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 376–569 | 194 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 398–569 | 158 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 402–408 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 403–470 | 62 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 409–503 | 80 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 412–519 | 95 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 423–424 | 2 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 436–529 | 39 | 5 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 444–522 | 74 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 482–509 | 23 | 3 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 511–512 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 512–514 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 519–526 | 8 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 551–554 | 4 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 553–569 | 17 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 554–555 | 2 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 565–567 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `19` (C): Annotated start 296 != Inferred start 307
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 123 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 332: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 126 frames exceeds threshold 90 frames [start=296, end=421].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 126 frames exceeds threshold 90 frames [start=296, end=421].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 126 frames exceeds threshold 90 frames [start=296, end=421].
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [293–306], lower_priority='Action_ZoneBlock' annotated_start=296, effective_Action_ZoneBlock_start=307.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 126 frames exceeds threshold 90 frames [start=296, end=421].
- ⚠️ Action 'Action_None' range [293-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-411] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-518] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-556] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-569] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-500] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-508] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-516] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-532] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-327] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-467] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-496] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-567] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-542] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-563] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-432] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-447] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-473] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-333] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-371] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-521] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-540] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-331] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-351] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-530] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-550] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-561] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-505] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-515] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-537] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-342] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-529] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [304-408] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-390] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-516] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-527] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-318] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-358] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-384] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-569] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-321] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-334] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-522] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-554] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [307-421] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-515] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-540] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-549] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-554] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-561] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-332] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-388] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-569] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-360] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-392] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-469] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-498] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-408] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-435] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-470] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-414] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-474] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-503] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-495] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-501] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-519] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-450] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-463] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-525] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-453] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-471] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-507] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-522] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-489] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-503] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-526] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-554] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-569] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>