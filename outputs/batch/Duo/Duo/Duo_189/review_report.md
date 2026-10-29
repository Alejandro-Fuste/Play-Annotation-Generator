# Play-Annotation-Generator Annotation Review — Duo_189

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_189`
- **Frame Range:** 0 to 274 (275 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 274
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_ComboBlock` | LB1 | defense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `12` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 173 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `9` | `9` | 163 | START | 163 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `10` | `10` | 163 | START | 163 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `15` | `15` | 163 | START | 189 | 200 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | `21` | `19` | 163 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | LB1 | `2` | `2` | 163 | START | 163 | 205 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 205 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 196 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 274 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 189 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 51 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 175 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 163 | 189 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 196 | 205 | 10 | inferred_complete_timeline |
| `Action_None` | 206 | 274 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 152 | 128 | inferred_complete_timeline |
| `Action_ComboBlock` | 189 | 200 | 12 | inferred_complete_timeline |
| `Action_ComboBlock` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 206 | 240 | 35 | inferred_complete_timeline |
| `Action_None` | 243 | 274 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_ComboBlock` | 163 | 190 | 28 | inferred_complete_timeline |
| `Action_ComboBlock` | 195 | 205 | 11 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |
| `Action_None` | 245 | 274 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 274 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 206 | 207 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 265 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 273 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 69 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_ComboBlock` | 163 | 205 | 43 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_None` | 214 | 217 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 222 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 274 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–274
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 236 | 231 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 250 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 274 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | Position_Unknown | Team_Unknown | 21–26 | 6 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 21–149 | 129 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 46–166 | 41 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 68–158 | 54 | 4 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 95–274 | 164 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 118–211 | 94 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 179–189 | 10 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 186–274 | 85 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 186–274 | 84 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 194–234 | 41 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 200–274 | 73 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 206–274 | 57 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 217–220 | 4 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 224–252 | 29 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 226–274 | 46 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_ComboBlock` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 274 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '19' has invalid range: start=163, end=149. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-196] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-189] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [163-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [163-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-37] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-69] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [189-200] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-240] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-68] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-158] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-157] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-274] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-211] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-184] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-260] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-274] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-252] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-274] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-258] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-268] for track '33' has 3 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>