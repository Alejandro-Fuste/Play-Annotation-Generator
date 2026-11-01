# Play-Annotation-Generator Annotation Review — InsideZoneRead_187

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_187`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 327 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 327 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 325 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 325 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 362 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 327 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 327 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 326 | START | 326 | 335 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 328 | START | 328 | 367 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 328 | START | 328 | 393 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `16` | `15` | 328 | START | 336 | 393 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `3` | 328 | START | 328 | 371 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 328 | START | 328 | 393 |
| ✅ EXACT | `Action_SnapReceive` | RB | `2` | `1` | 335 | END | 326 | 335 |
| ✅ EXACT | `Action_ReadDefender` | RB | `2` | `1` | 340 | START | 340 | 354 |
| ✅ EXACT | `Action_Handoff` | RB | `2` | `1` | 355 | START | 355 | 367 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `3` | `2` | 368 | START | 368 | 448 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 393 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–452
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 362 | 363 | inferred_complete_timeline |
| `Action_PreSnap` | 367 | 367 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 368 | 448 | 81 | inferred_complete_timeline |
| `Action_BallCarry` | 450 | 452 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_SnapReceive` | 326 | 335 | 10 | inferred_complete_timeline |
| `Action_None` | 336 | 339 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 340 | 354 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 355 | 367 | 13 | inferred_complete_timeline |
| `Action_None` | 368 | 479 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 371 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 376 | 393 | 18 | inferred_complete_timeline |
| `Action_None` | 394 | 448 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 393 | 66 | inferred_complete_timeline |
| `Action_None` | 394 | 479 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_BallSnap` | 326 | 335 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 336 | 393 | 58 | inferred_complete_timeline |
| `Action_None` | 394 | 471 | 78 | inferred_complete_timeline |
| `Action_None` | 473 | 479 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 393 | 66 | inferred_complete_timeline |
| `Action_None` | 394 | 464 | 71 | inferred_complete_timeline |
| `Action_None` | 474 | 479 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 327 | 328 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 367 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 369 | 393 | 25 | inferred_complete_timeline |
| `Action_None` | 394 | 479 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_None` | 326 | 394 | 69 | inferred_complete_timeline |
| `Action_None` | 397 | 479 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_None` | 326 | 425 | 100 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 325 | 191 | inferred_complete_timeline |
| `Action_None` | 326 | 343 | 18 | inferred_complete_timeline |
| `Action_None` | 351 | 399 | 49 | inferred_complete_timeline |
| `Action_None` | 406 | 479 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_None` | 326 | 334 | 9 | inferred_complete_timeline |
| `Action_None` | 383 | 479 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 325 | 187 | inferred_complete_timeline |
| `Action_None` | 326 | 374 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 325 | 171 | inferred_complete_timeline |
| `Action_None` | 326 | 384 | 59 | inferred_complete_timeline |
| `Action_None` | 418 | 431 | 14 | inferred_complete_timeline |
| `Action_None` | 436 | 437 | 2 | inferred_complete_timeline |
| `Action_None` | 442 | 479 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_None` | 326 | 479 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_None` | 326 | 343 | 18 | inferred_complete_timeline |
| `Action_None` | 352 | 390 | 39 | inferred_complete_timeline |
| `Action_None` | 392 | 479 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–461
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 325 | 326 | inferred_complete_timeline |
| `Action_None` | 326 | 422 | 97 | inferred_complete_timeline |
| `Action_None` | 426 | 438 | 13 | inferred_complete_timeline |
| `Action_None` | 440 | 448 | 9 | inferred_complete_timeline |
| `Action_None` | 450 | 458 | 9 | inferred_complete_timeline |
| `Action_None` | 460 | 461 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 89–92 | 4 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 346–479 | 134 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 356–385 | 16 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 374–479 | 106 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 409–479 | 63 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 411–479 | 69 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 417–421 | 5 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 418–479 | 55 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `16` (C): Annotated start 328 != Inferred start 336
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 45 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [326–335], lower_priority='Action_ZoneBlock' annotated_start=328, effective_Action_ZoneBlock_start=336.
- ⚠️ Action 'Action_ZoneBlock' range [328-367] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [368-448] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [450-452] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [328-371] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-448] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-425] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-390] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-431] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-464] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-394] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-422] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-438] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-448] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-458] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-374] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-334] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-479] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-343] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-399] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-471] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-429] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-446] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-468] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-421] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-426] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-466] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-479] for track '23' has 1 frames without a visible bounding box.
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

</details>