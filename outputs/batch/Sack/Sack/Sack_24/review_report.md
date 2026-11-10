# Play-Annotation-Generator Annotation Review — Sack_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Sack_24`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Defense_Sack`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 49
- **Validation Warnings:** 49
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 30
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | LB1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | DT2 | defense | `6` | `6` |
| ✅ EXACT | `Action_CloseOnQuarterback` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_WrapQuarterback` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SackQuarterback` | LB1 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 6 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 6 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 6 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 6 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 6 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 6 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 6 | START | 0 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | LB1 | `13` | `13` | 173 | START | 173 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_CloseOnQuarterback` | DT2 | `6` | `6` | 173 | START | 173 | 184 |
| ✅ EXACT | `Action_CloseOnQuarterback` | LG | `8` | `8` | 173 | START | 173 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_WrapQuarterback` | LG | `8` | `8` | 194 | START | 194 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_SackQuarterback` | LB1 | `13` | `13` | 210 | START | 210 | 213 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 178 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 170 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 181 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 209 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 173 | 193 | 21 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 197 | 199 | 3 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 179 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 239 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 173 | 184 | 12 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 187 | 208 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 173 | 201 | 29 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 207 | 209 | 3 | inferred_complete_timeline |
| `Action_SackQuarterback` | 210 | 213 | 4 | inferred_complete_timeline |
| `Action_SackQuarterback` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_SackQuarterback` | 220 | 225 | 6 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 153 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 146–239 | 91 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 222–239 | 18 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 226–232 | 4 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CloseOnQuarterback` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CloseOnQuarterback` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_WrapQuarterback` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SackQuarterback` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 36 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [173-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [187-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [173-193] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_WrapQuarterback' range [194-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_WrapQuarterback' range [197-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_WrapQuarterback' range [201-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CloseOnQuarterback' range [173-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [210-213] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [216-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-131] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-199] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.

</details>