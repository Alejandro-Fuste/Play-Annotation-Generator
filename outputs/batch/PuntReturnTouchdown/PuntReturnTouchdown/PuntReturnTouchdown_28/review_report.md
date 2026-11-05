# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_28`
- **Frame Range:** 0 to 749 (750 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 749
- **Player Tracks:** 92
- **Ball Tracks:** 0
- **Action Segments:** 338
- **Validation Warnings:** 454
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 324
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_CatchPunt` | Punt_Returner2 | defense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner2 | defense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Punt_Returner2 | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `9` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 123 | START | 123 | 183 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 153 | END | 153 | 153 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 184 | START | 184 | 191 |
| ⚠️ START CHANGED | `Action_CatchPunt` | Punt_Returner2 | `3` | `3` | 274 | START | 282 | 283 |
| ✅ EXACT | `Action_BallCarry` | Punt_Returner2 | `3` | `3` | 291 | START | 291 | 299 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Punt_Returner2 | `3` | `3` | 734 | START | N/A | N/A |

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
- **Visible Frames:** 0–513
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 262 | 140 | inferred_complete_timeline |
| `Action_None` | 267 | 282 | 16 | inferred_complete_timeline |
| `Action_None` | 287 | 341 | 55 | inferred_complete_timeline |
| `Action_None` | 344 | 398 | 55 | inferred_complete_timeline |
| `Action_None` | 408 | 410 | 3 | inferred_complete_timeline |
| `Action_None` | 412 | 425 | 14 | inferred_complete_timeline |
| `Action_None` | 436 | 446 | 11 | inferred_complete_timeline |
| `Action_None` | 512 | 513 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–662
- **Visible Samples:** 574

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 269 | 147 | inferred_complete_timeline |
| `Action_None` | 275 | 386 | 112 | inferred_complete_timeline |
| `Action_None` | 394 | 470 | 77 | inferred_complete_timeline |
| `Action_None` | 482 | 497 | 16 | inferred_complete_timeline |
| `Action_None` | 563 | 659 | 97 | inferred_complete_timeline |
| `Action_None` | 661 | 662 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–380
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 172 | 50 | inferred_complete_timeline |
| `Action_None` | 175 | 264 | 90 | inferred_complete_timeline |
| `Action_None` | 287 | 310 | 24 | inferred_complete_timeline |
| `Action_None` | 316 | 380 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–674
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_LongSnap` | 123 | 183 | 61 | inferred_complete_timeline |
| `Action_None` | 184 | 354 | 171 | inferred_complete_timeline |
| `Action_None` | 359 | 494 | 136 | inferred_complete_timeline |
| `Action_None` | 497 | 498 | 2 | inferred_complete_timeline |
| `Action_None` | 500 | 509 | 10 | inferred_complete_timeline |
| `Action_None` | 518 | 520 | 3 | inferred_complete_timeline |
| `Action_None` | 572 | 640 | 69 | inferred_complete_timeline |
| `Action_None` | 644 | 663 | 20 | inferred_complete_timeline |
| `Action_None` | 668 | 669 | 2 | inferred_complete_timeline |
| `Action_None` | 673 | 674 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 253 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–563
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 501 | 379 | inferred_complete_timeline |
| `Action_None` | 512 | 559 | 48 | inferred_complete_timeline |
| `Action_None` | 561 | 563 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_SnapReceive` | 153 | 153 | 1 | inferred_complete_timeline |
| `Action_None` | 154 | 183 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 184 | 191 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–639
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 305 | 183 | inferred_complete_timeline |
| `Action_None` | 307 | 336 | 30 | inferred_complete_timeline |
| `Action_None` | 341 | 386 | 46 | inferred_complete_timeline |
| `Action_None` | 395 | 601 | 207 | inferred_complete_timeline |
| `Action_None` | 607 | 639 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–280
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 175 | 53 | inferred_complete_timeline |
| `Action_None` | 177 | 252 | 76 | inferred_complete_timeline |
| `Action_None` | 278 | 280 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 275 | 153 | inferred_complete_timeline |
| `Action_None` | 344 | 374 | 31 | inferred_complete_timeline |
| `Action_None` | 388 | 478 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–464
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 140 | 18 | inferred_complete_timeline |
| `Action_None` | 149 | 218 | 70 | inferred_complete_timeline |
| `Action_None` | 224 | 358 | 135 | inferred_complete_timeline |
| `Action_None` | 361 | 456 | 96 | inferred_complete_timeline |
| `Action_None` | 458 | 461 | 4 | inferred_complete_timeline |
| `Action_None` | 463 | 464 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 15 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 78 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 112 | 19 | inferred_complete_timeline |
| `Action_None` | 127 | 145 | 19 | inferred_complete_timeline |
| `Action_None` | 148 | 194 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 166 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–520
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 143 | 21 | inferred_complete_timeline |
| `Action_None` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 267 | 92 | inferred_complete_timeline |
| `Action_None` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 486 | 177 | inferred_complete_timeline |
| `Action_None` | 496 | 497 | 2 | inferred_complete_timeline |
| `Action_None` | 502 | 509 | 8 | inferred_complete_timeline |
| `Action_None` | 511 | 512 | 2 | inferred_complete_timeline |
| `Action_None` | 514 | 520 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 2–5
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 5 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 154 | 32 | inferred_complete_timeline |
| `Action_None` | 233 | 240 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 300 | 178 | inferred_complete_timeline |
| `Action_None` | 308 | 318 | 11 | inferred_complete_timeline |
| `Action_None` | 322 | 332 | 11 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 340 | 352 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_CatchPunt` | 282 | 283 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 290 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 291 | 299 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–499
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 395 | 273 | inferred_complete_timeline |
| `Action_None` | 397 | 467 | 71 | inferred_complete_timeline |
| `Action_None` | 472 | 499 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–602 | 586 | 11 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 14–173 | 113 | 9 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 158–315 | 133 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 167–201 | 33 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 170–340 | 161 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 172–266 | 43 | 10 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 178–455 | 248 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 182–307 | 110 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 184–749 | 552 | 7 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 204–542 | 339 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 218–418 | 154 | 4 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 231–253 | 21 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 261–607 | 339 | 4 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 302–475 | 169 | 3 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 325–420 | 86 | 2 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 326–366 | 41 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 340–359 | 20 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 361–387 | 27 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 365–411 | 41 | 2 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 367–378 | 8 | 2 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 373–393 | 18 | 3 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 392–749 | 355 | 2 | Undefined position; Undefined team |
| `42` | `48` | Position_Unknown | Team_Unknown | 400–498 | 99 | 1 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 418–429 | 9 | 3 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 424–749 | 240 | 9 | Undefined position; Undefined team |
| `45` | `53` | Position_Unknown | Team_Unknown | 427–705 | 160 | 5 | Undefined position; Undefined team |
| `46` | `55` | Position_Unknown | Team_Unknown | 429–469 | 40 | 2 | Undefined position; Undefined team |
| `47` | `57` | Position_Unknown | Team_Unknown | 434–553 | 77 | 5 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 444–497 | 53 | 2 | Undefined position; Undefined team |
| `49` | `60` | Position_Unknown | Team_Unknown | 451–646 | 170 | 8 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 465–748 | 221 | 12 | Undefined position; Undefined team |
| `51` | `64` | Position_Unknown | Team_Unknown | 468–749 | 251 | 7 | Undefined position; Undefined team |
| `52` | `65` | Position_Unknown | Team_Unknown | 473–521 | 44 | 4 | Undefined position; Undefined team |
| `53` | `66` | Position_Unknown | Team_Unknown | 479–749 | 262 | 4 | Undefined position; Undefined team |
| `54` | `67` | Position_Unknown | Team_Unknown | 482–553 | 72 | 1 | Undefined position; Undefined team |
| `55` | `68` | Position_Unknown | Team_Unknown | 485–554 | 70 | 1 | Undefined position; Undefined team |
| `56` | `69` | Position_Unknown | Team_Unknown | 491–654 | 158 | 2 | Undefined position; Undefined team |
| `57` | `70` | Position_Unknown | Team_Unknown | 498–505 | 8 | 1 | Undefined position; Undefined team |
| `58` | `73` | Position_Unknown | Team_Unknown | 524–563 | 40 | 1 | Undefined position; Undefined team |
| `59` | `75` | Position_Unknown | Team_Unknown | 531–554 | 21 | 3 | Undefined position; Undefined team |
| `60` | `76` | Position_Unknown | Team_Unknown | 556–656 | 64 | 9 | Undefined position; Undefined team |
| `61` | `77` | Position_Unknown | Team_Unknown | 560–749 | 188 | 3 | Undefined position; Undefined team |
| `62` | `79` | Position_Unknown | Team_Unknown | 570–659 | 42 | 8 | Undefined position; Undefined team |
| `63` | `82` | Position_Unknown | Team_Unknown | 584–598 | 5 | 2 | Undefined position; Undefined team |
| `64` | `85` | Position_Unknown | Team_Unknown | 591–749 | 143 | 5 | Undefined position; Undefined team |
| `65` | `87` | Position_Unknown | Team_Unknown | 599–600 | 2 | 1 | Undefined position; Undefined team |
| `66` | `88` | Position_Unknown | Team_Unknown | 599–659 | 52 | 5 | Undefined position; Undefined team |
| `67` | `90` | Position_Unknown | Team_Unknown | 608–749 | 109 | 5 | Undefined position; Undefined team |
| `68` | `91` | Position_Unknown | Team_Unknown | 615–749 | 122 | 4 | Undefined position; Undefined team |
| `69` | `93` | Position_Unknown | Team_Unknown | 619–649 | 12 | 3 | Undefined position; Undefined team |
| `70` | `94` | Position_Unknown | Team_Unknown | 625–749 | 97 | 6 | Undefined position; Undefined team |
| `71` | `95` | Position_Unknown | Team_Unknown | 650–749 | 100 | 1 | Undefined position; Undefined team |
| `72` | `96` | Position_Unknown | Team_Unknown | 655–656 | 2 | 1 | Undefined position; Undefined team |
| `73` | `97` | Position_Unknown | Team_Unknown | 656–659 | 4 | 1 | Undefined position; Undefined team |
| `74` | `98` | Position_Unknown | Team_Unknown | 657–749 | 93 | 1 | Undefined position; Undefined team |
| `75` | `99` | Position_Unknown | Team_Unknown | 659–660 | 2 | 1 | Undefined position; Undefined team |
| `76` | `104` | Position_Unknown | Team_Unknown | 669–749 | 81 | 1 | Undefined position; Undefined team |
| `77` | `105` | Position_Unknown | Team_Unknown | 669–675 | 7 | 1 | Undefined position; Undefined team |
| `78` | `106` | Position_Unknown | Team_Unknown | 672–673 | 2 | 1 | Undefined position; Undefined team |
| `79` | `107` | Position_Unknown | Team_Unknown | 673–684 | 12 | 1 | Undefined position; Undefined team |
| `80` | `108` | Position_Unknown | Team_Unknown | 677–678 | 2 | 1 | Undefined position; Undefined team |
| `81` | `109` | Position_Unknown | Team_Unknown | 681–749 | 57 | 6 | Undefined position; Undefined team |
| `82` | `115` | Position_Unknown | Team_Unknown | 702–749 | 47 | 2 | Undefined position; Undefined team |
| `83` | `116` | Position_Unknown | Team_Unknown | 702–742 | 21 | 5 | Undefined position; Undefined team |
| `84` | `118` | Position_Unknown | Team_Unknown | 709–743 | 35 | 1 | Undefined position; Undefined team |
| `85` | `119` | Position_Unknown | Team_Unknown | 709–728 | 19 | 2 | Undefined position; Undefined team |
| `86` | `121` | Position_Unknown | Team_Unknown | 719–749 | 28 | 2 | Undefined position; Undefined team |
| `87` | `124` | Position_Unknown | Team_Unknown | 729–735 | 7 | 1 | Undefined position; Undefined team |
| `88` | `125` | Position_Unknown | Team_Unknown | 729–749 | 15 | 2 | Undefined position; Undefined team |
| `89` | `126` | Position_Unknown | Team_Unknown | 729–740 | 12 | 1 | Undefined position; Undefined team |
| `90` | `128` | Position_Unknown | Team_Unknown | 731–738 | 8 | 1 | Undefined position; Undefined team |
| `91` | `129` | Position_Unknown | Team_Unknown | 732–733 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchPunt` for actor_track_id `3` (Punt_Returner2): Annotated start 274 != Inferred start 282
- ❌ Missing segment for action `Action_CrossGoalLine` on target `3` (Punt_Returner2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 73 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 73 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 146 |
| Missing visible bounding boxes during action | 304 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '3' has invalid range: start=734, end=299. Clamping end to start.
- ⚠️ Action 'Action_None' range [123-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-318] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-352] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [184-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-311] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-400] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-539] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-546] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-566] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-575] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-588] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-598] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-602] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [291-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-374] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-478] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-253] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-305] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-386] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-601] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-639] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-386] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-470] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-497] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-659] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-662] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-380] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-166] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-267] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-486] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-509] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-520] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-501] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-559] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-354] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-494] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-509] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-520] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-640] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-663] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-669] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-674] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-395] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-467] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-499] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-262] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-341] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-398] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-425] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-446] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-456] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-15] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-78] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-112] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-48] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-68] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-90] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-118] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-197] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-340] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-388] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-455] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-307] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-454] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-461] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-505] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-512] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-671] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-688] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-749] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-542] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-321] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-418] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-253] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-489] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-588] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-607] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-398] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-409] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-475] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-420] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-359] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-387] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-402] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-393] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-512] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-498] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-430] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-463] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-602] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-609] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-643] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-654] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-681] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-498] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-570] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-582] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-673] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-705] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-461] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-469] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-491] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-539] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-553] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-476] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-497] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-505] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-537] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-545] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-589] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-611] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-630] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-634] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-646] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-523] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-539] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-673] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-685] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-689] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [691-694] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [701-708] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [710-712] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-727] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [733-748] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-473] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-486] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-654] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-660] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-668] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-673] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-749] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-494] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-518] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-586] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-680] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-553] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-554] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-609] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-654] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-505] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-563] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-541] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-549] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-554] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-557] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-568] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-579] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-600] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-615] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-625] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-643] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-656] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-586] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-593] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-575] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-583] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-600] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-622] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-640] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-654] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-585] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-614] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-625] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-643] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-743] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-602] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-642] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-654] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-659] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-634] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-695] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-707] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-749] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-638] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-676] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-695] for track '68' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-625] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-639] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-649] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-641] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-662] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-671] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-688] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-705] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-656] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-659] for track '73' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-660] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-675] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-673] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [673-684] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [677-678] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-705] for track '81' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-712] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [715-718] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-743] for track '81' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [746-747] for track '81' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-706] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-749] for track '82' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-706] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-712] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [717-718] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [721-725] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [738-742] for track '83' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-743] for track '84' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-718] for track '85' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [720-728] for track '85' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [719-725] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-749] for track '86' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-735] for track '87' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-736] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [743-749] for track '88' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [729-740] for track '89' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [731-738] for track '90' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [732-733] for track '91' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '79' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '79' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '80' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '80' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '81' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '81' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '82' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '82' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '83' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '83' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '84' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '84' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '85' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '85' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '86' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '86' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '87' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '87' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '88' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '88' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '89' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '89' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '90' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '90' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '91' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '91' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>