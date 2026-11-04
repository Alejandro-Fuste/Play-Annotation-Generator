# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_46`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 719
- **Player Tracks:** 82
- **Ball Tracks:** 0
- **Action Segments:** 316
- **Validation Warnings:** 407
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
- **Inferred Coverage Segments (Action_None):** 299
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | defense | `0` | `0` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `12` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `13` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `14` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `16` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `17` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `18` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `19` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `9` | `Group` | 0 | START | 0 | 81 |
| ✅ EXACT | `Action_KickApproach` | Position_Unknown | `21` | `20` | 82 | START | 82 | 147 |
| ✅ EXACT | `Action_KickBall` | Position_Unknown | `21` | `20` | 148 | START | 148 | 153 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `0` | `0` | 262 | START | 262 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner2 | `0` | `0` | 290 | START | 290 | 355 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `8` | `8` | 715 | START | 715 | 719 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–616
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 248 | 167 | inferred_complete_timeline |
| `Action_None` | 251 | 375 | 125 | inferred_complete_timeline |
| `Action_None` | 391 | 434 | 44 | inferred_complete_timeline |
| `Action_None` | 442 | 453 | 12 | inferred_complete_timeline |
| `Action_None` | 455 | 468 | 14 | inferred_complete_timeline |
| `Action_None` | 471 | 616 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 138 | 57 | inferred_complete_timeline |
| `Action_None` | 141 | 158 | 18 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 258 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 132 | 51 | inferred_complete_timeline |
| `Action_None` | 134 | 209 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 327 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 233 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 697

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 240 | 159 | inferred_complete_timeline |
| `Action_None` | 247 | 329 | 83 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 339 | 365 | 27 | inferred_complete_timeline |
| `Action_None` | 367 | 504 | 138 | inferred_complete_timeline |
| `Action_None` | 506 | 509 | 4 | inferred_complete_timeline |
| `Action_None` | 515 | 709 | 195 | inferred_complete_timeline |
| `Action_None` | 713 | 719 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 6 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 66 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 282 | 128 | inferred_complete_timeline |
| `Action_None` | 285 | 312 | 28 | inferred_complete_timeline |
| `Action_None` | 316 | 385 | 70 | inferred_complete_timeline |
| `Action_None` | 394 | 397 | 4 | inferred_complete_timeline |
| `Action_None` | 399 | 417 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–515
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 395 | 314 | inferred_complete_timeline |
| `Action_None` | 397 | 426 | 30 | inferred_complete_timeline |
| `Action_None` | 439 | 509 | 71 | inferred_complete_timeline |
| `Action_None` | 511 | 515 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 235 | 154 | inferred_complete_timeline |
| `Action_None` | 237 | 254 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–711
- **Visible Samples:** 642

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 177 | 96 | inferred_complete_timeline |
| `Action_None` | 179 | 258 | 80 | inferred_complete_timeline |
| `Action_None` | 265 | 339 | 75 | inferred_complete_timeline |
| `Action_None` | 343 | 355 | 13 | inferred_complete_timeline |
| `Action_None` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_None` | 405 | 492 | 88 | inferred_complete_timeline |
| `Action_None` | 507 | 511 | 5 | inferred_complete_timeline |
| `Action_None` | 513 | 711 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 190 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 162 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 231 | 62 | inferred_complete_timeline |
| `Action_None` | 233 | 250 | 18 | inferred_complete_timeline |
| `Action_None` | 255 | 305 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 288 | 207 | inferred_complete_timeline |
| `Action_None` | 311 | 375 | 65 | inferred_complete_timeline |
| `Action_None` | 395 | 397 | 3 | inferred_complete_timeline |
| `Action_None` | 401 | 429 | 29 | inferred_complete_timeline |
| `Action_None` | 431 | 432 | 2 | inferred_complete_timeline |
| `Action_None` | 434 | 436 | 3 | inferred_complete_timeline |
| `Action_None` | 476 | 623 | 148 | inferred_complete_timeline |
| `Action_None` | 625 | 628 | 4 | inferred_complete_timeline |
| `Action_None` | 631 | 633 | 3 | inferred_complete_timeline |
| `Action_None` | 635 | 641 | 7 | inferred_complete_timeline |
| `Action_None` | 645 | 689 | 45 | inferred_complete_timeline |
| `Action_None` | 699 | 701 | 3 | inferred_complete_timeline |
| `Action_None` | 713 | 714 | 2 | inferred_complete_timeline |
| `Action_None` | 717 | 719 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–470
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 278 | 197 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 329 | 38 | inferred_complete_timeline |
| `Action_None` | 338 | 347 | 10 | inferred_complete_timeline |
| `Action_None` | 349 | 375 | 27 | inferred_complete_timeline |
| `Action_None` | 419 | 429 | 11 | inferred_complete_timeline |
| `Action_None` | 449 | 470 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 218 | 137 | inferred_complete_timeline |
| `Action_None` | 220 | 231 | 12 | inferred_complete_timeline |
| `Action_None` | 240 | 269 | 30 | inferred_complete_timeline |
| `Action_None` | 282 | 321 | 40 | inferred_complete_timeline |
| `Action_None` | 326 | 333 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 635

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 335 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 373 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 378 | 399 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 449 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 501 | 607 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 617 | 714 | 98 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 715 | 719 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 711

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_CatchKick` | 262 | 266 | 5 | inferred_complete_timeline |
| `Action_None` | 267 | 289 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 355 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 370 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 374 | 719 | 346 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–370
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 351 | 270 | inferred_complete_timeline |
| `Action_None` | 355 | 370 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 261 | 180 | inferred_complete_timeline |
| `Action_None` | 265 | 395 | 131 | inferred_complete_timeline |
| `Action_None` | 397 | 399 | 3 | inferred_complete_timeline |
| `Action_None` | 442 | 449 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 345 | 264 | inferred_complete_timeline |
| `Action_None` | 347 | 405 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 69–347 | 264 | 8 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 70–141 | 32 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 141–193 | 37 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 143–182 | 35 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 166–182 | 17 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 173–183 | 11 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 179–182 | 4 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 184–306 | 114 | 7 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 197–242 | 17 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 202–316 | 115 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 211–447 | 197 | 6 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 216–227 | 7 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 233–417 | 172 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 250–319 | 41 | 10 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 260–294 | 32 | 3 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 319–368 | 45 | 3 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 340–343 | 4 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 348–403 | 52 | 3 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 350–399 | 36 | 4 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 354–695 | 324 | 10 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 359–464 | 106 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 362–719 | 314 | 8 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 370–717 | 315 | 5 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 382–422 | 37 | 3 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 384–396 | 13 | 1 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 390–412 | 23 | 1 | Undefined position; Undefined team |
| `47` | `64` | Position_Unknown | Team_Unknown | 392–719 | 301 | 4 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 396–682 | 275 | 5 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 409–416 | 8 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 414–469 | 40 | 4 | Undefined position; Undefined team |
| `51` | `68` | Position_Unknown | Team_Unknown | 418–526 | 71 | 4 | Undefined position; Undefined team |
| `52` | `69` | Position_Unknown | Team_Unknown | 437–719 | 263 | 3 | Undefined position; Undefined team |
| `53` | `71` | Position_Unknown | Team_Unknown | 442–571 | 120 | 4 | Undefined position; Undefined team |
| `54` | `72` | Position_Unknown | Team_Unknown | 445–462 | 18 | 1 | Undefined position; Undefined team |
| `55` | `75` | Position_Unknown | Team_Unknown | 459–592 | 131 | 3 | Undefined position; Undefined team |
| `56` | `76` | Position_Unknown | Team_Unknown | 460–719 | 243 | 2 | Undefined position; Undefined team |
| `57` | `77` | Position_Unknown | Team_Unknown | 465–480 | 9 | 3 | Undefined position; Undefined team |
| `58` | `78` | Position_Unknown | Team_Unknown | 469–578 | 20 | 4 | Undefined position; Undefined team |
| `59` | `79` | Position_Unknown | Team_Unknown | 469–495 | 27 | 1 | Undefined position; Undefined team |
| `60` | `80` | Position_Unknown | Team_Unknown | 470–485 | 16 | 1 | Undefined position; Undefined team |
| `61` | `82` | Position_Unknown | Team_Unknown | 476–556 | 73 | 2 | Undefined position; Undefined team |
| `62` | `83` | Position_Unknown | Team_Unknown | 480–550 | 36 | 2 | Undefined position; Undefined team |
| `63` | `87` | Position_Unknown | Team_Unknown | 521–522 | 2 | 1 | Undefined position; Undefined team |
| `64` | `88` | Position_Unknown | Team_Unknown | 525–610 | 72 | 4 | Undefined position; Undefined team |
| `65` | `89` | Position_Unknown | Team_Unknown | 526–719 | 179 | 4 | Undefined position; Undefined team |
| `66` | `91` | Position_Unknown | Team_Unknown | 529–535 | 7 | 1 | Undefined position; Undefined team |
| `67` | `93` | Position_Unknown | Team_Unknown | 535–719 | 156 | 5 | Undefined position; Undefined team |
| `68` | `95` | Position_Unknown | Team_Unknown | 558–719 | 149 | 5 | Undefined position; Undefined team |
| `69` | `96` | Position_Unknown | Team_Unknown | 562–563 | 2 | 1 | Undefined position; Undefined team |
| `70` | `97` | Position_Unknown | Team_Unknown | 565–719 | 149 | 4 | Undefined position; Undefined team |
| `71` | `98` | Position_Unknown | Team_Unknown | 579–706 | 54 | 6 | Undefined position; Undefined team |
| `72` | `99` | Position_Unknown | Team_Unknown | 583–671 | 89 | 1 | Undefined position; Undefined team |
| `73` | `100` | Position_Unknown | Team_Unknown | 595–601 | 7 | 1 | Undefined position; Undefined team |
| `74` | `101` | Position_Unknown | Team_Unknown | 597–719 | 122 | 2 | Undefined position; Undefined team |
| `75` | `104` | Position_Unknown | Team_Unknown | 610–719 | 94 | 4 | Undefined position; Undefined team |
| `76` | `109` | Position_Unknown | Team_Unknown | 623–630 | 5 | 2 | Undefined position; Undefined team |
| `77` | `110` | Position_Unknown | Team_Unknown | 658–676 | 14 | 2 | Undefined position; Undefined team |
| `78` | `111` | Position_Unknown | Team_Unknown | 670–713 | 36 | 5 | Undefined position; Undefined team |
| `79` | `112` | Position_Unknown | Team_Unknown | 682–714 | 33 | 1 | Undefined position; Undefined team |
| `80` | `113` | Position_Unknown | Team_Unknown | 687–703 | 15 | 2 | Undefined position; Undefined team |
| `81` | `115` | Position_Unknown | Team_Unknown | 718–719 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ 62 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 62 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 124 |
| Missing visible bounding boxes during action | 282 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [290-355] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [362-370] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [374-719] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-351] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-370] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-321] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-278] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-375] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-429] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-470] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-395] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-449] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-288] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-375] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-429] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-436] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-623] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-628] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [631-633] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-641] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-689] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [699-701] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [713-714] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-258] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-339] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-355] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-492] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-711] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-327] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-335] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-373] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-399] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-449] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-607] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-240] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-365] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-504] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-709] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-345] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-405] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-395] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-426] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-509] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-515] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-209] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-231] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-250] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-305] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-327] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-248] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-375] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-434] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-453] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-468] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-616] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-138] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-158] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-312] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-385] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-417] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [82-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-186] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-231] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-342] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-347] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-110] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-182] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-209] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-273] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-290] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-306] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-316] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-397] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-447] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-323] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-366] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-417] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-326] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-371] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-397] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-370] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-399] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-363] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-371] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-459] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-587] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-605] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-621] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-628] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [630-691] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [693-695] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-464] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-365] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-374] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-389] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-450] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-473] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-531] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-719] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-633] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-642] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-681] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-708] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-717] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-399] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-417] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-396] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-412] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-413] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-455] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-493] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-426] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-436] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-525] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-682] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-416] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-427] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-445] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-469] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-434] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-479] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-526] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-441] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-557] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-541] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-552] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-568] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-462] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-588] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-700] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-473] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-474] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-486] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-495] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-485] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-546] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-508] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-550] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-534] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-549] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-604] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-553] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-564] for track '65' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-535] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-564] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-570] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-623] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [643-648] for track '67' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-583] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-617] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-658] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-662] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [664-719] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-603] for track '70' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-713] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-600] for track '71' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-620] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [681-684] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [688-689] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [694-696] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [703-706] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-671] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-601] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-618] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-655] for track '75' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [667-673] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-698] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [700-719] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-630] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [665-676] for track '77' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-672] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [675-676] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-683] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [686-708] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [712-713] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [682-714] for track '79' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [687-689] for track '80' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [692-703] for track '80' has 1 frames without a visible bounding box.
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

</details>