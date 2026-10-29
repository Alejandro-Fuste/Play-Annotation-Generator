# Play-Annotation-Generator Annotation Review — Duo_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_134`
- **Frame Range:** 0 to 418 (419 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 418
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 132
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
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 302 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 282 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 256 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 356 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 418 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | Position_Unknown | `18` | `18` | 265 | START | 265 | 270 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `11` | `11` | 291 | START | 291 | 304 |
| ✅ EXACT | `Action_ComboBlock` | LT | `12` | `12` | 291 | START | 291 | 311 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RG | `15` | `15` | 291 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `18` | `18` | 291 | START | 291 | 302 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 311 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 177 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 302 | 303 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 325 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–405
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 282 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 335 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 339 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 356 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 405 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 356 | 357 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 418 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |
| `Action_ComboBlock` | 291 | 311 | 21 | inferred_complete_timeline |
| `Action_None` | 312 | 330 | 19 | inferred_complete_timeline |
| `Action_None` | 338 | 352 | 15 | inferred_complete_timeline |
| `Action_None` | 358 | 372 | 15 | inferred_complete_timeline |
| `Action_None` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_None` | 380 | 406 | 27 | inferred_complete_timeline |
| `Action_None` | 408 | 418 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 258 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 342 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 411 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 416 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 418 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–379
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 290 | 291 | inferred_complete_timeline |
| `Action_ComboBlock` | 291 | 304 | 14 | inferred_complete_timeline |
| `Action_ComboBlock` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 317 | 6 | inferred_complete_timeline |
| `Action_None` | 321 | 345 | 25 | inferred_complete_timeline |
| `Action_None` | 354 | 373 | 20 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 256 | 257 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 281 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–370
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 288 | 289 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 418 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–370
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 281 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 293 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 335 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 339 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 351 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 370 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 387 | 355 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 418 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 318 | 319 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 344 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 415 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 418 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 104 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 109 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 317 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 373 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 386 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 388 | 418 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 19–418 | 369 | 15 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 132–306 | 164 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 165–258 | 11 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 238–401 | 147 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 267–399 | 131 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 268–378 | 53 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 278–418 | 118 | 6 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 282–418 | 136 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 329–418 | 85 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 332–333 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 340–383 | 41 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 367–403 | 37 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 379–415 | 34 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 380–418 | 39 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 406–414 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_ComboBlock` on target `15` (RG)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '15' has invalid range: start=291, end=281. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-104] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-317] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-373] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-386] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-288] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-370] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-318] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-344] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-415] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-356] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-281] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-293] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-335] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-351] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-370] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-302] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [291-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [307-308] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-345] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-373] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [291-311] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-330] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-352] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-372] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-406] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-282] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-335] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-339] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-356] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-405] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-258] for track '14' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-342] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-411] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-416] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-281] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-387] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-165] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-111] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-169] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-186] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-230] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-264] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [265-270] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [283-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [291-302] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-161] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-170] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-364] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-370] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-336] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-399] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-282] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-315] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-322] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-394] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-400] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-418] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-376] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-408] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-378] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-403] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-384] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-415] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-414] for track '32' has 2 frames without a visible bounding box.
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