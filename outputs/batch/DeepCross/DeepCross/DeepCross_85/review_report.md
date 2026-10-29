# Play-Annotation-Generator Annotation Review — DeepCross_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_85`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | offense | `3` | `3` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 2 | START | 2 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `13` | `13` | 5 | START | 5 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 5 | START | 7 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 5 | START | 5 | 10 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 5 | START | 5 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 5 | START | 5 | 10 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `16` | `16` | 6 | END | 2 | 6 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | `3` | `3` | 16 | START | 16 | 152 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `16` | `16` | 120 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 16 | 152 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 153 | 152 | inferred_complete_timeline |
| `Action_None` | 156 | 163 | 8 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 4 | 36 | 33 | inferred_complete_timeline |
| `Action_None` | 42 | 192 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 10 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 106 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 10 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 48 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 52 | 187 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 13 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 86 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 110 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 184 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 5 | 71 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 195 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 198 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 118 | 117 | inferred_complete_timeline |
| `Action_None` | 120 | 185 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 210 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 58 | 57 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 50 | 49 | inferred_complete_timeline |
| `Action_None` | 126 | 176 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 149 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 179 | 28 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 191 | 199 | 9 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 166 | 165 | inferred_complete_timeline |
| `Action_None` | 169 | 180 | 12 | inferred_complete_timeline |
| `Action_None` | 191 | 198 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 173 | 172 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–210 | 203 | 5 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–24 | 25 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–106 | 107 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–43 | 44 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 37–172 | 135 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 46–171 | 126 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 68–73 | 6 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 130–187 | 58 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 141–188 | 39 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 152–159 | 8 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 159–186 | 25 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 184–210 | 26 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `16` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 88: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '16' has invalid range: start=120, end=43. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [2–6], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=7.
- ⚠️ Action 'Action_None' range [2-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [16-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-58] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-198] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-106] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-195] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-179] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-43] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-13] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-110] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-106] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [5-10] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-15] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-48] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [52-187] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-192] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-188] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-169] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-206] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>