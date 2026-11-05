# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_74`
- **Frame Range:** 0 to 659 (660 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 659
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 281
- **Validation Warnings:** 349
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
- **Inferred Coverage Segments (Action_None):** 267
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `34` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `79` | `50` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `0` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `14` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 44 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `8` | `8` | 45 | START | 45 | 98 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 75 | END | 75 | 75 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 99 | START | 99 | 113 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `34` | `28` | 226 | START | 226 | 247 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `28` | 248 | START | 248 | 384 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `79` | `50` | 630 | START | 630 | 633 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 71 | 27 | inferred_complete_timeline |
| `Action_None` | 76 | 98 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 80 | 36 | inferred_complete_timeline |
| `Action_None` | 82 | 170 | 89 | inferred_complete_timeline |
| `Action_None` | 174 | 184 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_LongSnap` | 45 | 98 | 54 | inferred_complete_timeline |
| `Action_None` | 99 | 144 | 46 | inferred_complete_timeline |
| `Action_None` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 182 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 113 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–453
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 228 | 184 | inferred_complete_timeline |
| `Action_None` | 235 | 302 | 68 | inferred_complete_timeline |
| `Action_None` | 304 | 360 | 57 | inferred_complete_timeline |
| `Action_None` | 375 | 379 | 5 | inferred_complete_timeline |
| `Action_None` | 381 | 382 | 2 | inferred_complete_timeline |
| `Action_None` | 387 | 399 | 13 | inferred_complete_timeline |
| `Action_None` | 411 | 432 | 22 | inferred_complete_timeline |
| `Action_None` | 452 | 453 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 200 | 156 | inferred_complete_timeline |
| `Action_None` | 203 | 237 | 35 | inferred_complete_timeline |
| `Action_None` | 239 | 273 | 35 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 289 | 7 | inferred_complete_timeline |
| `Action_None` | 292 | 306 | 15 | inferred_complete_timeline |
| `Action_None` | 308 | 327 | 20 | inferred_complete_timeline |
| `Action_None` | 331 | 349 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–316
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 75 | 1 | inferred_complete_timeline |
| `Action_None` | 76 | 98 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 99 | 113 | 15 | inferred_complete_timeline |
| `Action_None` | 114 | 316 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 64 | 20 | inferred_complete_timeline |
| `Action_None` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 104 | 20 | inferred_complete_timeline |
| `Action_None` | 116 | 117 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–491
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 382 | 338 | inferred_complete_timeline |
| `Action_None` | 384 | 463 | 80 | inferred_complete_timeline |
| `Action_None` | 479 | 482 | 4 | inferred_complete_timeline |
| `Action_None` | 490 | 491 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–426
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 256 | 212 | inferred_complete_timeline |
| `Action_None` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_None` | 267 | 377 | 111 | inferred_complete_timeline |
| `Action_None` | 380 | 387 | 8 | inferred_complete_timeline |
| `Action_None` | 393 | 395 | 3 | inferred_complete_timeline |
| `Action_None` | 404 | 406 | 3 | inferred_complete_timeline |
| `Action_None` | 414 | 416 | 3 | inferred_complete_timeline |
| `Action_None` | 424 | 426 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–659
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 400 | 356 | inferred_complete_timeline |
| `Action_None` | 402 | 438 | 37 | inferred_complete_timeline |
| `Action_None` | 440 | 467 | 28 | inferred_complete_timeline |
| `Action_None` | 471 | 483 | 13 | inferred_complete_timeline |
| `Action_None` | 488 | 491 | 4 | inferred_complete_timeline |
| `Action_None` | 494 | 500 | 7 | inferred_complete_timeline |
| `Action_None` | 502 | 503 | 2 | inferred_complete_timeline |
| `Action_None` | 505 | 511 | 7 | inferred_complete_timeline |
| `Action_None` | 517 | 523 | 7 | inferred_complete_timeline |
| `Action_None` | 526 | 527 | 2 | inferred_complete_timeline |
| `Action_None` | 552 | 557 | 6 | inferred_complete_timeline |
| `Action_None` | 616 | 617 | 2 | inferred_complete_timeline |
| `Action_None` | 637 | 640 | 4 | inferred_complete_timeline |
| `Action_None` | 647 | 659 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–459
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 224 | 180 | inferred_complete_timeline |
| `Action_None` | 227 | 312 | 86 | inferred_complete_timeline |
| `Action_None` | 319 | 426 | 108 | inferred_complete_timeline |
| `Action_None` | 429 | 434 | 6 | inferred_complete_timeline |
| `Action_None` | 436 | 453 | 18 | inferred_complete_timeline |
| `Action_None` | 458 | 459 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–461
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 102 | 58 | inferred_complete_timeline |
| `Action_None` | 104 | 270 | 167 | inferred_complete_timeline |
| `Action_None` | 273 | 377 | 105 | inferred_complete_timeline |
| `Action_None` | 380 | 389 | 10 | inferred_complete_timeline |
| `Action_None` | 392 | 397 | 6 | inferred_complete_timeline |
| `Action_None` | 407 | 409 | 3 | inferred_complete_timeline |
| `Action_None` | 414 | 416 | 3 | inferred_complete_timeline |
| `Action_None` | 421 | 453 | 33 | inferred_complete_timeline |
| `Action_None` | 458 | 461 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–457
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 93 | 49 | inferred_complete_timeline |
| `Action_None` | 99 | 230 | 132 | inferred_complete_timeline |
| `Action_None` | 240 | 290 | 51 | inferred_complete_timeline |
| `Action_None` | 292 | 330 | 39 | inferred_complete_timeline |
| `Action_None` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 419 | 85 | inferred_complete_timeline |
| `Action_None` | 426 | 444 | 19 | inferred_complete_timeline |
| `Action_None` | 446 | 447 | 2 | inferred_complete_timeline |
| `Action_None` | 452 | 457 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–452 | 421 | 12 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 71–445 | 338 | 10 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 82–476 | 381 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 88–659 | 472 | 10 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 123–331 | 209 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 128–206 | 78 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 136–444 | 255 | 9 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 160–444 | 256 | 9 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 180–393 | 171 | 7 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 192–659 | 395 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 199–216 | 18 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 209–261 | 52 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 209–231 | 19 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 210–310 | 99 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 217–462 | 238 | 6 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 239–553 | 214 | 11 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 243–659 | 393 | 10 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 271–314 | 28 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 294–430 | 76 | 5 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 309–659 | 337 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 312–313 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 317–374 | 49 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 361–659 | 220 | 6 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 365–372 | 7 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 401–417 | 17 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 421–659 | 237 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 433–468 | 23 | 3 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 443–444 | 2 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 447–625 | 161 | 6 | Undefined position; Undefined team |
| `43` | `69` | Position_Unknown | Team_Unknown | 506–557 | 39 | 4 | Undefined position; Undefined team |
| `44` | `70` | Position_Unknown | Team_Unknown | 509–510 | 2 | 1 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 517–552 | 26 | 3 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 552–659 | 72 | 5 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 575–639 | 63 | 3 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 594–647 | 37 | 3 | Undefined position; Undefined team |
| `49` | `78` | Position_Unknown | Team_Unknown | 604–659 | 56 | 1 | Undefined position; Undefined team |
| `50` | `79` | Position_Unknown | Team_Unknown | 613–652 | 33 | 5 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 618–659 | 33 | 3 | Undefined position; Undefined team |
| `52` | `83` | Position_Unknown | Team_Unknown | 619–659 | 37 | 4 | Undefined position; Undefined team |
| `53` | `84` | Position_Unknown | Team_Unknown | 625–627 | 3 | 1 | Undefined position; Undefined team |
| `54` | `86` | Position_Unknown | Team_Unknown | 641–659 | 16 | 2 | Undefined position; Undefined team |
| `55` | `87` | Position_Unknown | Team_Unknown | 644–659 | 13 | 2 | Undefined position; Undefined team |
| `56` | `89` | Position_Unknown | Team_Unknown | 646–647 | 2 | 1 | Undefined position; Undefined team |
| `57` | `90` | Position_Unknown | Team_Unknown | 649–659 | 11 | 1 | Undefined position; Undefined team |
| `58` | `91` | Position_Unknown | Team_Unknown | 650–659 | 9 | 2 | Undefined position; Undefined team |
| `59` | `93` | Position_Unknown | Team_Unknown | 652–659 | 8 | 1 | Undefined position; Undefined team |
| `60` | `94` | Position_Unknown | Team_Unknown | 655–659 | 5 | 1 | Undefined position; Undefined team |
| `61` | `95` | Position_Unknown | Team_Unknown | 655–659 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 250 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [45-64] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-104] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-197] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-366] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-432] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-447] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-224] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-312] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-426] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-453] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-400] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-438] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-467] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-483] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-500] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-511] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-523] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-557] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-617] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-640] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-659] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-382] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-463] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-482] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-273] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-289] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-306] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-327] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-349] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-256] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-377] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-387] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-406] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-426] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-270] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-377] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-416] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-453] for track '9' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-93] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-330] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-419] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-444] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-457] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-80] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-316] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-302] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-360] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-399] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-432] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-82] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-361] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-397] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-417] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-432] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-459] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-186] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-407] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-432] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-518] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-331] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-310] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-370] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-395] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-417] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-431] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-261] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-325] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-387] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-420] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-434] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-444] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-238] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-273] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-339] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-393] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-379] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-388] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-535] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-541] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-591] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-659] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-298] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-310] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [248-384] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [386-397] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [402-407] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [411-462] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-338] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-397] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-422] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-433] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-455] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-461] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-519] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-532] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-373] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-517] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-532] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-577] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-616] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-639] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-642] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [648-659] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-314] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-338] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-430] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-659] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-360] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-374] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-553] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-559] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-578] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-587] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-625] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [658-659] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-417] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-438] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-446] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-453] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-468] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-457] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-474] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-504] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-609] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-625] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-527] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-557] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-519] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-543] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-552] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-554] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-578] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-594] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-659] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-631] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [633-635] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-639] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-638] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [645-647] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-659] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [613-616] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [630-633] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-645] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-652] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-630] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-645] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-621] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-630] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [632-645] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-627] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-645] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [649-659] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [644-645] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [646-647] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [650-657] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>