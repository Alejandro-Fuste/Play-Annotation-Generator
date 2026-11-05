# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_76`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 182
- **Validation Warnings:** 233
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 166
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `49` | `36` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `10` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `10` | `10` | 11 | START | 11 | 62 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 38 | END | 38 | 38 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 63 | START | 63 | 81 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `20` | `19` | 184 | START | 184 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `20` | `19` | 216 | START | 216 | 291 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `49` | `36` | 573 | START | 573 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 45 | 35 | inferred_complete_timeline |
| `Action_None` | 51 | 55 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 88 | 78 | inferred_complete_timeline |
| `Action_None` | 96 | 108 | 13 | inferred_complete_timeline |
| `Action_None` | 111 | 437 | 327 | inferred_complete_timeline |
| `Action_None` | 439 | 523 | 85 | inferred_complete_timeline |
| `Action_None` | 528 | 535 | 8 | inferred_complete_timeline |
| `Action_None` | 561 | 568 | 8 | inferred_complete_timeline |
| `Action_None` | 570 | 599 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 61 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_LongSnap` | 11 | 62 | 52 | inferred_complete_timeline |
| `Action_None` | 63 | 184 | 122 | inferred_complete_timeline |
| `Action_None` | 192 | 387 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–483
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 114 | 104 | inferred_complete_timeline |
| `Action_None` | 117 | 342 | 226 | inferred_complete_timeline |
| `Action_None` | 345 | 461 | 117 | inferred_complete_timeline |
| `Action_None` | 465 | 466 | 2 | inferred_complete_timeline |
| `Action_None` | 482 | 483 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–471
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 328 | 318 | inferred_complete_timeline |
| `Action_None` | 331 | 467 | 137 | inferred_complete_timeline |
| `Action_None` | 469 | 471 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 194 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–561
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 62 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_None` | 82 | 406 | 325 | inferred_complete_timeline |
| `Action_None` | 408 | 518 | 111 | inferred_complete_timeline |
| `Action_None` | 525 | 561 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 71 | 61 | inferred_complete_timeline |
| `Action_None` | 73 | 141 | 69 | inferred_complete_timeline |
| `Action_None` | 146 | 177 | 32 | inferred_complete_timeline |
| `Action_None` | 179 | 382 | 204 | inferred_complete_timeline |
| `Action_None` | 386 | 451 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–347
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 240 | 230 | inferred_complete_timeline |
| `Action_None` | 249 | 279 | 31 | inferred_complete_timeline |
| `Action_None` | 292 | 301 | 10 | inferred_complete_timeline |
| `Action_None` | 337 | 347 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 39 | 29 | inferred_complete_timeline |
| `Action_None` | 55 | 201 | 147 | inferred_complete_timeline |
| `Action_None` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 266 | 256 | inferred_complete_timeline |
| `Action_None` | 286 | 295 | 10 | inferred_complete_timeline |
| `Action_None` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 325 | 8 | inferred_complete_timeline |
| `Action_None` | 330 | 362 | 33 | inferred_complete_timeline |
| `Action_None` | 365 | 376 | 12 | inferred_complete_timeline |
| `Action_None` | 388 | 392 | 5 | inferred_complete_timeline |
| `Action_None` | 395 | 405 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 30 | 20 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 35 | 25 | inferred_complete_timeline |
| `Action_None` | 64 | 323 | 260 | inferred_complete_timeline |
| `Action_None` | 326 | 350 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 36 | 26 | inferred_complete_timeline |
| `Action_None` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 308 | 250 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–338
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 143 | 189 | 47 | inferred_complete_timeline |
| `Action_None` | 199 | 227 | 29 | inferred_complete_timeline |
| `Action_None` | 230 | 263 | 34 | inferred_complete_timeline |
| `Action_None` | 312 | 338 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 44 | 34 | inferred_complete_timeline |
| `Action_None` | 47 | 89 | 43 | inferred_complete_timeline |
| `Action_None` | 95 | 528 | 434 | inferred_complete_timeline |
| `Action_None` | 530 | 599 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 224 | 214 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 17–379 | 319 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 59–410 | 262 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 64–107 | 39 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 70–137 | 64 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 89–100 | 12 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 93–372 | 260 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 112–118 | 7 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 117–418 | 252 | 11 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 129–354 | 225 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 130–194 | 65 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 142–313 | 99 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 150–193 | 17 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 179–204 | 17 | 3 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 181–407 | 220 | 4 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 259–416 | 147 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 300–599 | 300 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 308–334 | 27 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 310–364 | 52 | 2 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 311–318 | 8 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 344–435 | 76 | 3 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 354–361 | 8 | 1 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 359–420 | 58 | 5 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 389–413 | 25 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 432–436 | 5 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 449–491 | 43 | 1 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 465–599 | 130 | 2 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 473–513 | 38 | 3 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 481–599 | 118 | 2 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 486–572 | 87 | 1 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 519–599 | 71 | 2 | Undefined position; Undefined team |
| `52` | `82` | Position_Unknown | Team_Unknown | 558–575 | 18 | 1 | Undefined position; Undefined team |
| `53` | `83` | Position_Unknown | Team_Unknown | 568–599 | 31 | 2 | Undefined position; Undefined team |
| `54` | `84` | Position_Unknown | Team_Unknown | 575–599 | 21 | 2 | Undefined position; Undefined team |
| `55` | `85` | Position_Unknown | Team_Unknown | 576–599 | 24 | 1 | Undefined position; Undefined team |
| `56` | `86` | Position_Unknown | Team_Unknown | 581–582 | 2 | 1 | Undefined position; Undefined team |
| `57` | `88` | Position_Unknown | Team_Unknown | 585–588 | 4 | 1 | Undefined position; Undefined team |
| `58` | `89` | Position_Unknown | Team_Unknown | 594–599 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 41 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 41 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 82 |
| Missing visible bounding boxes during action | 148 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [11-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-406] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-518] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-561] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-224] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-88] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-437] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-523] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-535] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-568] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-114] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-342] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-461] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-466] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-227] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-263] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-338] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-528] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-599] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-347] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-308] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-177] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-382] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-451] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-350] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-467] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-266] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-295] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-362] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-376] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-392] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-405] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-272] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-292] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-379] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-291] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [380-392] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [394-410] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-107] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-137] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-182] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-320] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-372] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-282] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-346] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-371] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-389] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-418] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-354] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-313] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-400] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-318] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-416] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-334] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-356] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-318] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-371] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-391] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-435] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-361] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-378] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-388] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-411] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-420] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-413] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-491] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-514] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-483] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-513] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-569] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-572] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-574] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-575] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-571] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-593] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-599] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '57' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>