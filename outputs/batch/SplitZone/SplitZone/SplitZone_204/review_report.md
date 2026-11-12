# Play-Annotation-Generator Annotation Review — SplitZone_204

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_204`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 126
- **Validation Warnings:** 154
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 110
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 7 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 68 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 138 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `16` | `15` | 131 | START | 136 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `11` | `11` | 134 | START | 134 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `14` | 134 | START | 134 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 134 | START | 134 | 141 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `5` | 134 | START | 134 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `6` | `6` | 139 | START | 139 | 144 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 145 | END | 131 | 145 |
| ✅ EXACT | `Action_Handoff` | QB | `1` | `1` | 152 | START | 152 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `10` | `10` | 163 | START | 182 | 183 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 213 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_SnapReceive` | 131 | 145 | 15 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_SplitBlock` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_SplitBlock` | 146 | 156 | 11 | inferred_complete_timeline |
| `Action_SplitBlock` | 172 | 213 | 42 | inferred_complete_timeline |
| `Action_None` | 214 | 228 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 68–249
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 133 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 144 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 159 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 165 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 213 | 39 | inferred_complete_timeline |
| `Action_None` | 214 | 223 | 10 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |
| `Action_None` | 246 | 249 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 141 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 181 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 196 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 158 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–298
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 133 | 127 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 149 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 192 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 213 | 20 | inferred_complete_timeline |
| `Action_None` | 214 | 295 | 82 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 359 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 139 | 187 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 167 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 177 | 47 | inferred_complete_timeline |
| `Action_None` | 179 | 206 | 28 | inferred_complete_timeline |
| `Action_None` | 209 | 214 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 243 | 359 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 130 | 48 | inferred_complete_timeline |
| `Action_None` | 131 | 183 | 53 | inferred_complete_timeline |
| `Action_None` | 185 | 218 | 34 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 243 | 259 | 17 | inferred_complete_timeline |
| `Action_None` | 304 | 308 | 5 | inferred_complete_timeline |
| `Action_None` | 313 | 359 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–305
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 177 | 47 | inferred_complete_timeline |
| `Action_None` | 189 | 217 | 29 | inferred_complete_timeline |
| `Action_None` | 260 | 265 | 6 | inferred_complete_timeline |
| `Action_None` | 267 | 305 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–359 | 292 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 11–32 | 22 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 27–235 | 198 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 136–359 | 112 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 151–189 | 33 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 177–277 | 95 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 183–229 | 46 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 200–359 | 160 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 200–359 | 157 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 205–310 | 95 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 214–273 | 42 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 222–359 | 112 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 229–359 | 119 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 248–359 | 107 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 251–305 | 50 | 3 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 261–359 | 98 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 272–359 | 87 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 276–312 | 28 | 5 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 278–304 | 27 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 279–296 | 18 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 299–317 | 19 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 305–359 | 55 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 318–359 | 42 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 322–323 | 2 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 330–359 | 30 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 331–359 | 29 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 356–359 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `16` (Position_Unknown): Annotated start 131 != Inferred start 136
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (6 segments found)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 410: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [131-359] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-259] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-305] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-141] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-181] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [187-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [139-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [146-156] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [172-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-228] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-214] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-197] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-149] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-192] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-213] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-227] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-144] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [136-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-221] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-344] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-310] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-243] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-336] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-305] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-295] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-304] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-296] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>