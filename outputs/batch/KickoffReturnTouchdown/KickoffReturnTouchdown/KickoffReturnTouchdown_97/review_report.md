# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_97

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_97`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 60
- **Ball Tracks:** 0
- **Action Segments:** 281
- **Validation Warnings:** 330
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 267
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `4` | `4` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `53` | `44` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `8` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `15` | `15` | 16 | START | 16 | 81 |
| ✅ EXACT | `Action_KickBall` | Kicker | `15` | `15` | 82 | START | 82 | 87 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `4` | `4` | 197 | START | 197 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `4` | `4` | 211 | START | 211 | 469 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `53` | `44` | 645 | START | 645 | 659 |

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
- **Visible Frames:** 0–377
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_KickApproach` | 16 | 81 | 66 | inferred_complete_timeline |
| `Action_KickBall` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 88 | 336 | 249 | inferred_complete_timeline |
| `Action_None` | 346 | 348 | 3 | inferred_complete_timeline |
| `Action_None` | 362 | 377 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 280 | 265 | inferred_complete_timeline |
| `Action_None` | 286 | 310 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–396
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 210 | 195 | inferred_complete_timeline |
| `Action_None` | 225 | 252 | 28 | inferred_complete_timeline |
| `Action_None` | 260 | 262 | 3 | inferred_complete_timeline |
| `Action_None` | 267 | 323 | 57 | inferred_complete_timeline |
| `Action_None` | 330 | 336 | 7 | inferred_complete_timeline |
| `Action_None` | 395 | 396 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 137 | 122 | inferred_complete_timeline |
| `Action_None` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 324 | 159 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 347 | 13 | inferred_complete_timeline |
| `Action_None` | 349 | 447 | 99 | inferred_complete_timeline |
| `Action_None` | 449 | 529 | 81 | inferred_complete_timeline |
| `Action_None` | 535 | 541 | 7 | inferred_complete_timeline |
| `Action_None` | 546 | 547 | 2 | inferred_complete_timeline |
| `Action_None` | 555 | 557 | 3 | inferred_complete_timeline |
| `Action_None` | 626 | 659 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 640

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 165 | 150 | inferred_complete_timeline |
| `Action_None` | 167 | 309 | 143 | inferred_complete_timeline |
| `Action_None` | 311 | 358 | 48 | inferred_complete_timeline |
| `Action_None` | 373 | 485 | 113 | inferred_complete_timeline |
| `Action_None` | 487 | 631 | 145 | inferred_complete_timeline |
| `Action_None` | 635 | 659 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 303 | 288 | inferred_complete_timeline |
| `Action_None` | 312 | 322 | 11 | inferred_complete_timeline |
| `Action_None` | 324 | 343 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 214 | 199 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 252 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 308 | 293 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–346
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 346 | 331 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 129 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 103 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 102 | 87 | inferred_complete_timeline |
| `Action_None` | 108 | 112 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 112 | 97 | inferred_complete_timeline |
| `Action_None` | 114 | 122 | 9 | inferred_complete_timeline |
| `Action_None` | 132 | 147 | 16 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 159 | 269 | 111 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 99 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–430
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 106 | 91 | inferred_complete_timeline |
| `Action_None` | 111 | 134 | 24 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 197 | 48 | inferred_complete_timeline |
| `Action_None` | 200 | 430 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_CatchKick` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 469 | 259 | inferred_complete_timeline |
| `Action_BallCarry` | 471 | 486 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 506 | 507 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 512 | 513 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 516 | 527 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 535 | 541 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 543 | 544 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 546 | 659 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–579
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 428 | 413 | inferred_complete_timeline |
| `Action_None` | 441 | 444 | 4 | inferred_complete_timeline |
| `Action_None` | 454 | 507 | 54 | inferred_complete_timeline |
| `Action_None` | 513 | 579 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 648

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 447 | 432 | inferred_complete_timeline |
| `Action_None` | 449 | 577 | 129 | inferred_complete_timeline |
| `Action_None` | 580 | 588 | 9 | inferred_complete_timeline |
| `Action_None` | 598 | 659 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 335 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 292 | 277 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–343 | 334 | 7 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 8–406 | 365 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 140–608 | 445 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 166–409 | 133 | 8 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 169–570 | 385 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 182–267 | 49 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 192–491 | 255 | 13 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 260–264 | 5 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 270–535 | 236 | 8 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 287–659 | 344 | 8 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 308–541 | 130 | 11 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 332–487 | 153 | 4 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 340–364 | 25 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 347–659 | 305 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 347–384 | 38 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 355–510 | 111 | 8 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 358–659 | 283 | 3 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 367–575 | 148 | 12 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 370–659 | 290 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 380–429 | 38 | 3 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 435–506 | 68 | 3 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 440–441 | 2 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 441–659 | 138 | 16 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 457–659 | 178 | 7 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 461–565 | 90 | 6 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 491–659 | 169 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 496–542 | 47 | 1 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 496–497 | 2 | 1 | Undefined position; Undefined team |
| `50` | `65` | Position_Unknown | Team_Unknown | 511–631 | 26 | 5 | Undefined position; Undefined team |
| `51` | `66` | Position_Unknown | Team_Unknown | 524–566 | 33 | 5 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 539–559 | 12 | 3 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 600–659 | 60 | 1 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 615–658 | 21 | 3 | Undefined position; Undefined team |
| `55` | `76` | Position_Unknown | Team_Unknown | 623–651 | 18 | 3 | Undefined position; Undefined team |
| `56` | `77` | Position_Unknown | Team_Unknown | 624–651 | 20 | 3 | Undefined position; Undefined team |
| `57` | `78` | Position_Unknown | Team_Unknown | 631–659 | 14 | 3 | Undefined position; Undefined team |
| `58` | `79` | Position_Unknown | Team_Unknown | 631–658 | 27 | 2 | Undefined position; Undefined team |
| `59` | `81` | Position_Unknown | Team_Unknown | 653–658 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (8 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 248 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 196: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action 'Action_None' range [16-106] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-134] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-197] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-430] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-428] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-507] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-579] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-292] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-335] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-469] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [471-486] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [506-507] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [512-513] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [516-527] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [535-541] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [543-544] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-447] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-577] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-588] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-659] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-309] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-358] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-485] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-631] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-659] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-308] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-122] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-147] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-269] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-179] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-324] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-343] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-137] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-347] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-447] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-529] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-541] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-659] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-280] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-310] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-252] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-336] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-336] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-377] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-303] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-343] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-346] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-129] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-15] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-21] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-397] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-243] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-327] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-608] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-238] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-302] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-349] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-397] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-282] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-541] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-553] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-570] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-287] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-312] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-408] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-428] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-447] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-486] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-491] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-264] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-306] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-315] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-338] for track '30' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-364] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-383] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-446] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-508] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-535] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-404] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-411] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-477] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-572] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-581] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-585] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-589] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-346] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-424] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-432] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-447] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-458] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-483] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-488] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-503] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-527] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-541] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-344] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-366] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-483] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-364] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-384] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-423] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-432] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-446] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-487] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-510] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-454] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-499] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-407] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-430] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-516] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-527] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-542] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-561] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-575] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-408] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-429] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-439] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-447] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-506] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-442] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-455] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-468] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-495] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-499] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-514] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-531] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [533-542] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-547] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-560] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [595-607] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [618-632] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [634-639] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [645-659] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-465] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-589] for track '45' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-605] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-620] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-634] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-526] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-561] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-659] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-542] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-522] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-531] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-585] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-631] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-531] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-534] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-542] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-552] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-566] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-542] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-559] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-618] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-625] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-658] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-632] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [638-641] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-651] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-637] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-651] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-633] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-652] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-659] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-652] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [654-658] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-658] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>