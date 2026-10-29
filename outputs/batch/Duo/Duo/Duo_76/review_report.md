# Play-Annotation-Generator Annotation Review — Duo_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_76`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 28
- **Ball Tracks:** 2
- **Action Segments:** 81
- **Validation Warnings:** 84
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | TE | offense | `22` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `21` | `Group` | 0 | START | 13 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 0 | START | 25 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 325 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 307 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `6` | `6` | 275 | START | 275 | 311 |
| ✅ EXACT | `Action_ComboBlock` | LG | `11` | `11` | 275 | START | 275 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `15` | `15` | 275 | START | 275 | 283 |
| ✅ EXACT | `Action_ComboBlock` | TE | `22` | `18` | 275 | START | 275 | 307 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RB | `5` | `5` | 275 | START | 275 | 308 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 311 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–358
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 358 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 308 | 34 | inferred_complete_timeline |
| `Action_ComboBlock` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 314 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `21`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–358
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 27 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 358 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 25–355
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 274 | 250 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 307 | 33 | inferred_complete_timeline |
| `Action_None` | 318 | 328 | 11 | inferred_complete_timeline |
| `Action_None` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |
| `Action_None` | 353 | 355 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 358 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 264 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 274 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 311 | 37 | inferred_complete_timeline |
| `Action_None` | 312 | 330 | 19 | inferred_complete_timeline |
| `Action_None` | 334 | 347 | 14 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 275 | 311 | 37 | inferred_complete_timeline |
| `Action_None` | 312 | 357 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–333
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 162 | 163 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 215 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 226 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 268 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 274 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 283 | 9 | inferred_complete_timeline |
| `Action_ComboBlock` | 286 | 304 | 19 | inferred_complete_timeline |
| `Action_None` | 326 | 327 | 2 | inferred_complete_timeline |
| `Action_None` | 331 | 333 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 307 | 308 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 333 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 308 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 314 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `23`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 26–92
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 56 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 86 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 92 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 235 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 358 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 337 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–306
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 298 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 306 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–26 | 27 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 138–242 | 75 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 162–358 | 186 | 5 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 229–358 | 130 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 240–358 | 95 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 282–358 | 77 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 307–312 | 6 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 313–358 | 45 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 340–355 | 16 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | 0 | 82 | 32 | 38.6% | 7–12, 15–23, 27–57, 65, 72–75 |
| `22` | `28` | 184 | 244 | 26 | 42.6% | 185–186, 201–203, 205–212, 217, 219–221, 225–242 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 63 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-337] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [275-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-357] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-307] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-317] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-333] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-308] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-306] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-264] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-330] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-347] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-162] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-215] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-226] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-268] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [275-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [286-304] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-327] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [275-307] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-328] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-56] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-86] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-215] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-306] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-316] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-333] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-350] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-312] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-318] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>