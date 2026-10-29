# Play-Annotation-Generator Annotation Review — Duo_61

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_61`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 268
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_ComboBlock` | LB1 | defense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | SAF | defense | `18` | `18` |
| ✅ EXACT | `Action_ComboBlock` | TE3 | offense | `20` | `19` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | defense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `0` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `20` | `Group` | 0 | START | 20 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 0 | START | 24 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `12` | `12` | 150 | START | 150 | 198 |
| ✅ EXACT | `Action_ComboBlock` | LB1 | `15` | `15` | 150 | START | 150 | 207 |
| ✅ EXACT | `Action_ComboBlock` | SAF | `18` | `18` | 150 | START | 150 | 207 |
| ✅ EXACT | `Action_ComboBlock` | TE3 | `20` | `19` | 150 | START | 150 | 207 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT1 | `21` | `20` | 156 | START | 156 | 207 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 207 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 225 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–222
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 149 | 130 | inferred_complete_timeline |
| `Action_ComboBlock` | 150 | 207 | 58 | inferred_complete_timeline |
| `Action_None` | 208 | 216 | 9 | inferred_complete_timeline |
| `Action_None` | 219 | 222 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 183 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 268 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_ComboBlock` | 150 | 198 | 49 | inferred_complete_timeline |
| `Action_ComboBlock` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 24–268
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 268 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 197 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 234 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 246 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 262 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 268 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 20–268
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 155 | 136 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 156 | 207 | 52 | inferred_complete_timeline |
| `Action_None` | 208 | 268 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 268 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_ComboBlock` | 150 | 207 | 58 | inferred_complete_timeline |
| `Action_None` | 208 | 216 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 268 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 226 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 268 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 8–268
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 149 | 142 | inferred_complete_timeline |
| `Action_ComboBlock` | 150 | 207 | 58 | inferred_complete_timeline |
| `Action_None` | 208 | 268 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–179 | 174 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 61–264 | 158 | 13 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 157–261 | 87 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 181–268 | 88 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 191–207 | 17 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 196–206 | 11 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 205–268 | 59 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 252–268 | 17 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 258–262 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 124: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-254] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-268] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [150-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [206-207] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-246] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-262] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-268] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-64] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-96] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-120] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-183] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-217] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-239] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-246] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-259] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-261] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-206] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-268] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>