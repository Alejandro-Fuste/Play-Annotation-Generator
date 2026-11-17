# Play-Annotation-Generator Annotation Review — Power_238

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_238`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 0
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB1 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 23 | START | 23 | 444 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 23 | START | 23 | 444 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 23 | START | 23 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 23 | START | 23 | 466 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 23 | START | 23 | 467 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `10` | `10` | 445 | START | 445 | 467 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `12` | `12` | 445 | START | 445 | 466 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB1 | `11` | `11` | 445 | START | 445 | 455 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 23–599
- **Visible Samples:** 573

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 466 | 444 | inferred_complete_timeline |
| `Action_PreSnap` | 468 | 470 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 524 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 527 | 599 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 23–505
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 467 | 445 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 489 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 491 | 505 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–195
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 77 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 100 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 148 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 158 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 170 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 195 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 23–484
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 444 | 422 | inferred_complete_timeline |
| `Action_DownBlock` | 445 | 467 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 480 | 481 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 483 | 483 | 1 | inferred_complete_timeline |
| `Action_None` | 484 | 484 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 23–585
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 444 | 422 | inferred_complete_timeline |
| `Action_DownBlock` | 445 | 466 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 476 | 483 | 8 | inferred_complete_timeline |
| `Action_None` | 484 | 487 | 4 | inferred_complete_timeline |
| `Action_None` | 495 | 555 | 61 | inferred_complete_timeline |
| `Action_None` | 557 | 585 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 23–513
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 505 | 483 | inferred_complete_timeline |
| `Action_PreSnap` | 508 | 513 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–553
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 466 | 444 | inferred_complete_timeline |
| `Action_PreSnap` | 473 | 476 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 479 | 484 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 509 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 511 | 514 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 517 | 553 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 23–599
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 524 | 502 | inferred_complete_timeline |
| `Action_PreSnap` | 526 | 574 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 576 | 599 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 23–516
- **Visible Samples:** 434

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 177 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 455 | 277 | inferred_complete_timeline |
| `Action_PreSnap` | 515 | 516 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 23–484
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 444 | 422 | inferred_complete_timeline |
| `Action_PullBlock` | 445 | 455 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 459 | 463 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 480 | 483 | 4 | inferred_complete_timeline |
| `Action_None` | 484 | 484 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 23–599
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 464 | 442 | inferred_complete_timeline |
| `Action_PreSnap` | 481 | 484 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 491 | 521 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 524 | 580 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 583 | 599 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–599
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 56 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 268 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 296 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 299 | 306 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 470 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 476 | 587 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 590 | 599 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–484
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 264 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 271 | 468 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 472 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 484 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 23–515 | 487 | 4 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 23–517 | 495 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 30–31 | 2 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 65–66 | 2 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 129–159 | 18 | 4 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 161–499 | 297 | 9 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 300–304 | 5 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 457–490 | 26 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 477–497 | 6 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 500–529 | 30 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 501–599 | 97 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 506–599 | 93 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 511–524 | 14 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 519–526 | 8 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 539–578 | 40 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 543–599 | 57 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 590–599 | 10 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 593–599 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 478: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 478: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 478: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 478: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [23-524] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [526-574] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-471] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-506] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [509-510] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [514-515] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-517] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-505] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [508-513] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-464] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-484] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-521] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [524-580] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-177] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-455] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-516] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-468] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-472] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-484] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-56] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-268] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-296] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-306] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-318] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-470] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-587] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-466] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-470] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-524] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-467] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-489] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-505] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [445-467] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [480-481] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 484, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [484-484] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [445-455] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [459-463] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 484, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [484-484] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [445-466] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-487] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-555] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-585] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-466] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-476] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-484] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-509] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-514] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-553] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-195] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-131] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-175] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-249] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-446] for track '18' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-465] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-489] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-499] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-465] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-490] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-492] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [496-497] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-529] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [501-592] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [506-572] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-524] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-526] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-578] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [543-599] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>