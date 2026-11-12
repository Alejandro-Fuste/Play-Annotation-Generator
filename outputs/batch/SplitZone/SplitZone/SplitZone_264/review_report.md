# Play-Annotation-Generator Annotation Review — SplitZone_264

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_264`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 509
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 140
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 11 | START | 11 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 11 | START | 13 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 11 | START | 30 | 183 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 11 | START | 55 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 11 | START | 136 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 11 | START | 11 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 11 | START | 11 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 11 | START | 11 | 57 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 184 | START | 184 | 366 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `14` | 184 | START | 184 | 366 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 184 | START | 184 | 303 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 184 | START | 184 | 294 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `9` | 184 | START | 193 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | Position_Unknown | `21` | `20` | 286 | START | 286 | 294 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 297 | END | 297 | 297 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 301 | START | 301 | 324 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `9` | `9` | 322 | START | 322 | 337 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `7` | 325 | START | 325 | 342 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 366 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 11–509
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 296 | 286 | inferred_complete_timeline |
| `Action_SnapReceive` | 297 | 297 | 1 | inferred_complete_timeline |
| `Action_None` | 298 | 300 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 301 | 324 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 325 | 342 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 385 | 509 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–386
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 323 | 311 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 386 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 136–365
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 136 | 179 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 301 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 335 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 365 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–446
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 115 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 183 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 294 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 319 | 323 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 331 | 366 | 36 | inferred_complete_timeline |
| `Action_None` | 367 | 446 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–506
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 57 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 180 | 112 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 210 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 235 | 274 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 282 | 321 | 40 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 322 | 337 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 344 | 352 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 359 | 366 | 8 | inferred_complete_timeline |
| `Action_None` | 367 | 421 | 55 | inferred_complete_timeline |
| `Action_None` | 426 | 440 | 15 | inferred_complete_timeline |
| `Action_None` | 460 | 464 | 5 | inferred_complete_timeline |
| `Action_None` | 467 | 506 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 30–493
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 183 | 154 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 366 | 183 | inferred_complete_timeline |
| `Action_None` | 367 | 493 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 55–303
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 55 | 76 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 183 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 303 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 11–509
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 59 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 183 | 105 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 366 | 183 | inferred_complete_timeline |
| `Action_None` | 367 | 449 | 83 | inferred_complete_timeline |
| `Action_None` | 453 | 493 | 41 | inferred_complete_timeline |
| `Action_None` | 498 | 509 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–488
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 131 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 251 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 488 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–345
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 108 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 345 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–509
- **Visible Samples:** 496

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 384 | 374 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 479 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 509 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–509
- **Visible Samples:** 460

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 20 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 99 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 360 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 489 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 509 | 509 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 32–509
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 355 | 324 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 418 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 442 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 445 | 509 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 11–384
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 316 | 306 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 384 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–316
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 316 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 11–495
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 42 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 458 | 415 | inferred_complete_timeline |
| `Action_PreSnap` | 493 | 495 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 11–507 | 470 | 9 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 11–79 | 59 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 93–110 | 18 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 113–123 | 11 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 273–323 | 50 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 318–321 | 4 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 324–509 | 172 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 333–503 | 164 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 348–509 | 157 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 358–507 | 150 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 373–480 | 89 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 376–377 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 399–431 | 33 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 402–509 | 108 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 408–509 | 96 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 426–509 | 84 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 452–455 | 4 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 452–509 | 58 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 465–468 | 4 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 476–509 | 30 | 3 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 479–509 | 31 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 501–509 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 183 frames exceeds threshold 90 frames [start=184, end=366].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 183 frames exceeds threshold 90 frames [start=184, end=366].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 138 frames exceeds threshold 90 frames [start=184, end=321].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 183 frames exceeds threshold 90 frames [start=184, end=366].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 120 frames exceeds threshold 90 frames [start=184, end=303].
- ⚠️ Action 'Action_PreSnap' range [11-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-366] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-449] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-493] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-245] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-345] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-393] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-404] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-417] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-427] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-507] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-42] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-458] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-495] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-384] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-479] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-509] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-488] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [319-323] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-446] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-316] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-384] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [325-342] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-26] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-316] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [235-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [322-337] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [344-352] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-421] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-440] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-464] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-506] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-345] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-24] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-360] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-489] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-323] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-386] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-366] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-493] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-355] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-418] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-442] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-303] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-110] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-301] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-335] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-365] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [286-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [296-323] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-349] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-386] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-408] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-503] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-353] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-507] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-480] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-431] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-420] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-485] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [490-509] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-455] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-509] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-468] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-502] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-506] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>