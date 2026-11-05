# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_66`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 281
- **Validation Warnings:** 333
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 266
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `54` | `41` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | `1` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing1 | `4` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing3 | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing2 | `9` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `0` | `0` | 26 | START | 26 | 92 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 63 | END | 63 | 63 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 93 | START | 93 | 112 |
| ⚠️ START CHANGED | `Action_CatchPunt` | Position_Unknown | `23` | `21` | 234 | START | 245 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `21` | 264 | START | 264 | 286 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `54` | `41` | 643 | START | 643 | 644 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_None` | 86 | 108 | 23 | inferred_complete_timeline |
| `Action_None` | 111 | 226 | 116 | inferred_complete_timeline |
| `Action_None` | 239 | 320 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 114 | 89 | inferred_complete_timeline |
| `Action_None` | 129 | 165 | 37 | inferred_complete_timeline |
| `Action_None` | 213 | 243 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_LongSnap` | 26 | 92 | 67 | inferred_complete_timeline |
| `Action_None` | 93 | 179 | 87 | inferred_complete_timeline |
| `Action_None` | 182 | 191 | 10 | inferred_complete_timeline |
| `Action_None` | 194 | 214 | 21 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 228 | 394 | 167 | inferred_complete_timeline |
| `Action_None` | 399 | 400 | 2 | inferred_complete_timeline |
| `Action_None` | 402 | 406 | 5 | inferred_complete_timeline |
| `Action_None` | 408 | 416 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–640
- **Visible Samples:** 602

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 194 | 207 | 14 | inferred_complete_timeline |
| `Action_None` | 215 | 272 | 58 | inferred_complete_timeline |
| `Action_None` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 502 | 214 | inferred_complete_timeline |
| `Action_None` | 512 | 515 | 4 | inferred_complete_timeline |
| `Action_None` | 521 | 618 | 98 | inferred_complete_timeline |
| `Action_None` | 622 | 623 | 2 | inferred_complete_timeline |
| `Action_None` | 630 | 640 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–653
- **Visible Samples:** 601

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_None` | 64 | 92 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 93 | 112 | 20 | inferred_complete_timeline |
| `Action_None` | 113 | 432 | 320 | inferred_complete_timeline |
| `Action_None` | 435 | 515 | 81 | inferred_complete_timeline |
| `Action_None` | 517 | 522 | 6 | inferred_complete_timeline |
| `Action_None` | 524 | 543 | 20 | inferred_complete_timeline |
| `Action_None` | 546 | 554 | 9 | inferred_complete_timeline |
| `Action_None` | 557 | 567 | 11 | inferred_complete_timeline |
| `Action_None` | 572 | 575 | 4 | inferred_complete_timeline |
| `Action_None` | 581 | 601 | 21 | inferred_complete_timeline |
| `Action_None` | 606 | 614 | 9 | inferred_complete_timeline |
| `Action_None` | 625 | 628 | 4 | inferred_complete_timeline |
| `Action_None` | 651 | 653 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 177 | 152 | inferred_complete_timeline |
| `Action_None` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_None` | 196 | 209 | 14 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 384 | 165 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 346 | 321 | inferred_complete_timeline |
| `Action_None` | 348 | 383 | 36 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 419 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 653

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 222 | 197 | inferred_complete_timeline |
| `Action_None` | 228 | 471 | 244 | inferred_complete_timeline |
| `Action_None` | 474 | 659 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 653

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 297 | 272 | inferred_complete_timeline |
| `Action_None` | 299 | 445 | 147 | inferred_complete_timeline |
| `Action_None` | 448 | 625 | 178 | inferred_complete_timeline |
| `Action_None` | 630 | 659 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–348
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 56 | 31 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 240 | 140 | inferred_complete_timeline |
| `Action_None` | 246 | 348 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 115 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 94 | 69 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 149 | 42 | inferred_complete_timeline |
| `Action_None` | 158 | 230 | 73 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–530
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 33 | 67 | 35 | inferred_complete_timeline |
| `Action_None` | 71 | 79 | 9 | inferred_complete_timeline |
| `Action_None` | 92 | 173 | 82 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 189 | 251 | 63 | inferred_complete_timeline |
| `Action_None` | 253 | 265 | 13 | inferred_complete_timeline |
| `Action_None` | 276 | 370 | 95 | inferred_complete_timeline |
| `Action_None` | 372 | 381 | 10 | inferred_complete_timeline |
| `Action_None` | 389 | 443 | 55 | inferred_complete_timeline |
| `Action_None` | 449 | 530 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 644

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 118 | 93 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_None` | 138 | 659 | 522 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–485
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 54 | 29 | inferred_complete_timeline |
| `Action_None` | 58 | 99 | 42 | inferred_complete_timeline |
| `Action_None` | 101 | 118 | 18 | inferred_complete_timeline |
| `Action_None` | 120 | 224 | 105 | inferred_complete_timeline |
| `Action_None` | 226 | 273 | 48 | inferred_complete_timeline |
| `Action_None` | 277 | 374 | 98 | inferred_complete_timeline |
| `Action_None` | 378 | 485 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 79 | 54 | inferred_complete_timeline |
| `Action_None` | 82 | 104 | 23 | inferred_complete_timeline |
| `Action_None` | 107 | 140 | 34 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–160 | 149 | 7 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–289 | 226 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 9–116 | 100 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 30–659 | 562 | 12 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 84–239 | 144 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 114–659 | 501 | 15 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 127–212 | 64 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 127–659 | 494 | 13 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 143–218 | 38 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 163–530 | 348 | 8 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 178–285 | 14 | 4 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 197–659 | 378 | 11 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 255–372 | 114 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 255–659 | 388 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 261–319 | 49 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 341–429 | 88 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 344–506 | 155 | 5 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 362–427 | 66 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 365–385 | 12 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 379–659 | 238 | 6 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 391–659 | 259 | 5 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 405–659 | 255 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 409–411 | 3 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 423–431 | 9 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 423–659 | 224 | 6 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 446–659 | 207 | 7 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 465–659 | 189 | 5 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 475–659 | 185 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 514–553 | 35 | 4 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 530–565 | 26 | 5 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 533–535 | 3 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 533–659 | 122 | 4 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 534–535 | 2 | 1 | Undefined position; Undefined team |
| `49` | `65` | Position_Unknown | Team_Unknown | 536–659 | 124 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 545–553 | 7 | 2 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 553–581 | 16 | 3 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 562–573 | 5 | 2 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 598–600 | 3 | 1 | Undefined position; Undefined team |
| `54` | `73` | Position_Unknown | Team_Unknown | 610–615 | 6 | 1 | Undefined position; Undefined team |
| `55` | `76` | Position_Unknown | Team_Unknown | 638–642 | 5 | 1 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 638–641 | 4 | 1 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 653–659 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchPunt` for actor_track_id `23` (Position_Unknown): Annotated start 234 != Inferred start 245
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (7 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `54` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Wing1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Wing3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Wing2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 244 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 134: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 134: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [93-179] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-214] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-394] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-406] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-207] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-272] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-502] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-515] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-618] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-623] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-640] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-346] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-383] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-419] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-432] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-515] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-522] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-543] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-554] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-567] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-575] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-601] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-614] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-628] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [651-653] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-273] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-374] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-485] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-165] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-297] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-445] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-625] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-471] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-384] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-173] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-251] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-370] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-381] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-443] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-530] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-230] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-226] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-148] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-280] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-289] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-56] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-348] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-330] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-385] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-398] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-462] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-485] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-515] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-558] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-620] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-624] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-649] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-161] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-199] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-133] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-138] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-171] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [264-286] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-347] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [349-352] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [360-400] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [402-420] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [423-471] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-290] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-321] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-488] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-493] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-659] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-346] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-385] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-430] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-525] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-530] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-243] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-522] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-536] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-561] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-585] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-611] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-284] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-372] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-330] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-454] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-638] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-396] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-429] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-365] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-387] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-491] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-506] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-427] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-374] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-478] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-490] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-551] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-558] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-582] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-659] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-445] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-516] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-530] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-659] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-431] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-474] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-484] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-505] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-545] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-587] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-659] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-538] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [541-543] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-594] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [596-642] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [643-644] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-476] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-521] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-527] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-591] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-659] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-520] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-529] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-542] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-536] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-546] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-535] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-544] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-603] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-659] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-547] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-553] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-562] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-567] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-600] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-615] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-642] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-641] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>