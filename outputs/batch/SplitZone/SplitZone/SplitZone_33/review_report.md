# Play-Annotation-Generator Annotation Review — SplitZone_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_33`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 509
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 13 | START | 13 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 13 | START | 13 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 13 | START | 13 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 13 | START | 13 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 13 | START | 13 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 13 | START | 13 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 13 | START | 13 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 13 | START | 13 | 289 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 13 | START | 13 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 13 | START | 13 | 292 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 13 | START | 13 | 289 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 290 | START | 290 | 306 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 293 | START | 293 | 387 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 293 | START | 293 | 324 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 293 | START | 307 | 333 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 293 | START | 293 | 387 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `8` | 293 | START | 293 | 311 |
| ✅ EXACT | `Action_SplitBlock` | WR2 | `7` | `7` | 296 | START | 296 | 387 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 306 | END | 290 | 306 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 316 | START | 316 | 329 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 330 | START | 330 | 354 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 387 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–469
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_SnapReceive` | 290 | 306 | 17 | inferred_complete_timeline |
| `Action_None` | 307 | 315 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 316 | 329 | 14 | inferred_complete_timeline |
| `Action_None` | 330 | 469 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–509
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 329 | 317 | inferred_complete_timeline |
| `Action_BallCarry` | 330 | 354 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 356 | 503 | 148 | inferred_complete_timeline |
| `Action_BallCarry` | 506 | 509 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–451
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 451 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–414
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 295 | 283 | inferred_complete_timeline |
| `Action_SplitBlock` | 296 | 387 | 92 | inferred_complete_timeline |
| `Action_None` | 388 | 414 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–473
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 292 | 280 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 387 | 95 | inferred_complete_timeline |
| `Action_None` | 388 | 473 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–475
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 292 | 280 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 324 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 333 | 387 | 55 | inferred_complete_timeline |
| `Action_None` | 388 | 475 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–489
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_BallSnap` | 290 | 306 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 307 | 333 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 337 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 343 | 387 | 45 | inferred_complete_timeline |
| `Action_None` | 388 | 489 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–477
- **Visible Samples:** 464

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 292 | 280 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 311 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 313 | 387 | 75 | inferred_complete_timeline |
| `Action_None` | 388 | 477 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 292 | 280 | inferred_complete_timeline |
| `Action_ZoneBlock` | 293 | 387 | 95 | inferred_complete_timeline |
| `Action_None` | 388 | 509 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–498
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 498 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 337 | 48 | inferred_complete_timeline |
| `Action_None` | 342 | 362 | 21 | inferred_complete_timeline |
| `Action_None` | 364 | 509 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–483
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 320 | 31 | inferred_complete_timeline |
| `Action_None` | 324 | 327 | 4 | inferred_complete_timeline |
| `Action_None` | 337 | 347 | 11 | inferred_complete_timeline |
| `Action_None` | 349 | 483 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–356
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 356 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 13–469
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 381 | 92 | inferred_complete_timeline |
| `Action_None` | 386 | 424 | 39 | inferred_complete_timeline |
| `Action_None` | 430 | 447 | 18 | inferred_complete_timeline |
| `Action_None` | 459 | 461 | 3 | inferred_complete_timeline |
| `Action_None` | 463 | 469 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 13–489
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 489 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–463
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 388 | 99 | inferred_complete_timeline |
| `Action_None` | 399 | 405 | 7 | inferred_complete_timeline |
| `Action_None` | 413 | 414 | 2 | inferred_complete_timeline |
| `Action_None` | 422 | 463 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–509
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 289 | 277 | inferred_complete_timeline |
| `Action_None` | 290 | 509 | 220 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 309–314 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 317–318 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 318–356 | 6 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 348–352 | 4 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 400–466 | 58 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 404–405 | 2 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 443–445 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [290–306], lower_priority='Action_ZoneBlock' annotated_start=293, effective_Action_ZoneBlock_start=307.
- ⚠️ Action 'Action_None' range [290-451] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-320] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-327] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-347] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-483] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-473] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-388] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-405] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-463] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-414] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [293-311] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [313-387] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-477] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-354] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [356-503] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-498] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-469] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-356] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-381] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-424] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-447] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-469] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-337] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-362] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-509] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [293-324] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-475] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [307-333] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [335-337] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-489] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-489] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-409] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-466] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-405] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-445] for track '28' has 1 frames without a visible bounding box.
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

</details>