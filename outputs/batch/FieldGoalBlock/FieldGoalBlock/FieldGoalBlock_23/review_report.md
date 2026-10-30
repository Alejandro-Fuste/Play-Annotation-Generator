# Play-Annotation-Generator Annotation Review — FieldGoalBlock_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_23`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 419
- **Player Tracks:** 59
- **Ball Tracks:** 0
- **Action Segments:** 254
- **Validation Warnings:** 326
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 2
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 243
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Left_Edge_Rusher | defense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | FG_Block_Support | defense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | Team_Unknown | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `2` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_PlaceBall` | Left_Edge_Rusher | `6` | `6` | 23 | START | 23 | 32 |
| ✅ EXACT | `Action_KickBall` | FG_Block_Support | `0` | `0` | 44 | START | 44 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | `15` | `15` | 50 | START | 50 | 54 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 62 | 19 | inferred_complete_timeline |
| `Action_None` | 65 | 110 | 46 | inferred_complete_timeline |
| `Action_None` | 115 | 257 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 30 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 50 | 7 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_None` | 109 | 154 | 46 | inferred_complete_timeline |
| `Action_None` | 156 | 265 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 36 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 248 | 199 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 48 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_None` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 188 | 18 | inferred_complete_timeline |
| `Action_None` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 206 | 227 | 22 | inferred_complete_timeline |
| `Action_None` | 234 | 247 | 14 | inferred_complete_timeline |
| `Action_None` | 251 | 284 | 34 | inferred_complete_timeline |
| `Action_None` | 288 | 298 | 11 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 306 | 313 | 8 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 335 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_KickBall` | 44 | 49 | 6 | inferred_complete_timeline |
| `Action_None` | 50 | 243 | 194 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 65 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 352 | 284 | inferred_complete_timeline |
| `Action_None` | 355 | 377 | 23 | inferred_complete_timeline |
| `Action_None` | 380 | 386 | 7 | inferred_complete_timeline |
| `Action_None` | 392 | 394 | 3 | inferred_complete_timeline |
| `Action_None` | 402 | 409 | 8 | inferred_complete_timeline |
| `Action_None` | 411 | 414 | 4 | inferred_complete_timeline |
| `Action_None` | 416 | 419 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 180 | 137 | inferred_complete_timeline |
| `Action_None` | 182 | 185 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 220 | 32 | inferred_complete_timeline |
| `Action_None` | 222 | 296 | 75 | inferred_complete_timeline |
| `Action_None` | 298 | 316 | 19 | inferred_complete_timeline |
| `Action_None` | 318 | 335 | 18 | inferred_complete_timeline |
| `Action_None` | 340 | 347 | 8 | inferred_complete_timeline |
| `Action_None` | 361 | 379 | 19 | inferred_complete_timeline |
| `Action_None` | 383 | 392 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 44 | 60 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 77 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 19–21
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 29 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `23`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 39–247
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 40 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 53 | 58 | 6 | inferred_complete_timeline |
| `Action_None` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 98 | 25 | inferred_complete_timeline |
| `Action_None` | 117 | 247 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_None` | 44 | 342 | 299 | inferred_complete_timeline |
| `Action_None` | 344 | 354 | 11 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 419 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PlaceBall` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_None` | 33 | 71 | 39 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_None` | 52 | 65 | 14 | inferred_complete_timeline |
| `Action_None` | 73 | 102 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–259 | 260 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–255 | 232 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–239 | 226 | 9 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–419 | 373 | 11 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–264 | 174 | 7 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 43–57 | 5 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 55–227 | 158 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 61–75 | 14 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 78–151 | 54 | 6 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 83–265 | 169 | 7 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 87–275 | 185 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 92–126 | 6 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 92–419 | 308 | 9 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 93–372 | 247 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 112–268 | 139 | 7 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 115–265 | 150 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 119–123 | 5 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 130–252 | 104 | 6 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 137–394 | 258 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 155–339 | 85 | 19 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 190–269 | 72 | 5 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 217–218 | 2 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 266–389 | 99 | 9 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 266–387 | 110 | 8 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 266–272 | 7 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `45` | `65` | Position_Unknown | Team_Unknown | 270–419 | 150 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 270–281 | 12 | 1 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 270–390 | 105 | 5 | Undefined position; Undefined team |
| `48` | `69` | Position_Unknown | Team_Unknown | 270–348 | 50 | 5 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 273–382 | 110 | 1 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 274–419 | 136 | 6 | Undefined position; Undefined team |
| `51` | `74` | Position_Unknown | Team_Unknown | 351–357 | 7 | 1 | Undefined position; Undefined team |
| `52` | `76` | Position_Unknown | Team_Unknown | 391–419 | 29 | 1 | Undefined position; Undefined team |
| `53` | `78` | Position_Unknown | Team_Unknown | 397–419 | 22 | 2 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 401–419 | 19 | 1 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 403–419 | 17 | 1 | Undefined position; Undefined team |
| `56` | `85` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `57` | `87` | Position_Unknown | Team_Unknown | 410–419 | 9 | 2 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 411–419 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `15` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `23`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 233 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 48: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 48: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 48: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 48: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [50-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-220] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-296] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-316] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-347] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-379] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-392] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-62] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-188] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-227] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-247] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-284] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-313] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-335] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-352] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-377] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-386] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-394] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-409] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-414] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-259] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-71] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-342] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-36] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-248] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-65] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-102] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-65] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-84] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-60] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-66] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-102] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-184] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-211] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-231] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [50-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [56-60] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [62-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [73-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-265] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-419] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-30] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-50] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-154] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-265] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-102] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-215] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 44, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [44-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-60] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-89] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-131] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-126] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-269] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-126] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-257] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-317] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-350] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-412] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-262] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-355] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-149] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-225] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-264] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-194] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-265] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-140] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-162] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-194] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-234] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-394] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-223] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-236] for track '38' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-243] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-285] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-299] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-312] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-351] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-379] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-389] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-290] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-305] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-329] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-362] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-370] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-387] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-272] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-419] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-281] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-298] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-309] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-352] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-374] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-390] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-287] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-326] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-348] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-382] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-284] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-338] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-346] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-357] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-381] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-419] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-410] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-419] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-414] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>