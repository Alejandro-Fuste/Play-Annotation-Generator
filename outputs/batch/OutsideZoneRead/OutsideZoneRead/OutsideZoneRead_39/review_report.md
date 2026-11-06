# Play-Annotation-Generator Annotation Review — OutsideZoneRead_39

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_39`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 70
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 169 | START | 169 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 169 | START | 169 | 192 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 169 | START | 169 | 203 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `5` | `5` | 169 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 169 | START | 169 | 203 |
| ❌ MISSING SEGMENT | `Action_PressEdge` | Position_Unknown | `16` | `15` | 182 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadEdgeDefender` | LG | `10` | `10` | 183 | START | 183 | 185 |
| ✅ EXACT | `Action_Handoff` | LG | `10` | `10` | 198 | START | 198 | 203 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 203 | 35 | inferred_complete_timeline |
| `Action_None` | 204 | 235 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 168 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 182 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 197 | 197 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_None` | 204 | 227 | 24 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 168 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 192 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 203 | 1 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 168 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 203 | 35 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–219
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 20 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 99 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 135 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 219 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 223 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 252 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–226 | 226 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 60–114 | 38 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 85–139 | 52 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 104–269 | 162 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 119–249 | 128 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 137–249 | 91 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 139–269 | 128 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 144–161 | 18 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 151–204 | 52 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 153–189 | 23 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 164–221 | 56 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 165–268 | 103 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 179–248 | 70 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 221–227 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | 108 | 108 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `5` (RG)
- ❌ Missing segment for action `Action_PressEdge` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ReadEdgeDefender` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 80: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '5' has invalid range: start=169, end=139. Clamping end to start.
- ⚠️ Segment 'Action_PressEdge' for track '15' has invalid range: start=182, end=139. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-168] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [183-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadEdgeDefender' range [187-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-227] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-192] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-31] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-135] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-152] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-148] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-204] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-165] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-189] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-257] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-248] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-227] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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