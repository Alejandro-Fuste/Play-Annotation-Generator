# Play-Annotation-Generator Annotation Review — Duo_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_98`
- **Frame Range:** 0 to 418 (419 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 418
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | DT1 | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 366 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 3 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 18 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 18 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `21` | `Group` | 0 | START | 18 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `22` | `Group` | 0 | START | 18 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_ComboBlock` | DT1 | `14` | `14` | 289 | START | 289 | 333 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `15` | `15` | 289 | START | 289 | 328 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 355 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–391
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 36 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 53 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 179 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 391 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 18–36
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 26 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 36 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 18–418
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 50 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 355 | 302 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 364 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 414 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 416 | 418 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 18–123
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 72 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 123 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 18–95
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 95 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–411
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 80 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 288 | 205 | inferred_complete_timeline |
| `Action_ComboBlock` | 289 | 328 | 40 | inferred_complete_timeline |
| `Action_ComboBlock` | 333 | 353 | 21 | inferred_complete_timeline |
| `Action_None` | 360 | 397 | 38 | inferred_complete_timeline |
| `Action_None` | 399 | 405 | 7 | inferred_complete_timeline |
| `Action_None` | 407 | 411 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 366 | 367 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 381 | 319 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 18–418
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 418 | 401 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 325 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 347 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 358 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 91 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 288 | 180 | inferred_complete_timeline |
| `Action_ComboBlock` | 289 | 333 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 305 | 306 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 313 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 319 | 325 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 356 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 364 | 418 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 384 | 385 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 18–418
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 300 | 283 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 308 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 324 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 418 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 18–375
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 316 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 345 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 355 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 362 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 371 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 375 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `26`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `26`
- **team_side:** `defense`
- **Visible Frames:** 18–418
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 418 | 401 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–17 | 18 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–17 | 18 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–17 | 18 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–394 | 372 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–17 | 18 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–418 | 416 | 3 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–17 | 14 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 12–109 | 39 | 11 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 14–17 | 4 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 31–55 | 15 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 35–121 | 73 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 93–417 | 321 | 2 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 251–418 | 141 | 6 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 310–401 | 85 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 313–418 | 104 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 328–418 | 90 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 337–348 | 11 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 350–361 | 12 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 372–418 | 44 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 377–418 | 42 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 378–388 | 10 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 383–418 | 19 | 3 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 384–395 | 9 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 387–418 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `25` (actor_track_id `26`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 119 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-384] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-394] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-83] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-144] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-158] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-179] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-391] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-384] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-54] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-418] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-317] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-325] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-347] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-17] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-305] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-325] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-356] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-418] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-381] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-366] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-91] for track '14' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-288] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [289-333] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [289-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [333-353] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-397] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-405] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-411] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-23] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-72] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-89] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-355] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-364] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-414] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-345] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-355] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-362] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-371] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-375] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-324] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-36] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-50] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-36] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-121] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-387] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-417] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-418] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-340] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-401] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-395] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-416] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-344] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-361] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-383] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-418] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-418] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-383] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-388] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-385] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-388] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-388] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-395] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>