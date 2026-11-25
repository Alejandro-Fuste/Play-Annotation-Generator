# Play-Annotation-Generator Annotation Review — InsideZoneRead_201

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_201`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
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
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `15` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `17` | `15` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `17` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 3 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 3 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 3 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 3 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 3 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 3 | START | 0 | 28 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `14` | 26 | START | 298 | 298 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 29 | START | 29 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 29 | START | 29 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 29 | START | 29 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `7` | 29 | START | 29 | 128 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `17` | `15` | 39 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `17` | `15` | 43 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `17` | `15` | 56 | START | 309 | 342 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 300 | 275 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 162 | 137 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 129 | 276 | 148 | inferred_complete_timeline |
| `Action_None` | 291 | 324 | 34 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 129 | 303 | 175 | inferred_complete_timeline |
| `Action_None` | 305 | 316 | 12 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 129 | 278 | 150 | inferred_complete_timeline |
| `Action_None` | 286 | 347 | 62 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 129 | 278 | 150 | inferred_complete_timeline |
| `Action_None` | 282 | 375 | 94 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 320 | 295 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 319 | 294 | inferred_complete_timeline |
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
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 168 | 116 | inferred_complete_timeline |
| `Action_None` | 177 | 294 | 118 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 381 | 356 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 222 | 197 | inferred_complete_timeline |
| `Action_None` | 230 | 362 | 133 | inferred_complete_timeline |
| `Action_None` | 364 | 372 | 9 | inferred_complete_timeline |
| `Action_None` | 381 | 383 | 3 | inferred_complete_timeline |
| `Action_None` | 385 | 419 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 13–419 | 360 | 8 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 168–295 | 128 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 286–419 | 101 | 6 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 298–419 | 81 | 4 | Undefined position; Undefined team |
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

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 26 != Inferred start 298
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `17` (Position_Unknown)
- ⚠️ `Action_BallCarry` for actor_track_id `17` (Position_Unknown): Annotated start 56 != Inferred start 309

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
| Track-related warning | 7 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=298, end=39. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '15' has invalid range: start=309, end=39. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '15' has invalid range: start=309, end=55. Clamping end to start.
- ⚠️ Action 'Action_None' range [26-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-362] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-303] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-316] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-371] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-375] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-320] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-351] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-300] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-294] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-398] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-412] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-347] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-368] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-381] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-276] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-346] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-361] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-375] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-419] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-337] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-353] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-370] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-342] for track '15' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_201'; source metadata written as null.

</details>