# Play-Annotation-Generator Annotation Review — SplitZone_257

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_257`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 509
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `24` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 14 | START | 17 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 14 | START | 17 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 14 | START | 17 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 14 | START | 17 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 14 | START | 17 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `24` | `Group` | 14 | START | 67 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 14 | START | 17 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 14 | START | 17 | 350 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 14 | START | 17 | 331 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 14 | START | 17 | 314 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 315 | START | 315 | 319 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 318 | START | 318 | 418 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `15` | 318 | START | 320 | 418 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `19` | 318 | START | 318 | 346 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `24` | `21` | 318 | START | 318 | 371 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 319 | END | 315 | 319 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `6` | `6` | 332 | START | 332 | 370 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 339 | START | 339 | 350 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `19` | `19` | 347 | START | 347 | 404 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 351 | START | 351 | 434 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 418 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 17–381
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_SnapReceive` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_None` | 320 | 338 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 339 | 350 | 12 | inferred_complete_timeline |
| `Action_None` | 351 | 381 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 17–434
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 350 | 334 | inferred_complete_timeline |
| `Action_BallCarry` | 351 | 434 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 17–434
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 434 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 17–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 509 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 17–434
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 434 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 17–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 331 | 315 | inferred_complete_timeline |
| `Action_SplitBlock` | 332 | 370 | 39 | inferred_complete_timeline |
| `Action_SplitBlock` | 373 | 418 | 46 | inferred_complete_timeline |
| `Action_None` | 419 | 509 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 17–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 317 | 301 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 418 | 101 | inferred_complete_timeline |
| `Action_None` | 419 | 509 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 17–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_BallSnap` | 315 | 319 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 320 | 418 | 99 | inferred_complete_timeline |
| `Action_None` | 419 | 509 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 67–371
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 67 | 317 | 251 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 371 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 17–434
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 317 | 301 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 346 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 347 | 404 | 58 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 417 | 418 | 2 | inferred_complete_timeline |
| `Action_None` | 419 | 434 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 17–434
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 361 | 47 | inferred_complete_timeline |
| `Action_None` | 363 | 434 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 17–487
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 487 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 27–499
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 314 | 288 | inferred_complete_timeline |
| `Action_None` | 315 | 349 | 35 | inferred_complete_timeline |
| `Action_None` | 352 | 353 | 2 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |
| `Action_None` | 363 | 434 | 72 | inferred_complete_timeline |
| `Action_None` | 466 | 499 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 17–509
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 434 | 120 | inferred_complete_timeline |
| `Action_None` | 447 | 509 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 17–469
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 369 | 55 | inferred_complete_timeline |
| `Action_None` | 374 | 385 | 12 | inferred_complete_timeline |
| `Action_None` | 387 | 388 | 2 | inferred_complete_timeline |
| `Action_None` | 391 | 401 | 11 | inferred_complete_timeline |
| `Action_None` | 409 | 469 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 17–509
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 466 | 152 | inferred_complete_timeline |
| `Action_None` | 473 | 509 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 17–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 509 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 17–434
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 434 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 17–482
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 56 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 314 | 238 | inferred_complete_timeline |
| `Action_None` | 315 | 349 | 35 | inferred_complete_timeline |
| `Action_None` | 353 | 363 | 11 | inferred_complete_timeline |
| `Action_None` | 368 | 374 | 7 | inferred_complete_timeline |
| `Action_None` | 376 | 482 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 17–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 314 | 298 | inferred_complete_timeline |
| `Action_None` | 315 | 509 | 195 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 17–509 | 476 | 5 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 17–509 | 493 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 385–392 | 8 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 401–483 | 83 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 435–447 | 13 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 435–509 | 75 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 435–509 | 66 | 4 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 486–490 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 318 != Inferred start 320
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 516: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 101 frames exceeds threshold 90 frames [start=318, end=418].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 101 frames exceeds threshold 90 frames [start=318, end=418].
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [315–319], lower_priority='Action_ZoneBlock' annotated_start=318, effective_Action_ZoneBlock_start=320.
- ⚠️ Action 'Action_None' range [315-487] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-375] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-434] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [351-434] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [332-370] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-381] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-369] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-385] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-401] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-469] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-56] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-349] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-363] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-374] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-482] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-361] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-434] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-466] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-509] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [318-418] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-434] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-434] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-434] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [347-404] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-434] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-349] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-434] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-499] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [318-371] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-392] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-483] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-447] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-475] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-494] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-490] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>