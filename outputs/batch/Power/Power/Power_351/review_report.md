# Play-Annotation-Generator Annotation Review — Power_351

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_351`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 144
- **Validation Warnings:** 157
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `27` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `21` | `18` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `27` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 13 | START | 13 | 377 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 13 | START | 13 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 13 | START | 13 | 539 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 13 | START | 13 | 471 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 13 | START | 26 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 13 | START | 28 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `26` | `Group` | 13 | START | 131 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `27` | `Group` | 13 | START | 132 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 13 | START | 13 | 366 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 13 | START | 13 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `10` | 378 | START | 378 | 388 |
| ✅ EXACT | `Action_DownBlock` | RT | `21` | `18` | 378 | START | 378 | 382 |
| ✅ EXACT | `Action_PullBlock` | LG | `27` | `23` | 378 | START | 378 | 409 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–484
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 471 | 459 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 480 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 484 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 13–539
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 366 | 354 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 539 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–539
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 156 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 172 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 389 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 403 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 407 | 486 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 489 | 539 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 539 | 527 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–539
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 39 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 384 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 457 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 461 | 539 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `26`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 131–539
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 393 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 424 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 426 | 427 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 448 | 450 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 454 | 458 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 461 | 472 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 474 | 475 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 539 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `27`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `27`
- **team_side:** `offense`
- **Visible Frames:** 132–409
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 132 | 147 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 377 | 204 | inferred_complete_timeline |
| `Action_PullBlock` | 378 | 409 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 13–539
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 377 | 365 | inferred_complete_timeline |
| `Action_DownBlock` | 378 | 388 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 397 | 400 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 421 | 425 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 428 | 430 | 3 | inferred_complete_timeline |
| `Action_None` | 434 | 442 | 9 | inferred_complete_timeline |
| `Action_None` | 445 | 522 | 78 | inferred_complete_timeline |
| `Action_None` | 528 | 539 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 28–538
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 36 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 59 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 149 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 403 | 232 | inferred_complete_timeline |
| `Action_PreSnap` | 457 | 484 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 486 | 490 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 494 | 512 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 519 | 533 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 536 | 538 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 26–382
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 103 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 155 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 377 | 220 | inferred_complete_timeline |
| `Action_DownBlock` | 378 | 382 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–402
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 19 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 402 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–425
- **Visible Samples:** 397

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 404 | 392 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 423 | 425 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `25`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 47–424
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 47 | 75 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 147 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 392 | 215 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 403 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 424 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `24`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 47–534
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 47 | 75 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 147 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 392 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 402 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 407 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 436 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 453 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 455 | 456 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 461 | 484 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 488 | 489 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 498 | 513 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 522 | 523 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 534 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–539
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 429 | 417 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 458 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 539 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 539 | 527 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 539 | 527 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 539 | 527 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 539 | 527 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–539
- **Visible Samples:** 514

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 433 | 421 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 436 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 438 | 482 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 494 | 539 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–51
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 40 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 51 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 13–539 | 518 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 13–539 | 432 | 11 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 25–28 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 403–433 | 23 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 422–510 | 65 | 11 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 462–494 | 28 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 462–539 | 76 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 467–539 | 69 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 477–539 | 54 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 496–507 | 11 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 517–523 | 7 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 530–539 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (4 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 132 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [13-433] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-436] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-482] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-511] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-523] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-533] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-539] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-404] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-425] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-366] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-539] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-429] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-458] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-19] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-402] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-39] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-384] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-457] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-539] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [378-388] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [397-400] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [421-425] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [428-430] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-442] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-522] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-51] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-539] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-172] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-389] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-403] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-486] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-539] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-19] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-404] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-417] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-484] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-488] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-471] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-480] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-484] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-155] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [378-382] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-36] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-149] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-403] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-484] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-490] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [494-512] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-533] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-538] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-147] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-392] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-402] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-436] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-453] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-456] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-484] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-489] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [498-513] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [522-523] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-534] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-147] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-392] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-403] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-407] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-424] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-175] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-393] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-424] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-427] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-450] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-458] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-472] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-475] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-539] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-377] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [378-409] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-412] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-433] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-429] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-434] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-441] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-450] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-458] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [460-466] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-470] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-482] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-490] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-496] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-510] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-468] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-484] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-494] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-466] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-471] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-489] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-539] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-484] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-491] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-539] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [496-504] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [506-507] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-523] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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