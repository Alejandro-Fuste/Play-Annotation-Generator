# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_98`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 66
- **Ball Tracks:** 0
- **Action Segments:** 221
- **Validation Warnings:** 276
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 205
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | defense | `15` | `15` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `34` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `4` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `1` | `1` | 17 | START | 17 | 69 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 42 | END | 42 | 42 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 70 | START | 70 | 83 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `15` | `15` | 206 | START | 206 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | `15` | `15` | 232 | START | 232 | 265 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `34` | `27` | 616 | START | 616 | 623 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 52 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 80 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–488
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 235 | 219 | inferred_complete_timeline |
| `Action_None` | 249 | 391 | 143 | inferred_complete_timeline |
| `Action_None` | 393 | 416 | 24 | inferred_complete_timeline |
| `Action_None` | 420 | 474 | 55 | inferred_complete_timeline |
| `Action_None` | 476 | 488 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_LongSnap` | 17 | 69 | 53 | inferred_complete_timeline |
| `Action_None` | 70 | 250 | 181 | inferred_complete_timeline |
| `Action_None` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 134 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 104 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 626

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 474 | 458 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 593 | 115 | inferred_complete_timeline |
| `Action_None` | 596 | 629 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 69 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 83 | 14 | inferred_complete_timeline |
| `Action_None` | 84 | 94 | 11 | inferred_complete_timeline |
| `Action_None` | 99 | 451 | 353 | inferred_complete_timeline |
| `Action_None` | 453 | 629 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 370 | 354 | inferred_complete_timeline |
| `Action_None` | 375 | 459 | 85 | inferred_complete_timeline |
| `Action_None` | 462 | 602 | 141 | inferred_complete_timeline |
| `Action_None` | 606 | 607 | 2 | inferred_complete_timeline |
| `Action_None` | 613 | 619 | 7 | inferred_complete_timeline |
| `Action_None` | 624 | 629 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–491
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 163 | 147 | inferred_complete_timeline |
| `Action_None` | 175 | 231 | 57 | inferred_complete_timeline |
| `Action_None` | 235 | 260 | 26 | inferred_complete_timeline |
| `Action_None` | 265 | 272 | 8 | inferred_complete_timeline |
| `Action_None` | 274 | 286 | 13 | inferred_complete_timeline |
| `Action_None` | 288 | 292 | 5 | inferred_complete_timeline |
| `Action_None` | 294 | 300 | 7 | inferred_complete_timeline |
| `Action_None` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_None` | 319 | 338 | 20 | inferred_complete_timeline |
| `Action_None` | 341 | 342 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 384 | 40 | inferred_complete_timeline |
| `Action_None` | 386 | 491 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–406
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 370 | 354 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 385 | 400 | 16 | inferred_complete_timeline |
| `Action_None` | 405 | 406 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 53 | 37 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 27 | 11 | inferred_complete_timeline |
| `Action_None` | 29 | 103 | 75 | inferred_complete_timeline |
| `Action_None` | 105 | 258 | 154 | inferred_complete_timeline |
| `Action_None` | 268 | 319 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–500
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 62 | 46 | inferred_complete_timeline |
| `Action_None` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 115 | 31 | inferred_complete_timeline |
| `Action_None` | 117 | 381 | 265 | inferred_complete_timeline |
| `Action_None` | 387 | 500 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 37 | 21 | inferred_complete_timeline |
| `Action_None` | 41 | 79 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 484 | 468 | inferred_complete_timeline |
| `Action_None` | 486 | 629 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–373
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 249 | 233 | inferred_complete_timeline |
| `Action_None` | 253 | 373 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_CatchPunt` | 206 | 213 | 8 | inferred_complete_timeline |
| `Action_None` | 214 | 231 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 232 | 265 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 272 | 305 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 294 | 278 | inferred_complete_timeline |
| `Action_None` | 300 | 355 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 60 | 44 | inferred_complete_timeline |
| `Action_None` | 66 | 181 | 116 | inferred_complete_timeline |
| `Action_None` | 186 | 416 | 231 | inferred_complete_timeline |
| `Action_None` | 421 | 425 | 5 | inferred_complete_timeline |
| `Action_None` | 427 | 430 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 58–84 | 27 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 72–435 | 349 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 81–629 | 531 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 84–629 | 515 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 86–142 | 57 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 99–491 | 340 | 12 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 102–629 | 507 | 8 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 117–629 | 512 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 138–592 | 340 | 10 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 152–507 | 356 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 272–276 | 5 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 308–495 | 188 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 327–373 | 30 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 356–493 | 137 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 359–364 | 6 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 368–376 | 9 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 371–384 | 13 | 2 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 380–415 | 32 | 3 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 382–416 | 35 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 392–393 | 2 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 394–629 | 222 | 4 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 398–629 | 196 | 4 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 426–483 | 58 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 447–448 | 2 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 450–519 | 65 | 3 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 454–488 | 27 | 2 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 460–493 | 34 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 460–461 | 2 | 1 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 468–469 | 2 | 1 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 475–605 | 25 | 4 | Undefined position; Undefined team |
| `51` | `65` | Position_Unknown | Team_Unknown | 492–493 | 2 | 1 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 494–497 | 4 | 1 | Undefined position; Undefined team |
| `53` | `68` | Position_Unknown | Team_Unknown | 514–629 | 116 | 1 | Undefined position; Undefined team |
| `54` | `69` | Position_Unknown | Team_Unknown | 516–593 | 69 | 3 | Undefined position; Undefined team |
| `55` | `70` | Position_Unknown | Team_Unknown | 516–629 | 114 | 1 | Undefined position; Undefined team |
| `56` | `71` | Position_Unknown | Team_Unknown | 519–629 | 98 | 5 | Undefined position; Undefined team |
| `57` | `73` | Position_Unknown | Team_Unknown | 522–605 | 58 | 6 | Undefined position; Undefined team |
| `58` | `74` | Position_Unknown | Team_Unknown | 538–544 | 7 | 1 | Undefined position; Undefined team |
| `59` | `76` | Position_Unknown | Team_Unknown | 544–629 | 86 | 1 | Undefined position; Undefined team |
| `60` | `77` | Position_Unknown | Team_Unknown | 552–626 | 72 | 2 | Undefined position; Undefined team |
| `61` | `78` | Position_Unknown | Team_Unknown | 556–629 | 74 | 1 | Undefined position; Undefined team |
| `62` | `82` | Position_Unknown | Team_Unknown | 564–590 | 17 | 5 | Undefined position; Undefined team |
| `63` | `87` | Position_Unknown | Team_Unknown | 585–605 | 17 | 2 | Undefined position; Undefined team |
| `64` | `89` | Position_Unknown | Team_Unknown | 598–627 | 30 | 1 | Undefined position; Undefined team |
| `65` | `90` | Position_Unknown | Team_Unknown | 600–617 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 46 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 46 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 92 |
| Missing visible bounding boxes during action | 181 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [17-474] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-593] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-60] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-416] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-425] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-62] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-381] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-500] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-163] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-338] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-384] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-491] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-451] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-370] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-459] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-602] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-607] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-619] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-235] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-391] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-416] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-474] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-488] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-484] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-249] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-373] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-104] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-265] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [272-305] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-370] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-400] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-294] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-355] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-27] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-103] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-319] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-366] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-423] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-435] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-332] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-351] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-423] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-629] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-332] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-464] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-506] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-547] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-317] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-328] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-355] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-395] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-443] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-456] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-491] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-481] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-414] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-390] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-403] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-421] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-442] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-533] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-586] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-592] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-507] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-495] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-331] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-343] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-373] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-484] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-493] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-364] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-376] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-381] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-393] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-415] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-416] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-464] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-493] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-507] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-412] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-493] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-606] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-629] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-483] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-456] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-507] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-519] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-488] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-493] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-593] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-605] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-518] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-527] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-593] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-530] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-545] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-529] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-547] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-575] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-593] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-605] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-544] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-606] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-626] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-570] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-580] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-586] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-590] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-592] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-605] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-627] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-612] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '65' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>