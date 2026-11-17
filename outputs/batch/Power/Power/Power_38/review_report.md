# Play-Annotation-Generator Annotation Review — Power_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_38`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 12 | START | 12 | 206 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 12 | START | 12 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 12 | START | 12 | 222 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 12 | START | 12 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `2` | `Group` | 12 | START | 12 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 12 | START | 12 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 12 | START | 12 | 104 |
| ✅ EXACT | `Action_DownBlock` | C | `11` | `11` | 105 | START | 105 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `9` | 105 | START | 105 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `5` | `5` | 105 | START | 105 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 12–225
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 222 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 63 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 154 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 269 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–228
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 104 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 130 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 140 | 9 | inferred_complete_timeline |
| `Action_None` | 141 | 222 | 82 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 160 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 269 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 104 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 140 | 36 | inferred_complete_timeline |
| `Action_None` | 141 | 269 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 104 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 105 | 118 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 124 | 126 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 128 | 140 | 13 | inferred_complete_timeline |
| `Action_None` | 141 | 174 | 34 | inferred_complete_timeline |
| `Action_None` | 184 | 269 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–232
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 206 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 232 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 168 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 269 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 228 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 250 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–213
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 128 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 153 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 199 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 213 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 30 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 269 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 12–250
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 187 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 250 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 188 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 224 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 246 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 269 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 190 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 242 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–268
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 214 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 242 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 268 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 17–268 | 235 | 3 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 105–152 | 48 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 130–140 | 11 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 157–269 | 109 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 248–252 | 5 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 248–249 | 2 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 49 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [12-187] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-250] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-63] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-154] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-188] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-232] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-190] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [105-118] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [124-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-174] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-268] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-228] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-250] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-206] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-232] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-222] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-153] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-207] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-258] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-268] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-252] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-269] for track '23' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.

</details>