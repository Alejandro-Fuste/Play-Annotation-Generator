# Play-Annotation-Generator Annotation Review — InsideZoneRead_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_137`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 42 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 288 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `15` | `14` | 274 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 276 | START | 276 | 374 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `15` | `14` | 276 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 276 | START | 276 | 374 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `8` | `7` | 287 | END | 274 | 287 |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | `8` | `7` | 290 | START | 290 | 304 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `8` | `7` | 305 | START | 305 | 319 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `6` | `5` | 320 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 374 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–316
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 316 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 275 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 374 | 99 | inferred_complete_timeline |
| `Action_None` | 375 | 382 | 8 | inferred_complete_timeline |
| `Action_None` | 384 | 425 | 42 | inferred_complete_timeline |
| `Action_None` | 427 | 449 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 42–73
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–430
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 275 | 163 | inferred_complete_timeline |
| `Action_ZoneBlock` | 276 | 374 | 99 | inferred_complete_timeline |
| `Action_None` | 375 | 430 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 449 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 332 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 273 | 162 | inferred_complete_timeline |
| `Action_None` | 274 | 281 | 8 | inferred_complete_timeline |
| `Action_None` | 333 | 335 | 3 | inferred_complete_timeline |
| `Action_None` | 375 | 408 | 34 | inferred_complete_timeline |
| `Action_None` | 412 | 449 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–350
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 273 | 268 | inferred_complete_timeline |
| `Action_None` | 274 | 350 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–328
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 273 | 268 | inferred_complete_timeline |
| `Action_None` | 274 | 328 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_None` | 274 | 420 | 147 | inferred_complete_timeline |
| `Action_None` | 424 | 449 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–388 | 389 | 2 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–158 | 154 | 2 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–180 | 181 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–376 | 377 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 81–449 | 359 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 111–413 | 295 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 116–143 | 22 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 144–449 | 306 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 164–285 | 122 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 185–449 | 240 | 11 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 293–449 | 78 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 336–342 | 7 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 343–449 | 100 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 353–407 | 55 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 358–402 | 44 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 413–449 | 33 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 417–419 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 432–449 | 17 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (C)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 274: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 274: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 274: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 99 frames exceeds threshold 90 frames [start=276, end=374].
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=320, end=316. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LG) duration 99 frames exceeds threshold 90 frames [start=276, end=374].
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=274, end=73. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=276, end=73. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-388] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-158] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-420] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-430] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-316] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [274-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-376] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-332] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-408] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-382] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-425] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-449] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-328] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-397] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-312] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-344] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-413] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-285] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-249] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-349] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-364] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-350] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-364] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-371] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-407] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-402] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-443] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-449] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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

</details>