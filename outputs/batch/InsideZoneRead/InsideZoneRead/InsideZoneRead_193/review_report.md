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
- **Action Segments:** 80
- **Validation Warnings:** 81
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
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
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `23` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | C | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT1 | defense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 154 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `23` | `18` | 152 | START | 339 | 339 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 155 | START | 155 | 224 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `11` | `10` | 155 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 155 | START | 155 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `4` | 155 | START | 155 | 224 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 155 | START | 155 | 224 |
| ✅ EXACT | `Action_SnapReceive` | C | `11` | `10` | 164 | END | 161 | 164 |
| ✅ EXACT | `Action_ReadDefender` | C | `11` | `10` | 171 | START | 171 | 187 |
| ✅ EXACT | `Action_Handoff` | C | `11` | `10` | 188 | START | 188 | 192 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT1 | `14` | `13` | 193 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 336 | 185 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 295 | 144 | inferred_complete_timeline |
| `Action_None` | 299 | 449 | 151 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 224 | 70 | inferred_complete_timeline |
| `Action_None` | 225 | 449 | 225 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 224 | 70 | inferred_complete_timeline |
| `Action_None` | 225 | 408 | 184 | inferred_complete_timeline |
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
| `Action_SnapReceive` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 170 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 188 | 192 | 5 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 241 | 250 | 10 | inferred_complete_timeline |
| `Action_None` | 252 | 262 | 11 | inferred_complete_timeline |
| `Action_None` | 266 | 300 | 35 | inferred_complete_timeline |
| `Action_None` | 302 | 389 | 88 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 224 | 70 | inferred_complete_timeline |
| `Action_None` | 225 | 449 | 225 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 224 | 70 | inferred_complete_timeline |
| `Action_None` | 225 | 359 | 135 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 449 | 298 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 449 | 298 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 281 | 130 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 406 | 255 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 352 | 201 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 421 | 270 | inferred_complete_timeline |
| `Action_None` | 423 | 425 | 3 | inferred_complete_timeline |
| `Action_None` | 428 | 430 | 3 | inferred_complete_timeline |
| `Action_None` | 435 | 449 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 24–165 | 98 | 7 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 205–266 | 56 | 4 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 290–449 | 160 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 329–343 | 12 | 3 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 339–340 | 2 | 2 | Undefined position; Undefined team |
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

- ⚠️ `Action_BallSnap` for actor_track_id `23` (Position_Unknown): Annotated start 152 != Inferred start 339
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `14` (DT1)

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
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=155, end=151. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '13' has invalid range: start=193, end=6. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=339, end=164. Clamping end to start.
- ⚠️ Action 'Action_None' range [152-336] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-408] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-359] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-352] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-432] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-421] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-430] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-406] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-449] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [161-164] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-300] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-281] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-311] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-345] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-393] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-32] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-151] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-165] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-246] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-266] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-336] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-339] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 340, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [340-340] for track '18' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_193'; source metadata written as null.

</details>