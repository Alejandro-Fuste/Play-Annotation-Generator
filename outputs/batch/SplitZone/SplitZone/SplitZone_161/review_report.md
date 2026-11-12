# Play-Annotation-Generator Annotation Review — SplitZone_161

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_161`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | WR3 | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 2 | START | 3 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 2 | START | 3 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 2 | START | 3 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 2 | START | 3 | 319 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 2 | START | 3 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 2 | START | 3 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 2 | START | 3 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 2 | START | 3 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 2 | START | 3 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 2 | START | 6 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 2 | START | 3 | 315 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 313 | START | 313 | 325 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 316 | START | 326 | 351 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 316 | START | 316 | 409 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `19` | 316 | START | 316 | 328 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 316 | START | 316 | 330 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 316 | START | 316 | 408 |
| ✅ EXACT | `Action_SplitBlock` | WR3 | `16` | `16` | 320 | START | 320 | 411 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 325 | END | 313 | 325 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `18` | `18` | 351 | START | 351 | 511 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 411 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_SnapReceive` | 313 | 325 | 13 | inferred_complete_timeline |
| `Action_None` | 326 | 350 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 351 | 511 | 161 | inferred_complete_timeline |
| `Action_BallCarry` | 513 | 539 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 6–339
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 312 | 307 | inferred_complete_timeline |
| `Action_None` | 313 | 339 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–487
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 487 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 319 | 317 | inferred_complete_timeline |
| `Action_SplitBlock` | 320 | 411 | 92 | inferred_complete_timeline |
| `Action_None` | 412 | 479 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–476
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 315 | 313 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 408 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 411 | 411 | 1 | inferred_complete_timeline |
| `Action_None` | 412 | 476 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 315 | 313 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 409 | 94 | inferred_complete_timeline |
| `Action_None` | 412 | 425 | 14 | inferred_complete_timeline |
| `Action_None` | 435 | 539 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–539
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_BallSnap` | 313 | 325 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 326 | 351 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 363 | 388 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 392 | 411 | 20 | inferred_complete_timeline |
| `Action_None` | 412 | 539 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–498
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 315 | 313 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 330 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 335 | 341 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 344 | 345 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 348 | 352 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 354 | 411 | 58 | inferred_complete_timeline |
| `Action_None` | 412 | 441 | 30 | inferred_complete_timeline |
| `Action_None` | 449 | 498 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–361
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 315 | 313 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 328 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 339 | 361 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–502
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 502 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–342
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 331 | 19 | inferred_complete_timeline |
| `Action_None` | 339 | 342 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–388
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 369 | 57 | inferred_complete_timeline |
| `Action_None` | 376 | 388 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–369
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 369 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–487
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 487 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 510 | 198 | inferred_complete_timeline |
| `Action_None` | 524 | 539 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–539
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 312 | 310 | inferred_complete_timeline |
| `Action_None` | 313 | 513 | 201 | inferred_complete_timeline |
| `Action_None` | 523 | 539 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 3–5 | 3 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 345–371 | 27 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 352–539 | 178 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 384–539 | 123 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 389–492 | 99 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 389–485 | 97 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 402–424 | 23 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 422–436 | 15 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 423–473 | 16 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 426–427 | 2 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 440–526 | 87 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 446–448 | 3 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 449–451 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [313–325], lower_priority='Action_ZoneBlock' annotated_start=316, effective_Action_ZoneBlock_start=326.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
- ⚠️ Action 'Action_None' range [313-487] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-369] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-408] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-476] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-510] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-539] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-513] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-502] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-331] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-369] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-388] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [326-351] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [363-388] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-487] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-479] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-409] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-425] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [351-511] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-328] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [339-361] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-330] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [335-341] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [344-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [348-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-441] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-498] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-371] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-539] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-412] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-434] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-506] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-539] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-397] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-492] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-485] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-424] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-436] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-473] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-526] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>