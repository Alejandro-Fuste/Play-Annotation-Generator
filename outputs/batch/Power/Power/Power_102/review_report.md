# Play-Annotation-Generator Annotation Review — Power_102

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_102`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `14` | `14` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 5 | START | 5 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 5 | START | 5 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 5 | START | 5 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 5 | START | 65 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 5 | START | 5 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 5 | START | 5 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 5 | START | 5 | 136 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 5 | START | 5 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `14` | `14` | 137 | START | 137 | 176 |
| ✅ EXACT | `Action_DownBlock` | LT | `7` | `7` | 137 | START | 137 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `9` | 137 | START | 137 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `10` | `10` | 137 | START | 137 | 142 |

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
- **Visible Frames:** 5–272
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 167 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 186 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 214 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 239 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 246 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 272 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–205
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 166 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 183 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 205 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 65–329
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 65 | 142 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 197 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 224 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 329 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 5–149
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 136 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 149 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–252
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 136 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 176 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 191 | 11 | inferred_complete_timeline |
| `Action_None` | 192 | 236 | 45 | inferred_complete_timeline |
| `Action_None` | 243 | 252 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 5–165
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 136 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 158 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 165 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–329
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 136 | 132 | inferred_complete_timeline |
| `Action_PullBlock` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 214 | 23 | inferred_complete_timeline |
| `Action_None` | 245 | 265 | 21 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–259
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 159 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 207 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 259 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 201 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 329 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–255
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 202 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 255 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–285
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 181 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 227 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 285 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 247 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–219
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 213 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 5–169
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 169 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 5–149 | 145 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 5–329 | 311 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 5–247 | 242 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 154–329 | 168 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 159–203 | 30 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 188–229 | 9 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 192–202 | 11 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 215–329 | 115 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 261–275 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [5-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-255] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-285] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-300] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-308] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [137-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [146-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [180-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-181] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-186] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-214] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-239] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-246] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-272] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-247] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '14' starts at frame 137, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [137-176] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-236] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-224] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-194] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-202] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-275] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>