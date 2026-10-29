# Play-Annotation-Generator Annotation Review — DeepCross_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_17`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 10 | START | 10 | 14 |
| ✅ EXACT | `Action_PassBlock` | RT | `12` | `12` | 13 | START | 13 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 13 | START | 13 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 13 | START | 15 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 13 | START | 13 | 144 |
| ✅ EXACT | `Action_RunDeepCrossRoute` | WR1 | `4` | `4` | 14 | START | 14 | 166 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 14 | END | 10 | 14 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 96 | START | 96 | 104 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `4` | `4` | 168 | START | 168 | 210 |

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
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 14 | 5 | inferred_complete_timeline |
| `Action_None` | 15 | 95 | 81 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 161 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 196 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 14 | 166 | 153 | inferred_complete_timeline |
| `Action_None` | 167 | 167 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 210 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 9 | 5 | inferred_complete_timeline |
| `Action_None` | 10 | 80 | 71 | inferred_complete_timeline |
| `Action_None` | 88 | 93 | 6 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 144 | 132 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 204 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 49 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 108 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 159 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 14 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 27 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 110 | 74 | inferred_complete_timeline |
| `Action_PassBlock` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 201 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 106 | 97 | inferred_complete_timeline |
| `Action_None` | 121 | 187 | 67 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 33 | 24 | inferred_complete_timeline |
| `Action_None` | 37 | 123 | 87 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 29 | 20 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_None` | 52 | 77 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 32 | 23 | inferred_complete_timeline |
| `Action_None` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 152 | 71 | inferred_complete_timeline |
| `Action_None` | 158 | 187 | 30 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 178 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 210 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 108 | 99 | inferred_complete_timeline |
| `Action_None` | 112 | 210 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 155 | 146 | inferred_complete_timeline |
| `Action_None` | 157 | 161 | 5 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–206 | 207 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–35 | 36 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 38–210 | 173 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 88–90 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 135–176 | 37 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 164–210 | 38 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 19: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [10–14], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=15.
- ⚠️ Action 'Action_None' range [10-108] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-206] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-35] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-196] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-144] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-152] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-123] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-49] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [60-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-159] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [174-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [112-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-80] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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