# Play-Annotation-Generator Annotation Review — DeepCross_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_59`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 16 | START | 16 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `10` | 19 | START | 32 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 19 | START | 19 | 223 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 19 | START | 19 | 194 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 19 | START | 19 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 19 | START | 19 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `1` | `1` | 31 | START | 31 | 202 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 31 | END | 16 | 31 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `7` | `7` | 127 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_None` | 32 | 54 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 146 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 149 | 134 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 31 | 202 | 172 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 204 | 221 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 100 | 85 | inferred_complete_timeline |
| `Action_None` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 118 | 144 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 194 | 176 | inferred_complete_timeline |
| `Action_PassBlock` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 52 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 128 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 269 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_BallSnap` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 81 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 96 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 269 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 223 | 205 | inferred_complete_timeline |
| `Action_PassBlock` | 230 | 246 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 253 | 261 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 43 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 174 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 203 | 215 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 197 | 182 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 223 | 16 | inferred_complete_timeline |
| `Action_None` | 236 | 242 | 7 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 83 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 269 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 152 | 137 | inferred_complete_timeline |
| `Action_None` | 154 | 218 | 65 | inferred_complete_timeline |
| `Action_None` | 220 | 269 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 195 | 180 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 244 | 13 | inferred_complete_timeline |
| `Action_None` | 246 | 259 | 14 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 251 | 236 | inferred_complete_timeline |
| `Action_None` | 253 | 265 | 13 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 201 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 49 | 34 | inferred_complete_timeline |
| `Action_None` | 51 | 91 | 41 | inferred_complete_timeline |
| `Action_None` | 93 | 141 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 203 | 188 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–268 | 237 | 10 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–269 | 241 | 6 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–269 | 269 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–54 | 6 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 53–269 | 217 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 54–122 | 69 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 166–269 | 102 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 170–269 | 100 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 185–269 | 80 | 5 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 192–269 | 73 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 214–242 | 25 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 219–259 | 28 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 227–265 | 34 | 6 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `7` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 62: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 62: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 62: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '7' has invalid range: start=127, end=54. Clamping end to start.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [16–31], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=32.
- ⚠️ Action 'Action_None' range [16-197] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-223] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [31-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [204-221] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-201] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-54] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-244] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-81] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-246] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-261] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-231] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-251] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-223] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [230-246] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [253-261] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [197-202] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-218] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-43] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [197-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [203-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-122] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-263] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-244] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-259] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-251] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>