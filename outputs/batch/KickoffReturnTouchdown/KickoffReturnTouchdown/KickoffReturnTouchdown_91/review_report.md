# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_91

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_91`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 252
- **Validation Warnings:** 307
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 238
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `42` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `42` | `25` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `42` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 16 | START | 16 | 67 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 68 | START | 68 | 72 |
| ❌ MISSING SEGMENT | `Action_CatchKick` | Position_Unknown | `42` | `25` | 183 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `42` | `25` | 206 | START | 214 | 356 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `42` | `25` | 588 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 67 | 52 | inferred_complete_timeline |
| `Action_KickBall` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_None` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 366 | 277 | inferred_complete_timeline |
| `Action_None` | 368 | 373 | 6 | inferred_complete_timeline |
| `Action_None` | 375 | 385 | 11 | inferred_complete_timeline |
| `Action_None` | 387 | 409 | 23 | inferred_complete_timeline |
| `Action_None` | 413 | 416 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–500
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 446 | 431 | inferred_complete_timeline |
| `Action_None` | 451 | 462 | 12 | inferred_complete_timeline |
| `Action_None` | 464 | 487 | 24 | inferred_complete_timeline |
| `Action_None` | 495 | 497 | 3 | inferred_complete_timeline |
| `Action_None` | 499 | 500 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 515 | 500 | inferred_complete_timeline |
| `Action_None` | 518 | 558 | 41 | inferred_complete_timeline |
| `Action_None` | 566 | 596 | 31 | inferred_complete_timeline |
| `Action_None` | 599 | 599 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 175 | 160 | inferred_complete_timeline |
| `Action_None` | 177 | 277 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 197 | 182 | inferred_complete_timeline |
| `Action_None` | 200 | 277 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 325 | 310 | inferred_complete_timeline |
| `Action_None` | 334 | 425 | 92 | inferred_complete_timeline |
| `Action_None` | 427 | 451 | 25 | inferred_complete_timeline |
| `Action_None` | 453 | 455 | 3 | inferred_complete_timeline |
| `Action_None` | 458 | 465 | 8 | inferred_complete_timeline |
| `Action_None` | 467 | 471 | 5 | inferred_complete_timeline |
| `Action_None` | 485 | 503 | 19 | inferred_complete_timeline |
| `Action_None` | 507 | 511 | 5 | inferred_complete_timeline |
| `Action_None` | 520 | 529 | 10 | inferred_complete_timeline |
| `Action_None` | 534 | 564 | 31 | inferred_complete_timeline |
| `Action_None` | 569 | 572 | 4 | inferred_complete_timeline |
| `Action_None` | 574 | 595 | 22 | inferred_complete_timeline |
| `Action_None` | 598 | 599 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 377 | 362 | inferred_complete_timeline |
| `Action_None` | 379 | 384 | 6 | inferred_complete_timeline |
| `Action_None` | 388 | 402 | 15 | inferred_complete_timeline |
| `Action_None` | 408 | 554 | 147 | inferred_complete_timeline |
| `Action_None` | 569 | 577 | 9 | inferred_complete_timeline |
| `Action_None` | 580 | 599 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–524
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 348 | 333 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 364 | 9 | inferred_complete_timeline |
| `Action_None` | 368 | 504 | 137 | inferred_complete_timeline |
| `Action_None` | 508 | 524 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 110 | 95 | inferred_complete_timeline |
| `Action_None` | 119 | 254 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 300 | 285 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 483 | 159 | inferred_complete_timeline |
| `Action_None` | 485 | 491 | 7 | inferred_complete_timeline |
| `Action_None` | 493 | 511 | 19 | inferred_complete_timeline |
| `Action_None` | 514 | 518 | 5 | inferred_complete_timeline |
| `Action_None` | 536 | 540 | 5 | inferred_complete_timeline |
| `Action_None` | 555 | 562 | 8 | inferred_complete_timeline |
| `Action_None` | 564 | 565 | 2 | inferred_complete_timeline |
| `Action_None` | 577 | 581 | 5 | inferred_complete_timeline |
| `Action_None` | 583 | 599 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 352 | 337 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 333 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 501 | 486 | inferred_complete_timeline |
| `Action_None` | 504 | 599 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–439
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 27 | 12 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 193 | 107 | inferred_complete_timeline |
| `Action_None` | 200 | 415 | 216 | inferred_complete_timeline |
| `Action_None` | 419 | 427 | 9 | inferred_complete_timeline |
| `Action_None` | 430 | 439 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 221 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 522

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 68 | 491 | 424 | inferred_complete_timeline |
| `Action_None` | 495 | 528 | 34 | inferred_complete_timeline |
| `Action_None` | 530 | 544 | 15 | inferred_complete_timeline |
| `Action_None` | 546 | 560 | 15 | inferred_complete_timeline |
| `Action_None` | 573 | 599 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 193 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–593
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 211 | 196 | inferred_complete_timeline |
| `Action_None` | 274 | 421 | 148 | inferred_complete_timeline |
| `Action_None` | 423 | 506 | 84 | inferred_complete_timeline |
| `Action_None` | 509 | 526 | 18 | inferred_complete_timeline |
| `Action_None` | 528 | 542 | 15 | inferred_complete_timeline |
| `Action_None` | 544 | 569 | 26 | inferred_complete_timeline |
| `Action_None` | 573 | 581 | 9 | inferred_complete_timeline |
| `Action_None` | 585 | 593 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–474
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 233 | 218 | inferred_complete_timeline |
| `Action_None` | 235 | 271 | 37 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |
| `Action_None` | 284 | 291 | 8 | inferred_complete_timeline |
| `Action_None` | 294 | 374 | 81 | inferred_complete_timeline |
| `Action_None` | 376 | 444 | 69 | inferred_complete_timeline |
| `Action_None` | 455 | 456 | 2 | inferred_complete_timeline |
| `Action_None` | 463 | 465 | 3 | inferred_complete_timeline |
| `Action_None` | 468 | 469 | 2 | inferred_complete_timeline |
| `Action_None` | 471 | 474 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–595
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 132 | 117 | inferred_complete_timeline |
| `Action_None` | 135 | 443 | 309 | inferred_complete_timeline |
| `Action_None` | 448 | 503 | 56 | inferred_complete_timeline |
| `Action_None` | 505 | 506 | 2 | inferred_complete_timeline |
| `Action_None` | 510 | 518 | 9 | inferred_complete_timeline |
| `Action_None` | 521 | 595 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 2–93 | 44 | 7 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 153–181 | 15 | 3 | Undefined position; Undefined team |
| `22` | `35` | Position_Unknown | Team_Unknown | 177–207 | 23 | 3 | Undefined position; Undefined team |
| `23` | `37` | Position_Unknown | Team_Unknown | 181–599 | 398 | 7 | Undefined position; Undefined team |
| `24` | `41` | Position_Unknown | Team_Unknown | 211–248 | 37 | 2 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 214–409 | 194 | 2 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 248–290 | 35 | 2 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 265–335 | 71 | 1 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 274–570 | 254 | 16 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 277–599 | 311 | 6 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 290–599 | 307 | 3 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 301–325 | 25 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 333–514 | 181 | 2 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 334–335 | 2 | 1 | Undefined position; Undefined team |
| `36` | `59` | Position_Unknown | Team_Unknown | 337–505 | 138 | 9 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 345–432 | 68 | 4 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 350–353 | 4 | 1 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 355–407 | 39 | 3 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 371–372 | 2 | 1 | Undefined position; Undefined team |
| `42` | `69` | Position_Unknown | Team_Unknown | 383–410 | 13 | 4 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 402–410 | 9 | 1 | Undefined position; Undefined team |
| `44` | `75` | Position_Unknown | Team_Unknown | 412–416 | 5 | 1 | Undefined position; Undefined team |
| `45` | `77` | Position_Unknown | Team_Unknown | 430–448 | 19 | 1 | Undefined position; Undefined team |
| `46` | `81` | Position_Unknown | Team_Unknown | 440–514 | 55 | 5 | Undefined position; Undefined team |
| `47` | `85` | Position_Unknown | Team_Unknown | 470–590 | 72 | 6 | Undefined position; Undefined team |
| `48` | `89` | Position_Unknown | Team_Unknown | 479–548 | 58 | 7 | Undefined position; Undefined team |
| `49` | `91` | Position_Unknown | Team_Unknown | 485–565 | 36 | 7 | Undefined position; Undefined team |
| `50` | `92` | Position_Unknown | Team_Unknown | 485–585 | 60 | 7 | Undefined position; Undefined team |
| `51` | `98` | Position_Unknown | Team_Unknown | 516–524 | 7 | 2 | Undefined position; Undefined team |
| `52` | `103` | Position_Unknown | Team_Unknown | 543–571 | 21 | 4 | Undefined position; Undefined team |
| `53` | `114` | Position_Unknown | Team_Unknown | 567–580 | 14 | 1 | Undefined position; Undefined team |
| `54` | `115` | Position_Unknown | Team_Unknown | 574–599 | 21 | 3 | Undefined position; Undefined team |
| `55` | `118` | Position_Unknown | Team_Unknown | 585–598 | 12 | 2 | Undefined position; Undefined team |
| `56` | `119` | Position_Unknown | Team_Unknown | 586–599 | 14 | 1 | Undefined position; Undefined team |
| `57` | `124` | Position_Unknown | Team_Unknown | 591–597 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CatchKick` on target `42` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `42` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `42` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 228 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '25' has invalid range: start=214, end=189. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '25' has invalid range: start=588, end=409. Clamping end to start.
- ⚠️ Action 'Action_None' range [16-348] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-364] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-504] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-524] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-377] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-402] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-554] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-577] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-599] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-325] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-425] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-451] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-465] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-471] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-503] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-529] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-564] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-572] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-595] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-515] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-558] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-596] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-175] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-277] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-446] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-462] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-487] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-352] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [16-67] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-366] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-385] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-409] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-300] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-483] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-491] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-511] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-518] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-540] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-562] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-581] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-197] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-277] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-110] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-254] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-211] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-421] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-506] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-526] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-542] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-569] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-581] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-593] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-132] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-443] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-503] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-518] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-595] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-501] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-599] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-333] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-221] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-193] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-193] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-415] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-427] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-439] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-271] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-374] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-444] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-465] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-491] for track '19' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-528] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-544] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-560] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-599] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-193] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-451] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-458] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-493] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-599] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-245] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-356] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [359-409] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-290] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-335] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-326] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-455] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-471] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-491] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-504] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-512] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-517] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-540] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-570] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-506] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-566] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-576] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-579] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-592] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-560] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-566] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-599] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-325] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-504] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-514] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-403] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-431] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-474] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-483] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-505] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-412] for track '37' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-386] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-410] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-410] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-416] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-448] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-449] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-470] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-485] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-500] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-514] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-480] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-484] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-517] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-536] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-590] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-499] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-523] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-538] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-548] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-491] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-513] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-522] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-534] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-538] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-565] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-495] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-547] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-585] for track '50' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-520] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-552] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-563] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-568] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-580] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-582] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-589] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-590] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-598] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-597] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.

</details>