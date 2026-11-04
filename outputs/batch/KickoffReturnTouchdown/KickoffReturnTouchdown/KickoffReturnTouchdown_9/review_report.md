# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_9`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 79
- **Ball Tracks:** 0
- **Action Segments:** 338
- **Validation Warnings:** 435
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 323
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `46` | `33` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `46` | `33` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `46` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `10` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `4` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `5` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `7` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `8` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `9` | `Group` | 0 | START | 0 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `10` | `10` | 56 | START | 56 | 125 |
| ✅ EXACT | `Action_KickBall` | Kicker | `10` | `10` | 146 | START | 146 | 147 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `46` | `33` | 252 | START | 252 | 257 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `46` | `33` | 268 | START | 268 | 394 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `46` | `33` | 603 | START | 603 | 615 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–466
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_KickApproach` | 56 | 125 | 70 | inferred_complete_timeline |
| `Action_KickApproach` | 129 | 145 | 17 | inferred_complete_timeline |
| `Action_KickBall` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 241 | 52 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 254 | 268 | 15 | inferred_complete_timeline |
| `Action_None` | 270 | 466 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 121 | 66 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 108 | 53 | inferred_complete_timeline |
| `Action_None` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_None` | 64 | 117 | 54 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 154 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 123 | 68 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 129 | 74 | inferred_complete_timeline |
| `Action_None` | 131 | 215 | 85 | inferred_complete_timeline |
| `Action_None` | 217 | 328 | 112 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |
| `Action_None` | 335 | 337 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 223 | 168 | inferred_complete_timeline |
| `Action_None` | 225 | 251 | 27 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 263 | 8 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 409 | 140 | inferred_complete_timeline |
| `Action_None` | 411 | 449 | 39 | inferred_complete_timeline |
| `Action_None` | 454 | 468 | 15 | inferred_complete_timeline |
| `Action_None` | 470 | 477 | 8 | inferred_complete_timeline |
| `Action_None` | 479 | 480 | 2 | inferred_complete_timeline |
| `Action_None` | 482 | 495 | 14 | inferred_complete_timeline |
| `Action_None` | 500 | 501 | 2 | inferred_complete_timeline |
| `Action_None` | 509 | 559 | 51 | inferred_complete_timeline |
| `Action_None` | 561 | 576 | 16 | inferred_complete_timeline |
| `Action_None` | 591 | 594 | 4 | inferred_complete_timeline |
| `Action_None` | 596 | 614 | 19 | inferred_complete_timeline |
| `Action_None` | 652 | 659 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–423
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 129 | 74 | inferred_complete_timeline |
| `Action_None` | 134 | 251 | 118 | inferred_complete_timeline |
| `Action_None` | 253 | 400 | 148 | inferred_complete_timeline |
| `Action_None` | 405 | 423 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 652

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 129 | 74 | inferred_complete_timeline |
| `Action_None` | 133 | 241 | 109 | inferred_complete_timeline |
| `Action_None` | 243 | 255 | 13 | inferred_complete_timeline |
| `Action_None` | 259 | 605 | 347 | inferred_complete_timeline |
| `Action_None` | 607 | 659 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–526
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 248 | 193 | inferred_complete_timeline |
| `Action_None` | 252 | 411 | 160 | inferred_complete_timeline |
| `Action_None` | 413 | 415 | 3 | inferred_complete_timeline |
| `Action_None` | 421 | 422 | 2 | inferred_complete_timeline |
| `Action_None` | 425 | 515 | 91 | inferred_complete_timeline |
| `Action_None` | 522 | 526 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–507
- **Visible Samples:** 484

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 257 | 202 | inferred_complete_timeline |
| `Action_None` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_None` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_None` | 281 | 413 | 133 | inferred_complete_timeline |
| `Action_None` | 415 | 468 | 54 | inferred_complete_timeline |
| `Action_None` | 476 | 488 | 13 | inferred_complete_timeline |
| `Action_None` | 490 | 507 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 351 | 296 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 285 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–436
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 436 | 381 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 242 | 187 | inferred_complete_timeline |
| `Action_None` | 244 | 359 | 116 | inferred_complete_timeline |
| `Action_None` | 362 | 365 | 4 | inferred_complete_timeline |
| `Action_None` | 371 | 376 | 6 | inferred_complete_timeline |
| `Action_None` | 382 | 385 | 4 | inferred_complete_timeline |
| `Action_None` | 390 | 395 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 659 | 604 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 157–655 | 468 | 16 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 165–263 | 95 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 165–171 | 7 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 167–189 | 16 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 176–651 | 469 | 6 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 182–659 | 478 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 185–659 | 464 | 5 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 190–356 | 125 | 7 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 195–301 | 95 | 6 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 201–243 | 23 | 6 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 203–615 | 398 | 12 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 208–245 | 38 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 246–368 | 117 | 3 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 251–517 | 255 | 5 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 276–659 | 328 | 5 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 290–617 | 240 | 7 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 304–353 | 4 | 2 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 312–550 | 133 | 9 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 319–327 | 7 | 2 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 325–344 | 20 | 1 | Undefined position; Undefined team |
| `44` | `64` | Position_Unknown | Team_Unknown | 334–348 | 15 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 336–350 | 15 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 345–659 | 286 | 12 | Undefined position; Undefined team |
| `47` | `70` | Position_Unknown | Team_Unknown | 354–376 | 20 | 3 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 359–382 | 23 | 2 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 375–659 | 257 | 10 | Undefined position; Undefined team |
| `50` | `76` | Position_Unknown | Team_Unknown | 382–616 | 174 | 5 | Undefined position; Undefined team |
| `51` | `77` | Position_Unknown | Team_Unknown | 395–659 | 258 | 4 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 402–659 | 219 | 15 | Undefined position; Undefined team |
| `53` | `79` | Position_Unknown | Team_Unknown | 407–589 | 167 | 9 | Undefined position; Undefined team |
| `54` | `83` | Position_Unknown | Team_Unknown | 431–567 | 65 | 5 | Undefined position; Undefined team |
| `55` | `84` | Position_Unknown | Team_Unknown | 441–659 | 167 | 8 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 443–490 | 35 | 4 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 450–457 | 8 | 1 | Undefined position; Undefined team |
| `58` | `91` | Position_Unknown | Team_Unknown | 490–656 | 80 | 11 | Undefined position; Undefined team |
| `59` | `92` | Position_Unknown | Team_Unknown | 494–633 | 90 | 7 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 494–529 | 13 | 2 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 500–526 | 21 | 2 | Undefined position; Undefined team |
| `62` | `95` | Position_Unknown | Team_Unknown | 509–534 | 15 | 3 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 511–513 | 3 | 1 | Undefined position; Undefined team |
| `64` | `97` | Position_Unknown | Team_Unknown | 527–583 | 21 | 8 | Undefined position; Undefined team |
| `65` | `99` | Position_Unknown | Team_Unknown | 536–545 | 9 | 2 | Undefined position; Undefined team |
| `66` | `100` | Position_Unknown | Team_Unknown | 537–659 | 115 | 6 | Undefined position; Undefined team |
| `67` | `102` | Position_Unknown | Team_Unknown | 589–599 | 11 | 1 | Undefined position; Undefined team |
| `68` | `103` | Position_Unknown | Team_Unknown | 591–592 | 2 | 1 | Undefined position; Undefined team |
| `69` | `104` | Position_Unknown | Team_Unknown | 600–601 | 2 | 1 | Undefined position; Undefined team |
| `70` | `105` | Position_Unknown | Team_Unknown | 603–608 | 6 | 1 | Undefined position; Undefined team |
| `71` | `107` | Position_Unknown | Team_Unknown | 607–659 | 53 | 1 | Undefined position; Undefined team |
| `72` | `108` | Position_Unknown | Team_Unknown | 607–608 | 2 | 1 | Undefined position; Undefined team |
| `73` | `109` | Position_Unknown | Team_Unknown | 614–659 | 34 | 3 | Undefined position; Undefined team |
| `74` | `110` | Position_Unknown | Team_Unknown | 623–624 | 2 | 1 | Undefined position; Undefined team |
| `75` | `114` | Position_Unknown | Team_Unknown | 629–632 | 4 | 1 | Undefined position; Undefined team |
| `76` | `115` | Position_Unknown | Team_Unknown | 632–638 | 7 | 1 | Undefined position; Undefined team |
| `77` | `121` | Position_Unknown | Team_Unknown | 656–659 | 4 | 1 | Undefined position; Undefined team |
| `78` | `123` | Position_Unknown | Team_Unknown | 658–659 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `46` (8 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 63 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 63 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 126 |
| Missing visible bounding boxes during action | 308 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [56-242] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-359] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-376] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-385] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-395] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-413] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-468] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-488] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-507] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-351] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-215] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-328] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-248] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-411] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-415] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-515] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-526] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-436] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-241] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-605] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-123] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-223] for track '9' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-251] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-263] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-409] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-449] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-468] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-477] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-495] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-559] for track '9' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-576] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-614] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [56-125] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [146-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-241] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-466] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-251] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-400] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-423] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-285] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-154] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-230] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-313] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-428] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-457] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-471] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-521] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-530] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-550] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-603] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-655] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-195] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-254] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-583] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-589] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-651] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-659] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-487] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-526] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-543] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-243] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-280] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-319] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-245] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-275] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-301] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-394] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [396-397] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [399-406] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [408-410] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [413-417] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [421-423] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [428-432] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [603-615] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-245] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-340] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-368] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-479] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-498] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-503] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-322] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-450] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-493] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-428] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-543] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-574] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-610] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-617] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-342] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-445] for track '41' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-542] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-550] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-344] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-348] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-350] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-371] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-468] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-486] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-492] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-503] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-513] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-534] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-649] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-376] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-379] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-493] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-508] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-527] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-538] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-552] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-571] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-659] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-612] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-616] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-412] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-519] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-556] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-659] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-505] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-514] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-551] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-571] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-587] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-594] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-613] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-637] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-640] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-651] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-428] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-512] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-518] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-532] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-547] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-576] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-589] for track '53' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-434] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-547] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-559] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-567] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-465] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-483] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-498] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-523] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-607] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-611] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-447] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-463] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-479] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-457] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-557] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-575] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-597] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-613] for track '58' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-632] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-644] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-651] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [655-656] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-496] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-556] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-561] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-575] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-614] for track '59' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-633] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-529] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-513] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-526] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-519] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-513] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-572] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-579] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-541] for track '65' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-539] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-553] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-574] for track '66' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-579] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-659] for track '66' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-599] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-608] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-659] for track '71' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-617] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-629] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-624] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-632] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-638] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [656-659] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>