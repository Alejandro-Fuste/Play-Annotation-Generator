# Play-Annotation-Generator Annotation Review — SplitZone_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_78`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 14 | START | 15 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 14 | START | 15 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 14 | START | 15 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 14 | START | 15 | 286 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 14 | START | 15 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 14 | START | 15 | 283 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 14 | START | 15 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 284 | START | 284 | 301 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 287 | START | 287 | 371 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `12` | `12` | 287 | START | 302 | 371 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `2` | `2` | 287 | START | 287 | 371 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 287 | START | 287 | 371 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 292 | START | 292 | 371 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 301 | END | 284 | 301 |
| ✅ EXACT | `Action_BallCarry` | QB | `8` | `8` | 327 | START | 327 | 474 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 371 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 15–474
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 283 | 234 | inferred_complete_timeline |
| `Action_SnapReceive` | 284 | 301 | 18 | inferred_complete_timeline |
| `Action_None` | 302 | 326 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 327 | 474 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 15–408
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 326 | 43 | inferred_complete_timeline |
| `Action_None` | 406 | 408 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 291 | 277 | inferred_complete_timeline |
| `Action_SplitBlock` | 292 | 371 | 80 | inferred_complete_timeline |
| `Action_None` | 372 | 479 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 286 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 371 | 85 | inferred_complete_timeline |
| `Action_None` | 372 | 479 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–464
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_BallSnap` | 284 | 301 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 371 | 70 | inferred_complete_timeline |
| `Action_None` | 372 | 413 | 42 | inferred_complete_timeline |
| `Action_None` | 415 | 464 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 286 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 371 | 85 | inferred_complete_timeline |
| `Action_None` | 372 | 479 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 286 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 287 | 371 | 85 | inferred_complete_timeline |
| `Action_None` | 372 | 479 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 314 | 31 | inferred_complete_timeline |
| `Action_None` | 331 | 345 | 15 | inferred_complete_timeline |
| `Action_None` | 347 | 350 | 4 | inferred_complete_timeline |
| `Action_None` | 354 | 357 | 4 | inferred_complete_timeline |
| `Action_None` | 368 | 479 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 479 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 15–323
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 323 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 15–412
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 295 | 12 | inferred_complete_timeline |
| `Action_None` | 301 | 412 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 15–416
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 391 | 108 | inferred_complete_timeline |
| `Action_None` | 393 | 416 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 15–405
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 405 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 15–479
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 224 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 283 | 34 | inferred_complete_timeline |
| `Action_None` | 284 | 383 | 100 | inferred_complete_timeline |
| `Action_None` | 388 | 479 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 15–415
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 283 | 269 | inferred_complete_timeline |
| `Action_None` | 284 | 348 | 65 | inferred_complete_timeline |
| `Action_None` | 350 | 373 | 24 | inferred_complete_timeline |
| `Action_None` | 381 | 384 | 4 | inferred_complete_timeline |
| `Action_None` | 398 | 405 | 8 | inferred_complete_timeline |
| `Action_None` | 408 | 415 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 15–308 | 272 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 40–43 | 4 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 320–479 | 159 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 332–408 | 77 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 346–415 | 15 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 362–479 | 107 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 369–479 | 111 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 388–479 | 92 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 421–479 | 59 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 434–479 | 46 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 434–464 | 31 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 437–473 | 37 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 440–451 | 4 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 452–468 | 17 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 463–479 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `12` (C): Annotated start 287 != Inferred start 302

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 158: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [284–301], lower_priority='Action_ZoneBlock' annotated_start=287, effective_Action_ZoneBlock_start=302.
- ⚠️ Action 'Action_PreSnap' range [15-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-383] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-479] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [287-371] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-348] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-373] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-405] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-415] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [292-371] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-326] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-47] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-474] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-314] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-345] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-350] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-323] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-391] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-416] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-413] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-464] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-295] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-412] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-223] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-405] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-438] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-479] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-408] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-352] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-357] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-415] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-457] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-471] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-464] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-473] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-468] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>