# Play-Annotation-Generator Annotation Review — DeepCross_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_33`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR3 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 23 | START | 23 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 26 | START | 40 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 26 | START | 26 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 26 | START | 26 | 61 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 26 | START | 26 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 26 | START | 26 | 174 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR3 | `4` | `4` | 39 | START | 39 | 184 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 39 | END | 23 | 39 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 117 | START | 117 | 126 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `4` | `4` | 185 | START | 185 | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_None` | 40 | 116 | 77 | inferred_complete_timeline |
| `Action_ThrowPass` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 170 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 129 | 107 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 39 | 184 | 146 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 194 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 73 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 150 | 66 | inferred_complete_timeline |
| `Action_PassBlock` | 155 | 162 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 189 | 195 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 58 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 66 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 61 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 97 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 108 | 206 | 99 | inferred_complete_timeline |
| `Action_PassBlock` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 174 | 149 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 183 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 150 | 128 | inferred_complete_timeline |
| `Action_None` | 155 | 163 | 9 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 195 | 12 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 219 | 236 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 151 | 129 | inferred_complete_timeline |
| `Action_None` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 209 | 45 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 150 | 128 | inferred_complete_timeline |
| `Action_None` | 154 | 187 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 150 | 128 | inferred_complete_timeline |
| `Action_None` | 153 | 195 | 43 | inferred_complete_timeline |
| `Action_None` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 239 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 77 | 55 | inferred_complete_timeline |
| `Action_None` | 79 | 239 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 156 | 134 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 132 | 110 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 202 | 180 | inferred_complete_timeline |
| `Action_None` | 204 | 235 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 239 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 37–39 | 3 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 40–239 | 199 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 43–95 | 45 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–239 | 152 | 8 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 78–196 | 103 | 7 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 137–165 | 29 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 169–205 | 12 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 200–219 | 19 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 205–233 | 6 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 219–232 | 14 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 225–239 | 15 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (9 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 35: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [23–39], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=40.
- ⚠️ Action 'Action_None' range [23-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-209] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-150] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-163] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-236] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-174] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-150] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-132] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-170] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-58] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-150] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [155-162] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [189-195] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [204-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [210-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [219-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-97] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [108-206] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [215-239] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-151] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-165] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-209] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-219] for track '28' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-232] for track '31' has 1 frames without a visible bounding box.
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

</details>