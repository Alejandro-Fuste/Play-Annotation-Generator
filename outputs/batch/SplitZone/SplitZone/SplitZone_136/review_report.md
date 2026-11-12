# Play-Annotation-Generator Annotation Review — SplitZone_136

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_136`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 84
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 28 | START | 29 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 28 | START | 29 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 28 | START | 29 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 28 | START | 29 | 316 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 28 | START | 29 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 28 | START | 29 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 28 | START | 29 | 296 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 28 | START | 29 | 296 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `2` | 288 | START | 288 | 301 |
| ✅ EXACT | `Action_SplitBlock` | TE | `0` | `0` | 291 | START | 291 | 412 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `1` | 297 | START | 297 | 412 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `14` | 297 | START | 297 | 412 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `2` | `2` | 297 | START | 302 | 319 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 297 | START | 297 | 412 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `4` | `4` | 297 | START | 297 | 394 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 301 | END | 288 | 301 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 307 | START | 307 | 316 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `13` | 317 | START | 317 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `2` | `2` | 320 | START | 320 | 404 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 412 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 29–458
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 287 | 259 | inferred_complete_timeline |
| `Action_SnapReceive` | 288 | 301 | 14 | inferred_complete_timeline |
| `Action_None` | 302 | 306 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 307 | 316 | 10 | inferred_complete_timeline |
| `Action_None` | 317 | 458 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 29–479
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 316 | 288 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 326 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 330 | 430 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 437 | 447 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 452 | 453 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 469 | 479 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 290 | 262 | inferred_complete_timeline |
| `Action_SplitBlock` | 291 | 412 | 122 | inferred_complete_timeline |
| `Action_None` | 413 | 479 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 29–440
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 296 | 268 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 412 | 116 | inferred_complete_timeline |
| `Action_None` | 413 | 440 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 29–457
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 296 | 268 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 412 | 116 | inferred_complete_timeline |
| `Action_None` | 413 | 457 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 29–462
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 161 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 178 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 240 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 287 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 288 | 301 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 319 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 320 | 404 | 85 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 406 | 412 | 7 | inferred_complete_timeline |
| `Action_None` | 413 | 417 | 5 | inferred_complete_timeline |
| `Action_None` | 422 | 462 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 29–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 296 | 268 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 412 | 116 | inferred_complete_timeline |
| `Action_None` | 413 | 479 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 29–479
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 296 | 268 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 394 | 98 | inferred_complete_timeline |
| `Action_ZoneBlock` | 397 | 410 | 14 | inferred_complete_timeline |
| `Action_None` | 415 | 479 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 51–352
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 51 | 287 | 237 | inferred_complete_timeline |
| `Action_None` | 288 | 352 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 29–479
- **Visible Samples:** 451

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 287 | 259 | inferred_complete_timeline |
| `Action_None` | 288 | 479 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 29–332
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 118 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 287 | 168 | inferred_complete_timeline |
| `Action_None` | 288 | 332 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 29–387
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 287 | 259 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |
| `Action_None` | 299 | 309 | 11 | inferred_complete_timeline |
| `Action_None` | 311 | 387 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 29–422
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 287 | 259 | inferred_complete_timeline |
| `Action_None` | 288 | 333 | 46 | inferred_complete_timeline |
| `Action_None` | 348 | 354 | 7 | inferred_complete_timeline |
| `Action_None` | 403 | 407 | 5 | inferred_complete_timeline |
| `Action_None` | 420 | 422 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 29–363
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 287 | 259 | inferred_complete_timeline |
| `Action_None` | 288 | 363 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 29–439
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 287 | 259 | inferred_complete_timeline |
| `Action_None` | 288 | 378 | 91 | inferred_complete_timeline |
| `Action_None` | 384 | 414 | 31 | inferred_complete_timeline |
| `Action_None` | 418 | 439 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 29–41 | 12 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 117–123 | 6 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 334–479 | 146 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 351–479 | 129 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 358–479 | 121 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 364–479 | 116 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 365–368 | 4 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 368–463 | 93 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 371–376 | 6 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 372–374 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 373–384 | 9 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 388–479 | 92 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 394–479 | 86 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 400–479 | 76 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 406–479 | 69 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 410–479 | 69 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 452–479 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 244 | 244 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `2` (C): Annotated start 297 != Inferred start 302
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LG) duration 116 frames exceeds threshold 90 frames [start=297, end=412].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '2' (C) duration 93 frames exceeds threshold 90 frames [start=320, end=412].
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [288–301], lower_priority='Action_ZoneBlock' annotated_start=297, effective_Action_ZoneBlock_start=302.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 116 frames exceeds threshold 90 frames [start=297, end=412].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 116 frames exceeds threshold 90 frames [start=297, end=412].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 116 frames exceeds threshold 90 frames [start=297, end=412].
- ⚠️ Action 'Action_None' range [413-457] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-178] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [320-404] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-417] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-462] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-440] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-394] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [397-410] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-479] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-363] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-378] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-414] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-439] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-332] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-333] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-354] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-407] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-309] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-387] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-458] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-38] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-326] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-430] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [437-447] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [452-453] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-352] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-479] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-385] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-458] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-376] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-384] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-479] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-405] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-416] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-479] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-412] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>