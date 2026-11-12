# Play-Annotation-Generator Annotation Review — SplitZone_215

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_215`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `16` | `16` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `16` | `16` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | offense | `17` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 4 | START | 5 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 4 | START | 5 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 4 | START | 5 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 4 | START | 5 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 4 | START | 30 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 4 | START | 5 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 4 | START | 5 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 4 | START | 5 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 4 | START | 5 | 327 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 4 | START | 5 | 315 |
| ✅ EXACT | `Action_BallSnap` | RB | `17` | `17` | 316 | START | 316 | 330 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `13` | 319 | START | 319 | 343 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `18` | 319 | START | 319 | 417 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 319 | START | 319 | 373 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 319 | START | 319 | 417 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | QB | `7` | `7` | 328 | START | 328 | 351 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `16` | `16` | 330 | END | 316 | 330 |
| ✅ EXACT | `Action_Handoff` | DE2 | `16` | `16` | 333 | START | 333 | 343 |
| ✅ EXACT | `Action_BallCarry` | C | `13` | `13` | 344 | START | 344 | 434 |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | `17` | `17` | 356 | START | 356 | 417 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 417 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 5–539
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 327 | 323 | inferred_complete_timeline |
| `Action_SplitBlock` | 328 | 351 | 24 | inferred_complete_timeline |
| `Action_SplitBlock` | 353 | 380 | 28 | inferred_complete_timeline |
| `Action_SplitBlock` | 382 | 389 | 8 | inferred_complete_timeline |
| `Action_SplitBlock` | 395 | 396 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 415 | 417 | 3 | inferred_complete_timeline |
| `Action_None` | 418 | 422 | 5 | inferred_complete_timeline |
| `Action_None` | 424 | 539 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_BallSnap` | 316 | 330 | 15 | inferred_complete_timeline |
| `Action_None` | 331 | 353 | 23 | inferred_complete_timeline |
| `Action_None` | 355 | 355 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 356 | 417 | 62 | inferred_complete_timeline |
| `Action_None` | 418 | 422 | 5 | inferred_complete_timeline |
| `Action_None` | 426 | 539 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–461
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 373 | 58 | inferred_complete_timeline |
| `Action_None` | 377 | 396 | 20 | inferred_complete_timeline |
| `Action_None` | 398 | 461 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–496
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 383 | 68 | inferred_complete_timeline |
| `Action_None` | 387 | 393 | 7 | inferred_complete_timeline |
| `Action_None` | 396 | 488 | 93 | inferred_complete_timeline |
| `Action_None` | 491 | 496 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 30–539
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 315 | 274 | inferred_complete_timeline |
| `Action_None` | 316 | 507 | 192 | inferred_complete_timeline |
| `Action_None` | 514 | 539 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 539 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 318 | 314 | inferred_complete_timeline |
| `Action_ZoneBlock` | 319 | 417 | 99 | inferred_complete_timeline |
| `Action_None` | 418 | 539 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 5–507
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 318 | 314 | inferred_complete_timeline |
| `Action_ZoneBlock` | 319 | 417 | 99 | inferred_complete_timeline |
| `Action_None` | 418 | 500 | 83 | inferred_complete_timeline |
| `Action_None` | 502 | 507 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 5–434
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 25 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 318 | 288 | inferred_complete_timeline |
| `Action_ZoneBlock` | 319 | 343 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 344 | 434 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–414
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 16 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 318 | 300 | inferred_complete_timeline |
| `Action_ZoneBlock` | 319 | 373 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 381 | 396 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 398 | 414 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–535
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 492 | 177 | inferred_complete_timeline |
| `Action_None` | 494 | 502 | 9 | inferred_complete_timeline |
| `Action_None` | 513 | 514 | 2 | inferred_complete_timeline |
| `Action_None` | 516 | 517 | 2 | inferred_complete_timeline |
| `Action_None` | 519 | 528 | 10 | inferred_complete_timeline |
| `Action_None` | 530 | 535 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_SnapReceive` | 316 | 330 | 15 | inferred_complete_timeline |
| `Action_None` | 331 | 332 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 333 | 343 | 11 | inferred_complete_timeline |
| `Action_None` | 344 | 539 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 31 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 315 | 256 | inferred_complete_timeline |
| `Action_None` | 316 | 409 | 94 | inferred_complete_timeline |
| `Action_None` | 413 | 422 | 10 | inferred_complete_timeline |
| `Action_None` | 464 | 539 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–358
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 358 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–357
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 54 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 315 | 246 | inferred_complete_timeline |
| `Action_None` | 316 | 346 | 31 | inferred_complete_timeline |
| `Action_None` | 351 | 357 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–465
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 392 | 77 | inferred_complete_timeline |
| `Action_None` | 415 | 437 | 23 | inferred_complete_timeline |
| `Action_None` | 458 | 460 | 3 | inferred_complete_timeline |
| `Action_None` | 462 | 465 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 439 | 124 | inferred_complete_timeline |
| `Action_None` | 441 | 446 | 6 | inferred_complete_timeline |
| `Action_None` | 448 | 539 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–536
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 536 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–387
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 387 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–524
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 442 | 127 | inferred_complete_timeline |
| `Action_None` | 451 | 524 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 315 | 311 | inferred_complete_timeline |
| `Action_None` | 316 | 539 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 116–327 | 210 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 121–125 | 5 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 347–539 | 193 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 357–539 | 181 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 373–463 | 91 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 407–539 | 133 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 419–507 | 89 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 431–539 | 84 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 443–457 | 15 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 459–539 | 78 | 3 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 465–472 | 8 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 469–514 | 45 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 520–539 | 20 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 538–539 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 99 frames exceeds threshold 90 frames [start=319, end=417].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 99 frames exceeds threshold 90 frames [start=319, end=417].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 96 frames exceeds threshold 90 frames [start=319, end=414].
- ⚠️ Action 'Action_None' range [316-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-439] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-446] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-492] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-502] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-514] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-528] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-535] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-373] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-396] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-461] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-383] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-393] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-488] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-496] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-57] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-409] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-422] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [328-351] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [353-380] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [382-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [395-396] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-392] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-437] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-460] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-465] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-536] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-442] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-524] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-54] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-346] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-357] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-25] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [344-434] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-387] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-353] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-318] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-500] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-507] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [319-373] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [381-396] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [398-414] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-40] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-507] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-327] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-539] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-466] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-463] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-539] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-507] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-502] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-457] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-524] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-537] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-472] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-477] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-514] for track '32' has 1 frames without a visible bounding box.
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

</details>