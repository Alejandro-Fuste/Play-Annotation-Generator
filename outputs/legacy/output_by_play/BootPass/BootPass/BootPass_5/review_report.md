# Play-Annotation-Generator Annotation Review — BootPass_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_5`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 57
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_BootAway` | RB | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `59` | `54` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 211 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `15` | `15` | 122 | START | 122 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `17` | `17` | 122 | START | 122 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `20` | `20` | 122 | START | 122 | 139 |
| ✅ EXACT | `Action_RunBlock` | LG | `21` | `21` | 122 | START | 122 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `6` | `6` | 122 | START | 122 | 157 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `11` | `11` | 126 | END | 126 | 126 |
| ✅ EXACT | `Action_FakeHandoff` | RB | `4` | `4` | 132 | START | 132 | 162 |
| ✅ EXACT | `Action_BootAway` | RB | `4` | `4` | 163 | START | 163 | 170 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `59` | `54` | 311 | START | 312 | 318 |

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
- **Visible Frames:** 0–252
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 252 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_FakeHandoff` | 132 | 162 | 31 | inferred_complete_timeline |
| `Action_BootAway` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_None` | 171 | 177 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 211 | 212 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 278 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 250 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 224 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 157 | 36 | inferred_complete_timeline |
| `Action_RunBlock` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 170 | 178 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 188 | 244 | 57 | inferred_complete_timeline |
| `Action_RunBlock` | 247 | 248 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 249 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 139 | 141 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 143 | 162 | 20 | inferred_complete_timeline |
| `Action_RunBlock` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 253 | 257 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_RunBlock` | 122 | 139 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 149 | 153 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 127 | 172 | 46 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 252 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 247 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 111 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 252 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 252 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 278 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 265 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 245 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–247 | 243 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 142–145 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 147–252 | 105 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 158–160 | 3 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 186–250 | 63 | 2 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 190–250 | 61 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 196–248 | 51 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 217–259 | 10 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 232–252 | 17 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 232–246 | 15 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 236–252 | 17 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 253–263 | 11 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 253–259 | 7 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 253–265 | 13 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 253–265 | 13 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 253–263 | 11 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 253–260 | 8 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 254–255 | 2 | 1 | Undefined position; Undefined team |
| `40` | `44` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `41` | `45` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `42` | `46` | Position_Unknown | Team_Unknown | 266–359 | 75 | 2 | Undefined position; Undefined team |
| `43` | `47` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `44` | `48` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |
| `45` | `50` | Position_Unknown | Team_Unknown | 270–278 | 9 | 1 | Undefined position; Undefined team |
| `46` | `51` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `47` | `52` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `48` | `53` | Position_Unknown | Team_Unknown | 270–281 | 12 | 1 | Undefined position; Undefined team |
| `49` | `54` | Position_Unknown | Team_Unknown | 273–275 | 3 | 1 | Undefined position; Undefined team |
| `50` | `55` | Position_Unknown | Team_Unknown | 279–289 | 11 | 1 | Undefined position; Undefined team |
| `51` | `56` | Position_Unknown | Team_Unknown | 279–359 | 81 | 1 | Undefined position; Undefined team |
| `52` | `57` | Position_Unknown | Team_Unknown | 279–302 | 24 | 1 | Undefined position; Undefined team |
| `53` | `58` | Position_Unknown | Team_Unknown | 282–314 | 33 | 1 | Undefined position; Undefined team |
| `54` | `59` | Position_Unknown | Team_Unknown | 312–359 | 47 | 3 | Undefined position; Undefined team |
| `55` | `60` | Position_Unknown | Team_Unknown | 323–359 | 25 | 2 | Undefined position; Undefined team |
| `56` | `61` | Position_Unknown | Team_Unknown | 343–359 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (7 segments found)
- ⚠️ `Action_SecureCatch` for actor_track_id `59` (Position_Unknown): Annotated start 311 != Inferred start 312

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 11: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-265] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-278] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-250] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [132-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-252] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [160-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [164-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [170-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [180-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [188-244] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [247-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-247] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [139-141] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [130-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [143-162] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [165-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [184-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [253-257] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [141-147] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [149-153] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [122-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-145] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-188] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-252] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-250] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-248] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-252] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-263] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-265] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-265] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-278] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-281] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-289] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-302] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-314] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-334] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-359] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.

</details>