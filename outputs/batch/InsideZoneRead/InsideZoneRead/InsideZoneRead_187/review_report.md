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
- **Action Segments:** 81
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
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
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `18` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `21` | `18` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | Team_Unknown | `21` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 3 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 3 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 3 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 3 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 3 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 3 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 3 | START | 0 | 5 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 4 | START | 346 | 346 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 6 | START | 6 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 6 | START | 6 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `15` | 6 | START | 6 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 6 | START | 6 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 6 | START | 6 | 80 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `21` | `18` | 18 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `21` | `18` | 23 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | Position_Unknown | `22` | `19` | 24 | START | 374 | 374 |
| ❌ MISSING SEGMENT | `Action_Handoff` | Position_Unknown | `21` | `18` | 38 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `18` | 47 | START | 356 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 80 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 362 | 359 | inferred_complete_timeline |
| `Action_None` | 367 | 448 | 82 | inferred_complete_timeline |
| `Action_None` | 450 | 452 | 3 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 479 | 476 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 80 | 75 | inferred_complete_timeline |
| `Action_None` | 81 | 371 | 291 | inferred_complete_timeline |
| `Action_None` | 376 | 448 | 73 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 80 | 75 | inferred_complete_timeline |
| `Action_None` | 81 | 479 | 399 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 80 | 75 | inferred_complete_timeline |
| `Action_None` | 81 | 471 | 391 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 80 | 75 | inferred_complete_timeline |
| `Action_None` | 81 | 464 | 384 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 80 | 75 | inferred_complete_timeline |
| `Action_None` | 81 | 367 | 287 | inferred_complete_timeline |
| `Action_None` | 369 | 479 | 111 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 394 | 391 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 425 | 422 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 126 | 123 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 343 | 209 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 334 | 331 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 133 | 130 | inferred_complete_timeline |
| `Action_None` | 139 | 374 | 236 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 132 | 129 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 153 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 384 | 230 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 479 | 476 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 343 | 340 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 422 | 419 | inferred_complete_timeline |
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
| `17` | `20` | Position_Unknown | Team_Unknown | 346–479 | 134 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 356–385 | 16 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 374–479 | 106 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 409–479 | 63 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 411–479 | 69 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 417–421 | 5 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 418–479 | 55 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 4 != Inferred start 346
- ❌ Missing segment for action `Action_SnapReceive` on target `18` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `18` (Position_Unknown)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `22` (Position_Unknown): Annotated start 24 != Inferred start 374
- ❌ Missing segment for action `Action_Handoff` on target `18` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=346, end=18. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '18' has invalid range: start=356, end=18. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '18' has invalid range: start=356, end=37. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '18' has invalid range: start=356, end=46. Clamping end to start.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '19' has invalid range: start=374, end=80. Clamping end to start.
- ⚠️ Action 'Action_None' range [81-367] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-448] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-452] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-371] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-448] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-425] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-390] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-132] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-431] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-437] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-464] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-394] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-422] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-438] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-448] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-458] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-461] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-374] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-334] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-479] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-126] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-343] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-399] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-471] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [356-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [368-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [383-385] for track '18' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_187'; source metadata written as null.

</details>