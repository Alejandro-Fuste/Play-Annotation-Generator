# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_17`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 689
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 228
- **Validation Warnings:** 296
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 216
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | Team_Unknown | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `43` | `34` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `43` | `34` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `43` | `34` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `11` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `4` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Position_Unknown | `14` | `14` | 66 | START | 66 | 78 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 90 | END | 90 | 90 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 113 | START | 113 | 123 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `43` | `34` | 233 | START | 233 | 239 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `43` | `34` | 278 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `43` | `34` | 673 | START | N/A | N/A |

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
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 82 | 17 | inferred_complete_timeline |
| `Action_None` | 84 | 145 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 667

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 168 | 103 | inferred_complete_timeline |
| `Action_None` | 170 | 181 | 12 | inferred_complete_timeline |
| `Action_None` | 184 | 248 | 65 | inferred_complete_timeline |
| `Action_None` | 250 | 255 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 469 | 211 | inferred_complete_timeline |
| `Action_None` | 475 | 479 | 5 | inferred_complete_timeline |
| `Action_None` | 481 | 516 | 36 | inferred_complete_timeline |
| `Action_None` | 518 | 536 | 19 | inferred_complete_timeline |
| `Action_None` | 538 | 539 | 2 | inferred_complete_timeline |
| `Action_None` | 544 | 670 | 127 | inferred_complete_timeline |
| `Action_None` | 675 | 689 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 326 | 261 | inferred_complete_timeline |
| `Action_None` | 328 | 374 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 229 | 164 | inferred_complete_timeline |
| `Action_None` | 232 | 237 | 6 | inferred_complete_timeline |
| `Action_None` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 268 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 276 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 91 | 112 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 139 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 86 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 113 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 200 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 98 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–394
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 368 | 303 | inferred_complete_timeline |
| `Action_None` | 371 | 372 | 2 | inferred_complete_timeline |
| `Action_None` | 374 | 376 | 3 | inferred_complete_timeline |
| `Action_None` | 393 | 394 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–444
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 119 | 54 | inferred_complete_timeline |
| `Action_None` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 225 | 84 | inferred_complete_timeline |
| `Action_None` | 231 | 327 | 97 | inferred_complete_timeline |
| `Action_None` | 330 | 444 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 174 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 235 | 170 | inferred_complete_timeline |
| `Action_None` | 237 | 250 | 14 | inferred_complete_timeline |
| `Action_None` | 253 | 297 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–373
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 368 | 303 | inferred_complete_timeline |
| `Action_None` | 371 | 373 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–602 | 537 | 24 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–689 | 628 | 9 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 4–5 | 2 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 32–607 | 503 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 37–602 | 558 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 89–196 | 106 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 89–96 | 7 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 99–476 | 362 | 7 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 105–390 | 264 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 117–129 | 12 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 122–150 | 25 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 138–248 | 109 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 142–145 | 4 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 149–157 | 5 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 160–430 | 261 | 7 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 163–372 | 197 | 7 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 185–189 | 5 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 202–250 | 48 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 231–284 | 41 | 8 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 258–485 | 184 | 11 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 263–689 | 417 | 6 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 271–689 | 417 | 2 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 287–689 | 401 | 2 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 305–369 | 65 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 319–480 | 152 | 6 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 383–689 | 305 | 3 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 390–689 | 300 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 391–431 | 41 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 394–398 | 5 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 408–689 | 280 | 2 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 416–526 | 105 | 4 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 419–420 | 2 | 1 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 420–471 | 52 | 1 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 424–425 | 2 | 1 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 429–689 | 240 | 9 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 429–446 | 15 | 3 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 440–689 | 248 | 2 | Undefined position; Undefined team |
| `55` | `77` | Position_Unknown | Team_Unknown | 447–689 | 225 | 3 | Undefined position; Undefined team |
| `56` | `79` | Position_Unknown | Team_Unknown | 487–488 | 2 | 1 | Undefined position; Undefined team |
| `57` | `85` | Position_Unknown | Team_Unknown | 500–508 | 9 | 1 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 504–592 | 89 | 1 | Undefined position; Undefined team |
| `59` | `91` | Position_Unknown | Team_Unknown | 608–689 | 82 | 1 | Undefined position; Undefined team |
| `60` | `92` | Position_Unknown | Team_Unknown | 623–689 | 67 | 1 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 625–678 | 54 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `14` (4 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `43` (Position_Unknown)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `43` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 46 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 46 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 92 |
| Missing visible bounding boxes during action | 197 |
| Track-related warning | 4 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 36: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 36: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BallCarry' for track '34' has invalid range: start=278, end=250. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '34' has invalid range: start=673, end=250. Clamping end to start.
- ⚠️ Action 'Action_None' range [66-235] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-250] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-368] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-168] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-181] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-469] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-516] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-536] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-670] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-326] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-374] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-98] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-229] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-268] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-276] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-225] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-327] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-444] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-200] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [66-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [84-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [96-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-243] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-459] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-471] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-483] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-517] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-533] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-602] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-368] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-280] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-366] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-661] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [666-689] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-64] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-295] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-368] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-434] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-607] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-246] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-281] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-365] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-602] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-192] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-378] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-404] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-445] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-462] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-476] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-366] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-277] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-368] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-378] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-425] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-214] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-257] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-367] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-232] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-238] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-273] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-274] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-370] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-400] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-472] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-485] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-280] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-487] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-551] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-577] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-620] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-500] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-689] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-583] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-369] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-349] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-387] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-415] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-480] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-489] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-507] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-689] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-431] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-398] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-613] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-427] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-443] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-526] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-471] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-433] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-562] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-572] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-602] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-613] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-689] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-442] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-446] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-689] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-545] for track '55' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-561] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-508] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-592] for track '58' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-678] for track '61' has 3 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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