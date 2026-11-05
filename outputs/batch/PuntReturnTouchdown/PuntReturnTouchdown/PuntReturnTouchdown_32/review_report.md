# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_32`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 205
- **Validation Warnings:** 253
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 191
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `34` | `28` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `28` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `49` | `38` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `11` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `4` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `8` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 19 | START | 19 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 43 | END | 43 | 43 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 67 | START | 67 | 79 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `34` | `28` | 188 | START | 188 | 196 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `34` | `28` | 197 | START | 197 | 209 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `49` | `38` | 426 | START | 426 | 434 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 59 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 54 | 36 | inferred_complete_timeline |
| `Action_None` | 56 | 61 | 6 | inferred_complete_timeline |
| `Action_None` | 80 | 252 | 173 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 357 | 54 | inferred_complete_timeline |
| `Action_None` | 360 | 362 | 3 | inferred_complete_timeline |
| `Action_None` | 364 | 449 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 66 | 48 | inferred_complete_timeline |
| `Action_None` | 69 | 449 | 381 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 19 | 66 | 48 | inferred_complete_timeline |
| `Action_None` | 67 | 221 | 155 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 246 | 10 | inferred_complete_timeline |
| `Action_None` | 248 | 280 | 33 | inferred_complete_timeline |
| `Action_None` | 290 | 306 | 17 | inferred_complete_timeline |
| `Action_None` | 308 | 310 | 3 | inferred_complete_timeline |
| `Action_None` | 338 | 361 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 70 | 52 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 81 | 95 | 15 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 114 | 11 | inferred_complete_timeline |
| `Action_None` | 116 | 301 | 186 | inferred_complete_timeline |
| `Action_None` | 307 | 312 | 6 | inferred_complete_timeline |
| `Action_None` | 322 | 449 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 83 | 65 | inferred_complete_timeline |
| `Action_None` | 89 | 218 | 130 | inferred_complete_timeline |
| `Action_None` | 220 | 320 | 101 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 43 | 1 | inferred_complete_timeline |
| `Action_None` | 44 | 66 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_None` | 80 | 99 | 20 | inferred_complete_timeline |
| `Action_None` | 107 | 326 | 220 | inferred_complete_timeline |
| `Action_None` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 184 | 166 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |
| `Action_None` | 241 | 275 | 35 | inferred_complete_timeline |
| `Action_None` | 279 | 297 | 19 | inferred_complete_timeline |
| `Action_None` | 302 | 449 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 59 | 41 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 109 | 6 | inferred_complete_timeline |
| `Action_None` | 114 | 132 | 19 | inferred_complete_timeline |
| `Action_None` | 134 | 159 | 26 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 217 | 46 | inferred_complete_timeline |
| `Action_None` | 225 | 250 | 26 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 302 | 47 | inferred_complete_timeline |
| `Action_None` | 315 | 324 | 10 | inferred_complete_timeline |
| `Action_None` | 326 | 328 | 3 | inferred_complete_timeline |
| `Action_None` | 340 | 343 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 35 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 335 | 317 | inferred_complete_timeline |
| `Action_None` | 337 | 436 | 100 | inferred_complete_timeline |
| `Action_None` | 439 | 449 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 83 | 65 | inferred_complete_timeline |
| `Action_None` | 86 | 105 | 20 | inferred_complete_timeline |
| `Action_None` | 114 | 125 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_None` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_None` | 75 | 83 | 9 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 107 | 89 | inferred_complete_timeline |
| `Action_None` | 113 | 297 | 185 | inferred_complete_timeline |
| `Action_None` | 299 | 306 | 8 | inferred_complete_timeline |
| `Action_None` | 312 | 394 | 83 | inferred_complete_timeline |
| `Action_None` | 400 | 449 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 177 | 159 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–56 | 52 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–152 | 83 | 7 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–53 | 41 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 4–150 | 141 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 30–449 | 358 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 30–62 | 27 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 33–77 | 30 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 49–377 | 318 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 76–141 | 66 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 82–308 | 222 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 84–242 | 159 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 112–448 | 236 | 7 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 116–138 | 23 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 121–209 | 88 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 122–284 | 163 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 129–206 | 78 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 138–413 | 272 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 145–449 | 299 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 163–272 | 87 | 3 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 175–181 | 7 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 209–285 | 54 | 4 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 217–296 | 51 | 5 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 227–234 | 8 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 244–449 | 206 | 3 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 254–438 | 128 | 5 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 273–447 | 175 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 286–412 | 62 | 10 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 287–292 | 6 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 309–449 | 138 | 2 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 319–449 | 124 | 3 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 336–449 | 113 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 340–449 | 107 | 3 | Undefined position; Undefined team |
| `48` | `68` | Position_Unknown | Team_Unknown | 355–368 | 14 | 1 | Undefined position; Undefined team |
| `49` | `70` | Position_Unknown | Team_Unknown | 361–449 | 85 | 2 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 397–449 | 39 | 3 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 400–449 | 41 | 2 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 406–449 | 44 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 416–449 | 34 | 1 | Undefined position; Undefined team |
| `54` | `79` | Position_Unknown | Team_Unknown | 419–420 | 2 | 1 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 435–449 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 41 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 41 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 82 |
| Missing visible bounding boxes during action | 167 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 66: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [19-66] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-252] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-357] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-221] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-306] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-361] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-275] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-297] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-107] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-394] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-326] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-389] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-218] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-301] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-66] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-217] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-250] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-302] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-324] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-343] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-335] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-436] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-50] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-32] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-77] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-339] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-39] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-377] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-260] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-308] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-242] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-362] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-448] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-138] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-129] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-206] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-413] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-206] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-174] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-254] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-219] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-289] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-425] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-328] for track '39' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-423] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-438] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-447] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-338] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-360] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-390] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-404] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-412] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-292] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-393] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-436] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-396] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-449] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-357] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-393] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-368] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-413] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-449] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>