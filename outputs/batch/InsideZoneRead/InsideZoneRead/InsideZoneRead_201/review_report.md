# Play-Annotation-Generator Annotation Review — InsideZoneRead_201

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_201`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 265 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `12` | `11` | 263 | START | 263 | 277 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `10` | 266 | START | 266 | 276 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 266 | START | 266 | 295 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `3` | 266 | START | 266 | 278 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 266 | START | 266 | 278 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 277 | END | 263 | 277 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 280 | START | 280 | 292 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 293 | START | 293 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `3` | `2` | 296 | START | 296 | 303 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `10` | `9` | 306 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 335 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_SnapReceive` | 263 | 277 | 15 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 280 | 292 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 293 | 300 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 276 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 291 | 324 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 295 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 296 | 303 | 8 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 305 | 316 | 12 | inferred_complete_timeline |
| `Action_None` | 337 | 371 | 35 | inferred_complete_timeline |
| `Action_None` | 377 | 385 | 9 | inferred_complete_timeline |
| `Action_None` | 388 | 419 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 278 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 335 | 50 | inferred_complete_timeline |
| `Action_None` | 336 | 347 | 12 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 368 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 278 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 335 | 54 | inferred_complete_timeline |
| `Action_None` | 336 | 375 | 40 | inferred_complete_timeline |
| `Action_None` | 390 | 419 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_None` | 263 | 320 | 58 | inferred_complete_timeline |
| `Action_None` | 333 | 351 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_None` | 263 | 319 | 57 | inferred_complete_timeline |
| `Action_None` | 322 | 332 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–412
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 168 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 262 | 86 | inferred_complete_timeline |
| `Action_None` | 263 | 294 | 32 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 324 | 380 | 57 | inferred_complete_timeline |
| `Action_None` | 384 | 398 | 15 | inferred_complete_timeline |
| `Action_None` | 401 | 412 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_None` | 263 | 381 | 119 | inferred_complete_timeline |
| `Action_None` | 383 | 419 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 262 | 33 | inferred_complete_timeline |
| `Action_None` | 263 | 362 | 100 | inferred_complete_timeline |
| `Action_None` | 364 | 372 | 9 | inferred_complete_timeline |
| `Action_None` | 381 | 383 | 3 | inferred_complete_timeline |
| `Action_None` | 385 | 419 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 13–419 | 360 | 9 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 168–295 | 128 | 2 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 286–419 | 101 | 6 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 298–419 | 81 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 309–342 | 34 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 319–334 | 16 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 329–407 | 65 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 350–366 | 17 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 352–414 | 63 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 371–400 | 30 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 373–419 | 47 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 380–406 | 27 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 383–419 | 37 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 390–419 | 26 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 393–419 | 23 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 395–419 | 25 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 403–419 | 16 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 405–419 | 15 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 419–419 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=306, end=162. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-362] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [296-303] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [305-316] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-371] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-375] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-320] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-351] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [293-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-294] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-398] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-412] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-368] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-381] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [291-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-346] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-375] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-337] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-353] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-370] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-342] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-334] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-360] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-407] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-366] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-414] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-400] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-406] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-419] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-407] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-403] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-416] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>