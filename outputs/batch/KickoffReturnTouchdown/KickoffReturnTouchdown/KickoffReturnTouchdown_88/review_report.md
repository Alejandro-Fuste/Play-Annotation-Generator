# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_88

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_88`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 201
- **Validation Warnings:** 239
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 190
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Second_Level_Blocker3 | defense | `13` | `13` |
| ✅ EXACT | `Action_KickBall` | Second_Level_Blocker3 | defense | `13` | `13` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `15` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `5` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `7` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `8` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 55 |
| ✅ EXACT | `Action_KickApproach` | Second_Level_Blocker3 | `13` | `13` | 56 | START | 56 | 132 |
| ✅ EXACT | `Action_KickBall` | Second_Level_Blocker3 | `13` | `13` | 133 | START | 133 | 138 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `23` | `21` | 249 | START | 249 | 256 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `21` | 266 | START | 266 | 571 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 203 | 148 | inferred_complete_timeline |
| `Action_None` | 205 | 220 | 16 | inferred_complete_timeline |
| `Action_None` | 223 | 245 | 23 | inferred_complete_timeline |
| `Action_None` | 247 | 295 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–343
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 343 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 157–629
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 157 | 338 | 182 | inferred_complete_timeline |
| `Action_None` | 341 | 346 | 6 | inferred_complete_timeline |
| `Action_None` | 349 | 351 | 3 | inferred_complete_timeline |
| `Action_None` | 399 | 402 | 4 | inferred_complete_timeline |
| `Action_None` | 405 | 409 | 5 | inferred_complete_timeline |
| `Action_None` | 411 | 414 | 4 | inferred_complete_timeline |
| `Action_None` | 425 | 629 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–625
- **Visible Samples:** 608

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 409 | 354 | inferred_complete_timeline |
| `Action_None` | 411 | 493 | 83 | inferred_complete_timeline |
| `Action_None` | 496 | 588 | 93 | inferred_complete_timeline |
| `Action_None` | 590 | 601 | 12 | inferred_complete_timeline |
| `Action_None` | 610 | 611 | 2 | inferred_complete_timeline |
| `Action_None` | 616 | 621 | 6 | inferred_complete_timeline |
| `Action_None` | 624 | 625 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 284 | 229 | inferred_complete_timeline |
| `Action_None` | 286 | 300 | 15 | inferred_complete_timeline |
| `Action_None` | 306 | 313 | 8 | inferred_complete_timeline |
| `Action_None` | 316 | 333 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 310 | 255 | inferred_complete_timeline |
| `Action_None` | 313 | 324 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 267 | 212 | inferred_complete_timeline |
| `Action_None` | 269 | 271 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 245 | 190 | inferred_complete_timeline |
| `Action_None` | 247 | 284 | 38 | inferred_complete_timeline |
| `Action_None` | 286 | 295 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 265 | 210 | inferred_complete_timeline |
| `Action_None` | 273 | 284 | 12 | inferred_complete_timeline |
| `Action_None` | 287 | 296 | 10 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 358 | 5 | inferred_complete_timeline |
| `Action_None` | 366 | 629 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 266 | 211 | inferred_complete_timeline |
| `Action_None` | 269 | 284 | 16 | inferred_complete_timeline |
| `Action_None` | 287 | 300 | 14 | inferred_complete_timeline |
| `Action_None` | 302 | 333 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 608 | 553 | inferred_complete_timeline |
| `Action_None` | 610 | 614 | 5 | inferred_complete_timeline |
| `Action_None` | 616 | 629 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 325 | 270 | inferred_complete_timeline |
| `Action_None` | 328 | 333 | 6 | inferred_complete_timeline |
| `Action_None` | 400 | 401 | 2 | inferred_complete_timeline |
| `Action_None` | 405 | 409 | 5 | inferred_complete_timeline |
| `Action_None` | 411 | 414 | 4 | inferred_complete_timeline |
| `Action_None` | 457 | 458 | 2 | inferred_complete_timeline |
| `Action_None` | 460 | 462 | 3 | inferred_complete_timeline |
| `Action_None` | 468 | 469 | 2 | inferred_complete_timeline |
| `Action_None` | 473 | 474 | 2 | inferred_complete_timeline |
| `Action_None` | 477 | 483 | 7 | inferred_complete_timeline |
| `Action_None` | 486 | 487 | 2 | inferred_complete_timeline |
| `Action_None` | 489 | 629 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 302 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 245 | 190 | inferred_complete_timeline |
| `Action_None` | 247 | 267 | 21 | inferred_complete_timeline |
| `Action_None` | 269 | 283 | 15 | inferred_complete_timeline |
| `Action_None` | 286 | 296 | 11 | inferred_complete_timeline |
| `Action_None` | 316 | 326 | 11 | inferred_complete_timeline |
| `Action_None` | 328 | 334 | 7 | inferred_complete_timeline |
| `Action_None` | 338 | 341 | 4 | inferred_complete_timeline |
| `Action_None` | 346 | 354 | 9 | inferred_complete_timeline |
| `Action_None` | 358 | 475 | 118 | inferred_complete_timeline |
| `Action_None` | 477 | 478 | 2 | inferred_complete_timeline |
| `Action_None` | 480 | 551 | 72 | inferred_complete_timeline |
| `Action_None` | 554 | 575 | 22 | inferred_complete_timeline |
| `Action_None` | 577 | 605 | 29 | inferred_complete_timeline |
| `Action_None` | 611 | 629 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 196–456
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 196 | 324 | 129 | inferred_complete_timeline |
| `Action_None` | 328 | 364 | 37 | inferred_complete_timeline |
| `Action_None` | 391 | 393 | 3 | inferred_complete_timeline |
| `Action_None` | 400 | 402 | 3 | inferred_complete_timeline |
| `Action_None` | 405 | 409 | 5 | inferred_complete_timeline |
| `Action_None` | 411 | 414 | 4 | inferred_complete_timeline |
| `Action_None` | 427 | 431 | 5 | inferred_complete_timeline |
| `Action_None` | 433 | 439 | 7 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 447 | 456 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 212 | 157 | inferred_complete_timeline |
| `Action_None` | 214 | 296 | 83 | inferred_complete_timeline |
| `Action_None` | 318 | 346 | 29 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 163–313
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 163 | 313 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–340
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 267 | 212 | inferred_complete_timeline |
| `Action_None` | 269 | 304 | 36 | inferred_complete_timeline |
| `Action_None` | 310 | 325 | 16 | inferred_complete_timeline |
| `Action_None` | 328 | 340 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–556
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_KickApproach` | 56 | 132 | 77 | inferred_complete_timeline |
| `Action_KickBall` | 133 | 138 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 236 | 98 | inferred_complete_timeline |
| `Action_None` | 238 | 256 | 19 | inferred_complete_timeline |
| `Action_None` | 262 | 271 | 10 | inferred_complete_timeline |
| `Action_None` | 278 | 512 | 235 | inferred_complete_timeline |
| `Action_None` | 514 | 515 | 2 | inferred_complete_timeline |
| `Action_None` | 534 | 535 | 2 | inferred_complete_timeline |
| `Action_None` | 554 | 556 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–629 | 592 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 140–629 | 482 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 224–629 | 378 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 281–296 | 15 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 317–370 | 31 | 5 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 317–378 | 61 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 319–403 | 85 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 323–324 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 324–610 | 257 | 10 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 329–629 | 289 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 330–342 | 13 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 368–629 | 241 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 386–629 | 243 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 401–629 | 193 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 406–606 | 192 | 7 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 406–629 | 212 | 4 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 406–414 | 8 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 406–414 | 8 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 423–629 | 206 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 443–445 | 3 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 452–453 | 2 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 454–472 | 19 | 1 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 460–482 | 23 | 1 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 467–629 | 162 | 2 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 522–530 | 7 | 2 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 543–573 | 21 | 5 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 561–565 | 4 | 2 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 568–629 | 62 | 1 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 608–629 | 13 | 3 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 624–625 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `22`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 90, Column 'Cross Goal Line': Unknown actor track ID '?' in entry '636,641,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 172 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 178: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [56-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-360] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-445] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-304] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-325] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-340] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-296] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-629] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-325] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-462] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-483] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-629] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-343] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-608] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-614] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-284] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-295] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-300] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-313] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-333] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-300] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-333] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-267] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-326] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-334] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-341] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-354] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-475] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-551] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-575] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-605] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-629] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-310] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-324] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-256] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-512] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-556] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-220] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-409] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-493] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-588] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-601] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [610-611] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-621] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-212] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-346] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-302] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-333] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-620] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-629] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-338] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-402] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-629] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-313] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-324] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-364] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-393] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-402] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-409] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-431] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-439] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-456] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-571] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [587-600] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [607-610] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [618-629] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-333] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-370] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-378] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-403] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-465] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-551] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-573] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-582] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-589] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-605] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-610] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-602] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-608] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-629] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-342] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-379] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-629] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-394] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-629] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-430] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-573] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-580] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-601] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-606] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-605] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-603] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-629] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-472] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-482] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-614] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-523] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-530] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-550] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-558] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-568] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-573] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-614] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-620] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'KickoffReturnTouchdown_88'; source metadata written as null.

</details>