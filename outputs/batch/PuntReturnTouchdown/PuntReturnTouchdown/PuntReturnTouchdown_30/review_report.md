# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_30

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_30`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 159
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
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `11` | `11` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `1` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `11` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `17` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `18` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `2` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `7` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 140 | START | 140 | 193 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `11` | `11` | 167 | END | 167 | 167 |
| ✅ EXACT | `Action_PuntBall` | Punter | `11` | `11` | 194 | START | 194 | 210 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `25` | 294 | START | 294 | 301 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `25` | 318 | START | 318 | 536 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `25` | 622 | START | 622 | 629 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 613

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 167 | 28 | inferred_complete_timeline |
| `Action_None` | 183 | 384 | 202 | inferred_complete_timeline |
| `Action_None` | 387 | 629 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–510
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 182 | 43 | inferred_complete_timeline |
| `Action_None` | 186 | 259 | 74 | inferred_complete_timeline |
| `Action_None` | 264 | 404 | 141 | inferred_complete_timeline |
| `Action_None` | 408 | 510 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 385 | 246 | inferred_complete_timeline |
| `Action_None` | 387 | 446 | 60 | inferred_complete_timeline |
| `Action_None` | 449 | 629 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_LongSnap` | 140 | 193 | 54 | inferred_complete_timeline |
| `Action_None` | 194 | 508 | 315 | inferred_complete_timeline |
| `Action_None` | 511 | 512 | 2 | inferred_complete_timeline |
| `Action_None` | 523 | 562 | 40 | inferred_complete_timeline |
| `Action_None` | 564 | 571 | 8 | inferred_complete_timeline |
| `Action_None` | 573 | 629 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–570
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 372 | 233 | inferred_complete_timeline |
| `Action_None` | 375 | 544 | 170 | inferred_complete_timeline |
| `Action_None` | 558 | 570 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–600
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 407 | 268 | inferred_complete_timeline |
| `Action_None` | 416 | 439 | 24 | inferred_complete_timeline |
| `Action_None` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 444 | 445 | 2 | inferred_complete_timeline |
| `Action_None` | 450 | 600 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_SnapReceive` | 167 | 167 | 1 | inferred_complete_timeline |
| `Action_None` | 168 | 193 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_None` | 211 | 273 | 63 | inferred_complete_timeline |
| `Action_None` | 275 | 291 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 613

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 161 | 22 | inferred_complete_timeline |
| `Action_None` | 175 | 306 | 132 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 445 | 134 | inferred_complete_timeline |
| `Action_None` | 447 | 629 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 167 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 344 | 205 | inferred_complete_timeline |
| `Action_None` | 346 | 350 | 5 | inferred_complete_timeline |
| `Action_None` | 357 | 629 | 273 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–489
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 489 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 219 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 629 | 490 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 384 | 245 | inferred_complete_timeline |
| `Action_None` | 387 | 558 | 172 | inferred_complete_timeline |
| `Action_None` | 566 | 567 | 2 | inferred_complete_timeline |
| `Action_None` | 573 | 629 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–497
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 190 | 51 | inferred_complete_timeline |
| `Action_None` | 192 | 320 | 129 | inferred_complete_timeline |
| `Action_None` | 329 | 359 | 31 | inferred_complete_timeline |
| `Action_None` | 361 | 497 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 217 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 236 | 97 | inferred_complete_timeline |
| `Action_None` | 239 | 367 | 129 | inferred_complete_timeline |
| `Action_None` | 379 | 380 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 629 | 490 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 629 | 490 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 197–226 | 30 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 227–556 | 330 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 237–247 | 11 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 237–629 | 392 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 244–629 | 373 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 246–629 | 378 | 6 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 255–571 | 317 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 287–388 | 102 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 336–629 | 293 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 396–629 | 223 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 413–430 | 16 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 434–629 | 196 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 464–591 | 90 | 8 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 487–627 | 133 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 491–629 | 139 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 492–493 | 2 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 500–554 | 55 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 507–508 | 2 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 513–546 | 33 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 523–613 | 33 | 8 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 539–546 | 8 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 549–561 | 12 | 2 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 569–629 | 61 | 1 | Undefined position; Undefined team |
| `43` | `50` | Position_Unknown | Team_Unknown | 580–585 | 6 | 1 | Undefined position; Undefined team |
| `44` | `51` | Position_Unknown | Team_Unknown | 583–629 | 32 | 4 | Undefined position; Undefined team |
| `45` | `52` | Position_Unknown | Team_Unknown | 596–629 | 34 | 1 | Undefined position; Undefined team |
| `46` | `53` | Position_Unknown | Team_Unknown | 600–629 | 30 | 1 | Undefined position; Undefined team |
| `47` | `54` | Position_Unknown | Team_Unknown | 612–613 | 2 | 1 | Undefined position; Undefined team |
| `48` | `55` | Position_Unknown | Team_Unknown | 623–629 | 7 | 1 | Undefined position; Undefined team |
| `49` | `56` | Position_Unknown | Team_Unknown | 624–629 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 94 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [140-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-167] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-384] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-629] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-508] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-562] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-571] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-629] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-344] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-629] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-372] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-544] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-570] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-190] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-497] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-407] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-439] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-600] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-306] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-445] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-629] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-291] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-367] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-489] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-384] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-558] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-385] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-446] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-404] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-510] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-556] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-397] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [318-536] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [543-621] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-571] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-388] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-450] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-629] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-566] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-587] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-419] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-430] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-476] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-484] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-495] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-518] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-555] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-591] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-611] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [620-627] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-493] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-554] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-540] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-546] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-526] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-540] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-546] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-557] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-560] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-546] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-553] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-561] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-585] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-595] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-609] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-624] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '47' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>