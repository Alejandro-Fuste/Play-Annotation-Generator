# Play-Annotation-Generator Annotation Review — Duo_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_18`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | SAF | defense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 178 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 328 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `10` | `10` | 189 | START | 189 | 202 |
| ✅ EXACT | `Action_ComboBlock` | C | `15` | `15` | 189 | START | 189 | 207 |
| ✅ EXACT | `Action_ComboBlock` | C | `15` | `15` | 189 | START | 189 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | SAF | `5` | `5` | 189 | START | 207 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `3` | 213 | START | 213 | 257 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | `15` | `15` | 215 | START | 217 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 249 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 328 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–300
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_BallCarry` | 213 | 257 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 264 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 280 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 286 | 290 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 299 | 300 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 240 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 181 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 224 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_ComboBlock` | 189 | 207 | 19 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 217 | 230 | 14 | inferred_complete_timeline |
| `Action_None` | 265 | 328 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 217 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 178 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 188 | 6 | inferred_complete_timeline |
| `Action_ComboBlock` | 189 | 202 | 14 | inferred_complete_timeline |
| `Action_ComboBlock` | 207 | 249 | 43 | inferred_complete_timeline |
| `Action_None` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_None` | 259 | 263 | 5 | inferred_complete_timeline |
| `Action_None` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 328 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 314 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 300 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 328 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 217 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 296 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 317 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 304 | 305 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 232 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 281 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 328 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_ComboBlock` | 207 | 233 | 27 | inferred_complete_timeline |
| `Action_ComboBlock` | 242 | 249 | 8 | inferred_complete_timeline |
| `Action_None` | 250 | 328 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 7–279 | 263 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 10–327 | 312 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 145–328 | 168 | 6 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 170–326 | 150 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 196–328 | 133 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 203–328 | 126 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 275–328 | 54 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 277–328 | 46 | 3 | Undefined position; Undefined team |
| `24` | `39` | Position_Unknown | Team_Unknown | 302–327 | 26 | 1 | Undefined position; Undefined team |
| `25` | `40` | Position_Unknown | Team_Unknown | 316–328 | 11 | 3 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 320–321 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (5 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `15` (C): Annotated start 215 != Inferred start 217

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 38: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Deduplicated duplicate event 'Action_ComboBlock' at frame 189 for track '15'.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-304] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-281] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [213-257] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-280] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [286-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [299-300] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [207-233] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-328] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-300] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-328] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [189-202] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-314] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-328] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-181] for track '14' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-224] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [189-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [217-230] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-254] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-311] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-193] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-208] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-250] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-267] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-311] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-321] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-310] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '26' has 1 frames without a visible bounding box.
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

</details>