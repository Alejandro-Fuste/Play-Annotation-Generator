# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_54`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 180
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
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `18` | `18` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `18` | `18` |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `16` | `16` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `12` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `13` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `7` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `8` | `Group` | 0 | START | 0 | 8 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `18` | `18` | 9 | START | 9 | 98 |
| ✅ EXACT | `Action_KickBall` | Kicker | `18` | `18` | 99 | START | 99 | 101 |
| ✅ EXACT | `Action_CatchKick` | Kick_Returner1 | `16` | `16` | 210 | START | 210 | 216 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `16` | `16` | 235 | START | 235 | 402 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `16` | `16` | 620 | START | 620 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_KickApproach` | 9 | 98 | 90 | inferred_complete_timeline |
| `Action_KickBall` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 418 | 317 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 613

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 576 | 568 | inferred_complete_timeline |
| `Action_None` | 585 | 588 | 4 | inferred_complete_timeline |
| `Action_None` | 597 | 598 | 2 | inferred_complete_timeline |
| `Action_None` | 600 | 629 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 618

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 393 | 385 | inferred_complete_timeline |
| `Action_None` | 398 | 399 | 2 | inferred_complete_timeline |
| `Action_None` | 408 | 629 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–305
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 235 | 227 | inferred_complete_timeline |
| `Action_None` | 245 | 264 | 20 | inferred_complete_timeline |
| `Action_None` | 284 | 305 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 222 | 214 | inferred_complete_timeline |
| `Action_None` | 225 | 629 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–625
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 467 | 459 | inferred_complete_timeline |
| `Action_None` | 470 | 471 | 2 | inferred_complete_timeline |
| `Action_None` | 474 | 475 | 2 | inferred_complete_timeline |
| `Action_None` | 479 | 484 | 6 | inferred_complete_timeline |
| `Action_None` | 503 | 619 | 117 | inferred_complete_timeline |
| `Action_None` | 622 | 625 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–542
- **Visible Samples:** 543

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 542 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–334
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 262 | 254 | inferred_complete_timeline |
| `Action_None` | 266 | 325 | 60 | inferred_complete_timeline |
| `Action_None` | 328 | 334 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 588 | 580 | inferred_complete_timeline |
| `Action_None` | 603 | 629 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–394
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 394 | 386 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 629 | 621 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–452
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 282 | 274 | inferred_complete_timeline |
| `Action_None` | 294 | 452 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 250 | 242 | inferred_complete_timeline |
| `Action_None` | 255 | 319 | 65 | inferred_complete_timeline |
| `Action_None` | 330 | 629 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 614

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 440 | 432 | inferred_complete_timeline |
| `Action_None` | 450 | 516 | 67 | inferred_complete_timeline |
| `Action_None` | 524 | 629 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 214 | 206 | inferred_complete_timeline |
| `Action_None` | 218 | 272 | 55 | inferred_complete_timeline |
| `Action_None` | 275 | 629 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_CatchKick` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_None` | 217 | 234 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 402 | 168 | inferred_complete_timeline |
| `Action_BallCarry` | 420 | 477 | 58 | inferred_complete_timeline |
| `Action_BallCarry` | 479 | 480 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 509 | 519 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 521 | 530 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 542 | 619 | 78 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 620 | 629 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 629 | 621 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–530
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 328 | 320 | inferred_complete_timeline |
| `Action_None` | 330 | 415 | 86 | inferred_complete_timeline |
| `Action_None` | 421 | 481 | 61 | inferred_complete_timeline |
| `Action_None` | 483 | 490 | 8 | inferred_complete_timeline |
| `Action_None` | 521 | 522 | 2 | inferred_complete_timeline |
| `Action_None` | 529 | 530 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 606

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 455 | 447 | inferred_complete_timeline |
| `Action_None` | 471 | 583 | 113 | inferred_complete_timeline |
| `Action_None` | 593 | 629 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–516
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 516 | 508 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 611

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 472 | 464 | inferred_complete_timeline |
| `Action_None` | 474 | 574 | 101 | inferred_complete_timeline |
| `Action_None` | 577 | 578 | 2 | inferred_complete_timeline |
| `Action_None` | 595 | 629 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 39–550 | 461 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 52–107 | 20 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 139–212 | 23 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 176–178 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 244–247 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 305–334 | 24 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 327–334 | 8 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 336–618 | 256 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 358–629 | 260 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 377–378 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 389–421 | 30 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 410–411 | 2 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 410–532 | 87 | 8 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 410–591 | 129 | 10 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 437–439 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 447–452 | 6 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 448–458 | 5 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 476–629 | 142 | 3 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 517–629 | 112 | 2 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 535–629 | 95 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 539–560 | 20 | 2 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 540–629 | 80 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 545–629 | 85 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 548–556 | 9 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 554–555 | 2 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 562–629 | 64 | 4 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 589–595 | 7 | 1 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 629–629 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 121 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_None' range [9-472] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-574] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-455] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-583] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-440] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-516] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-516] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-328] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-415] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-481] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-490] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-629] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-542] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-394] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-588] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-282] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-452] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-467] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-484] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-619] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-625] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-325] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-334] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-402] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [420-477] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [479-480] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [509-519] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [521-530] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [542-619] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-576] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-418] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-319] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-629] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-393] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-629] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-498] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-550] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-328] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-334] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-417] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-442] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-478] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-497] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-618] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-477] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-543] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-400] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-415] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-462] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-480] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-500] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-511] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-515] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-421] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-506] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-514] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-544] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-556] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-591] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-452] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-506] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-514] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-629] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-541] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-629] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-629] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-556] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-599] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-629] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-556] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-608] for track '47' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-615] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-620] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-595] for track '48' has 1 frames without a visible bounding box.
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

</details>