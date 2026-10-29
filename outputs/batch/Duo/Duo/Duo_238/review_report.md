# Play-Annotation-Generator Annotation Review — Duo_238

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_238`
- **Frame Range:** 0 to 448 (449 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 448
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 273 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 170 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 214 |
| ✅ EXACT | `Action_ComboBlock` | C | `13` | `13` | 215 | START | 215 | 266 |
| ✅ EXACT | `Action_ComboBlock` | RG | `4` | `4` | 215 | START | 215 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `6` | `6` | 215 | START | 215 | 251 |
| ✅ EXACT | `Action_ComboBlock` | LT | `7` | `7` | 215 | START | 215 | 266 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 266 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 103 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 163 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 180 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 295 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_ComboBlock` | 215 | 266 | 52 | inferred_complete_timeline |
| `Action_None` | 267 | 275 | 9 | inferred_complete_timeline |
| `Action_None` | 278 | 281 | 4 | inferred_complete_timeline |
| `Action_None` | 287 | 448 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 170 | 171 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 214 | 38 | inferred_complete_timeline |
| `Action_ComboBlock` | 215 | 251 | 37 | inferred_complete_timeline |
| `Action_ComboBlock` | 253 | 260 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–403
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 157 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 214 | 40 | inferred_complete_timeline |
| `Action_ComboBlock` | 215 | 266 | 52 | inferred_complete_timeline |
| `Action_None` | 267 | 324 | 58 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 343 | 12 | inferred_complete_timeline |
| `Action_None` | 345 | 403 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–437
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_ComboBlock` | 215 | 266 | 52 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |
| `Action_None` | 275 | 282 | 8 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 359 | 68 | inferred_complete_timeline |
| `Action_None` | 362 | 373 | 12 | inferred_complete_timeline |
| `Action_None` | 379 | 437 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 298 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 324 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 158 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 183 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 218 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 252 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 333 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–346
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 314 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 323 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 336 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 344 | 346 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 226 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 234 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 261 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 251 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 311 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 353 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–296
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 281 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 296 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 245 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 252 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 323 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 448 | 449 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 11–382 | 351 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 60–448 | 389 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 84–224 | 141 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 218–448 | 221 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 227–448 | 222 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 236–253 | 12 | 4 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 263–448 | 186 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 270–343 | 66 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 273–337 | 65 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 276–277 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 287–448 | 162 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 338–345 | 8 | 1 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 359–385 | 22 | 2 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 382–421 | 40 | 1 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 388–448 | 32 | 2 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 434–438 | 5 | 1 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 435–448 | 14 | 1 | Undefined position; Undefined team |
| `32` | `52` | Position_Unknown | Team_Unknown | 441–448 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 85 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 448 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-314] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-323] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-336] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-298] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-324] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-252] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-323] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [215-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-282] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-373] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-437] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [215-251] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [253-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-281] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-296] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-311] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-353] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-448] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-158] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-252] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-333] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-324] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-343] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-403] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-163] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-295] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-382] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-337] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-358] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-448] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-448] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-448] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-283] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-308] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-343] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-337] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-277] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-345] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-367] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-385] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-421] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-415] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-438] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [441-448] for track '32' has 1 frames without a visible bounding box.
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

</details>