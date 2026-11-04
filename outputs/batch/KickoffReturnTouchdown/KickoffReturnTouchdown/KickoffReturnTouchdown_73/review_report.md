# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_73`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 176
- **Validation Warnings:** 210
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 163
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | Team_Unknown | `32` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `32` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `32` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `1` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `12` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `7` | `7` | 40 | START | 40 | 92 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 93 | START | 93 | 97 |
| ⚠️ START CHANGED | `Action_CatchKick` | Position_Unknown | `32` | `25` | 205 | START | 215 | 215 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `32` | `25` | 223 | START | 223 | 557 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `32` | `25` | 558 | START | 558 | 567 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–434
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_KickApproach` | 40 | 92 | 53 | inferred_complete_timeline |
| `Action_KickBall` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 161 | 64 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 176 | 186 | 11 | inferred_complete_timeline |
| `Action_None` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_None` | 200 | 399 | 200 | inferred_complete_timeline |
| `Action_None` | 401 | 423 | 23 | inferred_complete_timeline |
| `Action_None` | 426 | 427 | 2 | inferred_complete_timeline |
| `Action_None` | 433 | 434 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–440
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 264 | 225 | inferred_complete_timeline |
| `Action_None` | 270 | 440 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–406
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 269 | 230 | inferred_complete_timeline |
| `Action_None` | 271 | 274 | 4 | inferred_complete_timeline |
| `Action_None` | 277 | 282 | 6 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 307 | 312 | 6 | inferred_complete_timeline |
| `Action_None` | 314 | 321 | 8 | inferred_complete_timeline |
| `Action_None` | 323 | 406 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–413
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 282 | 243 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_None` | 307 | 312 | 6 | inferred_complete_timeline |
| `Action_None` | 314 | 413 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–378
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 102 | 63 | inferred_complete_timeline |
| `Action_None` | 105 | 140 | 36 | inferred_complete_timeline |
| `Action_None` | 143 | 236 | 94 | inferred_complete_timeline |
| `Action_None` | 238 | 266 | 29 | inferred_complete_timeline |
| `Action_None` | 269 | 378 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 118 | 79 | inferred_complete_timeline |
| `Action_None` | 125 | 302 | 178 | inferred_complete_timeline |
| `Action_None` | 305 | 417 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 62 | 20 | inferred_complete_timeline |
| `Action_None` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 71 | 93 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 569 | 530 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 222 | 183 | inferred_complete_timeline |
| `Action_None` | 227 | 261 | 35 | inferred_complete_timeline |
| `Action_None` | 266 | 412 | 147 | inferred_complete_timeline |
| `Action_None` | 415 | 419 | 5 | inferred_complete_timeline |
| `Action_None` | 422 | 424 | 3 | inferred_complete_timeline |
| `Action_None` | 428 | 430 | 3 | inferred_complete_timeline |
| `Action_None` | 433 | 434 | 2 | inferred_complete_timeline |
| `Action_None` | 436 | 569 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–362
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 221 | 182 | inferred_complete_timeline |
| `Action_None` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 253 | 6 | inferred_complete_timeline |
| `Action_None` | 260 | 272 | 13 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_None` | 305 | 323 | 19 | inferred_complete_timeline |
| `Action_None` | 325 | 362 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–416
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 252 | 213 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 322 | 38 | inferred_complete_timeline |
| `Action_None` | 324 | 348 | 25 | inferred_complete_timeline |
| `Action_None` | 350 | 416 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–411
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 233 | 194 | inferred_complete_timeline |
| `Action_None` | 235 | 247 | 13 | inferred_complete_timeline |
| `Action_None` | 258 | 286 | 29 | inferred_complete_timeline |
| `Action_None` | 288 | 411 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–410
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 266 | 227 | inferred_complete_timeline |
| `Action_None` | 273 | 281 | 9 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_None` | 307 | 310 | 4 | inferred_complete_timeline |
| `Action_None` | 315 | 354 | 40 | inferred_complete_timeline |
| `Action_None` | 356 | 391 | 36 | inferred_complete_timeline |
| `Action_None` | 393 | 410 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 2–569 | 508 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 26–569 | 521 | 11 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 39–45 | 7 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 49–242 | 183 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 88–89 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 102–217 | 105 | 6 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 108–255 | 130 | 5 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 110–200 | 87 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 132–442 | 260 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 143–151 | 9 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 145–369 | 211 | 8 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 157–371 | 168 | 8 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 215–569 | 355 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 223–226 | 4 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 261–262 | 2 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 281–569 | 282 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 289–359 | 67 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 292–430 | 134 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 314–345 | 32 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 364–383 | 20 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 393–396 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 459–466 | 6 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 474–496 | 10 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 554–555 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 557–569 | 13 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 557–558 | 2 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 563–569 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchKick` for actor_track_id `32` (Position_Unknown): Annotated start 205 != Inferred start 215
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `32` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 154 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_CatchKick' for track '25' has invalid range: start=215, end=211. Clamping end to start.
- ⚠️ Action 'Action_None' range [40-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-321] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-406] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-440] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-261] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-412] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-424] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-569] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-272] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-323] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-252] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-322] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-348] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-416] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-233] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-286] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-411] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-282] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-413] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [40-92] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-399] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-423] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-434] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-417] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-266] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-354] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-391] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-410] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 40, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [40-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-62] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-69] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-93] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-236] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-266] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-378] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-283] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-105] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-249] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-313] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-569] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-58] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-186] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-232] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-189] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-217] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-255] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-184] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-282] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-414] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-303] for track '23' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-369] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-212] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-345] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-371] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-559] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-303] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-430] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-345] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-383] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-480] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-496] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-555] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-569] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-569] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>