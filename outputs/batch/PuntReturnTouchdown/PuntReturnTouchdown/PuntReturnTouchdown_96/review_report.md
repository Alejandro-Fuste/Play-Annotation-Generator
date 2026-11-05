# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_96`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 58
- **Ball Tracks:** 0
- **Action Segments:** 160
- **Validation Warnings:** 202
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 143
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `31` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Interior_Rusher5 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `1` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `11` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `16` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `18` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 111 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `1` | `1` | 112 | START | 112 | 167 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 142 | END | 142 | 142 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 168 | START | 168 | 169 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `31` | `25` | 276 | START | 276 | 286 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `31` | `25` | 318 | START | 318 | 467 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Interior_Rusher5 | `5` | `5` | 541 | START | 541 | 542 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 212 | 101 | inferred_complete_timeline |
| `Action_None` | 218 | 455 | 238 | inferred_complete_timeline |
| `Action_None` | 457 | 528 | 72 | inferred_complete_timeline |
| `Action_None` | 531 | 564 | 34 | inferred_complete_timeline |
| `Action_None` | 567 | 569 | 3 | inferred_complete_timeline |
| `Action_None` | 571 | 599 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 194 | 83 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 322 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_LongSnap` | 112 | 167 | 56 | inferred_complete_timeline |
| `Action_None` | 168 | 561 | 394 | inferred_complete_timeline |
| `Action_None` | 564 | 566 | 3 | inferred_complete_timeline |
| `Action_None` | 575 | 584 | 10 | inferred_complete_timeline |
| `Action_None` | 588 | 599 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–548
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 391 | 280 | inferred_complete_timeline |
| `Action_None` | 394 | 415 | 22 | inferred_complete_timeline |
| `Action_None` | 421 | 493 | 73 | inferred_complete_timeline |
| `Action_None` | 495 | 542 | 48 | inferred_complete_timeline |
| `Action_None` | 545 | 548 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–400
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 111 | 33 | inferred_complete_timeline |
| `Action_None` | 112 | 395 | 284 | inferred_complete_timeline |
| `Action_None` | 398 | 400 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 190 | 79 | inferred_complete_timeline |
| `Action_None` | 196 | 360 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_SnapReceive` | 142 | 142 | 1 | inferred_complete_timeline |
| `Action_None` | 143 | 167 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 147 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 399 | 288 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 133 | 22 | inferred_complete_timeline |
| `Action_None` | 136 | 220 | 85 | inferred_complete_timeline |
| `Action_None` | 224 | 305 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 183 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–468
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 449 | 338 | inferred_complete_timeline |
| `Action_None` | 465 | 468 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–586
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 560 | 449 | inferred_complete_timeline |
| `Action_None` | 563 | 572 | 10 | inferred_complete_timeline |
| `Action_None` | 578 | 586 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 280 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 460 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 465 | 540 | 76 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 541 | 542 | 2 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 545 | 599 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 392 | 281 | inferred_complete_timeline |
| `Action_None` | 394 | 510 | 117 | inferred_complete_timeline |
| `Action_None` | 512 | 522 | 11 | inferred_complete_timeline |
| `Action_None` | 528 | 571 | 44 | inferred_complete_timeline |
| `Action_None` | 574 | 599 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 212 | 101 | inferred_complete_timeline |
| `Action_None` | 218 | 337 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 234 | 123 | inferred_complete_timeline |
| `Action_None` | 241 | 553 | 313 | inferred_complete_timeline |
| `Action_None` | 557 | 599 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–442
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 442 | 331 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 16–55 | 21 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 154–488 | 330 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 181–311 | 131 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 195–497 | 301 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 202–251 | 50 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 213–599 | 342 | 6 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 229–515 | 280 | 6 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 229–599 | 341 | 6 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 278–436 | 159 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 318–465 | 148 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 323–419 | 84 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 324–325 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 336–472 | 136 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 341–354 | 13 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 347–399 | 52 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 368–369 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 384–386 | 3 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 389–390 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 396–508 | 113 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 414–599 | 141 | 8 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 422–599 | 171 | 2 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 423–454 | 16 | 3 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 430–479 | 38 | 3 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 443–447 | 5 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 443–569 | 120 | 3 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 475–482 | 8 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 475–487 | 13 | 1 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 480–489 | 10 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 483–490 | 8 | 1 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 500–599 | 76 | 6 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 506–510 | 5 | 1 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 508–599 | 90 | 2 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 508–599 | 48 | 2 | Undefined position; Undefined team |
| `52` | `73` | Position_Unknown | Team_Unknown | 512–577 | 60 | 4 | Undefined position; Undefined team |
| `53` | `74` | Position_Unknown | Team_Unknown | 522–539 | 17 | 2 | Undefined position; Undefined team |
| `54` | `78` | Position_Unknown | Team_Unknown | 554–599 | 46 | 1 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 571–572 | 2 | 1 | Undefined position; Undefined team |
| `56` | `83` | Position_Unknown | Team_Unknown | 588–590 | 3 | 1 | Undefined position; Undefined team |
| `57` | `85` | Position_Unknown | Team_Unknown | 595–599 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `31` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 39 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 39 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 78 |
| Missing visible bounding boxes during action | 121 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [112-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-553] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-561] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-566] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-584] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-194] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-399] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-391] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-415] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-493] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-542] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-548] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-280] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-460] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [541-542] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-455] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-528] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-564] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [168-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-468] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-322] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-442] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-392] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-510] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-522] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-571] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-337] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-360] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-560] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-572] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-586] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-395] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-18] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-296] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-488] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-491] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-497] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-251] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-273] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-394] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-467] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [473-515] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-321] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-393] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-520] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-436] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-465] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-419] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-371] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-472] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-391] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-399] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-508] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-491] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-540] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-547] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-576] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-497] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-433] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-460] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-447] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-451] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-553] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-569] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-482] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-487] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-489] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-490] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-529] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-563] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-581] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-510] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-590] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-546] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-518] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-527] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-541] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-577] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-532] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-539] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-590] for track '56' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>