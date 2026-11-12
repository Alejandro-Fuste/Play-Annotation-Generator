# Play-Annotation-Generator Annotation Review — SplitZone_163

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_163`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 539
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `22` | `22` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 3 | START | 4 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 3 | START | 4 | 337 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 3 | START | 4 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 3 | START | 4 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 3 | START | 4 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 3 | START | 107 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 3 | START | 4 | 321 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 3 | START | 4 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 3 | START | 4 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 3 | START | 4 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 3 | START | 4 | 312 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 301 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | RG | `22` | `22` | 313 | START | 313 | 315 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `16` | 316 | START | 316 | 539 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `21` | `21` | 316 | START | 316 | 539 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `22` | 316 | START | 316 | 346 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 316 | START | 316 | 394 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `7` | 316 | START | 316 | 344 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `3` | `3` | 322 | START | 322 | 362 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 324 | END | 313 | 324 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 326 | START | 326 | 337 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 338 | START | 338 | 482 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_SnapReceive` | 313 | 324 | 12 | inferred_complete_timeline |
| `Action_None` | 325 | 325 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 326 | 337 | 12 | inferred_complete_timeline |
| `Action_None` | 338 | 539 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–520
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 337 | 334 | inferred_complete_timeline |
| `Action_BallCarry` | 338 | 482 | 145 | inferred_complete_timeline |
| `Action_BallCarry` | 488 | 520 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 321 | 318 | inferred_complete_timeline |
| `Action_SplitBlock` | 322 | 362 | 41 | inferred_complete_timeline |
| `Action_SplitBlock` | 369 | 539 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 315 | 312 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 539 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–349
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 315 | 312 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 344 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 347 | 349 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 315 | 312 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 394 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 397 | 539 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 107–381
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 107 | 312 | 206 | inferred_complete_timeline |
| `Action_BallSnap` | 313 | 315 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 346 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 373 | 374 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 378 | 381 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 315 | 312 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 539 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–420
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 28 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 312 | 273 | inferred_complete_timeline |
| `Action_None` | 313 | 341 | 29 | inferred_complete_timeline |
| `Action_None` | 359 | 367 | 9 | inferred_complete_timeline |
| `Action_None` | 369 | 378 | 10 | inferred_complete_timeline |
| `Action_None` | 380 | 412 | 33 | inferred_complete_timeline |
| `Action_None` | 419 | 420 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 4–539
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 370 | 58 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–344
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 344 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–539
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 337 | 25 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_None` | 353 | 361 | 9 | inferred_complete_timeline |
| `Action_None` | 369 | 412 | 44 | inferred_complete_timeline |
| `Action_None` | 420 | 539 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 354 | 42 | inferred_complete_timeline |
| `Action_None` | 361 | 539 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 4–535
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 35 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 312 | 275 | inferred_complete_timeline |
| `Action_None` | 313 | 480 | 168 | inferred_complete_timeline |
| `Action_None` | 482 | 513 | 32 | inferred_complete_timeline |
| `Action_None` | 520 | 526 | 7 | inferred_complete_timeline |
| `Action_None` | 534 | 535 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 539 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–537
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 399 | 87 | inferred_complete_timeline |
| `Action_None` | 401 | 488 | 88 | inferred_complete_timeline |
| `Action_None` | 492 | 498 | 7 | inferred_complete_timeline |
| `Action_None` | 501 | 508 | 8 | inferred_complete_timeline |
| `Action_None` | 511 | 527 | 17 | inferred_complete_timeline |
| `Action_None` | 534 | 537 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–511
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 312 | 309 | inferred_complete_timeline |
| `Action_None` | 313 | 511 | 199 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 4–68 | 58 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 235–275 | 25 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 360–539 | 156 | 10 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 362–384 | 21 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 366–370 | 5 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 387–388 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 390–505 | 116 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 416–539 | 124 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 443–454 | 12 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 443–467 | 10 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 459–501 | 31 | 3 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 519–539 | 21 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 528–537 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 224 frames exceeds threshold 90 frames [start=316, end=539].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LT) duration 224 frames exceeds threshold 90 frames [start=316, end=539].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 224 frames exceeds threshold 90 frames [start=316, end=539].
- ⚠️ Action 'Action_None' range [313-511] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [322-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-399] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-488] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-498] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-508] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-527] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-394] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-28] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-341] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-367] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-378] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-412] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-344] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [347-349] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-344] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [338-482] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [488-520] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-370] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-354] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-337] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-361] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-412] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-539] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-34] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-63] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-26] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-35] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-312] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-480] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-513] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-526] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-346] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [373-374] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [378-381] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-244] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-271] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-378] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-488] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-496] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-505] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-523] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-531] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-375] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-384] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-505] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-454] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-449] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-475] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-486] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-501] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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