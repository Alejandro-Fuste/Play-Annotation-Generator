# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_87`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 300
- **Validation Warnings:** 332
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 286
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage1 | offense | `14` | `14` |
| ✅ EXACT | `Action_KickBall` | Left_Coverage1 | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `22` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `22` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `4` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ EXACT | `Action_KickApproach` | Left_Coverage1 | `14` | `14` | 28 | START | 28 | 97 |
| ✅ EXACT | `Action_KickBall` | Left_Coverage1 | `14` | `14` | 98 | START | 98 | 103 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `22` | `22` | 218 | START | 218 | 222 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `22` | 235 | START | 235 | 337 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `22` | `22` | 600 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 599 | 572 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_KickApproach` | 28 | 97 | 70 | inferred_complete_timeline |
| `Action_KickBall` | 98 | 103 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 337 | 234 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 353 | 356 | 4 | inferred_complete_timeline |
| `Action_None` | 359 | 374 | 16 | inferred_complete_timeline |
| `Action_None` | 379 | 382 | 4 | inferred_complete_timeline |
| `Action_None` | 391 | 394 | 4 | inferred_complete_timeline |
| `Action_None` | 400 | 401 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 337 | 310 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 585

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 322 | 295 | inferred_complete_timeline |
| `Action_None` | 331 | 337 | 7 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 353 | 9 | inferred_complete_timeline |
| `Action_None` | 356 | 599 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 205 | 178 | inferred_complete_timeline |
| `Action_None` | 209 | 279 | 71 | inferred_complete_timeline |
| `Action_None` | 285 | 292 | 8 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 310 | 341 | 32 | inferred_complete_timeline |
| `Action_None` | 403 | 417 | 15 | inferred_complete_timeline |
| `Action_None` | 423 | 480 | 58 | inferred_complete_timeline |
| `Action_None` | 483 | 599 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–591
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 154 | 127 | inferred_complete_timeline |
| `Action_None` | 157 | 246 | 90 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_None` | 265 | 300 | 36 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 336 | 4 | inferred_complete_timeline |
| `Action_None` | 338 | 342 | 5 | inferred_complete_timeline |
| `Action_None` | 344 | 425 | 82 | inferred_complete_timeline |
| `Action_None` | 429 | 490 | 62 | inferred_complete_timeline |
| `Action_None` | 501 | 591 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 341 | 314 | inferred_complete_timeline |
| `Action_None` | 345 | 363 | 19 | inferred_complete_timeline |
| `Action_None` | 368 | 599 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 161 | 134 | inferred_complete_timeline |
| `Action_None` | 163 | 232 | 70 | inferred_complete_timeline |
| `Action_None` | 245 | 253 | 9 | inferred_complete_timeline |
| `Action_None` | 256 | 259 | 4 | inferred_complete_timeline |
| `Action_None` | 261 | 338 | 78 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 374 | 10 | inferred_complete_timeline |
| `Action_None` | 379 | 417 | 39 | inferred_complete_timeline |
| `Action_None` | 425 | 454 | 30 | inferred_complete_timeline |
| `Action_None` | 456 | 471 | 16 | inferred_complete_timeline |
| `Action_None` | 473 | 478 | 6 | inferred_complete_timeline |
| `Action_None` | 487 | 491 | 5 | inferred_complete_timeline |
| `Action_None` | 493 | 534 | 42 | inferred_complete_timeline |
| `Action_None` | 541 | 554 | 14 | inferred_complete_timeline |
| `Action_None` | 558 | 559 | 2 | inferred_complete_timeline |
| `Action_None` | 562 | 568 | 7 | inferred_complete_timeline |
| `Action_None` | 570 | 572 | 3 | inferred_complete_timeline |
| `Action_None` | 575 | 599 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 152 | 125 | inferred_complete_timeline |
| `Action_None` | 154 | 208 | 55 | inferred_complete_timeline |
| `Action_None` | 215 | 309 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 302 | 275 | inferred_complete_timeline |
| `Action_None` | 311 | 323 | 13 | inferred_complete_timeline |
| `Action_None` | 325 | 336 | 12 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 332 | 305 | inferred_complete_timeline |
| `Action_None` | 337 | 341 | 5 | inferred_complete_timeline |
| `Action_None` | 344 | 350 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 253 | 226 | inferred_complete_timeline |
| `Action_None` | 260 | 336 | 77 | inferred_complete_timeline |
| `Action_None` | 353 | 356 | 4 | inferred_complete_timeline |
| `Action_None` | 358 | 360 | 3 | inferred_complete_timeline |
| `Action_None` | 365 | 374 | 10 | inferred_complete_timeline |
| `Action_None` | 379 | 417 | 39 | inferred_complete_timeline |
| `Action_None` | 423 | 426 | 4 | inferred_complete_timeline |
| `Action_None` | 429 | 432 | 4 | inferred_complete_timeline |
| `Action_None` | 434 | 480 | 47 | inferred_complete_timeline |
| `Action_None` | 483 | 527 | 45 | inferred_complete_timeline |
| `Action_None` | 532 | 534 | 3 | inferred_complete_timeline |
| `Action_None` | 539 | 540 | 2 | inferred_complete_timeline |
| `Action_None` | 542 | 548 | 7 | inferred_complete_timeline |
| `Action_None` | 550 | 599 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–558
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 338 | 311 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 373 | 9 | inferred_complete_timeline |
| `Action_None` | 379 | 384 | 6 | inferred_complete_timeline |
| `Action_None` | 386 | 410 | 25 | inferred_complete_timeline |
| `Action_None` | 412 | 416 | 5 | inferred_complete_timeline |
| `Action_None` | 429 | 432 | 4 | inferred_complete_timeline |
| `Action_None` | 435 | 476 | 42 | inferred_complete_timeline |
| `Action_None` | 487 | 488 | 2 | inferred_complete_timeline |
| `Action_None` | 490 | 491 | 2 | inferred_complete_timeline |
| `Action_None` | 500 | 516 | 17 | inferred_complete_timeline |
| `Action_None` | 519 | 533 | 15 | inferred_complete_timeline |
| `Action_None` | 557 | 558 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 361 | 334 | inferred_complete_timeline |
| `Action_None` | 363 | 374 | 12 | inferred_complete_timeline |
| `Action_None` | 377 | 403 | 27 | inferred_complete_timeline |
| `Action_None` | 406 | 410 | 5 | inferred_complete_timeline |
| `Action_None` | 415 | 416 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 425 | 3 | inferred_complete_timeline |
| `Action_None` | 427 | 506 | 80 | inferred_complete_timeline |
| `Action_None` | 509 | 599 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 128 | 101 | inferred_complete_timeline |
| `Action_None` | 130 | 337 | 208 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 355 | 11 | inferred_complete_timeline |
| `Action_None` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_None` | 364 | 599 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–589
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 337 | 310 | inferred_complete_timeline |
| `Action_None` | 345 | 350 | 6 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 360 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 374 | 10 | inferred_complete_timeline |
| `Action_None` | 379 | 393 | 15 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_None` | 399 | 406 | 8 | inferred_complete_timeline |
| `Action_None` | 415 | 416 | 2 | inferred_complete_timeline |
| `Action_None` | 423 | 424 | 2 | inferred_complete_timeline |
| `Action_None` | 427 | 546 | 120 | inferred_complete_timeline |
| `Action_None` | 548 | 589 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–599 | 598 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–599 | 483 | 13 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–256 | 143 | 13 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–416 | 379 | 7 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–251 | 252 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–599 | 562 | 12 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–337 | 338 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 76–87 | 11 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 136–138 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 238–240 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 295–599 | 188 | 18 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 296–320 | 24 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 305–370 | 14 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 315–320 | 6 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 324–599 | 270 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 346–350 | 5 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 346–598 | 234 | 9 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 368–417 | 48 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 369–538 | 135 | 8 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 378–599 | 214 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 384–388 | 5 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 410–513 | 64 | 14 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 436–599 | 139 | 7 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 436–508 | 67 | 4 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 441–475 | 14 | 3 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 451–521 | 28 | 7 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 470–471 | 2 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 478–480 | 3 | 1 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 492–533 | 21 | 4 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 560–561 | 2 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 566–599 | 29 | 2 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 584–599 | 11 | 2 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 596–599 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `22` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 263 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '22' has invalid range: start=600, end=337. Clamping end to start.
- ⚠️ Action 'Action_None' range [28-337] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-374] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-393] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-406] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-546] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-589] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-332] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-350] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-338] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-373] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-410] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-416] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-476] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-516] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-533] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-208] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-309] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-232] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-253] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-338] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-374] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-417] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-454] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-471] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-478] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-491] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-534] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-554] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-568] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-572] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-599] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-361] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-374] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-403] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-506] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-599] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-253] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-336] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-374] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-417] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-480] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-527] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-534] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-548] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-341] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-363] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-599] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-246] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-300] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-425] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-490] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-591] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-337] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-355] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-362] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-279] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-341] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-417] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-480] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-599] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-302] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-323] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-322] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-353] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-337] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-356] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-374] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-394] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-273] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-599] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-337] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-350] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-247] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-312] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-374] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-417] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-477] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-485] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-498] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-522] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-71] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-90] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-138] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-300] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-322] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-338] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-346] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-374] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-416] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-251] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-357] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-364] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-417] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-501] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-528] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-544] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-560] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-573] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-599] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-337] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-305] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-332] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-386] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-412] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-448] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-480] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-538] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-546] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-552] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-568] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-591] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-317] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-336] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-536] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-553] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-560] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-480] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-490] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-516] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-558] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-578] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-592] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-374] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-417] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-409] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-448] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-468] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-480] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-493] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-538] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-418] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-599] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-440] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-462] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-474] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-484] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-506] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-478] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-508] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-535] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-548] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-439] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-444] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-459] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-508] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-446] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-475] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-453] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-471] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-486] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-502] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-505] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-568] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-589] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 600. Video range is [0, 599].

</details>