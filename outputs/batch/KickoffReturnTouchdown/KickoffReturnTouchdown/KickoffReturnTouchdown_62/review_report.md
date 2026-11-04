# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_62`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 159
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 142
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `7` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `17` | `17` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Kick_Returner1 | defense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | defense | `20` | `20` |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | defense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `10` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `11` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `2` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `6` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `17` | `17` | 15 | START | 15 | 94 |
| ✅ EXACT | `Action_KickBall` | Kicker | `17` | `17` | 101 | START | 101 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchKick` | Kick_Returner1 | `20` | `20` | 218 | START | 218 | 223 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Kick_Returner1 | `20` | `20` | 246 | START | 246 | 359 |
| ✅ EXACT | `Action_CrossGoalLine` | Kick_Returner1 | `20` | `20` | 594 | START | 594 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–447
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_KickApproach` | 15 | 94 | 80 | inferred_complete_timeline |
| `Action_KickBall` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 386 | 281 | inferred_complete_timeline |
| `Action_None` | 389 | 444 | 56 | inferred_complete_timeline |
| `Action_None` | 446 | 447 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 465 | 451 | inferred_complete_timeline |
| `Action_None` | 468 | 473 | 6 | inferred_complete_timeline |
| `Action_None` | 475 | 503 | 29 | inferred_complete_timeline |
| `Action_None` | 506 | 511 | 6 | inferred_complete_timeline |
| `Action_None` | 536 | 537 | 2 | inferred_complete_timeline |
| `Action_None` | 546 | 547 | 2 | inferred_complete_timeline |
| `Action_None` | 549 | 551 | 3 | inferred_complete_timeline |
| `Action_None` | 598 | 599 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–596
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 241 | 227 | inferred_complete_timeline |
| `Action_None` | 282 | 467 | 186 | inferred_complete_timeline |
| `Action_None` | 472 | 483 | 12 | inferred_complete_timeline |
| `Action_None` | 487 | 489 | 3 | inferred_complete_timeline |
| `Action_None` | 493 | 497 | 5 | inferred_complete_timeline |
| `Action_None` | 510 | 511 | 2 | inferred_complete_timeline |
| `Action_None` | 528 | 567 | 40 | inferred_complete_timeline |
| `Action_None` | 572 | 573 | 2 | inferred_complete_timeline |
| `Action_None` | 576 | 580 | 5 | inferred_complete_timeline |
| `Action_None` | 586 | 589 | 4 | inferred_complete_timeline |
| `Action_None` | 594 | 596 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 265 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 380 | 366 | inferred_complete_timeline |
| `Action_None` | 382 | 562 | 181 | inferred_complete_timeline |
| `Action_None` | 568 | 599 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–554
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 322 | 308 | inferred_complete_timeline |
| `Action_None` | 325 | 381 | 57 | inferred_complete_timeline |
| `Action_None` | 384 | 397 | 14 | inferred_complete_timeline |
| `Action_None` | 403 | 554 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 515 | 501 | inferred_complete_timeline |
| `Action_None` | 520 | 599 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 372 | 358 | inferred_complete_timeline |
| `Action_None` | 374 | 460 | 87 | inferred_complete_timeline |
| `Action_None` | 464 | 466 | 3 | inferred_complete_timeline |
| `Action_None` | 468 | 599 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |
| `Action_None` | 212 | 331 | 120 | inferred_complete_timeline |
| `Action_None` | 349 | 353 | 5 | inferred_complete_timeline |
| `Action_None` | 362 | 367 | 6 | inferred_complete_timeline |
| `Action_None` | 371 | 372 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 555 | 181 | inferred_complete_timeline |
| `Action_None` | 557 | 599 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 185 | 171 | inferred_complete_timeline |
| `Action_None` | 187 | 599 | 413 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 511 | 497 | inferred_complete_timeline |
| `Action_None` | 513 | 542 | 30 | inferred_complete_timeline |
| `Action_None` | 555 | 557 | 3 | inferred_complete_timeline |
| `Action_None` | 563 | 567 | 5 | inferred_complete_timeline |
| `Action_None` | 571 | 599 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 234 | 220 | inferred_complete_timeline |
| `Action_None` | 236 | 248 | 13 | inferred_complete_timeline |
| `Action_None` | 261 | 289 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–571
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 536 | 522 | inferred_complete_timeline |
| `Action_None` | 538 | 571 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–344
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 257 | 243 | inferred_complete_timeline |
| `Action_None` | 278 | 339 | 62 | inferred_complete_timeline |
| `Action_None` | 342 | 344 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 337 | 323 | inferred_complete_timeline |
| `Action_None` | 341 | 511 | 171 | inferred_complete_timeline |
| `Action_None` | 521 | 599 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 273 | 259 | inferred_complete_timeline |
| `Action_None` | 275 | 599 | 325 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_CatchKick` | 218 | 223 | 6 | inferred_complete_timeline |
| `Action_CatchKick` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 245 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 359 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 362 | 593 | 232 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 594 | 599 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 453 | 439 | inferred_complete_timeline |
| `Action_None` | 455 | 599 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–532
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 361 | 347 | inferred_complete_timeline |
| `Action_None` | 369 | 532 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 473 | 459 | inferred_complete_timeline |
| `Action_None` | 478 | 599 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–459
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 355 | 341 | inferred_complete_timeline |
| `Action_None` | 367 | 370 | 4 | inferred_complete_timeline |
| `Action_None` | 375 | 377 | 3 | inferred_complete_timeline |
| `Action_None` | 380 | 383 | 4 | inferred_complete_timeline |
| `Action_None` | 385 | 386 | 2 | inferred_complete_timeline |
| `Action_None` | 388 | 398 | 11 | inferred_complete_timeline |
| `Action_None` | 401 | 451 | 51 | inferred_complete_timeline |
| `Action_None` | 458 | 459 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 2–599 | 515 | 13 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 113–117 | 5 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 141–206 | 11 | 3 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 187–207 | 6 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 204–210 | 5 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 240–599 | 353 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 275–282 | 8 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 300–586 | 285 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 332–338 | 7 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 376–599 | 216 | 3 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 454–543 | 8 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 457–574 | 54 | 7 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 473–476 | 4 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 487–599 | 103 | 3 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 494–497 | 4 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 537–555 | 7 | 2 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 545–556 | 7 | 2 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 593–599 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchKick` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Kick_Returner1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 120 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [15-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-467] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-483] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-497] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-567] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-573] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-580] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-589] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-515] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-599] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-185] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-599] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-465] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-473] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-503] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-511] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-536] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-571] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-331] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-353] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-367] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-555] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-460] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-380] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-562] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-234] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-289] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-381] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-397] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-554] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-265] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-257] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-339] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-511] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-542] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-557] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-567] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-361] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-532] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-473] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-453] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [15-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-386] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-444] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-337] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-511] for track '18' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-599] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-355] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-370] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-398] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-451] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [218-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-8] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-31] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-399] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-275] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-395] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-582] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-586] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-396] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-430] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-599] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-471] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-492] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-504] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-508] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-550] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-476] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-503] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-515] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-541] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '38' has 1 frames without a visible bounding box.
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

</details>