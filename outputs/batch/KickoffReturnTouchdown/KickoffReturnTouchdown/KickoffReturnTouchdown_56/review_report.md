# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_56`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 61
- **Ball Tracks:** 0
- **Action Segments:** 217
- **Validation Warnings:** 261
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
- **Inferred Coverage Segments (Action_None):** 201
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `0` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `1` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `11` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `14` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `19` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `2` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `3` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `6` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `9` | `Group` | 0 | START | 0 | 116 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 117 | START | 117 | 170 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 171 | START | 171 | 176 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `21` | `21` | 278 | START | 278 | 288 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `21` | `21` | 313 | START | 313 | 613 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner2 | `21` | `21` | 614 | START | 614 | 621 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–431
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_KickApproach` | 117 | 170 | 54 | inferred_complete_timeline |
| `Action_KickBall` | 171 | 176 | 6 | inferred_complete_timeline |
| `Action_None` | 177 | 420 | 244 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |
| `Action_None` | 428 | 431 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 210 | 94 | inferred_complete_timeline |
| `Action_None` | 213 | 224 | 12 | inferred_complete_timeline |
| `Action_None` | 228 | 629 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 208 | 92 | inferred_complete_timeline |
| `Action_None` | 210 | 218 | 9 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 265 | 149 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 275 | 411 | 137 | inferred_complete_timeline |
| `Action_None` | 420 | 620 | 201 | inferred_complete_timeline |
| `Action_None` | 624 | 625 | 2 | inferred_complete_timeline |
| `Action_None` | 627 | 629 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 317 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 629 | 513 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 335 | 219 | inferred_complete_timeline |
| `Action_None` | 338 | 359 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 465 | 349 | inferred_complete_timeline |
| `Action_None` | 469 | 579 | 111 | inferred_complete_timeline |
| `Action_None` | 581 | 583 | 3 | inferred_complete_timeline |
| `Action_None` | 586 | 589 | 4 | inferred_complete_timeline |
| `Action_None` | 596 | 629 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 353 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 190 | 74 | inferred_complete_timeline |
| `Action_None` | 192 | 292 | 101 | inferred_complete_timeline |
| `Action_None` | 299 | 395 | 97 | inferred_complete_timeline |
| `Action_None` | 397 | 486 | 90 | inferred_complete_timeline |
| `Action_None` | 489 | 629 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 247 | 131 | inferred_complete_timeline |
| `Action_None` | 249 | 336 | 88 | inferred_complete_timeline |
| `Action_None` | 344 | 346 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 284 | 168 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–541
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 328 | 212 | inferred_complete_timeline |
| `Action_None` | 334 | 514 | 181 | inferred_complete_timeline |
| `Action_None` | 516 | 537 | 22 | inferred_complete_timeline |
| `Action_None` | 540 | 541 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–562
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 313 | 197 | inferred_complete_timeline |
| `Action_None` | 317 | 562 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 116 | 40 | inferred_complete_timeline |
| `Action_None` | 117 | 482 | 366 | inferred_complete_timeline |
| `Action_None` | 486 | 490 | 5 | inferred_complete_timeline |
| `Action_None` | 494 | 495 | 2 | inferred_complete_timeline |
| `Action_None` | 517 | 629 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 296 | 180 | inferred_complete_timeline |
| `Action_None` | 298 | 317 | 20 | inferred_complete_timeline |
| `Action_None` | 326 | 410 | 85 | inferred_complete_timeline |
| `Action_None` | 412 | 629 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–369
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 369 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–628
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 277 | 257 | inferred_complete_timeline |
| `Action_CatchKick` | 278 | 288 | 11 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_None` | 296 | 312 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 313 | 613 | 301 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 614 | 621 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 626 | 628 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 372 | 256 | inferred_complete_timeline |
| `Action_None` | 374 | 378 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 490 | 374 | inferred_complete_timeline |
| `Action_None` | 494 | 515 | 22 | inferred_complete_timeline |
| `Action_None` | 517 | 518 | 2 | inferred_complete_timeline |
| `Action_None` | 522 | 523 | 2 | inferred_complete_timeline |
| `Action_None` | 526 | 527 | 2 | inferred_complete_timeline |
| `Action_None` | 539 | 573 | 35 | inferred_complete_timeline |
| `Action_None` | 584 | 610 | 27 | inferred_complete_timeline |
| `Action_None` | 612 | 629 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 259 | 143 | inferred_complete_timeline |
| `Action_None` | 263 | 309 | 47 | inferred_complete_timeline |
| `Action_None` | 314 | 316 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–500
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 296 | 180 | inferred_complete_timeline |
| `Action_None` | 298 | 500 | 203 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 255–393 | 133 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 312–402 | 72 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 329–629 | 299 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 347–629 | 262 | 6 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 353–508 | 156 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 377–629 | 243 | 7 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 378–472 | 93 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 386–511 | 126 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 391–575 | 145 | 8 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 400–629 | 176 | 9 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 413–429 | 9 | 3 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 424–440 | 15 | 2 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 438–588 | 139 | 9 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 439–481 | 14 | 4 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 440–571 | 38 | 9 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 442–444 | 3 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 444–445 | 2 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 446–447 | 2 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 454–629 | 146 | 5 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 457–459 | 3 | 1 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 460–629 | 170 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 472–623 | 139 | 2 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 492–535 | 42 | 2 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 492–617 | 116 | 3 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 499–604 | 52 | 3 | Undefined position; Undefined team |
| `47` | `59` | Position_Unknown | Team_Unknown | 515–601 | 47 | 6 | Undefined position; Undefined team |
| `48` | `60` | Position_Unknown | Team_Unknown | 519–583 | 35 | 3 | Undefined position; Undefined team |
| `49` | `61` | Position_Unknown | Team_Unknown | 557–565 | 6 | 2 | Undefined position; Undefined team |
| `50` | `62` | Position_Unknown | Team_Unknown | 559–629 | 65 | 3 | Undefined position; Undefined team |
| `51` | `63` | Position_Unknown | Team_Unknown | 569–570 | 2 | 1 | Undefined position; Undefined team |
| `52` | `67` | Position_Unknown | Team_Unknown | 578–629 | 52 | 1 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 585–588 | 4 | 1 | Undefined position; Undefined team |
| `54` | `70` | Position_Unknown | Team_Unknown | 588–625 | 38 | 1 | Undefined position; Undefined team |
| `55` | `73` | Position_Unknown | Team_Unknown | 603–604 | 2 | 1 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 611–629 | 18 | 2 | Undefined position; Undefined team |
| `57` | `77` | Position_Unknown | Team_Unknown | 611–619 | 7 | 2 | Undefined position; Undefined team |
| `58` | `79` | Position_Unknown | Team_Unknown | 615–629 | 15 | 1 | Undefined position; Undefined team |
| `59` | `80` | Position_Unknown | Team_Unknown | 616–629 | 11 | 2 | Undefined position; Undefined team |
| `60` | `81` | Position_Unknown | Team_Unknown | 624–629 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 182 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [117-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-218] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-336] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-411] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-620] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-490] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-515] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-573] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-610] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-482] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-490] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-335] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-359] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-465] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-579] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-589] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-372] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-629] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-309] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-317] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-500] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-395] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-486] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-629] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-420] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-431] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-313] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-562] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-296] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-410] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-328] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-514] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-537] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-629] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-369] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-277] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-613] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [614-621] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [626-628] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-290] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-344] for track '22' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-393] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-365] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-543] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-629] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-392] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-451] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-470] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-523] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-629] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-508] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-410] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-470] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-496] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-523] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-542] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-629] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-467] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-511] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-403] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-480] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-488] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-512] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-575] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-416] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-463] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-469] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-557] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-578] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-612] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-621] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-429] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-429] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-440] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-449] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-460] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-472] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-553] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-564] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-575] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-582] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-445] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-477] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-523] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-571] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-444] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-473] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-490] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-525] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-629] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-607] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-623] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-531] for track '44' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-503] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-607] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-541] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-604] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-541] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-592] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-601] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-548] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-583] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-560] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-577] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-629] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-625] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-604] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-621] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-614] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-619] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-629] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-621] for track '59' has 1 frames without a visible bounding box.
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

</details>