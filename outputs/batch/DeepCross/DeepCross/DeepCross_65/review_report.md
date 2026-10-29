# Play-Annotation-Generator Annotation Review — DeepCross_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_65`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 13 | START | 13 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `14` | 16 | START | 16 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 16 | START | 29 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 16 | START | 16 | 26 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 16 | START | 16 | 50 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 28 | END | 13 | 28 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR2 | `1` | `1` | 30 | START | 30 | 202 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 121 | START | 121 | 131 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_None` | 29 | 120 | 92 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 231 | 100 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 90 | 78 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 148 | 39 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 169 | 176 | 8 | inferred_complete_timeline |
| `Action_None` | 180 | 184 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 209 | 7 | inferred_complete_timeline |
| `Action_None` | 211 | 234 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 30 | 202 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 206 | 194 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 26 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 51 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 74 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 80 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 13 | 28 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 183 | 155 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 196 | 225 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 50 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 78 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 207 | 121 | inferred_complete_timeline |
| `Action_PassBlock` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 215 | 231 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 108 | 96 | inferred_complete_timeline |
| `Action_None` | 112 | 177 | 66 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 233 | 221 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 55 | 43 | inferred_complete_timeline |
| `Action_None` | 71 | 74 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 175 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 222 | 43 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_None` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–202 | 200 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–175 | 170 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 45–76 | 21 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 49–155 | 58 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 49–239 | 173 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 140–239 | 75 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 203–238 | 33 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 205–237 | 31 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 217–231 | 10 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 218–239 | 19 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 68: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 68: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [13–28], lower_priority='Action_PassBlock' annotated_start=16, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [13-206] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [30-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-239] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-177] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-207] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [209-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [215-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-183] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [196-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [227-228] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-234] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-167] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-231] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-80] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-148] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-230] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>