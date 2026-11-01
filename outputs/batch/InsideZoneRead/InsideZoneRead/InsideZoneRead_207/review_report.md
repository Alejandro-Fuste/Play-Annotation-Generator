# Play-Annotation-Generator Annotation Review — InsideZoneRead_207

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_207`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 31
- **Ball Tracks:** 2
- **Action Segments:** 106
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 458 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 294 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 261 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 456 | START | 456 | 470 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 459 | START | 459 | 544 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 459 | START | 471 | 483 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `12` | 459 | START | 459 | 488 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 459 | START | 459 | 541 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 459 | START | 459 | 527 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `11` | `10` | 470 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | QB | `11` | `10` | 479 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB | `11` | `10` | 505 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 544 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 294 | 295 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 355 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–498
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 455 | 188 | inferred_complete_timeline |
| `Action_None` | 456 | 498 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–558
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 458 | 459 | inferred_complete_timeline |
| `Action_ZoneBlock` | 459 | 544 | 86 | inferred_complete_timeline |
| `Action_None` | 545 | 558 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 271 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 316 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 341 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 458 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 459 | 488 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 509 | 544 | 36 | inferred_complete_timeline |
| `Action_None` | 545 | 629 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 612

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 455 | 373 | inferred_complete_timeline |
| `Action_BallSnap` | 456 | 470 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 471 | 483 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 501 | 544 | 44 | inferred_complete_timeline |
| `Action_None` | 545 | 629 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 458 | 385 | inferred_complete_timeline |
| `Action_ZoneBlock` | 459 | 527 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 529 | 533 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 536 | 537 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 541 | 544 | 4 | inferred_complete_timeline |
| `Action_None` | 545 | 629 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 620

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 458 | 390 | inferred_complete_timeline |
| `Action_ZoneBlock` | 459 | 541 | 83 | inferred_complete_timeline |
| `Action_None` | 549 | 551 | 3 | inferred_complete_timeline |
| `Action_None` | 554 | 629 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–555
- **Visible Samples:** 555

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 455 | 351 | inferred_complete_timeline |
| `Action_None` | 456 | 555 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 455 | 402 | inferred_complete_timeline |
| `Action_None` | 456 | 629 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 136 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 214 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 262 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 292 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 605

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 341 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 455 | 113 | inferred_complete_timeline |
| `Action_None` | 456 | 494 | 39 | inferred_complete_timeline |
| `Action_None` | 519 | 629 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–540
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 322 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 348 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 355 | 384 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 455 | 66 | inferred_complete_timeline |
| `Action_None` | 456 | 540 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 455 | 209 | inferred_complete_timeline |
| `Action_None` | 456 | 629 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–624
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 289 | 290 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 455 | 100 | inferred_complete_timeline |
| `Action_None` | 456 | 598 | 143 | inferred_complete_timeline |
| `Action_None` | 600 | 618 | 19 | inferred_complete_timeline |
| `Action_None` | 623 | 624 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 40–120 | 77 | 3 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 231–521 | 210 | 11 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 335–345 | 11 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 359–629 | 267 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 486–596 | 111 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 488–599 | 112 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 506–560 | 55 | 1 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 544–606 | 58 | 3 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 556–629 | 74 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 561–629 | 69 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 577–578 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 581–629 | 46 | 2 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 584–629 | 35 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 587–629 | 43 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 594–629 | 36 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 597–629 | 21 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 607–610 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | 499 | 499 | 1 | 100.0% | None |
| `32` | `47` | 621 | 621 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (6 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (QB)
- ❌ Missing segment for action `Action_ReadDefender` on target `11` (QB)
- ❌ Missing segment for action `Action_BallCarry` on target `11` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [456–470], lower_priority='Action_ZoneBlock' annotated_start=459, effective_Action_ZoneBlock_start=471.
- ⚠️ Segment 'Action_SnapReceive' for track '10' has invalid range: start=456, end=355. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '10' has invalid range: start=479, end=355. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '10' has invalid range: start=505, end=355. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-458] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-558] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-555] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-598] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-618] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-624] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-455] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-498] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [459-541] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-322] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-348] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-540] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [459-527] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [529-533] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [536-537] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [541-544] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [471-483] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-294] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-355] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-341] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-455] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-494] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-341] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [459-488] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-262] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-292] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-368] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-411] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-501] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-345] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-607] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-629] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-596] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-599] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-560] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-588] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-600] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-606] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-614] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-600] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-610] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>