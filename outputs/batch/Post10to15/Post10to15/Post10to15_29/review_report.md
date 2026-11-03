# Play-Annotation-Generator Annotation Review — Post10to15_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR4 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 7 | START | 7 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `1` | `1` | 10 | START | 10 | 98 |
| ✅ EXACT | `Action_PassBlock` | LG | `11` | `11` | 10 | START | 10 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 10 | START | 10 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 10 | START | 28 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `6` | `6` | 10 | START | 10 | 52 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR4 | `0` | `0` | 21 | START | 21 | 126 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 27 | END | 7 | 27 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 76 | START | 76 | 84 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 27 | 21 | inferred_complete_timeline |
| `Action_None` | 28 | 75 | 48 | inferred_complete_timeline |
| `Action_ThrowPass` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 85 | 94 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 77 | 71 | inferred_complete_timeline |
| `Action_None` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 168 | 162 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 123 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunPostRoute` | 21 | 126 | 106 | inferred_complete_timeline |
| `Action_RunPostRoute` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_RunPostRoute` | 152 | 194 | 43 | inferred_complete_timeline |
| `Action_RunPostRoute` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 177 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 184 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 27 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 51 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 148 | 96 | inferred_complete_timeline |
| `Action_PassBlock` | 153 | 163 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 209 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 97 | 88 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 52 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 171 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 41 | 35 | inferred_complete_timeline |
| `Action_None` | 43 | 105 | 63 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 135 | 25 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 165 | 159 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 156 | 80 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 91 | 85 | inferred_complete_timeline |
| `Action_None` | 93 | 120 | 28 | inferred_complete_timeline |
| `Action_None` | 122 | 130 | 9 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 34 | 28 | inferred_complete_timeline |
| `Action_None` | 36 | 116 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 19 | 13 | inferred_complete_timeline |
| `Action_None` | 26 | 190 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 111 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 163 | 157 | inferred_complete_timeline |
| `Action_None` | 170 | 189 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 149 | 143 | inferred_complete_timeline |
| `Action_None` | 155 | 210 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 104 | 98 | inferred_complete_timeline |
| `Action_None` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 205 | 51 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 100–192 | 59 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 102–159 | 52 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 165–167 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 168–205 | 38 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 170–210 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [7–27], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=28.
- ⚠️ Action 'Action_RunPostRoute' range [21-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [145-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [152-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [198-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-177] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-77] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-205] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-165] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-156] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-97] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-116] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-120] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-130] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-190] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-51] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [153-163] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [165-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-209] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-159] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-205] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '26' has 1 frames without a visible bounding box.
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