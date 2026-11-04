# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_8`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 77
- **Ball Tracks:** 0
- **Action Segments:** 218
- **Validation Warnings:** 302
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 205
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `19` | `19` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `19` | `19` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | defense | `16` | `16` |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner | defense | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `17` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `18` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `8` | `Group` | 0 | START | 0 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `19` | `19` | 62 | START | 62 | 75 |
| ✅ EXACT | `Action_KickBall` | Kicker | `19` | `19` | 119 | START | 119 | 124 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner | `16` | `16` | 238 | START | 238 | 246 |
| ✅ EXACT | `Action_BallCarry` | Kick_Returner | `16` | `16` | 254 | START | 254 | 659 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Kick_Returner | `16` | `16` | 660 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–504
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_KickApproach` | 62 | 75 | 14 | inferred_complete_timeline |
| `Action_KickApproach` | 80 | 113 | 34 | inferred_complete_timeline |
| `Action_KickApproach` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_KickBall` | 119 | 124 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 135 | 11 | inferred_complete_timeline |
| `Action_None` | 138 | 159 | 22 | inferred_complete_timeline |
| `Action_None` | 162 | 197 | 36 | inferred_complete_timeline |
| `Action_None` | 200 | 400 | 201 | inferred_complete_timeline |
| `Action_None` | 402 | 460 | 59 | inferred_complete_timeline |
| `Action_None` | 462 | 474 | 13 | inferred_complete_timeline |
| `Action_None` | 476 | 489 | 14 | inferred_complete_timeline |
| `Action_None` | 491 | 504 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 659 | 598 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–379
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 104 | 43 | inferred_complete_timeline |
| `Action_None` | 108 | 340 | 233 | inferred_complete_timeline |
| `Action_None` | 351 | 379 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–407
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 100 | 39 | inferred_complete_timeline |
| `Action_None` | 107 | 317 | 211 | inferred_complete_timeline |
| `Action_None` | 361 | 407 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 127 | 66 | inferred_complete_timeline |
| `Action_None` | 131 | 142 | 12 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 195 | 37 | inferred_complete_timeline |
| `Action_None` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_None` | 207 | 475 | 269 | inferred_complete_timeline |
| `Action_None` | 523 | 659 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 650

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 159 | 98 | inferred_complete_timeline |
| `Action_None` | 161 | 223 | 63 | inferred_complete_timeline |
| `Action_None` | 225 | 285 | 61 | inferred_complete_timeline |
| `Action_None` | 287 | 291 | 5 | inferred_complete_timeline |
| `Action_None` | 299 | 659 | 361 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–397
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 129 | 68 | inferred_complete_timeline |
| `Action_None` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_None` | 158 | 160 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 206 | 14 | inferred_complete_timeline |
| `Action_None` | 212 | 344 | 133 | inferred_complete_timeline |
| `Action_None` | 393 | 397 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–659
- **Visible Samples:** 659

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 302 | 241 | inferred_complete_timeline |
| `Action_None` | 304 | 659 | 356 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–646
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 104 | 43 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 328 | 162 | inferred_complete_timeline |
| `Action_None` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_None` | 353 | 355 | 3 | inferred_complete_timeline |
| `Action_None` | 361 | 646 | 286 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 659 | 598 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 232 | 171 | inferred_complete_timeline |
| `Action_None` | 239 | 257 | 19 | inferred_complete_timeline |
| `Action_None` | 261 | 301 | 41 | inferred_complete_timeline |
| `Action_None` | 308 | 329 | 22 | inferred_complete_timeline |
| `Action_None` | 332 | 335 | 4 | inferred_complete_timeline |
| `Action_None` | 338 | 356 | 19 | inferred_complete_timeline |
| `Action_None` | 358 | 382 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 263 | 202 | inferred_complete_timeline |
| `Action_None` | 269 | 385 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 264 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 345 | 284 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 383 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 615

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 226 | 165 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 268 | 296 | 29 | inferred_complete_timeline |
| `Action_None` | 309 | 342 | 34 | inferred_complete_timeline |
| `Action_None` | 344 | 614 | 271 | inferred_complete_timeline |
| `Action_None` | 616 | 659 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 660

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_CatchKick` | 238 | 246 | 9 | inferred_complete_timeline |
| `Action_None` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 659 | 406 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 294 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 323 | 262 | inferred_complete_timeline |
| `Action_None` | 329 | 378 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–382
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 307 | 246 | inferred_complete_timeline |
| `Action_None` | 311 | 323 | 13 | inferred_complete_timeline |
| `Action_None` | 326 | 382 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–415
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 302 | 241 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 319 | 12 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 330 | 3 | inferred_complete_timeline |
| `Action_None` | 332 | 340 | 9 | inferred_complete_timeline |
| `Action_None` | 344 | 415 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 20–352 | 328 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 20–386 | 358 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 102–107 | 5 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 178–182 | 4 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 195–203 | 9 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 196–199 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 276–294 | 18 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 290–336 | 15 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 297–320 | 13 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 301–402 | 81 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 306–565 | 260 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 338–387 | 40 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 358–655 | 296 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 398–461 | 64 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 441–497 | 57 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 448–455 | 8 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 452–659 | 204 | 2 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 452–461 | 6 | 2 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 459–462 | 4 | 1 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 470–472 | 3 | 1 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 480–496 | 7 | 2 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 481–506 | 18 | 4 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 486–487 | 2 | 1 | Undefined position; Undefined team |
| `43` | `67` | Position_Unknown | Team_Unknown | 497–502 | 5 | 2 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 504–507 | 4 | 1 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 521–536 | 11 | 2 | Undefined position; Undefined team |
| `46` | `71` | Position_Unknown | Team_Unknown | 524–586 | 61 | 2 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 529–659 | 131 | 1 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 533–565 | 33 | 1 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 540–602 | 30 | 6 | Undefined position; Undefined team |
| `50` | `75` | Position_Unknown | Team_Unknown | 546–656 | 106 | 2 | Undefined position; Undefined team |
| `51` | `76` | Position_Unknown | Team_Unknown | 546–598 | 46 | 5 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 551–580 | 30 | 1 | Undefined position; Undefined team |
| `53` | `81` | Position_Unknown | Team_Unknown | 561–565 | 5 | 1 | Undefined position; Undefined team |
| `54` | `82` | Position_Unknown | Team_Unknown | 561–591 | 25 | 3 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 567–569 | 3 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 571–657 | 44 | 2 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 571–574 | 4 | 1 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 572–584 | 5 | 2 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 575–586 | 9 | 2 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 575–576 | 2 | 1 | Undefined position; Undefined team |
| `61` | `91` | Position_Unknown | Team_Unknown | 577–589 | 4 | 2 | Undefined position; Undefined team |
| `62` | `92` | Position_Unknown | Team_Unknown | 579–585 | 6 | 2 | Undefined position; Undefined team |
| `63` | `93` | Position_Unknown | Team_Unknown | 579–582 | 4 | 1 | Undefined position; Undefined team |
| `64` | `94` | Position_Unknown | Team_Unknown | 581–584 | 4 | 1 | Undefined position; Undefined team |
| `65` | `95` | Position_Unknown | Team_Unknown | 583–584 | 2 | 1 | Undefined position; Undefined team |
| `66` | `97` | Position_Unknown | Team_Unknown | 593–612 | 12 | 3 | Undefined position; Undefined team |
| `67` | `99` | Position_Unknown | Team_Unknown | 604–659 | 56 | 1 | Undefined position; Undefined team |
| `68` | `101` | Position_Unknown | Team_Unknown | 610–657 | 48 | 1 | Undefined position; Undefined team |
| `69` | `105` | Position_Unknown | Team_Unknown | 626–655 | 30 | 1 | Undefined position; Undefined team |
| `70` | `106` | Position_Unknown | Team_Unknown | 628–655 | 10 | 3 | Undefined position; Undefined team |
| `71` | `107` | Position_Unknown | Team_Unknown | 629–642 | 11 | 2 | Undefined position; Undefined team |
| `72` | `108` | Position_Unknown | Team_Unknown | 640–659 | 20 | 1 | Undefined position; Undefined team |
| `73` | `109` | Position_Unknown | Team_Unknown | 644–654 | 11 | 1 | Undefined position; Undefined team |
| `74` | `110` | Position_Unknown | Team_Unknown | 650–655 | 6 | 1 | Undefined position; Undefined team |
| `75` | `111` | Position_Unknown | Team_Unknown | 652–655 | 4 | 1 | Undefined position; Undefined team |
| `76` | `112` | Position_Unknown | Team_Unknown | 653–655 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `16` (Kick_Returner)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Kicker` position mapped to `offense` team
- ⚠️ 57 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 57 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 114 |
| Missing visible bounding boxes during action | 185 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '16' has invalid range: start=660, end=659. Clamping end to start.
- ⚠️ Action 'Action_None' range [62-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-223] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-659] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-328] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-344] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-646] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-129] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-142] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-206] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-344] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-397] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-232] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-301] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-356] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-382] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-659] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-296] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-342] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-614] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-385] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-659] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-345] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-383] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-294] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-323] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-378] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-302] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-415] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-127] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-475] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-307] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-382] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-407] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-104] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-340] for track '18' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-379] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [62-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [80-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-197] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-400] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-460] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-474] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-489] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-504] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-328] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-352] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-183] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-386] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-286] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-304] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-329] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-365] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-395] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-565] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-387] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-551] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-655] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-461] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-497] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-455] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-488] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-659] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-455] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-472] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-501] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-506] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-502] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-507] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-536] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-577] for track '46' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-586] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-565] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-544] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-564] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-592] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-580] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-656] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-557] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-564] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-580] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-593] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-580] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-580] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-584] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-603] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-657] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-574] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-584] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-578] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-586] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-585] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-582] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-584] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-595] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-603] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-612] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-657] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-655] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-631] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-648] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-655] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [629-632] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-642] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-654] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-655] for track '74' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-655] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [653-655] for track '76' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 660. Video range is [0, 659].

</details>