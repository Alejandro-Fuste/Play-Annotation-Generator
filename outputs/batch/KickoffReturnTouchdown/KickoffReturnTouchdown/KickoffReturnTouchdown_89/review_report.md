# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_89

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_89`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 78
- **Ball Tracks:** 0
- **Action Segments:** 261
- **Validation Warnings:** 340
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 248
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `11` | `11` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `5` | `5` |
| ⚠️ START CHANGED | `Action_CrossGoalLine` | Kick_Returner2 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `10` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `13` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `16` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `11` | `11` | 40 | START | 40 | 115 |
| ✅ EXACT | `Action_KickBall` | Kicker | `11` | `11` | 116 | START | 116 | 122 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `5` | `5` | 234 | START | 234 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `5` | `5` | 256 | START | 256 | 523 |
| ⚠️ START CHANGED | `Action_CrossGoalLine` | Kick_Returner2 | `5` | `5` | 612 | START | 616 | 628 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–498
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_KickApproach` | 40 | 115 | 76 | inferred_complete_timeline |
| `Action_KickBall` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_None` | 123 | 498 | 376 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 110 | 71 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 131 | 151 | 21 | inferred_complete_timeline |
| `Action_None` | 154 | 170 | 17 | inferred_complete_timeline |
| `Action_None` | 173 | 194 | 22 | inferred_complete_timeline |
| `Action_None` | 199 | 212 | 14 | inferred_complete_timeline |
| `Action_None` | 218 | 350 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 280 | 241 | inferred_complete_timeline |
| `Action_None` | 284 | 342 | 59 | inferred_complete_timeline |
| `Action_None` | 359 | 417 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–432
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 127 | 88 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 171 | 34 | inferred_complete_timeline |
| `Action_None` | 174 | 195 | 22 | inferred_complete_timeline |
| `Action_None` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 223 | 234 | 12 | inferred_complete_timeline |
| `Action_None` | 236 | 248 | 13 | inferred_complete_timeline |
| `Action_None` | 250 | 302 | 53 | inferred_complete_timeline |
| `Action_None` | 308 | 432 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 111 | 72 | inferred_complete_timeline |
| `Action_None` | 113 | 122 | 10 | inferred_complete_timeline |
| `Action_None` | 125 | 247 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 280 | 241 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 629 | 590 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 334 | 295 | inferred_complete_timeline |
| `Action_None` | 344 | 629 | 286 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–422
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 341 | 302 | inferred_complete_timeline |
| `Action_None` | 343 | 422 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 293 | 254 | inferred_complete_timeline |
| `Action_None` | 297 | 629 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 255 | 216 | inferred_complete_timeline |
| `Action_None` | 258 | 560 | 303 | inferred_complete_timeline |
| `Action_None` | 562 | 626 | 65 | inferred_complete_timeline |
| `Action_None` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–530
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 352 | 313 | inferred_complete_timeline |
| `Action_None` | 355 | 357 | 3 | inferred_complete_timeline |
| `Action_None` | 362 | 530 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–365
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 365 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–441
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 441 | 402 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_CatchKick` | 234 | 242 | 9 | inferred_complete_timeline |
| `Action_None` | 243 | 255 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 523 | 268 | inferred_complete_timeline |
| `Action_BallCarry` | 526 | 532 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 536 | 538 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 543 | 546 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 548 | 552 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 556 | 578 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 580 | 594 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 597 | 603 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 607 | 608 | 2 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 616 | 628 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 574 | 535 | inferred_complete_timeline |
| `Action_None` | 576 | 629 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 303 | 264 | inferred_complete_timeline |
| `Action_None` | 306 | 629 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 300 | 261 | inferred_complete_timeline |
| `Action_None` | 303 | 614 | 312 | inferred_complete_timeline |
| `Action_None` | 616 | 629 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 572 | 533 | inferred_complete_timeline |
| `Action_None` | 580 | 581 | 2 | inferred_complete_timeline |
| `Action_None` | 583 | 629 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–190 | 171 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 2–533 | 526 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 3–149 | 109 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 14–273 | 211 | 11 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 66–80 | 9 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 95–356 | 233 | 11 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 103–465 | 352 | 8 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 114–254 | 122 | 7 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 119–187 | 14 | 6 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 129–135 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 200–209 | 10 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 201–406 | 80 | 15 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 232–234 | 3 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 245–249 | 5 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 264–629 | 319 | 6 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 306–453 | 143 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 309–339 | 4 | 2 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 362–534 | 171 | 2 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 363–629 | 253 | 2 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 398–403 | 6 | 1 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 423–430 | 8 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 431–497 | 67 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 435–459 | 12 | 3 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 447–473 | 27 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 449–559 | 35 | 7 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 476–477 | 2 | 1 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 477–492 | 14 | 2 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 481–629 | 122 | 8 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 483–489 | 7 | 1 | Undefined position; Undefined team |
| `51` | `73` | Position_Unknown | Team_Unknown | 485–489 | 5 | 1 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 486–487 | 2 | 1 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 493–559 | 49 | 4 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 500–512 | 11 | 2 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 502–570 | 53 | 9 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 511–514 | 4 | 1 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 512–554 | 42 | 2 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 516–549 | 34 | 1 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 518–527 | 8 | 2 | Undefined position; Undefined team |
| `60` | `91` | Position_Unknown | Team_Unknown | 523–546 | 21 | 3 | Undefined position; Undefined team |
| `61` | `92` | Position_Unknown | Team_Unknown | 526–531 | 6 | 1 | Undefined position; Undefined team |
| `62` | `93` | Position_Unknown | Team_Unknown | 526–534 | 9 | 1 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 531–555 | 13 | 4 | Undefined position; Undefined team |
| `64` | `97` | Position_Unknown | Team_Unknown | 532–629 | 98 | 1 | Undefined position; Undefined team |
| `65` | `98` | Position_Unknown | Team_Unknown | 533–540 | 8 | 1 | Undefined position; Undefined team |
| `66` | `99` | Position_Unknown | Team_Unknown | 534–535 | 2 | 1 | Undefined position; Undefined team |
| `67` | `101` | Position_Unknown | Team_Unknown | 535–536 | 2 | 1 | Undefined position; Undefined team |
| `68` | `109` | Position_Unknown | Team_Unknown | 545–629 | 85 | 1 | Undefined position; Undefined team |
| `69` | `111` | Position_Unknown | Team_Unknown | 546–568 | 16 | 2 | Undefined position; Undefined team |
| `70` | `113` | Position_Unknown | Team_Unknown | 549–568 | 19 | 2 | Undefined position; Undefined team |
| `71` | `114` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `72` | `122` | Position_Unknown | Team_Unknown | 585–629 | 45 | 1 | Undefined position; Undefined team |
| `73` | `123` | Position_Unknown | Team_Unknown | 587–629 | 40 | 3 | Undefined position; Undefined team |
| `74` | `125` | Position_Unknown | Team_Unknown | 592–629 | 34 | 3 | Undefined position; Undefined team |
| `75` | `127` | Position_Unknown | Team_Unknown | 596–602 | 7 | 1 | Undefined position; Undefined team |
| `76` | `128` | Position_Unknown | Team_Unknown | 603–605 | 3 | 1 | Undefined position; Undefined team |
| `77` | `131` | Position_Unknown | Team_Unknown | 622–629 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (10 segments found)
- ⚠️ `Action_CrossGoalLine` for actor_track_id `5` (Kick_Returner2): Annotated start 612 != Inferred start 616

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ 59 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 59 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 118 |
| Missing visible bounding boxes during action | 221 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [40-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-614] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-303] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-629] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-365] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-341] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-422] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-523] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [526-532] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [536-538] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [543-546] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [548-552] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [556-578] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [580-594] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [597-603] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [607-608] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-629] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-334] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-572] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-629] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-560] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-626] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-111] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-247] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-498] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-574] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-171] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-195] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-302] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-432] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-151] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-194] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-350] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-280] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-342] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-441] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-352] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-530] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-533] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-149] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-202] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-242] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-217] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-324] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-356] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-122] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-220] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-238] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-465] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-218] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-217] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-373] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-406] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-283] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-324] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-350] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-609] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-615] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-343] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-453] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-534] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-613] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-403] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-430] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-497] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-438] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-459] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-473] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-464] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-474] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-559] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-481] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-492] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-523] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-531] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-550] for track '49' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-567] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-584] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-629] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-489] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-489] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-497] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-513] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-559] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-508] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-508] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-518] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-550] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-559] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-570] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-514] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-554] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-549] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-520] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-527] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-542] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-531] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-534] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-555] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-540] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-559] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-560] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-568] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-615] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-619] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-602] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-620] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-602] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-605] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-629] for track '77' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.

</details>