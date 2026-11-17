# Play-Annotation-Generator Annotation Review — Power_338

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_338`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 132
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 20 | START | 20 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 20 | START | 20 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 20 | START | 20 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 20 | START | 20 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 20 | START | 20 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 20 | START | 20 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 20 | START | 20 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `10` | `10` | 155 | START | 155 | 165 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `16` | `16` | 155 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `4` | `4` | 155 | START | 155 | 156 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 177 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 191 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 202 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 266 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 329 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–281
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 225 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 239 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 281 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 20–163
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 163 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 20–157
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 157 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 49 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 154 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 167 | 180 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 222 | 25 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 20–156
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 151 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–179
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 157 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 179 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–238
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 44 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 232 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 159 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 313 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 329 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 175 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 208 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 271 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 308 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–215
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 193 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 215 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 20–328 | 308 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 20–329 | 278 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 20–310 | 193 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 29–56 | 27 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 48–163 | 9 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 135–146 | 8 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 145–153 | 9 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 160–221 | 62 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 161–319 | 145 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 164–177 | 14 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 165–290 | 123 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 169–329 | 139 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 186–216 | 26 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 235–329 | 95 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 248–329 | 80 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 267–279 | 13 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 273–295 | 20 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 276–280 | 5 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 281–329 | 49 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 284–329 | 46 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 291–329 | 39 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 299–328 | 30 | 1 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `16` (Position_Unknown)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 676: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_DownBlock' for track '16' has invalid range: start=155, end=146. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [20-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-328] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-157] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-193] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-215] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [155-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-271] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-44] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-232] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-191] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-266] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-246] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-154] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-165] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [167-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-310] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-179] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-146] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-153] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-179] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-319] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-229] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-283] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-288] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-328] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>