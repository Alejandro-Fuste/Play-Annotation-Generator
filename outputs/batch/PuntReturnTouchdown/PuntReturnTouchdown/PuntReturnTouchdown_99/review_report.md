# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_99`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 131
- **Validation Warnings:** 145
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `35` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `35` | `29` |
| ✅ EXACT | `Action_CrossGoalLine` | Interior_Rusher2 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `1` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `16` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `6` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 80 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 76 | END | 76 | 76 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 81 | START | 81 | 100 |
| ✅ EXACT | `Action_PuntBall` | Punter | `14` | `14` | 101 | START | 101 | 119 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `35` | `29` | 239 | START | 239 | 254 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `35` | `29` | 268 | START | 268 | 434 |
| ✅ EXACT | `Action_CrossGoalLine` | Interior_Rusher2 | `13` | `13` | 610 | START | 610 | 615 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_None` | 81 | 418 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 328 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–401
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 140 | 60 | inferred_complete_timeline |
| `Action_None` | 142 | 165 | 24 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 348 | 175 | inferred_complete_timeline |
| `Action_None` | 352 | 401 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–364
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_LongSnap` | 81 | 100 | 20 | inferred_complete_timeline |
| `Action_None` | 101 | 262 | 162 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 268 | 364 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 616

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 157 | 77 | inferred_complete_timeline |
| `Action_None` | 160 | 181 | 22 | inferred_complete_timeline |
| `Action_None` | 194 | 629 | 436 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–383
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 319 | 239 | inferred_complete_timeline |
| `Action_None` | 337 | 383 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 621

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 218 | 138 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |
| `Action_None` | 237 | 629 | 393 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_SnapReceive` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_None` | 77 | 100 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 101 | 119 | 19 | inferred_complete_timeline |
| `Action_None` | 120 | 174 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–422
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 82 | 422 | 341 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 116 | 36 | inferred_complete_timeline |
| `Action_None` | 129 | 167 | 39 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 339 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–611
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_None` | 81 | 180 | 100 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 190 | 288 | 99 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 298 | 301 | 4 | inferred_complete_timeline |
| `Action_None` | 303 | 611 | 309 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 121 | 41 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_PreSnap` | 520 | 560 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 564 | 609 | 46 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 610 | 615 | 6 | inferred_complete_timeline |
| `Action_None` | 616 | 629 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 242 | 162 | inferred_complete_timeline |
| `Action_None` | 248 | 380 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 78 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 204 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 218 | 138 | inferred_complete_timeline |
| `Action_None` | 222 | 629 | 408 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 160 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 119 | 39 | inferred_complete_timeline |
| `Action_None` | 124 | 424 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 107 | 27 | inferred_complete_timeline |
| `Action_None` | 109 | 381 | 273 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 27–89 | 58 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 80–146 | 59 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 123–403 | 280 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 152–442 | 290 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 154–173 | 17 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 162–629 | 459 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 176–616 | 437 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 186–285 | 20 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 204–629 | 421 | 6 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 242–388 | 147 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 320–401 | 74 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 350–377 | 26 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 368–392 | 25 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 417–443 | 14 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 441–629 | 189 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 454–588 | 122 | 5 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 478–479 | 2 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 586–602 | 9 | 3 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 601–602 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `35` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 100 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [81-328] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-218] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-629] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-319] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-383] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-424] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-629] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-116] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-381] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-262] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-364] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-348] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-401] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-242] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-380] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-517] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-560] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-174] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-422] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-288] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-611] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-418] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-218] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-629] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-31] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-105] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-351] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-403] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-442] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-173] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-616] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-431] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-439] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-616] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-434] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [436-624] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-388] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-401] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-363] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-377] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-392] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-443] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-552] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-570] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-576] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-584] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-588] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-593] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-602] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [601-602] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>