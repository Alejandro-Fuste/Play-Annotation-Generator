# Play-Annotation-Generator Annotation Review — InsideZoneRead_230

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_230`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB | defense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | RT | `5` | `4` | 82 | START | 82 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `12` | 85 | START | 85 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `2` | 85 | START | 85 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 85 | START | 85 | 124 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `7` | `6` | 85 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 85 | START | 85 | 139 |
| ✅ EXACT | `Action_SnapReceive` | RB | `10` | `9` | 94 | END | 82 | 94 |
| ✅ EXACT | `Action_ReadDefender` | RB | `10` | `9` | 97 | START | 97 | 108 |
| ✅ EXACT | `Action_Handoff` | RB | `10` | `9` | 109 | START | 109 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB | `6` | `5` | 118 | START | 118 | 172 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 131 | 50 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 94 | 13 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 109 | 117 | 9 | inferred_complete_timeline |
| `Action_None` | 118 | 147 | 30 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 149 | 65 | inferred_complete_timeline |
| `Action_None` | 150 | 163 | 14 | inferred_complete_timeline |
| `Action_None` | 167 | 269 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 84 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 149 | 65 | inferred_complete_timeline |
| `Action_None` | 150 | 169 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 84 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 139 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 150 | 204 | 55 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 54 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 124 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 160 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 81 | 24 | inferred_complete_timeline |
| `Action_None` | 82 | 132 | 51 | inferred_complete_timeline |
| `Action_None` | 138 | 206 | 69 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 182 | 101 | inferred_complete_timeline |
| `Action_None` | 190 | 192 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 211 | 15 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 238 | 15 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 192 | 111 | inferred_complete_timeline |
| `Action_None` | 197 | 269 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_BallCarry` | 118 | 172 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–6 | 7 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 49–269 | 212 | 3 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 65–269 | 135 | 5 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 132–269 | 110 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 146–269 | 120 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 148–167 | 15 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 152–269 | 118 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 168–269 | 100 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 176–226 | 51 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 193–269 | 74 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 201–252 | 51 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 217–269 | 53 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 217–269 | 51 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 220–269 | 38 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 232–269 | 20 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 244–258 | 15 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 247–269 | 23 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 261–269 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `7` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '6' has invalid range: start=85, end=4. Clamping end to start.
- ⚠️ Action 'Action_None' range [82-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-211] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-238] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-206] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-124] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [118-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [190-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-192] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-71] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-242] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-242] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_230'; source metadata written as null.

</details>