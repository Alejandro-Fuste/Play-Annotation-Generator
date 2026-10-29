# Play-Annotation-Generator Annotation Review — Duo_25

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `Duo_25`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 268
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 99
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 186 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 157 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 7 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 203 |
| ✅ EXACT | `Action_ComboBlock` | C | `19` | `19` | 167 | START | 167 | 167 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | `19` | `19` | 174 | START | 180 | 199 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 212 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 186 | 187 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 206 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 203 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 226 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 197 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 209 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 250 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 258 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 7–268
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 178 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 201 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 229 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 248 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 265 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_ComboBlock` | 167 | 167 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 180 | 199 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 170 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 268 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 211 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 241 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 249 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 261 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 268 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 258 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 229 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 268 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 250 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 267 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 219 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–250 | 246 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 20–42 | 23 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 183–189 | 5 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 200–268 | 48 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 213–268 | 48 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 225–268 | 30 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 238–258 | 10 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 247–268 | 15 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 247–268 | 12 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 258–268 | 11 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 264–268 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BlockSecondLevel` for actor_track_id `19` (C): Annotated start 174 != Inferred start 180

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_ComboBlock' at frame 167 targets track ID '220', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-203] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-206] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-213] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-250] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-267] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-219] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-209] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-211] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-241] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-261] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-230] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-250] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '19' starts at frame 167, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [167-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [180-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-178] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-229] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-248] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-42] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-216] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-235] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-222] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-230] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-238] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>