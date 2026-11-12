# Play-Annotation-Generator Annotation Review — SplitZone_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_68`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 65
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 8
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 21 | START | 22 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 21 | START | 22 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 21 | START | 22 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 21 | START | 22 | 284 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 21 | START | 22 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 21 | START | 22 | 284 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 21 | START | 22 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 21 | START | 22 | 287 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 285 | START | 285 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `0` | `0` | 288 | START | 288 | 349 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 288 | START | 288 | 369 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 288 | START | 288 | 369 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 288 | START | 288 | 369 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `4` | 288 | START | 300 | 344 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 288 | START | 288 | 303 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 299 | END | 285 | 299 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `7` | `7` | 304 | START | 304 | 369 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 304 | START | 304 | 319 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 320 | START | 320 | 476 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 369 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 22–400
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_SnapReceive` | 285 | 299 | 15 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 304 | 319 | 16 | inferred_complete_timeline |
| `Action_None` | 321 | 400 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–476
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 319 | 298 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 476 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–391
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 287 | 266 | inferred_complete_timeline |
| `Action_SplitBlock` | 288 | 349 | 62 | inferred_complete_timeline |
| `Action_SplitBlock` | 353 | 369 | 17 | inferred_complete_timeline |
| `Action_None` | 370 | 391 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–421
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 287 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 288 | 369 | 82 | inferred_complete_timeline |
| `Action_None` | 370 | 421 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–431
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 287 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 288 | 303 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 304 | 369 | 66 | inferred_complete_timeline |
| `Action_None` | 370 | 404 | 35 | inferred_complete_timeline |
| `Action_None` | 409 | 431 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 22–355
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_BallSnap` | 285 | 299 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 300 | 344 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 348 | 355 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 22–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 287 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 288 | 369 | 82 | inferred_complete_timeline |
| `Action_None` | 370 | 419 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 22–422
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 287 | 266 | inferred_complete_timeline |
| `Action_ZoneBlock` | 288 | 369 | 82 | inferred_complete_timeline |
| `Action_None` | 370 | 422 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–432
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_None` | 285 | 432 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 96–268
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 96 | 268 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–459
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_None` | 285 | 459 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–424
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_None` | 285 | 348 | 64 | inferred_complete_timeline |
| `Action_None` | 360 | 364 | 5 | inferred_complete_timeline |
| `Action_None` | 368 | 380 | 13 | inferred_complete_timeline |
| `Action_None` | 382 | 392 | 11 | inferred_complete_timeline |
| `Action_None` | 395 | 424 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 22–377
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_None` | 285 | 377 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–433
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 284 | 263 | inferred_complete_timeline |
| `Action_None` | 285 | 335 | 51 | inferred_complete_timeline |
| `Action_None` | 338 | 355 | 18 | inferred_complete_timeline |
| `Action_None` | 357 | 433 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–50
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 50 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 22–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 70 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 284 | 212 | inferred_complete_timeline |
| `Action_None` | 285 | 479 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 22–479 | 458 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 331–470 | 140 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 340–375 | 36 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 352–358 | 7 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 355–479 | 125 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 362–415 | 54 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 383–407 | 25 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 385–479 | 90 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 386–455 | 70 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 387–392 | 6 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 405–406 | 2 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 459–464 | 6 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 293 | 293 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [285–299], lower_priority='Action_ZoneBlock' annotated_start=288, effective_Action_ZoneBlock_start=300.
- ⚠️ Action 'Action_SplitBlock' range [288-349] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-391] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [288-369] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-421] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-422] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-377] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [300-344] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [348-355] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '5' starts at frame 320, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [320-476] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-404] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-431] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-459] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-432] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [288-369] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-335] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-433] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [304-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-400] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-348] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-364] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-380] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-392] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-424] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-70] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-268] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-470] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-375] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-358] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-415] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-407] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-467] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-455] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-392] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-464] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>