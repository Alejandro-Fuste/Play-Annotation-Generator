# Play-Annotation-Generator Annotation Review — Duo_164

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_164`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 268
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 266 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `10` | `10` | 187 | START | 187 | 215 |
| ✅ EXACT | `Action_ComboBlock` | LG | `13` | `13` | 187 | START | 187 | 252 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | `2` | `2` | 187 | START | 187 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `6` | `6` | 187 | START | 187 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 252 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 35 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 80 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 266 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 161 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 181 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 186 | 4 | inferred_complete_timeline |
| `Action_ComboBlock` | 187 | 193 | 7 | inferred_complete_timeline |
| `Action_ComboBlock` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 212 | 226 | 15 | inferred_complete_timeline |
| `Action_ComboBlock` | 232 | 252 | 21 | inferred_complete_timeline |
| `Action_None` | 253 | 264 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ComboBlock` | 187 | 252 | 66 | inferred_complete_timeline |
| `Action_None` | 253 | 264 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_ComboBlock` | 187 | 215 | 29 | inferred_complete_timeline |
| `Action_ComboBlock` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_ComboBlock` | 252 | 252 | 1 | inferred_complete_timeline |
| `Action_None` | 253 | 268 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 186 | 27 | inferred_complete_timeline |
| `Action_ComboBlock` | 187 | 238 | 52 | inferred_complete_timeline |
| `Action_ComboBlock` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 245 | 246 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 268 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 230 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 260 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 264 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 259 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–1
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 256 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 263 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 13–268 | 250 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 64–177 | 13 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 100–268 | 169 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 104–268 | 165 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 134–165 | 32 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 181–264 | 79 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 192–262 | 60 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 193–268 | 76 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 211–268 | 9 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 230–268 | 24 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 231–268 | 6 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 251–268 | 17 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 265–268 | 4 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 265–268 | 4 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 265–268 | 4 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-259] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-161] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [187-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [205-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [212-226] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [187-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [241-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [245-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [187-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [246-250] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-35] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [187-252] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-268] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-268] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-165] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-238] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-262] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-268] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-266] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-268] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>