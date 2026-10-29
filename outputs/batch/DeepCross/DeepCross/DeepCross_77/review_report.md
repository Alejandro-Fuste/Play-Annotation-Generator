# Play-Annotation-Generator Annotation Review — DeepCross_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_77`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB1 | defense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 11 | START | 11 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 14 | START | 24 | 39 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 14 | START | 14 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 14 | START | 14 | 42 |
| ✅ EXACT | `Action_PassBlock` | RT | `21` | `21` | 14 | START | 14 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `6` | 14 | START | 14 | 97 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | CB1 | `0` | `0` | 23 | START | 23 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 23 | END | 11 | 23 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 155 | START | 155 | 165 |

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
- **Visible Frames:** 0–234
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_None` | 24 | 154 | 131 | inferred_complete_timeline |
| `Action_ThrowPass` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 198 | 33 | inferred_complete_timeline |
| `Action_None` | 204 | 234 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 62 | 52 | inferred_complete_timeline |
| `Action_None` | 68 | 99 | 32 | inferred_complete_timeline |
| `Action_None` | 102 | 269 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 269 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 97 | 87 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 158 | 171 | 14 | inferred_complete_timeline |
| `Action_None` | 175 | 214 | 40 | inferred_complete_timeline |
| `Action_None` | 217 | 227 | 11 | inferred_complete_timeline |
| `Action_None` | 234 | 246 | 13 | inferred_complete_timeline |
| `Action_None` | 248 | 260 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 157 | 147 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 97 | 84 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 227 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 151 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 23 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 39 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 90 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 113 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 150 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 269 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 42 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 72 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 232 | 158 | inferred_complete_timeline |
| `Action_PassBlock` | 237 | 269 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 227 | 214 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 118 | 108 | inferred_complete_timeline |
| `Action_None` | 134 | 143 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 163 | 198 | 36 | inferred_complete_timeline |
| `Action_None` | 205 | 216 | 12 | inferred_complete_timeline |
| `Action_None` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_None` | 231 | 254 | 24 | inferred_complete_timeline |
| `Action_None` | 260 | 267 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 117 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 156 | 146 | inferred_complete_timeline |
| `Action_None` | 159 | 269 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 227 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 23 | 226 | 204 | inferred_complete_timeline |
| `Action_None` | 227 | 246 | 20 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 251 | 261 | 11 | inferred_complete_timeline |
| `Action_None` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 181 | 171 | inferred_complete_timeline |
| `Action_None` | 183 | 231 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 159 | 149 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 183 | 20 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 206 | 5 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 231 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 227 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 227 | 217 | inferred_complete_timeline |
| `Action_None` | 240 | 269 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–227 | 228 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–227 | 228 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–269 | 269 | 3 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 72–74 | 3 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 121–128 | 8 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 140–165 | 23 | 2 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 172–265 | 81 | 4 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 188–227 | 40 | 1 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 189–269 | 42 | 2 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 228–266 | 36 | 3 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 228–255 | 23 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 228–269 | 41 | 2 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 228–242 | 15 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 228–267 | 40 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 228–251 | 24 | 1 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 241–260 | 8 | 2 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 245–250 | 6 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 258–269 | 12 | 1 | Undefined position; Undefined team |
| `41` | `60` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 80: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ Row 80: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 80: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–23], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [23-226] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-246] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-157] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-227] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-231] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-227] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-143] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-198] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-216] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-254] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-227] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-198] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-159] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-183] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-227] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-269] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-62] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-90] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-113] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-97] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-227] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-232] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-157] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-257] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-251] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-242] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-251] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>