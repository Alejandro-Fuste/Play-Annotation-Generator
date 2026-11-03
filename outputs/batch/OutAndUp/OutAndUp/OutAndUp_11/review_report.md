# Play-Annotation-Generator Annotation Review — OutAndUp_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `7` | `7` |
| ✅ EXACT | `Action_SellOut` | WR1 | offense | `8` | `8` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB1 | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 66 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 15 | START | 15 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `13` | 19 | START | 30 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 19 | START | 19 | 103 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 19 | START | 19 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 19 | START | 19 | 162 |
| ✅ EXACT | `Action_PassBlock` | RT | `6` | `6` | 19 | START | 19 | 183 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `7` | `7` | 29 | END | 15 | 29 |
| ✅ EXACT | `Action_SellOut` | WR1 | `8` | `8` | 67 | START | 67 | 86 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `8` | `8` | 87 | START | 87 | 210 |
| ✅ EXACT | `Action_ThrowPass` | QB1 | `7` | `7` | 105 | START | 105 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_None` | 30 | 104 | 75 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_None` | 118 | 173 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 51 | 37 | inferred_complete_timeline |
| `Action_None` | 53 | 93 | 41 | inferred_complete_timeline |
| `Action_None` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 131 | 8 | inferred_complete_timeline |
| `Action_None` | 134 | 157 | 24 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SellOut` | 67 | 86 | 20 | inferred_complete_timeline |
| `Action_RunGoRoute` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 129 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 161 | 147 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 56 | 42 | inferred_complete_timeline |
| `Action_None` | 59 | 129 | 71 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_None` | 142 | 153 | 12 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 210 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 103 | 85 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 176 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 186 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 77 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 114 | 169 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 209 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 162 | 144 | inferred_complete_timeline |
| `Action_PassBlock` | 183 | 184 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 186 | 193 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 183 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 167 | 153 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_None` | 175 | 180 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 170 | 156 | inferred_complete_timeline |
| `Action_None` | 177 | 180 | 4 | inferred_complete_timeline |
| `Action_None` | 182 | 197 | 16 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 114 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 44 | 30 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 173 | 119 | inferred_complete_timeline |
| `Action_None` | 184 | 191 | 8 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 171 | 157 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 142 | 128 | inferred_complete_timeline |
| `Action_None` | 144 | 162 | 19 | inferred_complete_timeline |
| `Action_None` | 166 | 210 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 122 | 108 | inferred_complete_timeline |
| `Action_None` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 96 | 82 | inferred_complete_timeline |
| `Action_None` | 99 | 129 | 31 | inferred_complete_timeline |
| `Action_None` | 134 | 179 | 46 | inferred_complete_timeline |
| `Action_None` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 210 | 196 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 119–162 | 38 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 120–125 | 6 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 128–210 | 83 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [15–29], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=30.
- ⚠️ Action 'Action_None' range [15-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-93] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-131] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-96] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-179] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-183] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [87-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-171] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [110-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-173] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [114-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-186] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-153] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-162] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [183-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [186-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-157] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
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

</details>