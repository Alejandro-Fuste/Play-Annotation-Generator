# Play-Annotation-Generator Annotation Review — InsideZoneRead_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_82`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 363 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 392 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 363 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 363 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `10` | `9` | 364 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 364 | START | 364 | 422 |
| ✅ EXACT | `Action_ZoneBlock` | C | `10` | `9` | 364 | START | 364 | 449 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `6` | 364 | START | 364 | 422 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 373 | END | 364 | 373 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `2` | 378 | START | 378 | 390 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `2` | 391 | START | 391 | 396 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `1` | 397 | START | 397 | 458 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 452 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–396
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_SnapReceive` | 364 | 373 | 10 | inferred_complete_timeline |
| `Action_None` | 374 | 377 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 378 | 390 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 391 | 396 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–458
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 392 | 393 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 396 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 397 | 458 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 47 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 201 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 212 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 225 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 273 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 275 | 363 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 364 | 449 | 86 | inferred_complete_timeline |
| `Action_None` | 454 | 509 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_ZoneBlock` | 364 | 422 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 430 | 452 | 23 | inferred_complete_timeline |
| `Action_None` | 453 | 509 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 363 | 364 | inferred_complete_timeline |
| `Action_ZoneBlock` | 364 | 422 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 432 | 452 | 21 | inferred_complete_timeline |
| `Action_None` | 453 | 509 | 57 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 101–449
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 101 | 136 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 184 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 363 | 175 | inferred_complete_timeline |
| `Action_None` | 364 | 440 | 77 | inferred_complete_timeline |
| `Action_None` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `24`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 135–430
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 135 | 363 | 229 | inferred_complete_timeline |
| `Action_None` | 364 | 396 | 33 | inferred_complete_timeline |
| `Action_None` | 424 | 430 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `25`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 143–375
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 298 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 329 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 337 | 357 | 21 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 375 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `27`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `27`
- **team_side:** `defense`
- **Visible Frames:** 166–429
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 166 | 186 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 363 | 174 | inferred_complete_timeline |
| `Action_None` | 364 | 399 | 36 | inferred_complete_timeline |
| `Action_None` | 407 | 429 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 168 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 227 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 363 | 114 | inferred_complete_timeline |
| `Action_None` | 364 | 424 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–30 | 31 | 1 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–509 | 507 | 3 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–295 | 296 | 1 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–102 | 103 | 1 | Undefined position; Undefined team |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–89 | 87 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–266 | 267 | 1 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 5–38 | 29 | 2 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 6–169 | 143 | 2 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 38–70 | 33 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 78–158 | 80 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 108–126 | 18 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 149–173 | 15 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 309–509 | 189 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 387–459 | 72 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 395–471 | 75 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 402–485 | 80 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 421–431 | 6 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 439–491 | 53 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 445–474 | 30 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 450–509 | 51 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 454–498 | 45 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 480–509 | 30 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 480–509 | 21 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 485–493 | 9 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 494–509 | 16 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 498–509 | 12 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 506–509 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 166: Duplicate assignment for track ID '25' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Overlapping action conflict at frame 364 for track '9': 'Action_BallSnap' vs 'Action_ZoneBlock'. Overriding with 'Action_ZoneBlock'.
- ⚠️ Action 'Action_ZoneBlock' range [364-422] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-392] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [397-458] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [391-396] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-334] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [364-422] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-227] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-424] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-225] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [364-449] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-266] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-52] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-70] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-158] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-136] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-184] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-440] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-396] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-430] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-357] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-375] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-399] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-429] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-429] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-466] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-509] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-428] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-459] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-446] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-471] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-446] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-467] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-485] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-424] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-491] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-474] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-483] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-505] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-498] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-485] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-497] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-493] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>