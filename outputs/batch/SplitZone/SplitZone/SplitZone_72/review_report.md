# Play-Annotation-Generator Annotation Review — SplitZone_72

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_72`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `24` | `19` |
| ✅ EXACT | `Action_SplitBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `0` | `Group` | 27 | START | 28 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 27 | START | 28 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 27 | START | 28 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 27 | START | 28 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 27 | START | 28 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 27 | START | 28 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 27 | START | 28 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 27 | START | 28 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 27 | START | 28 | 290 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `24` | `19` | 291 | START | 348 | 348 |
| ✅ EXACT | `Action_SplitBlock` | RT | `2` | `2` | 291 | START | 291 | 293 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `1` | 294 | START | 294 | 336 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 294 | START | 298 | 336 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 294 | START | 294 | 336 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 294 | START | 294 | 336 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 294 | START | 294 | 307 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 300 | END | 291 | 300 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `5` | `5` | 308 | START | 308 | 336 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `12` | 325 | START | 325 | 479 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 336 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 28–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_SnapReceive` | 291 | 300 | 10 | inferred_complete_timeline |
| `Action_None` | 301 | 324 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 325 | 479 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 28–362
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_None` | 291 | 350 | 60 | inferred_complete_timeline |
| `Action_None` | 353 | 362 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 28–346
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 125 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 290 | 163 | inferred_complete_timeline |
| `Action_None` | 291 | 346 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 28–359
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 165 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 290 | 123 | inferred_complete_timeline |
| `Action_None` | 291 | 359 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 28–373
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 293 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 294 | 307 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 308 | 336 | 29 | inferred_complete_timeline |
| `Action_None` | 337 | 373 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 28–367
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 180 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 202 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 293 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 294 | 336 | 43 | inferred_complete_timeline |
| `Action_None` | 337 | 367 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 28–357
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 216 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 225 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 289 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 298 | 336 | 39 | inferred_complete_timeline |
| `Action_None` | 337 | 353 | 17 | inferred_complete_timeline |
| `Action_None` | 356 | 357 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 28–365
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 230 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 293 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 294 | 336 | 43 | inferred_complete_timeline |
| `Action_None` | 337 | 365 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 28–361
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 143 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 244 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 290 | 42 | inferred_complete_timeline |
| `Action_SplitBlock` | 291 | 293 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 294 | 336 | 43 | inferred_complete_timeline |
| `Action_None` | 337 | 361 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 28–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_None` | 291 | 479 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 28–344
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_None` | 291 | 344 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 28–361
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 109 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 160 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 218 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 290 | 71 | inferred_complete_timeline |
| `Action_None` | 291 | 361 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 28–357
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_None` | 291 | 311 | 21 | inferred_complete_timeline |
| `Action_None` | 313 | 357 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 28–359
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_None` | 291 | 330 | 40 | inferred_complete_timeline |
| `Action_None` | 337 | 359 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 28–479
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 290 | 263 | inferred_complete_timeline |
| `Action_None` | 291 | 479 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 28–363
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 37 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 290 | 240 | inferred_complete_timeline |
| `Action_None` | 291 | 363 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 67–68 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 133–201 | 52 | 4 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 335–479 | 145 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 348–369 | 13 | 4 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 362–379 | 18 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 382–479 | 97 | 2 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 388–449 | 61 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 389–479 | 91 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 457–462 | 6 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 457–479 | 22 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 461–479 | 19 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 463–479 | 14 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 471–478 | 8 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 471–474 | 4 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 473–474 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `24` (Position_Unknown): Annotated start 291 != Inferred start 348
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 294 != Inferred start 298

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=348, end=300. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [28-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-290] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-359] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-367] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-361] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-230] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-330] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-359] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-373] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-125] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-346] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-479] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-344] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-350] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-362] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-311] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-357] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-225] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-116] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-125] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-160] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-361] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-30] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-37] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-290] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-363] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 349, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [349-349] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-369] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-379] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-472] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-446] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-462] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-476] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-470] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-478] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '30' has 1 frames without a visible bounding box.
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

</details>