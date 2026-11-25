# Play-Annotation-Generator Annotation Review — InsideZoneRead_290

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_290`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ReadDefender` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_Keep` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 3 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `16` | 4 | START | 96 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 7 | START | 7 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `12` | `11` | 7 | START | 7 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 7 | START | 7 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 7 | START | 7 | 82 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 7 | START | 7 | 82 |
| ✅ EXACT | `Action_SnapReceive` | RG | `3` | `2` | 20 | END | 4 | 20 |
| ✅ EXACT | `Action_ReadDefender` | RG | `3` | `2` | 25 | START | 25 | 28 |
| ✅ EXACT | `Action_Keep` | RG | `3` | `2` | 29 | START | 29 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `3` | `2` | 51 | START | 51 | 86 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 82 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 197 | 194 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 419 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–245
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 74 | 71 | inferred_complete_timeline |
| `Action_None` | 88 | 245 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–415
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 132 | 129 | inferred_complete_timeline |
| `Action_None` | 136 | 177 | 42 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 358 | 175 | inferred_complete_timeline |
| `Action_None` | 362 | 367 | 6 | inferred_complete_timeline |
| `Action_None` | 371 | 415 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 82 | 76 | inferred_complete_timeline |
| `Action_None` | 83 | 314 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 82 | 76 | inferred_complete_timeline |
| `Action_None` | 83 | 297 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–263
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 82 | 76 | inferred_complete_timeline |
| `Action_None` | 83 | 263 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 20 | 17 | inferred_complete_timeline |
| `Action_None` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 25 | 28 | 4 | inferred_complete_timeline |
| `Action_Keep` | 29 | 50 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 86 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 256 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 82 | 76 | inferred_complete_timeline |
| `Action_None` | 83 | 252 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 73 | 398 | 326 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 70 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 90 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 77 | 74 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 266 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–307
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 307 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 152 | 149 | inferred_complete_timeline |
| `Action_None` | 154 | 383 | 230 | inferred_complete_timeline |
| `Action_None` | 387 | 389 | 3 | inferred_complete_timeline |
| `Action_None` | 391 | 419 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `19` | Position_Unknown | Team_Unknown | 88–419 | 331 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 96–231 | 136 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 97–262 | 166 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 98–350 | 245 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 106–280 | 170 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 115–127 | 4 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 121–172 | 51 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 157–419 | 263 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 175–412 | 237 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 197–419 | 207 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 199–407 | 197 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 207–268 | 44 | 6 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 239–256 | 6 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 251–258 | 7 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 303–331 | 27 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 313–342 | 17 | 4 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 325–328 | 4 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 332–353 | 21 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 332–368 | 37 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 336–347 | 12 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 365–378 | 13 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 366–388 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 4 != Inferred start 96
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '2' has invalid range: start=7, end=3. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=96, end=20. Clamping end to start.
- ⚠️ Action 'Action_None' range [4-307] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-266] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-297] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-383] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-398] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-358] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-367] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-415] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-197] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-419] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-70] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-74] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-369] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-262] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-344] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-156] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-172] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-412] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-373] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-339] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-391] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-235] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-350] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-368] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-347] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-388] for track '37' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_290'; source metadata written as null.

</details>