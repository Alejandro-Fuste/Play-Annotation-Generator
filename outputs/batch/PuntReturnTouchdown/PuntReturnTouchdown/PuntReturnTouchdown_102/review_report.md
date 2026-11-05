# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_102`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 65
- **Ball Tracks:** 1
- **Action Segments:** 338
- **Validation Warnings:** 406
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 324
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `18` | `18` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `18` | `18` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `18` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `6` | `6` | 30 | START | 30 | 82 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `18` | `18` | 57 | END | 57 | 57 |
| ✅ EXACT | `Action_PuntBall` | Punter | `18` | `18` | 83 | START | 83 | 99 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `23` | `21` | 215 | START | 215 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `21` | 230 | START | 230 | 391 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `1` | `1` | 620 | START | 620 | 626 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 115 | 86 | inferred_complete_timeline |
| `Action_None` | 118 | 167 | 50 | inferred_complete_timeline |
| `Action_None` | 170 | 192 | 23 | inferred_complete_timeline |
| `Action_None` | 195 | 267 | 73 | inferred_complete_timeline |
| `Action_None` | 271 | 273 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–503
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 272 | 243 | inferred_complete_timeline |
| `Action_None` | 275 | 347 | 73 | inferred_complete_timeline |
| `Action_None` | 350 | 388 | 39 | inferred_complete_timeline |
| `Action_None` | 390 | 393 | 4 | inferred_complete_timeline |
| `Action_None` | 397 | 404 | 8 | inferred_complete_timeline |
| `Action_None` | 406 | 411 | 6 | inferred_complete_timeline |
| `Action_None` | 419 | 421 | 3 | inferred_complete_timeline |
| `Action_None` | 425 | 430 | 6 | inferred_complete_timeline |
| `Action_None` | 441 | 473 | 33 | inferred_complete_timeline |
| `Action_None` | 476 | 482 | 7 | inferred_complete_timeline |
| `Action_None` | 487 | 500 | 14 | inferred_complete_timeline |
| `Action_None` | 502 | 503 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 30 | 82 | 53 | inferred_complete_timeline |
| `Action_None` | 83 | 267 | 185 | inferred_complete_timeline |
| `Action_None` | 273 | 373 | 101 | inferred_complete_timeline |
| `Action_None` | 375 | 431 | 57 | inferred_complete_timeline |
| `Action_None` | 434 | 529 | 96 | inferred_complete_timeline |
| `Action_None` | 531 | 629 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 80 | 51 | inferred_complete_timeline |
| `Action_None` | 109 | 113 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 272 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 57 | 1 | inferred_complete_timeline |
| `Action_None` | 58 | 82 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 83 | 99 | 17 | inferred_complete_timeline |
| `Action_None` | 100 | 100 | 1 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 114 | 199 | 86 | inferred_complete_timeline |
| `Action_None` | 205 | 415 | 211 | inferred_complete_timeline |
| `Action_None` | 418 | 419 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 388 | 359 | inferred_complete_timeline |
| `Action_None` | 391 | 411 | 21 | inferred_complete_timeline |
| `Action_None` | 431 | 432 | 2 | inferred_complete_timeline |
| `Action_None` | 452 | 455 | 4 | inferred_complete_timeline |
| `Action_None` | 457 | 571 | 115 | inferred_complete_timeline |
| `Action_None` | 573 | 622 | 50 | inferred_complete_timeline |
| `Action_None` | 627 | 629 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–453
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 307 | 278 | inferred_complete_timeline |
| `Action_None` | 311 | 332 | 22 | inferred_complete_timeline |
| `Action_None` | 335 | 359 | 25 | inferred_complete_timeline |
| `Action_None` | 361 | 367 | 7 | inferred_complete_timeline |
| `Action_None` | 369 | 387 | 19 | inferred_complete_timeline |
| `Action_None` | 389 | 423 | 35 | inferred_complete_timeline |
| `Action_None` | 425 | 437 | 13 | inferred_complete_timeline |
| `Action_None` | 439 | 453 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–433
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 153 | 124 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 200 | 38 | inferred_complete_timeline |
| `Action_None` | 203 | 381 | 179 | inferred_complete_timeline |
| `Action_None` | 384 | 433 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 81 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–456
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 81 | 52 | inferred_complete_timeline |
| `Action_None` | 84 | 369 | 286 | inferred_complete_timeline |
| `Action_None` | 371 | 375 | 5 | inferred_complete_timeline |
| `Action_None` | 377 | 382 | 6 | inferred_complete_timeline |
| `Action_None` | 385 | 387 | 3 | inferred_complete_timeline |
| `Action_None` | 394 | 408 | 15 | inferred_complete_timeline |
| `Action_None` | 410 | 437 | 28 | inferred_complete_timeline |
| `Action_None` | 439 | 446 | 8 | inferred_complete_timeline |
| `Action_None` | 449 | 450 | 2 | inferred_complete_timeline |
| `Action_None` | 455 | 456 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 209 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_None` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_None` | 77 | 195 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–442
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 43 | 14 | inferred_complete_timeline |
| `Action_None` | 46 | 49 | 4 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_None` | 66 | 69 | 4 | inferred_complete_timeline |
| `Action_None` | 71 | 329 | 259 | inferred_complete_timeline |
| `Action_None` | 331 | 372 | 42 | inferred_complete_timeline |
| `Action_None` | 374 | 381 | 8 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 393 | 5 | inferred_complete_timeline |
| `Action_None` | 395 | 401 | 7 | inferred_complete_timeline |
| `Action_None` | 403 | 404 | 2 | inferred_complete_timeline |
| `Action_None` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_None` | 425 | 429 | 5 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 209 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 210 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–527
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 269 | 240 | inferred_complete_timeline |
| `Action_None` | 271 | 310 | 40 | inferred_complete_timeline |
| `Action_None` | 319 | 356 | 38 | inferred_complete_timeline |
| `Action_None` | 358 | 374 | 17 | inferred_complete_timeline |
| `Action_None` | 378 | 380 | 3 | inferred_complete_timeline |
| `Action_None` | 386 | 425 | 40 | inferred_complete_timeline |
| `Action_None` | 450 | 499 | 50 | inferred_complete_timeline |
| `Action_None` | 511 | 513 | 3 | inferred_complete_timeline |
| `Action_None` | 515 | 521 | 7 | inferred_complete_timeline |
| `Action_None` | 525 | 527 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–629 | 582 | 15 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–618 | 584 | 12 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 95–113 | 19 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 95–376 | 262 | 9 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 104–402 | 284 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 111–302 | 187 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 129–363 | 208 | 6 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 130–144 | 15 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 145–148 | 4 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 156–213 | 58 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 213–513 | 297 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 248–433 | 182 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 262–499 | 196 | 14 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 265–336 | 72 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 283–553 | 190 | 12 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 294–429 | 107 | 5 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 343–419 | 36 | 2 | Undefined position; Undefined team |
| `37` | `60` | Position_Unknown | Team_Unknown | 352–400 | 45 | 3 | Undefined position; Undefined team |
| `38` | `64` | Position_Unknown | Team_Unknown | 360–361 | 2 | 1 | Undefined position; Undefined team |
| `39` | `66` | Position_Unknown | Team_Unknown | 363–366 | 4 | 1 | Undefined position; Undefined team |
| `41` | `69` | Position_Unknown | Team_Unknown | 367–391 | 24 | 2 | Undefined position; Undefined team |
| `42` | `70` | Position_Unknown | Team_Unknown | 372–629 | 233 | 11 | Undefined position; Undefined team |
| `43` | `71` | Position_Unknown | Team_Unknown | 395–398 | 4 | 1 | Undefined position; Undefined team |
| `44` | `72` | Position_Unknown | Team_Unknown | 396–503 | 62 | 6 | Undefined position; Undefined team |
| `45` | `73` | Position_Unknown | Team_Unknown | 404–629 | 196 | 12 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 430–467 | 26 | 4 | Undefined position; Undefined team |
| `47` | `75` | Position_Unknown | Team_Unknown | 438–610 | 123 | 15 | Undefined position; Undefined team |
| `48` | `76` | Position_Unknown | Team_Unknown | 440–474 | 17 | 2 | Undefined position; Undefined team |
| `49` | `77` | Position_Unknown | Team_Unknown | 451–452 | 2 | 1 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 453–454 | 2 | 1 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 460–518 | 10 | 3 | Undefined position; Undefined team |
| `52` | `81` | Position_Unknown | Team_Unknown | 464–629 | 25 | 10 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 468–472 | 5 | 1 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 470–629 | 148 | 6 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 496–497 | 2 | 1 | Undefined position; Undefined team |
| `56` | `87` | Position_Unknown | Team_Unknown | 508–629 | 115 | 3 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 509–511 | 3 | 1 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 511–629 | 61 | 12 | Undefined position; Undefined team |
| `59` | `90` | Position_Unknown | Team_Unknown | 530–629 | 97 | 3 | Undefined position; Undefined team |
| `60` | `92` | Position_Unknown | Team_Unknown | 537–629 | 52 | 8 | Undefined position; Undefined team |
| `61` | `93` | Position_Unknown | Team_Unknown | 538–629 | 62 | 8 | Undefined position; Undefined team |
| `62` | `94` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 549–629 | 66 | 6 | Undefined position; Undefined team |
| `64` | `102` | Position_Unknown | Team_Unknown | 571–602 | 22 | 3 | Undefined position; Undefined team |
| `65` | `104` | Position_Unknown | Team_Unknown | 618–629 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `40` | `68` | 365 | 365 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Punter` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 305 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 206: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 206: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [30-272] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-347] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-388] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-404] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-411] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-421] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-430] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-473] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-482] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-500] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-331] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-375] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-397] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-432] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-436] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-456] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-471] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-484] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-506] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-520] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-388] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-411] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-455] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-571] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-622] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-307] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-332] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-387] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-423] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-437] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-453] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-200] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-381] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-433] for track '5' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-267] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-373] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-431] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-529] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-209] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-272] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-269] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-310] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-356] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-374] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-425] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-499] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-61] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-75] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-413] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-422] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-431] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-457] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-471] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-602] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-618] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-369] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-408] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-437] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-446] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-450] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-192] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-267] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-69] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-372] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-381] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-393] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-401] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-429] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [83-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 100, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [100-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-415] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-341] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-361] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-369] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-391] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [398-402] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-295] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-302] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-213] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-422] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-435] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-513] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-423] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-433] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-285] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-304] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-323] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-345] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-361] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-394] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-437] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-445] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-456] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-499] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-336] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-409] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-450] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-471] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-499] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-529] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-543] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-553] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-372] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-411] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-366] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-419] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-387] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-391] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-400] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-379] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-391] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-490] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-504] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-526] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-546] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-557] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-569] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-575] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-582] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-452] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-473] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-484] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-503] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-456] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-464] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-492] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-511] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-527] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-559] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-593] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-600] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-605] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-437] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-452] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-467] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-447] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-474] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-485] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-496] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-517] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-524] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-537] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-571] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-581] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-599] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-610] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-454] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-464] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-511] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-472] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-499] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-472] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-488] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-505] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-622] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-629] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-527] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-629] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-511] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-547] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-561] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-567] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-602] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-605] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-610] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-629] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-534] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-575] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-629] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-554] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-569] for track '60' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-581] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-613] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-620] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-627] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-568] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-575] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-610] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-627] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-561] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-583] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-595] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-611] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-573] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-588] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-602] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-629] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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