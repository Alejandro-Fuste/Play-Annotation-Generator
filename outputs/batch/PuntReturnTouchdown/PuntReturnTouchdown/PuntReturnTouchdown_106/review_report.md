# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_106

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_106`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 215
- **Validation Warnings:** 251
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 201
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | defense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `45` | `36` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 13 | START | 13 | 69 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 38 | END | 38 | 38 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 70 | START | 70 | 84 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `10` | `10` | 191 | START | 191 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | `10` | `10` | 226 | START | 246 | 248 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `45` | `36` | 599 | START | 599 | 600 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 92 | 80 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 139 | 39 | inferred_complete_timeline |
| `Action_None` | 144 | 167 | 24 | inferred_complete_timeline |
| `Action_None` | 169 | 436 | 268 | inferred_complete_timeline |
| `Action_None` | 439 | 501 | 63 | inferred_complete_timeline |
| `Action_None` | 505 | 554 | 50 | inferred_complete_timeline |
| `Action_None` | 560 | 588 | 29 | inferred_complete_timeline |
| `Action_None` | 595 | 608 | 14 | inferred_complete_timeline |
| `Action_None` | 612 | 618 | 7 | inferred_complete_timeline |
| `Action_None` | 625 | 629 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 171 | 159 | inferred_complete_timeline |
| `Action_None` | 219 | 267 | 49 | inferred_complete_timeline |
| `Action_None` | 273 | 319 | 47 | inferred_complete_timeline |
| `Action_None` | 322 | 324 | 3 | inferred_complete_timeline |
| `Action_None` | 326 | 489 | 164 | inferred_complete_timeline |
| `Action_None` | 493 | 554 | 62 | inferred_complete_timeline |
| `Action_None` | 556 | 598 | 43 | inferred_complete_timeline |
| `Action_None` | 604 | 629 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–614
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_LongSnap` | 13 | 69 | 57 | inferred_complete_timeline |
| `Action_None` | 70 | 149 | 80 | inferred_complete_timeline |
| `Action_None` | 151 | 261 | 111 | inferred_complete_timeline |
| `Action_None` | 267 | 287 | 21 | inferred_complete_timeline |
| `Action_None` | 290 | 295 | 6 | inferred_complete_timeline |
| `Action_None` | 298 | 312 | 15 | inferred_complete_timeline |
| `Action_None` | 314 | 361 | 48 | inferred_complete_timeline |
| `Action_None` | 365 | 408 | 44 | inferred_complete_timeline |
| `Action_None` | 410 | 513 | 104 | inferred_complete_timeline |
| `Action_None` | 516 | 614 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–519
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 98 | 86 | inferred_complete_timeline |
| `Action_None` | 102 | 424 | 323 | inferred_complete_timeline |
| `Action_None` | 427 | 512 | 86 | inferred_complete_timeline |
| `Action_None` | 516 | 519 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 490 | 478 | inferred_complete_timeline |
| `Action_None` | 493 | 615 | 123 | inferred_complete_timeline |
| `Action_None` | 618 | 620 | 3 | inferred_complete_timeline |
| `Action_None` | 622 | 629 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 128 | 116 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 207 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 69 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_None` | 85 | 235 | 151 | inferred_complete_timeline |
| `Action_None` | 237 | 267 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–618
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 129 | 117 | inferred_complete_timeline |
| `Action_None` | 135 | 175 | 41 | inferred_complete_timeline |
| `Action_None` | 177 | 190 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 213 | 15 | inferred_complete_timeline |
| `Action_None` | 216 | 458 | 243 | inferred_complete_timeline |
| `Action_None` | 464 | 494 | 31 | inferred_complete_timeline |
| `Action_None` | 497 | 570 | 74 | inferred_complete_timeline |
| `Action_None` | 573 | 618 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 121 | 109 | inferred_complete_timeline |
| `Action_None` | 132 | 151 | 20 | inferred_complete_timeline |
| `Action_None` | 154 | 176 | 23 | inferred_complete_timeline |
| `Action_None` | 199 | 209 | 11 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 207 | 195 | inferred_complete_timeline |
| `Action_None` | 209 | 256 | 48 | inferred_complete_timeline |
| `Action_None` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 321 | 48 | inferred_complete_timeline |
| `Action_None` | 328 | 360 | 33 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |
| `Action_None` | 371 | 394 | 24 | inferred_complete_timeline |
| `Action_None` | 397 | 493 | 97 | inferred_complete_timeline |
| `Action_None` | 495 | 562 | 68 | inferred_complete_timeline |
| `Action_None` | 626 | 629 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 133 | 121 | inferred_complete_timeline |
| `Action_None` | 135 | 273 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 358 | 346 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–614
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_CatchPunt` | 191 | 207 | 17 | inferred_complete_timeline |
| `Action_None` | 208 | 220 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 277 | 544 | 268 | inferred_complete_timeline |
| `Action_BallCarry` | 556 | 567 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 571 | 574 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 580 | 582 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 584 | 586 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 590 | 593 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 613 | 614 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–600
- **Visible Samples:** 566

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 35 | 23 | inferred_complete_timeline |
| `Action_None` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_None` | 46 | 90 | 45 | inferred_complete_timeline |
| `Action_None` | 96 | 478 | 383 | inferred_complete_timeline |
| `Action_None` | 481 | 548 | 68 | inferred_complete_timeline |
| `Action_None` | 551 | 567 | 17 | inferred_complete_timeline |
| `Action_None` | 572 | 574 | 3 | inferred_complete_timeline |
| `Action_None` | 579 | 582 | 4 | inferred_complete_timeline |
| `Action_None` | 596 | 600 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 8–629 | 581 | 9 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 16–140 | 125 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 42–94 | 53 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 59–606 | 494 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 98–194 | 97 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 100–403 | 239 | 6 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 122–311 | 189 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 127–276 | 150 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 163–617 | 401 | 6 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 226–446 | 218 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 237–629 | 374 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 254–273 | 20 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 263–629 | 356 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 269–629 | 352 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 279–436 | 158 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 302–622 | 232 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 308–443 | 132 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 329–589 | 243 | 6 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 363–481 | 113 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 373–629 | 246 | 4 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 453–628 | 176 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 461–626 | 129 | 11 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 462–629 | 161 | 2 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 483–569 | 75 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 503–599 | 48 | 9 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 516–579 | 22 | 4 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 527–629 | 81 | 5 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 599–629 | 13 | 4 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 618–629 | 12 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 620–626 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (8 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `45` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 186 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [13-98] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-424] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-512] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-519] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-207] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-256] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-321] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-360] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-394] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-493] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-562] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-235] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-273] for track '3' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-171] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-267] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-319] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-489] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-554] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-598] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-629] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [13-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-312] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-361] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-408] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-513] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-614] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-490] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-615] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-620] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-629] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-207] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-139] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-436] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-501] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-554] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-588] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-608] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-618] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-629] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [246-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [277-544] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [556-567] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [571-574] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [580-582] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [584-586] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [590-593] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [613-614] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-121] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-151] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-190] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-458] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-494] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-570] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-618] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-478] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-548] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-567] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-582] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-600] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-395] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-441] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-499] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-545] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-140] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-276] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-465] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-552] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-598] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-606] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-227] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-265] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-281] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-403] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-311] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-276] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-327] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-477] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-608] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-617] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-346] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-428] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-446] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-284] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-610] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-617] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-532] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-540] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-570] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-383] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-528] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-436] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-515] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-535] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-622] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-390] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-443] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-459] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-535] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-555] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-578] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-589] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-388] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-420] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-481] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-397] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-429] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-608] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-629] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-628] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-513] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-520] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-542] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [544-551] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [555-574] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [577-580] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [592-594] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [599-600] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-626] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-544] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-522] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-536] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-569] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-506] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-521] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-530] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-569] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-580] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-599] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-526] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-542] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-579] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-544] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-568] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-593] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-606] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-629] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-605] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-624] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-622] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-626] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>