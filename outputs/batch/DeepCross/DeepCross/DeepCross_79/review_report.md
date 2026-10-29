# Play-Annotation-Generator Annotation Review — DeepCross_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_79`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF1 | defense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | SAF1 | `16` | `16` | 3 | START | 3 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 6 | START | 6 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 6 | START | 6 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `9` | `9` | 6 | START | 6 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `0` | `0` | 20 | START | 20 | 181 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 20 | END | 3 | 20 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 122 | START | 122 | 130 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_None` | 21 | 79 | 59 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 112 | 17 | inferred_complete_timeline |
| `Action_None` | 121 | 121 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_None` | 132 | 148 | 17 | inferred_complete_timeline |
| `Action_None` | 156 | 169 | 14 | inferred_complete_timeline |
| `Action_None` | 173 | 225 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 128 | 126 | inferred_complete_timeline |
| `Action_None` | 130 | 173 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 151 | 149 | inferred_complete_timeline |
| `Action_None` | 159 | 163 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 214 | 224 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 20 | 181 | 162 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 220 | 22 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 199 | 197 | inferred_complete_timeline |
| `Action_None` | 203 | 204 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 215 | 10 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 108 | 106 | inferred_complete_timeline |
| `Action_None` | 116 | 164 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 106 | 101 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 177 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 61 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 91 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 214 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 132 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 214 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 154 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 71 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 184 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 221 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 116 | 114 | inferred_complete_timeline |
| `Action_None` | 127 | 167 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 217 | 215 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 226 | 224 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 233 | 231 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 3 | 20 | 18 | inferred_complete_timeline |
| `Action_None` | 21 | 32 | 12 | inferred_complete_timeline |
| `Action_None` | 46 | 53 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 179 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–239 | 237 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–239 | 237 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–233 | 234 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 33–36 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 45–191 | 137 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 84–103 | 20 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 138–203 | 66 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 182–185 | 4 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 82: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 82: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 82: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [20-181] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [185-190] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-220] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-226] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-233] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-108] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-179] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-239] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-128] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [122-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-169] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-225] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [6-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-46] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-103] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '27' has 1 frames without a visible bounding box.
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

</details>