# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_85`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 267
- **Validation Warnings:** 337
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 252
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `32` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `32` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `44` | `35` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `13` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `16` | `16` | 30 | START | 30 | 48 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 59 | END | 59 | 59 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 89 | START | 89 | 101 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `32` | `26` | 202 | START | 202 | 217 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `32` | `26` | 273 | START | 273 | 371 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `44` | `35` | 609 | START | 609 | 609 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 578

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_None` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_None` | 89 | 463 | 375 | inferred_complete_timeline |
| `Action_None` | 467 | 480 | 14 | inferred_complete_timeline |
| `Action_None` | 482 | 483 | 2 | inferred_complete_timeline |
| `Action_None` | 488 | 495 | 8 | inferred_complete_timeline |
| `Action_None` | 498 | 629 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–410
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 61 | 32 | inferred_complete_timeline |
| `Action_None` | 63 | 300 | 238 | inferred_complete_timeline |
| `Action_None` | 303 | 307 | 5 | inferred_complete_timeline |
| `Action_None` | 312 | 362 | 51 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_None` | 382 | 394 | 13 | inferred_complete_timeline |
| `Action_None` | 397 | 398 | 2 | inferred_complete_timeline |
| `Action_None` | 400 | 404 | 5 | inferred_complete_timeline |
| `Action_None` | 408 | 410 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_LongSnap` | 30 | 48 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–628
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 76 | 47 | inferred_complete_timeline |
| `Action_None` | 78 | 460 | 383 | inferred_complete_timeline |
| `Action_None` | 469 | 473 | 5 | inferred_complete_timeline |
| `Action_None` | 481 | 497 | 17 | inferred_complete_timeline |
| `Action_None` | 499 | 501 | 3 | inferred_complete_timeline |
| `Action_None` | 503 | 504 | 2 | inferred_complete_timeline |
| `Action_None` | 514 | 617 | 104 | inferred_complete_timeline |
| `Action_None` | 624 | 628 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 89 | 60 | inferred_complete_timeline |
| `Action_None` | 91 | 111 | 21 | inferred_complete_timeline |
| `Action_None` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 317 | 201 | inferred_complete_timeline |
| `Action_None` | 322 | 359 | 38 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_None` | 403 | 404 | 2 | inferred_complete_timeline |
| `Action_None` | 410 | 418 | 9 | inferred_complete_timeline |
| `Action_None` | 421 | 494 | 74 | inferred_complete_timeline |
| `Action_None` | 496 | 572 | 77 | inferred_complete_timeline |
| `Action_None` | 582 | 629 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–413
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 383 | 354 | inferred_complete_timeline |
| `Action_None` | 411 | 413 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_None` | 60 | 88 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 145 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 58 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 63 | 34 | inferred_complete_timeline |
| `Action_None` | 66 | 629 | 564 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 204 | 175 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 211 | 305 | 95 | inferred_complete_timeline |
| `Action_None` | 309 | 629 | 321 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 603

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 365 | 336 | inferred_complete_timeline |
| `Action_None` | 368 | 374 | 7 | inferred_complete_timeline |
| `Action_None` | 377 | 380 | 4 | inferred_complete_timeline |
| `Action_None` | 395 | 476 | 82 | inferred_complete_timeline |
| `Action_None` | 478 | 481 | 4 | inferred_complete_timeline |
| `Action_None` | 485 | 623 | 139 | inferred_complete_timeline |
| `Action_None` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 195 | 166 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 609

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 176 | 147 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 190 | 10 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_None` | 206 | 318 | 113 | inferred_complete_timeline |
| `Action_None` | 320 | 461 | 142 | inferred_complete_timeline |
| `Action_None` | 465 | 565 | 101 | inferred_complete_timeline |
| `Action_None` | 568 | 604 | 37 | inferred_complete_timeline |
| `Action_None` | 610 | 629 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–618
- **Visible Samples:** 610

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 605 | 576 | inferred_complete_timeline |
| `Action_None` | 612 | 613 | 2 | inferred_complete_timeline |
| `Action_None` | 617 | 618 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–629 | 622 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–378 | 370 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 15–41 | 16 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 16–628 | 565 | 7 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 62–225 | 144 | 6 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 64–315 | 249 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 95–629 | 495 | 7 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 95–99 | 5 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 96–404 | 293 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 107–296 | 187 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 124–462 | 245 | 10 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 185–383 | 198 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 205–472 | 259 | 5 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 212–262 | 28 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 236–298 | 36 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 320–629 | 309 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 332–402 | 71 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 339–510 | 132 | 12 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 363–550 | 181 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 404–421 | 4 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 409–629 | 181 | 15 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 419–422 | 4 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 423–424 | 2 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 427–429 | 3 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 433–629 | 181 | 6 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 439–623 | 170 | 6 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 442–443 | 2 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 449–629 | 131 | 8 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 453–454 | 2 | 1 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 458–459 | 2 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 458–603 | 111 | 4 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 467–552 | 44 | 9 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 498–568 | 46 | 3 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 537–629 | 91 | 2 | Undefined position; Undefined team |
| `50` | `71` | Position_Unknown | Team_Unknown | 541–572 | 9 | 3 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 558–574 | 15 | 2 | Undefined position; Undefined team |
| `52` | `74` | Position_Unknown | Team_Unknown | 566–586 | 6 | 2 | Undefined position; Undefined team |
| `53` | `75` | Position_Unknown | Team_Unknown | 571–580 | 8 | 2 | Undefined position; Undefined team |
| `54` | `76` | Position_Unknown | Team_Unknown | 572–588 | 10 | 2 | Undefined position; Undefined team |
| `55` | `77` | Position_Unknown | Team_Unknown | 581–583 | 3 | 1 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 584–586 | 3 | 1 | Undefined position; Undefined team |
| `57` | `80` | Position_Unknown | Team_Unknown | 592–628 | 32 | 4 | Undefined position; Undefined team |
| `58` | `81` | Position_Unknown | Team_Unknown | 601–618 | 7 | 3 | Undefined position; Undefined team |
| `59` | `83` | Position_Unknown | Team_Unknown | 604–616 | 13 | 1 | Undefined position; Undefined team |
| `60` | `84` | Position_Unknown | Team_Unknown | 606–629 | 15 | 2 | Undefined position; Undefined team |
| `61` | `85` | Position_Unknown | Team_Unknown | 620–622 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `32` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `44` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punt_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 47 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 47 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 94 |
| Missing visible bounding boxes during action | 239 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [30-63] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-629] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-144] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-305] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-629] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-383] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-378] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-58] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-605] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-176] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-318] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-461] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-565] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-604] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-365] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-476] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-623] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-111] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-359] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-418] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-494] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-572] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-629] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-460] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-473] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-497] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-617] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-628] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-61] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-300] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-362] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-377] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-394] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-410] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-463] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-480] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-495] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [30-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-88] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-628] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-191] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-138] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-309] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-315] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-153] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-273] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-337] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-370] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-225] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-271] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-351] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-365] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-392] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-296] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-263] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-288] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-377] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [273-371] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [373-383] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-436] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-450] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-466] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-472] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-250] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-290] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-438] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-629] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-402] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-352] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-405] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-426] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-471] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-476] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-483] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-503] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-541] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-427] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-446] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-453] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-472] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-481] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-552] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [559-561] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [563-564] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [566-575] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [577-578] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' for track '35' starts at frame 609, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_CrossGoalLine' range [609-609] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [612-619] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-623] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [628-629] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-422] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-429] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-494] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-502] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-516] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-606] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-485] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-552] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-560] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-586] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-596] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-623] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-452] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-461] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-484] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-503] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-526] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-629] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-519] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-565] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-603] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-479] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-485] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-499] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-536] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-547] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-552] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-526] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-541] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-568] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-549] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-629] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-567] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-572] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-570] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-586] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-576] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-580] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-575] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-588] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-583] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-586] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-597] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-601] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-623] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-628] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-606] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-618] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-616] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-616] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-629] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-622] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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