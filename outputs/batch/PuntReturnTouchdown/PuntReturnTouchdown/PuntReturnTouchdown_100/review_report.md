# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_100

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_100`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 217
- **Validation Warnings:** 265
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 202
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `8` | `8` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `37` | `32` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `37` | `32` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `46` | `39` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `8` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 50 | START | 50 | 107 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `8` | `8` | 78 | END | 78 | 78 |
| ✅ EXACT | `Action_PuntBall` | Punter | `8` | `8` | 108 | START | 108 | 121 |
| ⚠️ START CHANGED | `Action_CatchPunt` | Position_Unknown | `37` | `32` | 222 | START | 263 | 263 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `37` | `32` | 278 | START | 278 | 309 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `46` | `39` | 611 | START | 611 | 617 |

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
- **Visible Frames:** 0–355
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 60 | 11 | inferred_complete_timeline |
| `Action_None` | 70 | 201 | 132 | inferred_complete_timeline |
| `Action_None` | 204 | 277 | 74 | inferred_complete_timeline |
| `Action_None` | 280 | 281 | 2 | inferred_complete_timeline |
| `Action_None` | 351 | 355 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 96 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–382
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_LongSnap` | 50 | 107 | 58 | inferred_complete_timeline |
| `Action_None` | 108 | 273 | 166 | inferred_complete_timeline |
| `Action_None` | 285 | 337 | 53 | inferred_complete_timeline |
| `Action_None` | 339 | 382 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 170 | 121 | inferred_complete_timeline |
| `Action_None` | 173 | 218 | 46 | inferred_complete_timeline |
| `Action_None` | 220 | 270 | 51 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 346 | 66 | inferred_complete_timeline |
| `Action_None` | 348 | 360 | 13 | inferred_complete_timeline |
| `Action_None` | 363 | 364 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 374 | 5 | inferred_complete_timeline |
| `Action_None` | 381 | 400 | 20 | inferred_complete_timeline |
| `Action_None` | 402 | 405 | 4 | inferred_complete_timeline |
| `Action_None` | 407 | 408 | 2 | inferred_complete_timeline |
| `Action_None` | 475 | 629 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–627
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 149 | 100 | inferred_complete_timeline |
| `Action_None` | 154 | 326 | 173 | inferred_complete_timeline |
| `Action_None` | 328 | 339 | 12 | inferred_complete_timeline |
| `Action_None` | 345 | 432 | 88 | inferred_complete_timeline |
| `Action_None` | 445 | 572 | 128 | inferred_complete_timeline |
| `Action_None` | 578 | 584 | 7 | inferred_complete_timeline |
| `Action_None` | 587 | 627 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 144 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–332
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_None` | 79 | 107 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 108 | 121 | 14 | inferred_complete_timeline |
| `Action_None` | 122 | 332 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 178 | 129 | inferred_complete_timeline |
| `Action_None` | 184 | 260 | 77 | inferred_complete_timeline |
| `Action_None` | 283 | 305 | 23 | inferred_complete_timeline |
| `Action_None` | 307 | 411 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 162 | 113 | inferred_complete_timeline |
| `Action_None` | 166 | 201 | 36 | inferred_complete_timeline |
| `Action_None` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_None` | 230 | 247 | 18 | inferred_complete_timeline |
| `Action_None` | 302 | 421 | 120 | inferred_complete_timeline |
| `Action_None` | 423 | 461 | 39 | inferred_complete_timeline |
| `Action_None` | 465 | 508 | 44 | inferred_complete_timeline |
| `Action_None` | 511 | 629 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–593
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 59 | 10 | inferred_complete_timeline |
| `Action_None` | 119 | 326 | 208 | inferred_complete_timeline |
| `Action_None` | 328 | 373 | 46 | inferred_complete_timeline |
| `Action_None` | 377 | 593 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–474
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 70 | 21 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 267 | 127 | inferred_complete_timeline |
| `Action_None` | 269 | 474 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 66 | 17 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 243 | 167 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 82 | 33 | inferred_complete_timeline |
| `Action_None` | 84 | 248 | 165 | inferred_complete_timeline |
| `Action_None` | 251 | 511 | 261 | inferred_complete_timeline |
| `Action_None` | 514 | 629 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 67 | 18 | inferred_complete_timeline |
| `Action_None` | 78 | 81 | 4 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 123 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 129 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 93–629 | 490 | 8 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 94–115 | 22 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 106–629 | 501 | 9 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 114–354 | 241 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 122–305 | 165 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 140–226 | 87 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 143–232 | 84 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 147–339 | 193 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 154–572 | 416 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 160–251 | 92 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 219–293 | 53 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 226–349 | 118 | 4 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 243–315 | 60 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 257–423 | 167 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 262–282 | 21 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 263–309 | 47 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 266–283 | 18 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 270–572 | 303 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 289–625 | 303 | 8 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 297–332 | 8 | 2 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 298–629 | 290 | 12 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 320–629 | 284 | 10 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 332–629 | 285 | 7 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 338–351 | 14 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 355–479 | 123 | 2 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 356–629 | 248 | 7 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 358–571 | 189 | 3 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 361–629 | 247 | 9 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 375–629 | 248 | 2 | Undefined position; Undefined team |
| `46` | `53` | Position_Unknown | Team_Unknown | 418–629 | 183 | 7 | Undefined position; Undefined team |
| `47` | `54` | Position_Unknown | Team_Unknown | 418–456 | 39 | 1 | Undefined position; Undefined team |
| `48` | `55` | Position_Unknown | Team_Unknown | 419–627 | 205 | 3 | Undefined position; Undefined team |
| `49` | `56` | Position_Unknown | Team_Unknown | 427–629 | 173 | 6 | Undefined position; Undefined team |
| `50` | `60` | Position_Unknown | Team_Unknown | 506–585 | 79 | 2 | Undefined position; Undefined team |
| `51` | `61` | Position_Unknown | Team_Unknown | 519–520 | 2 | 1 | Undefined position; Undefined team |
| `52` | `63` | Position_Unknown | Team_Unknown | 534–557 | 24 | 1 | Undefined position; Undefined team |
| `53` | `65` | Position_Unknown | Team_Unknown | 557–558 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchPunt` for actor_track_id `37` (Position_Unknown): Annotated start 222 != Inferred start 263

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 185 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CatchPunt' for track '32' has invalid range: start=263, end=251. Clamping end to start.
- ⚠️ Action 'Action_None' range [50-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-326] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-339] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-432] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-572] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-584] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-627] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-227] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-421] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-461] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-508] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-305] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-411] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-273] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-337] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-382] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-332] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-243] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-218] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-270] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-346] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-360] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-400] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-405] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-408] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-67] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-474] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-326] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-373] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-593] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-248] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-511] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-629] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-201] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-115] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-391] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-446] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-482] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-503] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-297] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-332] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-418] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-487] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-553] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-566] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-584] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-629] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-354] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-305] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-226] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-339] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-572] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-251] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-263] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-293] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-291] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-345] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-315] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-423] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [278-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-572] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-350] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-381] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-405] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-442] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-508] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-625] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-302] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-326] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-425] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-441] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-453] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-568] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-571] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-583] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-629] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-336] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-368] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-381] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-454] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-483] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-580] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-585] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-604] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-608] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-374] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-381] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-409] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-419] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-351] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-391] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-479] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-382] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-457] for track '42' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-494] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-509] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-520] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-614] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-387] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-571] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-402] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-456] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-464] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-564] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-569] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-572] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-579] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-586] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-405] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-629] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-441] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-492] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-545] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-568] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-456] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-570] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-578] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-627] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-491] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-510] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-513] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-556] for track '49' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-562] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-629] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-580] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-585] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-557] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '53' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>