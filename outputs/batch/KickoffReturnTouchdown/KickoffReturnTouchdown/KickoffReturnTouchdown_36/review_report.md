# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_36`
- **Frame Range:** 0 to 869 (870 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 869
- **Player Tracks:** 72
- **Ball Tracks:** 0
- **Action Segments:** 349
- **Validation Warnings:** 432
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 308
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `18` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Left_Coverage5 | offense | `16` | `16` |
| ✅ EXACT | `Action_KickBall` | Left_Coverage5 | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `34` | `30` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `30` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `34` | `30` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `10` | `Group` | 0 | START | 0 | 363 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `11` | `Group` | 0 | START | 0 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `17` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `18` | `Group` | 0 | START | 0 | 3 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Left_Coverage5 | `16` | `16` | 364 | START | 364 | 380 |
| ✅ EXACT | `Action_KickBall` | Left_Coverage5 | `16` | `16` | 402 | START | 402 | 403 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `34` | `30` | 506 | START | 506 | 511 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `34` | `30` | 523 | START | 523 | 598 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `34` | `30` | 838 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 139 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 154 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 122 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–840
- **Visible Samples:** 757

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 321 | 322 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 329 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 363 | 33 | inferred_complete_timeline |
| `Action_None` | 364 | 372 | 9 | inferred_complete_timeline |
| `Action_None` | 408 | 410 | 3 | inferred_complete_timeline |
| `Action_None` | 425 | 426 | 2 | inferred_complete_timeline |
| `Action_None` | 430 | 433 | 4 | inferred_complete_timeline |
| `Action_None` | 448 | 453 | 6 | inferred_complete_timeline |
| `Action_None` | 456 | 464 | 9 | inferred_complete_timeline |
| `Action_None` | 471 | 556 | 86 | inferred_complete_timeline |
| `Action_None` | 561 | 579 | 19 | inferred_complete_timeline |
| `Action_None` | 582 | 702 | 121 | inferred_complete_timeline |
| `Action_None` | 705 | 840 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–559
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 380 | 17 | inferred_complete_timeline |
| `Action_None` | 389 | 393 | 5 | inferred_complete_timeline |
| `Action_None` | 403 | 405 | 3 | inferred_complete_timeline |
| `Action_None` | 414 | 415 | 2 | inferred_complete_timeline |
| `Action_None` | 417 | 446 | 30 | inferred_complete_timeline |
| `Action_None` | 448 | 559 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–506
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 213 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 242 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 295 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 363 | 30 | inferred_complete_timeline |
| `Action_None` | 364 | 365 | 2 | inferred_complete_timeline |
| `Action_None` | 368 | 370 | 3 | inferred_complete_timeline |
| `Action_None` | 398 | 400 | 3 | inferred_complete_timeline |
| `Action_None` | 411 | 415 | 5 | inferred_complete_timeline |
| `Action_None` | 419 | 422 | 4 | inferred_complete_timeline |
| `Action_None` | 424 | 431 | 8 | inferred_complete_timeline |
| `Action_None` | 464 | 465 | 2 | inferred_complete_timeline |
| `Action_None` | 468 | 506 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–429
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 264 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 271 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 294 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 310 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 363 | 36 | inferred_complete_timeline |
| `Action_KickApproach` | 364 | 380 | 17 | inferred_complete_timeline |
| `Action_KickApproach` | 382 | 385 | 4 | inferred_complete_timeline |
| `Action_KickBall` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 428 | 429 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 42 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 203 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 238 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–501
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 158 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 203 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 363 | 159 | inferred_complete_timeline |
| `Action_None` | 364 | 375 | 12 | inferred_complete_timeline |
| `Action_None` | 429 | 431 | 3 | inferred_complete_timeline |
| `Action_None` | 437 | 438 | 2 | inferred_complete_timeline |
| `Action_None` | 470 | 486 | 17 | inferred_complete_timeline |
| `Action_None` | 488 | 489 | 2 | inferred_complete_timeline |
| `Action_None` | 498 | 501 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–869
- **Visible Samples:** 826

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 543 | 180 | inferred_complete_timeline |
| `Action_None` | 546 | 603 | 58 | inferred_complete_timeline |
| `Action_None` | 605 | 611 | 7 | inferred_complete_timeline |
| `Action_None` | 613 | 772 | 160 | inferred_complete_timeline |
| `Action_None` | 813 | 869 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–541
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 491 | 128 | inferred_complete_timeline |
| `Action_None` | 493 | 528 | 36 | inferred_complete_timeline |
| `Action_None` | 531 | 541 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–493
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 426 | 63 | inferred_complete_timeline |
| `Action_None` | 436 | 493 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–579
- **Visible Samples:** 576

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 441 | 78 | inferred_complete_timeline |
| `Action_None` | 446 | 579 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–554
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 439 | 76 | inferred_complete_timeline |
| `Action_None` | 456 | 459 | 4 | inferred_complete_timeline |
| `Action_None` | 461 | 467 | 7 | inferred_complete_timeline |
| `Action_None` | 471 | 477 | 7 | inferred_complete_timeline |
| `Action_None` | 480 | 495 | 16 | inferred_complete_timeline |
| `Action_None` | 498 | 554 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 144 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–869
- **Visible Samples:** 859

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 582 | 219 | inferred_complete_timeline |
| `Action_None` | 592 | 642 | 51 | inferred_complete_timeline |
| `Action_None` | 645 | 869 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–651
- **Visible Samples:** 647

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 459 | 96 | inferred_complete_timeline |
| `Action_None` | 463 | 537 | 75 | inferred_complete_timeline |
| `Action_None` | 539 | 581 | 43 | inferred_complete_timeline |
| `Action_None` | 583 | 651 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–724
- **Visible Samples:** 682

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 453 | 90 | inferred_complete_timeline |
| `Action_None` | 456 | 564 | 109 | inferred_complete_timeline |
| `Action_None` | 600 | 680 | 81 | inferred_complete_timeline |
| `Action_None` | 682 | 690 | 9 | inferred_complete_timeline |
| `Action_None` | 695 | 698 | 4 | inferred_complete_timeline |
| `Action_None` | 700 | 724 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 417 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–510
- **Visible Samples:** 505

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_None` | 364 | 452 | 89 | inferred_complete_timeline |
| `Action_None` | 454 | 502 | 49 | inferred_complete_timeline |
| `Action_None` | 508 | 510 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 2–441 | 388 | 10 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 42–491 | 412 | 11 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 54–162 | 14 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 164–195 | 32 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 229–845 | 459 | 20 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 344–362 | 17 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 363–370 | 8 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 422–869 | 415 | 7 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 428–842 | 385 | 6 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 429–430 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 432–477 | 42 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 442–598 | 157 | 4 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 453–682 | 197 | 7 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 459–695 | 200 | 10 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 469–475 | 6 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 477–586 | 92 | 4 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 499–612 | 75 | 4 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 507–700 | 193 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 514–584 | 49 | 6 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 516–577 | 60 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 518–812 | 236 | 12 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 519–601 | 74 | 4 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 537–538 | 2 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 543–693 | 141 | 5 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 548–867 | 264 | 11 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 565–611 | 47 | 1 | Undefined position; Undefined team |
| `45` | `57` | Position_Unknown | Team_Unknown | 570–582 | 12 | 2 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 593–869 | 277 | 1 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 594–597 | 4 | 1 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 596–725 | 124 | 5 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 598–869 | 255 | 3 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 613–614 | 2 | 1 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 628–869 | 176 | 4 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 630–783 | 82 | 14 | Undefined position; Undefined team |
| `53` | `66` | Position_Unknown | Team_Unknown | 638–864 | 191 | 6 | Undefined position; Undefined team |
| `54` | `67` | Position_Unknown | Team_Unknown | 647–687 | 8 | 4 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 660–665 | 6 | 1 | Undefined position; Undefined team |
| `56` | `74` | Position_Unknown | Team_Unknown | 684–869 | 156 | 5 | Undefined position; Undefined team |
| `57` | `75` | Position_Unknown | Team_Unknown | 689–869 | 165 | 5 | Undefined position; Undefined team |
| `58` | `76` | Position_Unknown | Team_Unknown | 694–784 | 19 | 2 | Undefined position; Undefined team |
| `59` | `77` | Position_Unknown | Team_Unknown | 697–869 | 158 | 4 | Undefined position; Undefined team |
| `60` | `78` | Position_Unknown | Team_Unknown | 709–787 | 63 | 6 | Undefined position; Undefined team |
| `61` | `82` | Position_Unknown | Team_Unknown | 736–750 | 10 | 2 | Undefined position; Undefined team |
| `62` | `83` | Position_Unknown | Team_Unknown | 754–790 | 36 | 2 | Undefined position; Undefined team |
| `63` | `84` | Position_Unknown | Team_Unknown | 763–858 | 55 | 5 | Undefined position; Undefined team |
| `64` | `85` | Position_Unknown | Team_Unknown | 763–848 | 77 | 2 | Undefined position; Undefined team |
| `65` | `86` | Position_Unknown | Team_Unknown | 766–788 | 19 | 3 | Undefined position; Undefined team |
| `66` | `87` | Position_Unknown | Team_Unknown | 782–811 | 8 | 3 | Undefined position; Undefined team |
| `67` | `91` | Position_Unknown | Team_Unknown | 809–825 | 11 | 3 | Undefined position; Undefined team |
| `68` | `92` | Position_Unknown | Team_Unknown | 811–869 | 55 | 3 | Undefined position; Undefined team |
| `69` | `94` | Position_Unknown | Team_Unknown | 815–869 | 55 | 1 | Undefined position; Undefined team |
| `70` | `99` | Position_Unknown | Team_Unknown | 840–842 | 3 | 1 | Undefined position; Undefined team |
| `71` | `100` | Position_Unknown | Team_Unknown | 845–869 | 25 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `16` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `34` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kicker` position mapped to `offense` team
- ⚠️ 53 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 53 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 106 |
| Missing visible bounding boxes during action | 324 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 869 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '30' has invalid range: start=838, end=598. Clamping end to start.
- ⚠️ Action 'Action_None' range [364-417] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-459] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-537] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-581] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-651] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-582] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-642] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-491] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-528] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-541] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-453] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-564] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-680] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-690] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [695-698] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-724] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-452] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-502] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-439] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-467] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-477] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-495] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-554] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-543] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-603] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-611] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-772] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [813-869] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-426] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-493] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-380] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-393] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-405] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-446] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-559] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-321] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-363] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-372] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-453] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-464] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-556] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-579] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-702] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [705-840] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-375] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-486] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-501] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-441] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-579] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-431] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-506] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-55] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-203] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-238] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-271] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-318] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [364-380] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [382-385] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [402-403] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-139] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-62] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-376] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-421] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-433] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-363] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-461] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-474] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-284] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-332] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-372] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-424] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-446] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-556] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-640] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-646] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-655] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-672] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [674-679] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-687] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [691-706] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-709] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-712] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-722] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-845] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-348] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-362] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-370] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-560] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-654] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-709] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-784] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [790-813] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [825-826] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [828-869] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-476] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-489] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-566] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-842] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-442] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-477] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [523-598] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-465] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-597] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-647] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-653] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-682] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-544] for track '32' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-550] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-564] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-678] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-690] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-695] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-482] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-546] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-554] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-586] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-557] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-602] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-612] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-619] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-700] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-517] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-532] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-541] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-567] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-580] for track '37' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-538] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-577] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-532] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-551] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-580] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-674] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-707] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-753] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [755-778] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [780-805] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [807-812] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-529] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-575] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-587] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-601] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-538] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-612] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-625] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-637] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-690] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-693] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-603] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-625] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-630] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-669] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-711] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-729] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-749] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [775-777] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [779-812] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [825-867] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-611] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-582] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-869] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-597] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-701] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-704] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-712] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [714-719] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-725] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-780] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [793-858] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-656] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-782] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [785-789] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-634] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-673] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-678] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [680-682] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-690] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-693] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [701-702] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-713] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [727-728] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [731-733] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-743] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [750-753] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [767-769] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [779-783] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-702] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-733] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [740-797] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [799-800] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [808-827] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [837-864] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-648] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-679] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-683] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-687] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [660-665] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [696-697] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-710] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-717] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [722-869] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [689-715] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [718-730] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-755] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [761-762] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [767-869] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-695] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [768-784] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [697-713] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-730] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [742-750] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-713] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-718] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-722] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [724-725] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-742] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [748-787] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [736-743] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [749-750] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [754-769] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [771-790] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [763-765] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [772-782] for track '63' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [799-800] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [819-852] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [854-858] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [763-825] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [835-848] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [766-776] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [779-783] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [786-788] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [782-783] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [789-792] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [810-811] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [809-813] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [818-819] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [822-825] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [811-813] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [816-817] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [820-869] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [840-842] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.

</details>