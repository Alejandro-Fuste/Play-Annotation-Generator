# Play-Annotation-Generator Annotation Review — InsideZoneRead_193

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_193`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 261 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 265 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 265 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `11` | `10` | 262 | START | 262 | 262 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 266 | START | 266 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 266 | START | 274 | 300 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 266 | START | 266 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 266 | START | 266 | 326 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 266 | START | 266 | 326 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 273 | END | 262 | 273 |
| ✅ EXACT | `Action_ReadDefender` | QB | `2` | `1` | 279 | START | 279 | 289 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `1` | 290 | START | 290 | 299 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 300 | START | 300 | 449 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 326 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_SnapReceive` | 262 | 273 | 12 | inferred_complete_timeline |
| `Action_None` | 274 | 278 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 279 | 289 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 290 | 299 | 10 | inferred_complete_timeline |
| `Action_None` | 300 | 336 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 299 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 300 | 449 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 326 | 61 | inferred_complete_timeline |
| `Action_None` | 327 | 449 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 326 | 61 | inferred_complete_timeline |
| `Action_None` | 327 | 408 | 82 | inferred_complete_timeline |
| `Action_None` | 413 | 449 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 210 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 250 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 261 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 262 | 262 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 266 | 273 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 274 | 300 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 326 | 25 | inferred_complete_timeline |
| `Action_None` | 327 | 389 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 326 | 61 | inferred_complete_timeline |
| `Action_None` | 327 | 449 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 266 | 326 | 61 | inferred_complete_timeline |
| `Action_None` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_None` | 262 | 449 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_None` | 262 | 449 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_None` | 262 | 281 | 20 | inferred_complete_timeline |
| `Action_None` | 285 | 311 | 27 | inferred_complete_timeline |
| `Action_None` | 315 | 345 | 31 | inferred_complete_timeline |
| `Action_None` | 347 | 393 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_None` | 262 | 406 | 145 | inferred_complete_timeline |
| `Action_None` | 410 | 449 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–432
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_None` | 262 | 352 | 91 | inferred_complete_timeline |
| `Action_None` | 358 | 432 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_None` | 262 | 421 | 160 | inferred_complete_timeline |
| `Action_None` | 423 | 425 | 3 | inferred_complete_timeline |
| `Action_None` | 428 | 430 | 3 | inferred_complete_timeline |
| `Action_None` | 435 | 449 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 24–165 | 98 | 6 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 205–266 | 56 | 5 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 290–449 | 160 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 329–343 | 12 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 339–340 | 2 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 369–378 | 10 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 378–449 | 72 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 381–449 | 69 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 411–434 | 19 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 431–446 | 6 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 432–449 | 13 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 433–447 | 13 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [262–273], lower_priority='Action_ZoneBlock' annotated_start=266, effective_Action_ZoneBlock_start=274.
- ⚠️ Action 'Action_None' range [300-336] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [300-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-408] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [266-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-352] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-432] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-421] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-406] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-449] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '10' starts at frame 262, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [262-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [274-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-311] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-345] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-393] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-32] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-165] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-246] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-261] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-336] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-423] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-434] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-446] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-442] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-447] for track '25' has 1 frames without a visible bounding box.
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

</details>