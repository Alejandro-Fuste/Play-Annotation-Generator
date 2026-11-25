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
- **Action Segments:** 109
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
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
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `17` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `20` | `17` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `20` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 50 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `19` | 49 | START | 488 | 488 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 51 | START | 51 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 51 | START | 51 | 81 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `12` | 51 | START | 51 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 51 | START | 51 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `9` | `8` | 51 | START | 51 | 72 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `20` | `17` | 61 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `20` | `17` | 63 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `20` | `17` | 75 | START | 359 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `15` | 84 | START | 231 | 234 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 110 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 294 | 246 | inferred_complete_timeline |
| `Action_None` | 296 | 355 | 60 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 261 | 213 | inferred_complete_timeline |
| `Action_None` | 268 | 498 | 231 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 110 | 60 | inferred_complete_timeline |
| `Action_None` | 111 | 558 | 448 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 110 | 60 | inferred_complete_timeline |
| `Action_None` | 111 | 239 | 129 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 271 | 9 | inferred_complete_timeline |
| `Action_None` | 273 | 277 | 5 | inferred_complete_timeline |
| `Action_None` | 292 | 316 | 25 | inferred_complete_timeline |
| `Action_None` | 334 | 341 | 8 | inferred_complete_timeline |
| `Action_None` | 348 | 488 | 141 | inferred_complete_timeline |
| `Action_None` | 509 | 629 | 121 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 110 | 28 | inferred_complete_timeline |
| `Action_None` | 111 | 483 | 373 | inferred_complete_timeline |
| `Action_None` | 501 | 629 | 129 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 72 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 110 | 37 | inferred_complete_timeline |
| `Action_None` | 111 | 527 | 417 | inferred_complete_timeline |
| `Action_None` | 529 | 533 | 5 | inferred_complete_timeline |
| `Action_None` | 536 | 537 | 2 | inferred_complete_timeline |
| `Action_None` | 541 | 629 | 89 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 110 | 42 | inferred_complete_timeline |
| `Action_None` | 111 | 541 | 431 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 105 | 555 | 451 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 54 | 629 | 576 | inferred_complete_timeline |

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
| `Action_None` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 100 | 136 | 37 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_None` | 158 | 214 | 57 | inferred_complete_timeline |
| `Action_None` | 216 | 262 | 47 | inferred_complete_timeline |
| `Action_None` | 271 | 292 | 22 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 341 | 293 | inferred_complete_timeline |
| `Action_None` | 343 | 494 | 152 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 313 | 265 | inferred_complete_timeline |
| `Action_None` | 316 | 322 | 7 | inferred_complete_timeline |
| `Action_None` | 329 | 348 | 20 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |
| `Action_None` | 355 | 384 | 30 | inferred_complete_timeline |
| `Action_None` | 390 | 540 | 151 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 244 | 196 | inferred_complete_timeline |
| `Action_None` | 247 | 629 | 383 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 289 | 241 | inferred_complete_timeline |
| `Action_None` | 356 | 598 | 243 | inferred_complete_timeline |
| `Action_None` | 600 | 618 | 19 | inferred_complete_timeline |
| `Action_None` | 623 | 624 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 40–120 | 77 | 4 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 231–521 | 210 | 11 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 335–345 | 11 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 359–629 | 267 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 486–596 | 111 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 488–599 | 112 | 2 | Undefined position; Undefined team |
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

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 49 != Inferred start 488
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `20` (Position_Unknown)
- ⚠️ `Action_Handoff` for actor_track_id `20` (Position_Unknown): Annotated start 75 != Inferred start 359
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (11 segments found)

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
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=359, end=61. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '17' has invalid range: start=359, end=74. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '17' has invalid range: start=359, end=83. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=488, end=61. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [51-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-558] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-555] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-598] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [600-618] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-624] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-261] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-498] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-67] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-541] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-313] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-322] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-348] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-384] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-540] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-72] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-527] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-533] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-629] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-483] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-294] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-355] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-341] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-494] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-271] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-341] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-488] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-262] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-292] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [247-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [292-368] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [376-411] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [417-445] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [459-462] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [471-501] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [519-521] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-345] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-607] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-629] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-596] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-599] for track '19' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_207'; source metadata written as null.

</details>