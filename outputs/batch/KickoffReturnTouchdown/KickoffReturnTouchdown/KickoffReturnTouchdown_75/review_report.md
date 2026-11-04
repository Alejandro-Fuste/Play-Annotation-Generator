# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_75`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 76
- **Ball Tracks:** 0
- **Action Segments:** 210
- **Validation Warnings:** 289
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 195
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage6 | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Left_Coverage6 | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `0` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `12` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `3` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `5` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `6` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 6 | START | 6 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage6 | `9` | `Group` | 6 | START | 6 | 85 |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage6 | `9` | `9` | 86 | START | 86 | 141 |
| ✅ EXACT | `Action_KickBall` | Left_Coverage6 | `9` | `9` | 142 | START | 142 | 149 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `21` | `21` | 268 | START | 268 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `21` | `21` | 287 | START | 287 | 347 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `21` | `21` | 620 | START | 620 | 627 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–469
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 347 | 262 | inferred_complete_timeline |
| `Action_None` | 360 | 382 | 23 | inferred_complete_timeline |
| `Action_None` | 389 | 469 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–325
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 325 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 6–417
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 417 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–337
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 321 | 236 | inferred_complete_timeline |
| `Action_None` | 326 | 337 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 6–596
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 281 | 196 | inferred_complete_timeline |
| `Action_None` | 287 | 292 | 6 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 347 | 44 | inferred_complete_timeline |
| `Action_None` | 361 | 596 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–616
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_KickApproach` | 86 | 141 | 56 | inferred_complete_timeline |
| `Action_KickBall` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 150 | 616 | 467 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 6–506
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 347 | 262 | inferred_complete_timeline |
| `Action_None` | 350 | 353 | 4 | inferred_complete_timeline |
| `Action_None` | 356 | 506 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–511
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 347 | 262 | inferred_complete_timeline |
| `Action_None` | 361 | 455 | 95 | inferred_complete_timeline |
| `Action_None` | 457 | 511 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–469
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 345 | 260 | inferred_complete_timeline |
| `Action_None` | 352 | 469 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 6–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 629 | 544 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–629
- **Visible Samples:** 622

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 357 | 272 | inferred_complete_timeline |
| `Action_None` | 360 | 629 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–326
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 256 | 171 | inferred_complete_timeline |
| `Action_None` | 263 | 326 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–623
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 278 | 193 | inferred_complete_timeline |
| `Action_None` | 284 | 314 | 31 | inferred_complete_timeline |
| `Action_None` | 316 | 623 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–435
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 345 | 260 | inferred_complete_timeline |
| `Action_None` | 350 | 369 | 20 | inferred_complete_timeline |
| `Action_None` | 375 | 435 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 6–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 281 | 196 | inferred_complete_timeline |
| `Action_None` | 285 | 316 | 32 | inferred_complete_timeline |
| `Action_None` | 319 | 629 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–628
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 628 | 543 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 6–629
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 267 | 262 | inferred_complete_timeline |
| `Action_CatchKick` | 268 | 275 | 8 | inferred_complete_timeline |
| `Action_None` | 276 | 286 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 287 | 347 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 354 | 395 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 398 | 619 | 222 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 620 | 627 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 628 | 629 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 6–629
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 78 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 125 | 38 | inferred_complete_timeline |
| `Action_None` | 162 | 629 | 468 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–416
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 345 | 260 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 416 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–378
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 347 | 262 | inferred_complete_timeline |
| `Action_None` | 363 | 378 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 6–446
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 85 | 80 | inferred_complete_timeline |
| `Action_None` | 86 | 125 | 40 | inferred_complete_timeline |
| `Action_None` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 345 | 203 | inferred_complete_timeline |
| `Action_None` | 361 | 369 | 9 | inferred_complete_timeline |
| `Action_None` | 374 | 446 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 6–629 | 624 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 6–218 | 210 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 6–143 | 50 | 9 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 40–62 | 21 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 58–202 | 44 | 9 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 111–147 | 22 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 175–266 | 67 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 178–194 | 8 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 203–205 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 212–215 | 4 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 223–235 | 6 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 229–286 | 15 | 4 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 248–250 | 3 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 270–279 | 10 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 330–629 | 297 | 2 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 330–442 | 32 | 7 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 336–343 | 8 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 366–488 | 121 | 2 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 369–629 | 259 | 2 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 395–455 | 52 | 4 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 455–464 | 10 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 501–543 | 36 | 4 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 504–518 | 11 | 3 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 512–514 | 3 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 519–541 | 6 | 2 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 536–537 | 2 | 1 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 536–542 | 7 | 1 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 538–560 | 7 | 2 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 543–616 | 31 | 3 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 554–627 | 64 | 4 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 559–629 | 65 | 4 | Undefined position; Undefined team |
| `57` | `82` | Position_Unknown | Team_Unknown | 561–562 | 2 | 1 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 573–574 | 2 | 1 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 573–624 | 30 | 6 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 575–578 | 4 | 1 | Undefined position; Undefined team |
| `61` | `91` | Position_Unknown | Team_Unknown | 575–618 | 34 | 2 | Undefined position; Undefined team |
| `62` | `93` | Position_Unknown | Team_Unknown | 578–628 | 50 | 2 | Undefined position; Undefined team |
| `63` | `95` | Position_Unknown | Team_Unknown | 578–629 | 41 | 4 | Undefined position; Undefined team |
| `64` | `97` | Position_Unknown | Team_Unknown | 586–601 | 16 | 1 | Undefined position; Undefined team |
| `65` | `98` | Position_Unknown | Team_Unknown | 587–609 | 10 | 2 | Undefined position; Undefined team |
| `66` | `100` | Position_Unknown | Team_Unknown | 592–598 | 7 | 1 | Undefined position; Undefined team |
| `67` | `105` | Position_Unknown | Team_Unknown | 594–615 | 12 | 3 | Undefined position; Undefined team |
| `68` | `110` | Position_Unknown | Team_Unknown | 603–629 | 19 | 2 | Undefined position; Undefined team |
| `69` | `111` | Position_Unknown | Team_Unknown | 604–608 | 4 | 2 | Undefined position; Undefined team |
| `70` | `112` | Position_Unknown | Team_Unknown | 606–616 | 7 | 2 | Undefined position; Undefined team |
| `71` | `113` | Position_Unknown | Team_Unknown | 607–627 | 16 | 2 | Undefined position; Undefined team |
| `72` | `115` | Position_Unknown | Team_Unknown | 611–614 | 4 | 1 | Undefined position; Undefined team |
| `73` | `116` | Position_Unknown | Team_Unknown | 611–612 | 2 | 1 | Undefined position; Undefined team |
| `74` | `119` | Position_Unknown | Team_Unknown | 616–619 | 4 | 1 | Undefined position; Undefined team |
| `75` | `120` | Position_Unknown | Team_Unknown | 617–619 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `22` (actor_track_id `22`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 176 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 151: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 152: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [86-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-278] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-623] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-326] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-321] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-337] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-347] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-382] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-469] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-417] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-347] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-455] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-511] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-345] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-469] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-616] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-628] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-357] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-347] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-596] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-347] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-506] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-316] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-629] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-345] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-369] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-435] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-347] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-378] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-345] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-416] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-345] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-369] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-446] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-205] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-218] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [287-347] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-351] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [354-395] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-125] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-11] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-18] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-53] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-70] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-168] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-121] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-231] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-234] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-279] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-347] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-629] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-347] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-437] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-343] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-446] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-488] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-443] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-629] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-400] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-408] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-429] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-455] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-464] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-505] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-513] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-539] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-512] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-541] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-542] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-542] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-616] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-611] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-620] for track '55' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-627] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-565] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-618] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-624] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-629] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-578] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-588] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-608] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-624] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-578] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-580] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-618] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-588] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-628] for track '62' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-589] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-597] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-622] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-601] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-609] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-598] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-611] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-615] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-618] for track '68' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-605] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-610] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-616] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-615] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [621-627] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-614] for track '72' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-619] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-619] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>