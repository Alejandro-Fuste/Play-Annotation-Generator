# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_70

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_70`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 258
- **Validation Warnings:** 301
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 241
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `19` | `19` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `19` | `19` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `25` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `25` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `43` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `13` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `18` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `19` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `2` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `9` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `19` | `19` | 42 | START | 42 | 88 |
| ✅ EXACT | `Action_KickBall` | Kicker | `19` | `19` | 89 | START | 89 | 94 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `25` | `21` | 212 | START | 212 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `25` | `21` | 241 | START | 241 | 376 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `43` | `29` | 614 | START | 614 | 622 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–510
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 41 | 13 | inferred_complete_timeline |
| `Action_KickApproach` | 42 | 88 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_None` | 95 | 154 | 60 | inferred_complete_timeline |
| `Action_None` | 158 | 424 | 267 | inferred_complete_timeline |
| `Action_None` | 426 | 448 | 23 | inferred_complete_timeline |
| `Action_None` | 450 | 451 | 2 | inferred_complete_timeline |
| `Action_None` | 455 | 510 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–380
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 348 | 307 | inferred_complete_timeline |
| `Action_None` | 356 | 380 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 137 | 96 | inferred_complete_timeline |
| `Action_None` | 140 | 255 | 116 | inferred_complete_timeline |
| `Action_None` | 258 | 308 | 51 | inferred_complete_timeline |
| `Action_None` | 311 | 387 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 114 | 73 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–627
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 344 | 303 | inferred_complete_timeline |
| `Action_None` | 348 | 370 | 23 | inferred_complete_timeline |
| `Action_None` | 376 | 394 | 19 | inferred_complete_timeline |
| `Action_None` | 396 | 427 | 32 | inferred_complete_timeline |
| `Action_None` | 449 | 627 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 179 | 138 | inferred_complete_timeline |
| `Action_None` | 182 | 255 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 267 | 226 | inferred_complete_timeline |
| `Action_None` | 270 | 389 | 120 | inferred_complete_timeline |
| `Action_None` | 391 | 409 | 19 | inferred_complete_timeline |
| `Action_None` | 420 | 582 | 163 | inferred_complete_timeline |
| `Action_None` | 600 | 629 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–616
- **Visible Samples:** 545

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 299 | 258 | inferred_complete_timeline |
| `Action_None` | 303 | 411 | 109 | inferred_complete_timeline |
| `Action_None` | 416 | 422 | 7 | inferred_complete_timeline |
| `Action_None` | 425 | 426 | 2 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_None` | 435 | 452 | 18 | inferred_complete_timeline |
| `Action_None` | 455 | 470 | 16 | inferred_complete_timeline |
| `Action_None` | 486 | 525 | 40 | inferred_complete_timeline |
| `Action_None` | 554 | 555 | 2 | inferred_complete_timeline |
| `Action_None` | 558 | 587 | 30 | inferred_complete_timeline |
| `Action_None` | 590 | 598 | 9 | inferred_complete_timeline |
| `Action_None` | 601 | 606 | 6 | inferred_complete_timeline |
| `Action_None` | 613 | 616 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–364
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 148 | 107 | inferred_complete_timeline |
| `Action_None` | 150 | 164 | 15 | inferred_complete_timeline |
| `Action_None` | 168 | 356 | 189 | inferred_complete_timeline |
| `Action_None` | 361 | 364 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 490 | 449 | inferred_complete_timeline |
| `Action_None` | 492 | 519 | 28 | inferred_complete_timeline |
| `Action_None` | 522 | 535 | 14 | inferred_complete_timeline |
| `Action_None` | 538 | 539 | 2 | inferred_complete_timeline |
| `Action_None` | 548 | 551 | 4 | inferred_complete_timeline |
| `Action_None` | 553 | 554 | 2 | inferred_complete_timeline |
| `Action_None` | 561 | 563 | 3 | inferred_complete_timeline |
| `Action_None` | 567 | 571 | 5 | inferred_complete_timeline |
| `Action_None` | 575 | 576 | 2 | inferred_complete_timeline |
| `Action_None` | 580 | 581 | 2 | inferred_complete_timeline |
| `Action_None` | 584 | 588 | 5 | inferred_complete_timeline |
| `Action_None` | 593 | 602 | 10 | inferred_complete_timeline |
| `Action_None` | 612 | 617 | 6 | inferred_complete_timeline |
| `Action_None` | 620 | 621 | 2 | inferred_complete_timeline |
| `Action_None` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 59 | 78 | 20 | inferred_complete_timeline |
| `Action_None` | 80 | 416 | 337 | inferred_complete_timeline |
| `Action_None` | 424 | 426 | 3 | inferred_complete_timeline |
| `Action_None` | 453 | 553 | 101 | inferred_complete_timeline |
| `Action_None` | 563 | 569 | 7 | inferred_complete_timeline |
| `Action_None` | 571 | 574 | 4 | inferred_complete_timeline |
| `Action_None` | 580 | 583 | 4 | inferred_complete_timeline |
| `Action_None` | 599 | 601 | 3 | inferred_complete_timeline |
| `Action_None` | 607 | 613 | 7 | inferred_complete_timeline |
| `Action_None` | 615 | 629 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 198 | 157 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–558
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 348 | 307 | inferred_complete_timeline |
| `Action_None` | 364 | 463 | 100 | inferred_complete_timeline |
| `Action_None` | 475 | 540 | 66 | inferred_complete_timeline |
| `Action_None` | 543 | 545 | 3 | inferred_complete_timeline |
| `Action_None` | 551 | 552 | 2 | inferred_complete_timeline |
| `Action_None` | 554 | 558 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 173 | 132 | inferred_complete_timeline |
| `Action_None` | 206 | 219 | 14 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 241 | 14 | inferred_complete_timeline |
| `Action_None` | 243 | 263 | 21 | inferred_complete_timeline |
| `Action_None` | 266 | 270 | 5 | inferred_complete_timeline |
| `Action_None` | 277 | 301 | 25 | inferred_complete_timeline |
| `Action_None` | 305 | 309 | 5 | inferred_complete_timeline |
| `Action_None` | 311 | 312 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_None` | 329 | 629 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–615
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 265 | 224 | inferred_complete_timeline |
| `Action_None` | 267 | 440 | 174 | inferred_complete_timeline |
| `Action_None` | 444 | 445 | 2 | inferred_complete_timeline |
| `Action_None` | 449 | 450 | 2 | inferred_complete_timeline |
| `Action_None` | 465 | 525 | 61 | inferred_complete_timeline |
| `Action_None` | 528 | 529 | 2 | inferred_complete_timeline |
| `Action_None` | 536 | 615 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–303
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 124 | 83 | inferred_complete_timeline |
| `Action_None` | 130 | 146 | 17 | inferred_complete_timeline |
| `Action_None` | 148 | 220 | 73 | inferred_complete_timeline |
| `Action_None` | 234 | 263 | 30 | inferred_complete_timeline |
| `Action_None` | 275 | 278 | 4 | inferred_complete_timeline |
| `Action_None` | 282 | 285 | 4 | inferred_complete_timeline |
| `Action_None` | 302 | 303 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 203 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 124 | 83 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 378 | 235 | inferred_complete_timeline |
| `Action_None` | 386 | 414 | 29 | inferred_complete_timeline |
| `Action_None` | 417 | 425 | 9 | inferred_complete_timeline |
| `Action_None` | 429 | 430 | 2 | inferred_complete_timeline |
| `Action_None` | 432 | 555 | 124 | inferred_complete_timeline |
| `Action_None` | 563 | 565 | 3 | inferred_complete_timeline |
| `Action_None` | 589 | 591 | 3 | inferred_complete_timeline |
| `Action_None` | 593 | 604 | 12 | inferred_complete_timeline |
| `Action_None` | 609 | 622 | 14 | inferred_complete_timeline |
| `Action_None` | 624 | 629 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 508 | 467 | inferred_complete_timeline |
| `Action_None` | 510 | 527 | 18 | inferred_complete_timeline |
| `Action_None` | 530 | 544 | 15 | inferred_complete_timeline |
| `Action_None` | 548 | 556 | 9 | inferred_complete_timeline |
| `Action_None` | 559 | 623 | 65 | inferred_complete_timeline |
| `Action_None` | 626 | 629 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 284 | 243 | inferred_complete_timeline |
| `Action_None` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_None` | 292 | 315 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 4–437 | 405 | 9 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 168–393 | 223 | 6 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 215–333 | 113 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 234–402 | 145 | 8 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 246–629 | 382 | 3 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 294–380 | 79 | 4 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 303–504 | 199 | 3 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 327–391 | 57 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 338–414 | 28 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 376–629 | 242 | 8 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 395–464 | 70 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 402–629 | 196 | 5 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 409–623 | 215 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 424–554 | 113 | 5 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 448–606 | 159 | 1 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 452–606 | 155 | 1 | Undefined position; Undefined team |
| `36` | `58` | Position_Unknown | Team_Unknown | 453–543 | 28 | 7 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 456–479 | 18 | 2 | Undefined position; Undefined team |
| `38` | `66` | Position_Unknown | Team_Unknown | 482–486 | 5 | 1 | Undefined position; Undefined team |
| `39` | `67` | Position_Unknown | Team_Unknown | 482–608 | 121 | 5 | Undefined position; Undefined team |
| `40` | `68` | Position_Unknown | Team_Unknown | 487–516 | 30 | 1 | Undefined position; Undefined team |
| `41` | `72` | Position_Unknown | Team_Unknown | 499–500 | 2 | 1 | Undefined position; Undefined team |
| `42` | `74` | Position_Unknown | Team_Unknown | 503–505 | 3 | 1 | Undefined position; Undefined team |
| `43` | `75` | Position_Unknown | Team_Unknown | 504–626 | 108 | 4 | Undefined position; Undefined team |
| `44` | `76` | Position_Unknown | Team_Unknown | 506–507 | 2 | 1 | Undefined position; Undefined team |
| `45` | `77` | Position_Unknown | Team_Unknown | 509–576 | 40 | 6 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 515–516 | 2 | 1 | Undefined position; Undefined team |
| `47` | `79` | Position_Unknown | Team_Unknown | 519–521 | 3 | 1 | Undefined position; Undefined team |
| `48` | `80` | Position_Unknown | Team_Unknown | 527–574 | 47 | 2 | Undefined position; Undefined team |
| `49` | `83` | Position_Unknown | Team_Unknown | 581–586 | 6 | 1 | Undefined position; Undefined team |
| `50` | `84` | Position_Unknown | Team_Unknown | 585–611 | 8 | 3 | Undefined position; Undefined team |
| `51` | `85` | Position_Unknown | Team_Unknown | 586–613 | 12 | 4 | Undefined position; Undefined team |
| `52` | `86` | Position_Unknown | Team_Unknown | 590–613 | 20 | 2 | Undefined position; Undefined team |
| `53` | `87` | Position_Unknown | Team_Unknown | 592–599 | 4 | 2 | Undefined position; Undefined team |
| `54` | `89` | Position_Unknown | Team_Unknown | 600–611 | 12 | 1 | Undefined position; Undefined team |
| `55` | `91` | Position_Unknown | Team_Unknown | 610–622 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `25` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kicker` position mapped to `offense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 228 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [42-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-380] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-299] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-411] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-422] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-452] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-470] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-525] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-587] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-598] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-606] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-616] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-315] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-490] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-519] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-535] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-551] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-571] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-602] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-617] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-621] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-356] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-364] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-508] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-527] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-544] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-556] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-623] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-629] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-239] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-78] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-416] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-553] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-574] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-583] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-601] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-613] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-629] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-255] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-308] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-241] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-263] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-301] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-348] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-463] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-540] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-558] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-344] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-370] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-394] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-427] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-627] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-267] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-389] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-409] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-582] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-629] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-265] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-440] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-525] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-615] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-198] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-124] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-378] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-414] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-425] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-555] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-591] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-604] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-622] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-179] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-424] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-448] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-510] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-137] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-408] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-430] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-376] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [378-388] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [391-393] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-315] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-338] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-358] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-402] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-514] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-564] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-629] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-368] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-388] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-477] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-504] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-391] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-363] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-534] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-558] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-564] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [566-567] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [574-578] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [581-613] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-464] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-421] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-516] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-547] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-629] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-623] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-520] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-606] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-606] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-456] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-474] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-499] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-464] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-479] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-518] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-530] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-536] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-588] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-608] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-516] for track '40' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-526] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-611] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-615] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-626] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-520] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-545] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-555] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-566] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-576] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-542] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-574] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-586] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-611] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-596] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-607] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-613] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-607] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-593] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-599] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-611] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-618] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-622] for track '55' has 1 frames without a visible bounding box.
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

</details>