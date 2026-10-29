# Play-Annotation-Generator Annotation Review — DeepCross_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_95`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Completion`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 1 | START | 1 | 6 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 6 | END | 1 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 11 | START | 11 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `17` | `17` | 11 | START | 11 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 11 | START | 11 | 111 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | `0` | `0` | 14 | START | 14 | 169 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 87 | START | 87 | 96 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 6 | 6 | inferred_complete_timeline |
| `Action_None` | 7 | 86 | 80 | inferred_complete_timeline |
| `Action_ThrowPass` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_None` | 115 | 148 | 34 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 70 | 70 | inferred_complete_timeline |
| `Action_None` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_None` | 83 | 163 | 81 | inferred_complete_timeline |
| `Action_None` | 165 | 172 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 14 | 169 | 156 | inferred_complete_timeline |
| `Action_None` | 170 | 187 | 18 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 178 | 178 | inferred_complete_timeline |
| `Action_None` | 180 | 210 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 124 | 124 | inferred_complete_timeline |
| `Action_None` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 187 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 6 | 6 | inferred_complete_timeline |
| `Action_None` | 7 | 10 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 28 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 107 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 133 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 146 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 171 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 189 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 111 | 101 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 132 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 112 | 102 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 124 | 144 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 106 | 106 | inferred_complete_timeline |
| `Action_None` | 115 | 150 | 36 | inferred_complete_timeline |
| `Action_None` | 153 | 162 | 10 | inferred_complete_timeline |
| `Action_None` | 164 | 173 | 10 | inferred_complete_timeline |
| `Action_None` | 177 | 182 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 146 | 146 | inferred_complete_timeline |
| `Action_None` | 157 | 193 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 174 | 174 | inferred_complete_timeline |
| `Action_None` | 178 | 210 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 147 | 147 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_None` | 166 | 210 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 112 | 112 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 123 | 162 | 40 | inferred_complete_timeline |
| `Action_None` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_None` | 177 | 183 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 196 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 112 | 112 | inferred_complete_timeline |
| `Action_None` | 116 | 138 | 23 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 180 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 105 | 105 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 125 | 133 | 9 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 43 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–118 | 107 | 6 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–99 | 95 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 56–161 | 100 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 74–77 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 110–210 | 100 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 156–161 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 98: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 98: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 98: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 98: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [14-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-74] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-111] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-144] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-187] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-43] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-178] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-70] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-174] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-146] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-193] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-106] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-162] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-133] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-146] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-171] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-63] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-99] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-111] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [124-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-148] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-112] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-161] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>