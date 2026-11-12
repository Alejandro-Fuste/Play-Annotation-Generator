# Play-Annotation-Generator Annotation Review — SplitZone_281

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_281`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_SplitBlock` | WR | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `0` | `0` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 267 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 222 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `2` | 213 | START | 213 | 227 |
| ✅ EXACT | `Action_SplitBlock` | WR | `10` | `10` | 221 | START | 221 | 285 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RG | `0` | `0` | 223 | START | 228 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `2` | `2` | 223 | START | 228 | 242 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 223 | START | 223 | 276 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 223 | START | 223 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 223 | START | 223 | 247 |
| ✅ EXACT | `Action_SnapReceive` | RG | `0` | `0` | 227 | END | 213 | 227 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `5` | 240 | START | 240 | 254 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `9` | `9` | 248 | START | 248 | 263 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 255 | START | 255 | 264 |
| ✅ EXACT | `Action_PressEdge` | RB | `1` | `1` | 268 | START | 268 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `1` | 269 | START | 269 | 371 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–411
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 240 | 254 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 255 | 264 | 10 | inferred_complete_timeline |
| `Action_None` | 265 | 411 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 267 | 268 | inferred_complete_timeline |
| `Action_PressEdge` | 268 | 268 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 269 | 371 | 103 | inferred_complete_timeline |
| `Action_BallCarry` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 376 | 396 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 400 | 401 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 406 | 419 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_SplitBlock` | 221 | 285 | 65 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 328 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 276 | 54 | inferred_complete_timeline |
| `Action_None` | 277 | 419 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 276 | 54 | inferred_complete_timeline |
| `Action_None` | 277 | 328 | 52 | inferred_complete_timeline |
| `Action_None` | 332 | 419 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_BallSnap` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 242 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 244 | 276 | 33 | inferred_complete_timeline |
| `Action_None` | 277 | 419 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_SnapReceive` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 276 | 49 | inferred_complete_timeline |
| `Action_None` | 324 | 333 | 10 | inferred_complete_timeline |
| `Action_None` | 335 | 419 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 247 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 248 | 263 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 264 | 276 | 13 | inferred_complete_timeline |
| `Action_None` | 277 | 419 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 238 | 26 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 265 | 419 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 212 | 165 | inferred_complete_timeline |
| `Action_None` | 213 | 219 | 7 | inferred_complete_timeline |
| `Action_None` | 224 | 419 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 247 | 35 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 336 | 124 | inferred_complete_timeline |
| `Action_None` | 349 | 419 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 253 | 41 | inferred_complete_timeline |
| `Action_None` | 274 | 419 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 263 | 51 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_None` | 213 | 419 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 55–68 | 6 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 76–77 | 2 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 109–152 | 8 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 246–419 | 174 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 261–419 | 149 | 3 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 266–406 | 141 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 270–419 | 146 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 286–419 | 134 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 329–419 | 91 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 363–419 | 57 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 376–419 | 44 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 380–419 | 40 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 397–419 | 23 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 413–419 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `0` (RG): Annotated start 223 != Inferred start 228
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [213–227], lower_priority='Action_ZoneBlock' annotated_start=223, effective_Action_ZoneBlock_start=228.
- ⚠️ Action 'Action_ZoneBlock' range [228-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-333] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [269-371] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [373-374] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [376-396] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [400-401] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [406-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [228-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-411] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-263] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-328] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-238] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-419] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-406] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-305] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-419] for track '23' has 1 frames without a visible bounding box.
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

</details>