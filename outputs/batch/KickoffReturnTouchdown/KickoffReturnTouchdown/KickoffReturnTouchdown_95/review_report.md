# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_95`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 162
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | defense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner2 | defense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | defense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `15` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `10` | `10` | 21 | START | 21 | 54 |
| ✅ EXACT | `Action_KickBall` | Kicker | `10` | `10` | 61 | START | 61 | 66 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner2 | `19` | `19` | 168 | START | 168 | 178 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner2 | `19` | `19` | 192 | START | 192 | 347 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner2 | `19` | `19` | 597 | START | N/A | N/A |

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
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_KickApproach` | 21 | 54 | 34 | inferred_complete_timeline |
| `Action_KickApproach` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_KickBall` | 61 | 66 | 6 | inferred_complete_timeline |
| `Action_None` | 67 | 77 | 11 | inferred_complete_timeline |
| `Action_None` | 79 | 416 | 338 | inferred_complete_timeline |
| `Action_None` | 419 | 537 | 119 | inferred_complete_timeline |
| `Action_None` | 541 | 599 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 355 | 335 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 599 | 579 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–492
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 71 | 51 | inferred_complete_timeline |
| `Action_None` | 73 | 302 | 230 | inferred_complete_timeline |
| `Action_None` | 306 | 492 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–498
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 297 | 277 | inferred_complete_timeline |
| `Action_None` | 308 | 498 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 211 | 191 | inferred_complete_timeline |
| `Action_None` | 213 | 250 | 38 | inferred_complete_timeline |
| `Action_None` | 258 | 310 | 53 | inferred_complete_timeline |
| `Action_None` | 316 | 512 | 197 | inferred_complete_timeline |
| `Action_None` | 515 | 599 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–551
- **Visible Samples:** 547

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 298 | 278 | inferred_complete_timeline |
| `Action_None` | 304 | 551 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–475
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 105 | 85 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 218 | 90 | inferred_complete_timeline |
| `Action_None` | 227 | 276 | 50 | inferred_complete_timeline |
| `Action_None` | 281 | 284 | 4 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 475 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 116 | 96 | inferred_complete_timeline |
| `Action_None` | 121 | 587 | 467 | inferred_complete_timeline |
| `Action_None` | 589 | 599 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–457
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 457 | 437 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 303 | 283 | inferred_complete_timeline |
| `Action_None` | 309 | 373 | 65 | inferred_complete_timeline |
| `Action_None` | 376 | 382 | 7 | inferred_complete_timeline |
| `Action_None` | 385 | 387 | 3 | inferred_complete_timeline |
| `Action_None` | 389 | 599 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 215 | 195 | inferred_complete_timeline |
| `Action_None` | 225 | 227 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 306 | 75 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–313
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 221 | 201 | inferred_complete_timeline |
| `Action_None` | 232 | 296 | 65 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 307 | 4 | inferred_complete_timeline |
| `Action_None` | 310 | 313 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 213 | 193 | inferred_complete_timeline |
| `Action_None` | 215 | 223 | 9 | inferred_complete_timeline |
| `Action_None` | 229 | 263 | 35 | inferred_complete_timeline |
| `Action_None` | 265 | 353 | 89 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 192 | 172 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 190 | 170 | inferred_complete_timeline |
| `Action_None` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_None` | 206 | 232 | 27 | inferred_complete_timeline |
| `Action_None` | 237 | 262 | 26 | inferred_complete_timeline |
| `Action_None` | 271 | 305 | 35 | inferred_complete_timeline |
| `Action_None` | 308 | 320 | 13 | inferred_complete_timeline |
| `Action_None` | 323 | 432 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–460
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 310 | 290 | inferred_complete_timeline |
| `Action_None` | 313 | 460 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_CatchKick` | 168 | 178 | 11 | inferred_complete_timeline |
| `Action_None` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 347 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–572
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 562 | 542 | inferred_complete_timeline |
| `Action_None` | 565 | 568 | 4 | inferred_complete_timeline |
| `Action_None` | 570 | 572 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–513
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 225 | 205 | inferred_complete_timeline |
| `Action_None` | 229 | 368 | 140 | inferred_complete_timeline |
| `Action_None` | 371 | 413 | 43 | inferred_complete_timeline |
| `Action_None` | 416 | 448 | 33 | inferred_complete_timeline |
| `Action_None` | 451 | 470 | 20 | inferred_complete_timeline |
| `Action_None` | 474 | 475 | 2 | inferred_complete_timeline |
| `Action_None` | 477 | 513 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–288
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 230 | 210 | inferred_complete_timeline |
| `Action_None` | 239 | 288 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 270 | 250 | inferred_complete_timeline |
| `Action_None` | 275 | 321 | 47 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |
| `Action_None` | 331 | 599 | 269 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 76–156 | 20 | 6 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 214–599 | 386 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 300–599 | 252 | 5 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 302–304 | 3 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 309–599 | 288 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 322–599 | 271 | 2 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 332–344 | 8 | 2 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 335–599 | 264 | 2 | Undefined position; Undefined team |
| `32` | `55` | Position_Unknown | Team_Unknown | 360–366 | 4 | 2 | Undefined position; Undefined team |
| `33` | `56` | Position_Unknown | Team_Unknown | 364–365 | 2 | 1 | Undefined position; Undefined team |
| `34` | `57` | Position_Unknown | Team_Unknown | 365–366 | 2 | 1 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 366–599 | 219 | 6 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 385–599 | 215 | 1 | Undefined position; Undefined team |
| `37` | `64` | Position_Unknown | Team_Unknown | 446–452 | 7 | 1 | Undefined position; Undefined team |
| `38` | `66` | Position_Unknown | Team_Unknown | 473–480 | 6 | 3 | Undefined position; Undefined team |
| `39` | `70` | Position_Unknown | Team_Unknown | 544–545 | 2 | 1 | Undefined position; Undefined team |
| `40` | `71` | Position_Unknown | Team_Unknown | 545–551 | 7 | 1 | Undefined position; Undefined team |
| `41` | `74` | Position_Unknown | Team_Unknown | 563–572 | 10 | 1 | Undefined position; Undefined team |
| `42` | `77` | Position_Unknown | Team_Unknown | 571–572 | 2 | 1 | Undefined position; Undefined team |
| `43` | `78` | Position_Unknown | Team_Unknown | 579–599 | 21 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `19` (Kick_Returner2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 116 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '19' has invalid range: start=597, end=347. Clamping end to start.
- ⚠️ Action 'Action_None' range [21-599] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-302] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-492] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-306] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-221] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-296] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-307] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-355] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-192] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-498] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-562] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-568] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-572] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-105] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-218] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-475] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-298] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-551] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [21-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-77] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-416] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-537] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-587] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-321] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-599] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-368] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-413] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-448] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-470] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-513] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-310] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-460] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-457] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-288] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-211] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-310] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-512] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-599] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-373] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-382] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-387] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-599] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-347] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-232] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-262] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-305] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-320] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-432] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-213] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-263] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-353] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-599] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-369] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-599] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-418] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-599] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-396] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-477] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-452] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-545] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-551] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-572] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-599] for track '43' has 1 frames without a visible bounding box.
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

</details>