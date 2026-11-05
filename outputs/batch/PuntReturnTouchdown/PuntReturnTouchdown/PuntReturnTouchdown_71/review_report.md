# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_71`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 82
- **Ball Tracks:** 0
- **Action Segments:** 432
- **Validation Warnings:** 516
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 415
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `60` | `45` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `60` | `45` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `44` | `36` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `10` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `13` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `16` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `2` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `7` | `7` | 110 | START | 110 | 131 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 141 | END | 141 | 141 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 166 | START | 166 | 182 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `60` | `45` | 303 | START | 303 | 315 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `60` | `45` | 326 | START | 326 | 351 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `44` | `36` | 669 | START | 669 | 673 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 670

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 557 | 448 | inferred_complete_timeline |
| `Action_None` | 560 | 581 | 22 | inferred_complete_timeline |
| `Action_None` | 586 | 588 | 3 | inferred_complete_timeline |
| `Action_None` | 601 | 606 | 6 | inferred_complete_timeline |
| `Action_None` | 609 | 689 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 159 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 144 | 35 | inferred_complete_timeline |
| `Action_None` | 146 | 179 | 34 | inferred_complete_timeline |
| `Action_None` | 182 | 188 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 637

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_LongSnap` | 110 | 131 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 135 | 143 | 9 | inferred_complete_timeline |
| `Action_LongSnap` | 146 | 165 | 20 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 173 | 179 | 7 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 627 | 390 | inferred_complete_timeline |
| `Action_None` | 630 | 689 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 676

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 199 | 90 | inferred_complete_timeline |
| `Action_None` | 201 | 542 | 342 | inferred_complete_timeline |
| `Action_None` | 553 | 554 | 2 | inferred_complete_timeline |
| `Action_None` | 557 | 564 | 8 | inferred_complete_timeline |
| `Action_None` | 566 | 689 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 161 | 52 | inferred_complete_timeline |
| `Action_None` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_None` | 173 | 182 | 10 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 661

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 336 | 227 | inferred_complete_timeline |
| `Action_None` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_None` | 343 | 354 | 12 | inferred_complete_timeline |
| `Action_None` | 357 | 473 | 117 | inferred_complete_timeline |
| `Action_None` | 482 | 491 | 10 | inferred_complete_timeline |
| `Action_None` | 493 | 529 | 37 | inferred_complete_timeline |
| `Action_None` | 531 | 532 | 2 | inferred_complete_timeline |
| `Action_None` | 537 | 595 | 59 | inferred_complete_timeline |
| `Action_None` | 602 | 603 | 2 | inferred_complete_timeline |
| `Action_None` | 608 | 689 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 664

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 141 | 1 | inferred_complete_timeline |
| `Action_None` | 142 | 165 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_None` | 183 | 364 | 182 | inferred_complete_timeline |
| `Action_None` | 370 | 507 | 138 | inferred_complete_timeline |
| `Action_None` | 509 | 510 | 2 | inferred_complete_timeline |
| `Action_None` | 514 | 528 | 15 | inferred_complete_timeline |
| `Action_None` | 530 | 531 | 2 | inferred_complete_timeline |
| `Action_None` | 533 | 534 | 2 | inferred_complete_timeline |
| `Action_None` | 537 | 542 | 6 | inferred_complete_timeline |
| `Action_None` | 549 | 662 | 114 | inferred_complete_timeline |
| `Action_None` | 665 | 666 | 2 | inferred_complete_timeline |
| `Action_None` | 668 | 673 | 6 | inferred_complete_timeline |
| `Action_None` | 675 | 684 | 10 | inferred_complete_timeline |
| `Action_None` | 688 | 689 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 601

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 132 | 23 | inferred_complete_timeline |
| `Action_None` | 136 | 149 | 14 | inferred_complete_timeline |
| `Action_None` | 153 | 180 | 28 | inferred_complete_timeline |
| `Action_None` | 187 | 201 | 15 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 327 | 109 | inferred_complete_timeline |
| `Action_None` | 334 | 374 | 41 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |
| `Action_None` | 392 | 394 | 3 | inferred_complete_timeline |
| `Action_None` | 396 | 400 | 5 | inferred_complete_timeline |
| `Action_None` | 403 | 415 | 13 | inferred_complete_timeline |
| `Action_None` | 437 | 473 | 37 | inferred_complete_timeline |
| `Action_None` | 478 | 480 | 3 | inferred_complete_timeline |
| `Action_None` | 482 | 489 | 8 | inferred_complete_timeline |
| `Action_None` | 491 | 507 | 17 | inferred_complete_timeline |
| `Action_None` | 515 | 519 | 5 | inferred_complete_timeline |
| `Action_None` | 526 | 669 | 144 | inferred_complete_timeline |
| `Action_None` | 671 | 689 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–394
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 225 | 116 | inferred_complete_timeline |
| `Action_None` | 227 | 245 | 19 | inferred_complete_timeline |
| `Action_None` | 258 | 270 | 13 | inferred_complete_timeline |
| `Action_None` | 272 | 353 | 82 | inferred_complete_timeline |
| `Action_None` | 359 | 383 | 25 | inferred_complete_timeline |
| `Action_None` | 389 | 394 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 139 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 126 | 17 | inferred_complete_timeline |
| `Action_None` | 200 | 213 | 14 | inferred_complete_timeline |
| `Action_None` | 218 | 374 | 157 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 132 | 23 | inferred_complete_timeline |
| `Action_None` | 134 | 221 | 88 | inferred_complete_timeline |
| `Action_None` | 223 | 227 | 5 | inferred_complete_timeline |
| `Action_None` | 231 | 245 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–468
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 131 | 22 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 180 | 35 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 216 | 4 | inferred_complete_timeline |
| `Action_None` | 218 | 468 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 132 | 23 | inferred_complete_timeline |
| `Action_None` | 135 | 141 | 7 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 143 | 34 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 170 | 18 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 131 | 22 | inferred_complete_timeline |
| `Action_None` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 209 | 68 | inferred_complete_timeline |
| `Action_None` | 211 | 276 | 66 | inferred_complete_timeline |
| `Action_None` | 278 | 291 | 14 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_None` | 302 | 348 | 47 | inferred_complete_timeline |
| `Action_None` | 351 | 353 | 3 | inferred_complete_timeline |
| `Action_None` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_None` | 390 | 392 | 3 | inferred_complete_timeline |
| `Action_None` | 394 | 465 | 72 | inferred_complete_timeline |
| `Action_None` | 468 | 473 | 6 | inferred_complete_timeline |
| `Action_None` | 475 | 476 | 2 | inferred_complete_timeline |
| `Action_None` | 484 | 488 | 5 | inferred_complete_timeline |
| `Action_None` | 494 | 530 | 37 | inferred_complete_timeline |
| `Action_None` | 532 | 533 | 2 | inferred_complete_timeline |
| `Action_None` | 558 | 588 | 31 | inferred_complete_timeline |
| `Action_None` | 590 | 591 | 2 | inferred_complete_timeline |
| `Action_None` | 593 | 602 | 10 | inferred_complete_timeline |
| `Action_None` | 604 | 645 | 42 | inferred_complete_timeline |
| `Action_None` | 653 | 658 | 6 | inferred_complete_timeline |
| `Action_None` | 661 | 689 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–423
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 156 | 47 | inferred_complete_timeline |
| `Action_None` | 158 | 166 | 9 | inferred_complete_timeline |
| `Action_None` | 168 | 214 | 47 | inferred_complete_timeline |
| `Action_None` | 217 | 423 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 169 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 185 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 209 | 100 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 253 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 102–459 | 221 | 21 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 128–130 | 3 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 153–245 | 81 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 154–374 | 197 | 9 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 175–230 | 39 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 178–348 | 154 | 6 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 190–361 | 171 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 195–199 | 4 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 197–375 | 111 | 11 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 206–257 | 44 | 6 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 206–398 | 190 | 3 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 207–363 | 144 | 6 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 211–689 | 408 | 18 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 230–247 | 9 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 237–247 | 10 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 238–689 | 432 | 5 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 249–479 | 207 | 10 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 261–271 | 8 | 3 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 267–367 | 45 | 7 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 274–351 | 77 | 5 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 277–281 | 5 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 282–349 | 39 | 7 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 289–689 | 365 | 10 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 318–319 | 2 | 1 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 356–399 | 42 | 3 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 368–676 | 287 | 10 | Undefined position; Undefined team |
| `53` | `76` | Position_Unknown | Team_Unknown | 370–689 | 262 | 5 | Undefined position; Undefined team |
| `54` | `77` | Position_Unknown | Team_Unknown | 371–372 | 2 | 1 | Undefined position; Undefined team |
| `55` | `78` | Position_Unknown | Team_Unknown | 397–689 | 283 | 3 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 411–432 | 9 | 4 | Undefined position; Undefined team |
| `57` | `81` | Position_Unknown | Team_Unknown | 425–426 | 2 | 1 | Undefined position; Undefined team |
| `58` | `82` | Position_Unknown | Team_Unknown | 425–452 | 8 | 3 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 427–497 | 68 | 2 | Undefined position; Undefined team |
| `60` | `85` | Position_Unknown | Team_Unknown | 434–436 | 3 | 1 | Undefined position; Undefined team |
| `61` | `86` | Position_Unknown | Team_Unknown | 438–689 | 199 | 11 | Undefined position; Undefined team |
| `62` | `90` | Position_Unknown | Team_Unknown | 450–689 | 203 | 11 | Undefined position; Undefined team |
| `63` | `91` | Position_Unknown | Team_Unknown | 450–689 | 237 | 3 | Undefined position; Undefined team |
| `64` | `92` | Position_Unknown | Team_Unknown | 450–574 | 125 | 1 | Undefined position; Undefined team |
| `65` | `94` | Position_Unknown | Team_Unknown | 453–493 | 34 | 3 | Undefined position; Undefined team |
| `66` | `97` | Position_Unknown | Team_Unknown | 491–689 | 198 | 2 | Undefined position; Undefined team |
| `67` | `98` | Position_Unknown | Team_Unknown | 499–689 | 191 | 1 | Undefined position; Undefined team |
| `68` | `100` | Position_Unknown | Team_Unknown | 503–504 | 2 | 1 | Undefined position; Undefined team |
| `69` | `101` | Position_Unknown | Team_Unknown | 506–689 | 161 | 6 | Undefined position; Undefined team |
| `70` | `102` | Position_Unknown | Team_Unknown | 514–558 | 45 | 1 | Undefined position; Undefined team |
| `71` | `107` | Position_Unknown | Team_Unknown | 532–648 | 88 | 11 | Undefined position; Undefined team |
| `72` | `108` | Position_Unknown | Team_Unknown | 541–542 | 2 | 1 | Undefined position; Undefined team |
| `73` | `109` | Position_Unknown | Team_Unknown | 545–546 | 2 | 1 | Undefined position; Undefined team |
| `74` | `111` | Position_Unknown | Team_Unknown | 551–689 | 96 | 8 | Undefined position; Undefined team |
| `75` | `112` | Position_Unknown | Team_Unknown | 560–665 | 44 | 9 | Undefined position; Undefined team |
| `76` | `113` | Position_Unknown | Team_Unknown | 572–689 | 118 | 1 | Undefined position; Undefined team |
| `77` | `114` | Position_Unknown | Team_Unknown | 573–689 | 80 | 11 | Undefined position; Undefined team |
| `78` | `117` | Position_Unknown | Team_Unknown | 583–689 | 97 | 5 | Undefined position; Undefined team |
| `79` | `118` | Position_Unknown | Team_Unknown | 583–593 | 10 | 2 | Undefined position; Undefined team |
| `80` | `119` | Position_Unknown | Team_Unknown | 601–606 | 6 | 1 | Undefined position; Undefined team |
| `81` | `123` | Position_Unknown | Team_Unknown | 676–689 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Jammer` position mapped to `defense` team
- ⚠️ 61 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 61 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 122 |
| Missing visible bounding boxes during action | 391 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [110-185] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-143] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-170] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-149] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-201] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-374] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-400] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-415] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-473] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-489] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-507] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-519] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-669] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-276] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-291] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-348] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-465] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-473] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-488] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-530] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-588] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-602] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-645] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-658] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [110-131] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [135-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [146-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 166, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [166-170] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-627] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-364] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-507] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-528] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-542] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-662] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-666] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [668-673] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-684] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-542] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-554] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-564] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-689] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-225] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-245] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-270] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-353] for track '10' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-383] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-394] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-144] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-126] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-374] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-159] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-245] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-468] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-336] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-354] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-473] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-491] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-529] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-595] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-603] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-689] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-557] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-581] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-606] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-156] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-423] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 110, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [110-113] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-350] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-364] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-374] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-385] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-405] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-456] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-242] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-170] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-222] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-357] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-374] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-236] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-348] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-223] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-300] for track '31' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-375] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-221] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-240] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-257] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-398] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-215] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-363] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-390] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-487] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-497] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-509] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [513-530] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [547-549] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-556] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [560-561] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [563-564] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [567-570] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [582-586] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [594-595] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [597-598] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [600-601] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [606-638] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [649-668] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-244] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-262] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-274] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-689] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-288] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-301] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-376] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-408] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-415] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-460] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-475] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-319] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-330] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-349] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-302] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [326-351] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-331] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-349] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-381] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-499] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-520] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-568] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-627] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-632] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-639] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-689] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-396] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-534] for track '52' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-543] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-565] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-583] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-591] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-606] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-615] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-629] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-639] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-676] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-384] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-501] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-506] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-520] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-689] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-647] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-427] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-492] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-488] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-519] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-558] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-642] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-652] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-664] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-483] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-520] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-546] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-592] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-598] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-604] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-617] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-620] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-627] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-640] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-689] for track '62' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-464] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-471] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-574] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-472] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-493] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-680] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-689] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-524] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-529] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-534] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-558] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-548] for track '71' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-555] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-571] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-592] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-606] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-627] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-634] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-648] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-597] for track '74' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-610] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-633] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-648] for track '74' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-653] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-663] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-687] for track '74' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-564] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-577] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-588] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-594] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-606] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-629] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [634-636] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-647] for track '75' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-665] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-584] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-595] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-602] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-606] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-638] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-645] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-660] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [663-667] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-678] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-591] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-617] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-636] for track '78' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [640-642] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-689] for track '78' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-586] for track '79' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-593] for track '79' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-606] for track '80' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>