# Play-Annotation-Generator Annotation Review — InsideZoneRead_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_96`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 302 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `11` | `10` | 260 | START | 260 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `0` | 263 | START | 263 | 292 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `10` | 263 | START | 277 | 347 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `2` | `1` | 263 | START | 263 | 312 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `2` | 263 | START | 263 | 347 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `5` | 263 | START | 263 | 308 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 276 | END | 260 | 276 |
| ✅ EXACT | `Action_ReadDefender` | QB | `5` | `4` | 281 | START | 281 | 293 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `1` | `0` | 293 | START | 293 | 327 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `5` | `4` | 294 | START | 294 | 295 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `7` | 303 | START | 303 | 307 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 347 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–386
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_SnapReceive` | 260 | 276 | 17 | inferred_complete_timeline |
| `Action_None` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 281 | 293 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 294 | 295 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 303 | 386 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–395
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_BallCarry` | 303 | 307 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 313 | 358 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 370 | 381 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 390 | 395 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_ZoneBlock` | 263 | 312 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 348 | 372 | 25 | inferred_complete_timeline |
| `Action_None` | 374 | 419 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_ZoneBlock` | 263 | 308 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 311 | 331 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 340 | 345 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–417
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 62 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 259 | 196 | inferred_complete_timeline |
| `Action_BallSnap` | 260 | 266 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 268 | 276 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 277 | 347 | 71 | inferred_complete_timeline |
| `Action_None` | 348 | 417 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–385
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_ZoneBlock` | 263 | 292 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 293 | 327 | 35 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 332 | 347 | 16 | inferred_complete_timeline |
| `Action_None` | 348 | 385 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 262 | 263 | inferred_complete_timeline |
| `Action_ZoneBlock` | 263 | 347 | 85 | inferred_complete_timeline |
| `Action_None` | 348 | 419 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_None` | 260 | 419 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_None` | 260 | 306 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–405
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 259 | 204 | inferred_complete_timeline |
| `Action_None` | 260 | 354 | 95 | inferred_complete_timeline |
| `Action_None` | 356 | 390 | 35 | inferred_complete_timeline |
| `Action_None` | 399 | 400 | 2 | inferred_complete_timeline |
| `Action_None` | 404 | 405 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_None` | 260 | 315 | 56 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_None` | 260 | 393 | 134 | inferred_complete_timeline |
| `Action_None` | 405 | 419 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–413 | 414 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 11–67 | 57 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 68–91 | 24 | 1 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 86–398 | 307 | 5 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 287–419 | 133 | 1 | Undefined position; Undefined team |
| `17` | `26` | Position_Unknown | Team_Unknown | 312–419 | 105 | 3 | Undefined position; Undefined team |
| `18` | `27` | Position_Unknown | Team_Unknown | 313–353 | 41 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 320–378 | 59 | 1 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 343–419 | 41 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 351–419 | 67 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 355–419 | 60 | 2 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 362–419 | 37 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 386–419 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 263 != Inferred start 277
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 194: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [260–276], lower_priority='Action_ZoneBlock' annotated_start=263, effective_Action_ZoneBlock_start=277.
- ⚠️ Action 'Action_BlockSecondLevel' range [293-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-385] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [263-312] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-372] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-393] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [294-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-386] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [263-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [311-331] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [340-345] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-307] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [313-358] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [370-381] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [390-395] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-354] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-390] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-62] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [260-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [277-347] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-417] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-315] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-413] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-67] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-334] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-358] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-398] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-377] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-353] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-378] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-354] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-407] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-394] for track '23' has 1 frames without a visible bounding box.
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

</details>