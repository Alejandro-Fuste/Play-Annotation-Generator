# Play-Annotation-Generator Annotation Review — SplitZone_232

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_232`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 24 | START | 25 | 326 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 24 | START | 25 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 24 | START | 25 | 326 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 24 | START | 25 | 326 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 24 | START | 25 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 24 | START | 42 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 24 | START | 25 | 327 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 324 | START | 324 | 338 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 327 | START | 327 | 343 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 327 | START | 327 | 405 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `13` | 327 | START | 327 | 354 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 327 | START | 339 | 394 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 328 | START | 328 | 442 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 338 | END | 324 | 338 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 341 | START | 341 | 356 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `15` | 357 | START | 357 | 364 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 442 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 25–407
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_SnapReceive` | 324 | 338 | 15 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 341 | 356 | 16 | inferred_complete_timeline |
| `Action_None` | 357 | 374 | 18 | inferred_complete_timeline |
| `Action_None` | 377 | 390 | 14 | inferred_complete_timeline |
| `Action_None` | 393 | 407 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 42–479
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 75 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 219 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 356 | 125 | inferred_complete_timeline |
| `Action_BallCarry` | 357 | 364 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 366 | 479 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 327 | 303 | inferred_complete_timeline |
| `Action_SplitBlock` | 328 | 442 | 115 | inferred_complete_timeline |
| `Action_None` | 443 | 479 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 326 | 302 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 354 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 357 | 397 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 399 | 428 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 441 | 442 | 2 | inferred_complete_timeline |
| `Action_None` | 443 | 479 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 25–440
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 326 | 302 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 343 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 347 | 349 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 351 | 354 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 385 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 418 | 440 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 241 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 258 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 323 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 324 | 338 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 339 | 394 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 398 | 442 | 45 | inferred_complete_timeline |
| `Action_None` | 443 | 457 | 15 | inferred_complete_timeline |
| `Action_None` | 461 | 468 | 8 | inferred_complete_timeline |
| `Action_None` | 470 | 479 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 25–479
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 326 | 302 | inferred_complete_timeline |
| `Action_ZoneBlock` | 327 | 405 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 407 | 417 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 423 | 426 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 428 | 440 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 442 | 442 | 1 | inferred_complete_timeline |
| `Action_None` | 443 | 462 | 20 | inferred_complete_timeline |
| `Action_None` | 464 | 479 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 64 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 323 | 246 | inferred_complete_timeline |
| `Action_None` | 324 | 348 | 25 | inferred_complete_timeline |
| `Action_None` | 353 | 399 | 47 | inferred_complete_timeline |
| `Action_None` | 404 | 428 | 25 | inferred_complete_timeline |
| `Action_None` | 430 | 479 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 25–405
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 62 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 137 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 160 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 224 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 323 | 98 | inferred_complete_timeline |
| `Action_None` | 324 | 389 | 66 | inferred_complete_timeline |
| `Action_None` | 391 | 405 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_None` | 324 | 425 | 102 | inferred_complete_timeline |
| `Action_None` | 428 | 479 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 25–461
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_None` | 324 | 420 | 97 | inferred_complete_timeline |
| `Action_None` | 426 | 461 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 25–432
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_None` | 324 | 432 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_None` | 324 | 479 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 25–361
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_None` | 324 | 361 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 25–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 323 | 299 | inferred_complete_timeline |
| `Action_None` | 324 | 479 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 25–338 | 307 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 126–144 | 18 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 134–150 | 17 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 258–278 | 5 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 337–385 | 34 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 382–461 | 68 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 383–479 | 97 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 387–479 | 93 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 392–452 | 61 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 399–477 | 76 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 406–407 | 2 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 406–479 | 73 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 424–428 | 5 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 427–431 | 5 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 433–479 | 47 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 443–479 | 37 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 457–479 | 23 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 466–479 | 14 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 474–479 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 114 frames exceeds threshold 90 frames [start=327, end=440].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (RG) duration 116 frames exceeds threshold 90 frames [start=327, end=442].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 116 frames exceeds threshold 90 frames [start=327, end=442].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 116 frames exceeds threshold 90 frames [start=327, end=442].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [324–338], lower_priority='Action_ZoneBlock' annotated_start=327, effective_Action_ZoneBlock_start=339.
- ⚠️ Action 'Action_None' range [324-361] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-343] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [347-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [351-354] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [363-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [418-440] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-348] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-399] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-428] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-137] for track '4' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-224] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-323] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-405] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-327] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-432] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-142] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-323] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-338] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-420] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-461] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-374] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-390] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-407] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-425] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-405] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [407-417] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [423-426] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [428-440] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 443, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [443-462] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [327-354] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [357-397] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [399-428] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-479] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-29] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-258] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-323] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [339-394] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [398-442] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-457] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-75] for track '15' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [357-364] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-150] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-348] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-362] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-385] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-438] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-447] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-461] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-479] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-479] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-452] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-459] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-477] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-436] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-431] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>