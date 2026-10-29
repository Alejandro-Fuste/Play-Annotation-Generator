# Play-Annotation-Generator Annotation Review — Duo_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_36`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LB1 | defense | `12` | `12` |
| ✅ EXACT | `Action_ComboBlock` | DT1 | defense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `27` | `22` |
| ✅ EXACT | `Action_BlockSecondLevel` | DE1 | defense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 227 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 274 |
| ✅ EXACT | `Action_ComboBlock` | LB1 | `12` | `12` | 87 | START | 87 | 145 |
| ✅ EXACT | `Action_ComboBlock` | DT1 | `17` | `17` | 87 | START | 87 | 145 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | `20` | `19` | 87 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ComboBlock` | Position_Unknown | `27` | `22` | 87 | START | 172 | 172 |
| ✅ EXACT | `Action_BlockSecondLevel` | DE1 | `14` | `14` | 125 | START | 125 | 145 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 227 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 240 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 250 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 289 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 328 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 314 | 315 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 328 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 24 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 221 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 237 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 256 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 285 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 306 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 323 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 328 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 238 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 124 | 59 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 125 | 145 | 21 | inferred_complete_timeline |
| `Action_None` | 146 | 160 | 15 | inferred_complete_timeline |
| `Action_None` | 195 | 328 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 86 | 45 | inferred_complete_timeline |
| `Action_ComboBlock` | 87 | 145 | 59 | inferred_complete_timeline |
| `Action_None` | 146 | 220 | 75 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 230 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 272 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 286 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 293 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ComboBlock` | 87 | 145 | 59 | inferred_complete_timeline |
| `Action_None` | 146 | 265 | 120 | inferred_complete_timeline |
| `Action_None` | 271 | 328 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 218 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 221 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 226 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 282 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 310 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 328 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 248 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–252 | 226 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 31–42 | 12 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 36–188 | 153 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 51–276 | 226 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 172–173 | 2 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 192–327 | 115 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 205–328 | 124 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 220–328 | 73 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 231–328 | 97 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 278–305 | 4 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 287–328 | 39 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 302–307 | 6 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 309–327 | 18 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 328–328 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `20` (Position_Unknown)
- ⚠️ `Action_ComboBlock` for actor_track_id `27` (Position_Unknown): Annotated start 87 != Inferred start 172

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '19' has invalid range: start=87, end=42. Clamping end to start.
- ⚠️ Segment 'Action_ComboBlock' for track '22' has invalid range: start=172, end=145. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-221] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-237] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-256] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-328] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-218] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-24] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-238] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-328] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-272] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-286] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-293] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-86] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-220] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-314] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-276] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 173, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [173-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-327] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-328] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-328] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-305] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-291] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-307] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-327] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>