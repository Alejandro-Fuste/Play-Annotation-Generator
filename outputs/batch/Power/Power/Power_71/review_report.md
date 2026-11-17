# Play-Annotation-Generator Annotation Review — Power_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_71`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 629
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 188
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `32` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `35` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `36` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `32` | `24` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `36` | `26` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `35` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 24 | START | 24 | 482 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 24 | START | 24 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 24 | START | 24 | 559 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 24 | START | 24 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 24 | START | 24 | 567 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `32` | `Group` | 24 | START | 205 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `35` | `Group` | 24 | START | 208 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `36` | `Group` | 24 | START | 208 | 428 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 24 | START | 24 | 626 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `12` | `12` | 429 | START | 429 | 442 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `32` | `24` | 429 | START | 429 | 436 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `36` | `26` | 429 | START | 429 | 436 |
| ✅ EXACT | `Action_PullBlock` | LG | `35` | `25` | 429 | START | 429 | 461 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 24–548
- **Visible Samples:** 517

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 60 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 66 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 80 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 548 | 467 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 24–599
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 559 | 536 | inferred_complete_timeline |
| `Action_PreSnap` | 594 | 599 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 24–629
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 482 | 459 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 561 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 628 | 629 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 24–578
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 567 | 544 | inferred_complete_timeline |
| `Action_PreSnap` | 574 | 578 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 24–626
- **Visible Samples:** 603

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 626 | 603 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `35`</summary>

- **xml_track_id:** `25`
- **actor_track_id:** `35`
- **team_side:** `offense`
- **Visible Frames:** 208–629
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 208 | 218 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 255 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 265 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 270 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 280 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 428 | 98 | inferred_complete_timeline |
| `Action_PullBlock` | 429 | 461 | 33 | inferred_complete_timeline |
| `Action_None` | 462 | 479 | 18 | inferred_complete_timeline |
| `Action_None` | 483 | 485 | 3 | inferred_complete_timeline |
| `Action_None` | 487 | 629 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `36`</summary>

- **xml_track_id:** `26`
- **actor_track_id:** `36`
- **team_side:** `offense`
- **Visible Frames:** 208–557
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 208 | 428 | 221 | inferred_complete_timeline |
| `Action_DownBlock` | 429 | 436 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 440 | 444 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 446 | 457 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 461 | 461 | 1 | inferred_complete_timeline |
| `Action_None` | 462 | 479 | 18 | inferred_complete_timeline |
| `Action_None` | 483 | 485 | 3 | inferred_complete_timeline |
| `Action_None` | 487 | 557 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `32`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `32`
- **team_side:** `offense`
- **Visible Frames:** 205–466
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 205 | 218 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 236 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 428 | 190 | inferred_complete_timeline |
| `Action_DownBlock` | 429 | 436 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 439 | 459 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 461 | 461 | 1 | inferred_complete_timeline |
| `Action_None` | 462 | 466 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 24–629
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 34 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 141 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 255 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 294 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 306 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 311 | 316 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 428 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 429 | 442 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 452 | 461 | 10 | inferred_complete_timeline |
| `Action_None` | 462 | 485 | 24 | inferred_complete_timeline |
| `Action_None` | 487 | 489 | 3 | inferred_complete_timeline |
| `Action_None` | 491 | 629 | 139 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 24–629
- **Visible Samples:** 603

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 485 | 462 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 515 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 518 | 629 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 24–629
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 199 | 176 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 456 | 253 | inferred_complete_timeline |
| `Action_PreSnap` | 461 | 466 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 474 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 476 | 485 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 489 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 491 | 514 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 517 | 629 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 24–554
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 98 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 148 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 182 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 480 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 483 | 485 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 489 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 491 | 535 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 541 | 554 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 24–478
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 94 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 155 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 188 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 464 | 262 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 478 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 24–485
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 485 | 462 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 24–517
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 482 | 459 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 517 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 24–548
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 548 | 525 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 24–582
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 92 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 529 | 407 | inferred_complete_timeline |
| `Action_PreSnap` | 565 | 582 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 24–629
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 475 | 452 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 482 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 487 | 611 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 616 | 626 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 629 | 629 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 24–629
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 34 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 509 | 473 | inferred_complete_timeline |
| `Action_PreSnap` | 515 | 569 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 574 | 629 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 24–556 | 521 | 3 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 24–129 | 51 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 24–87 | 63 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 24–629 | 593 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 35–94 | 8 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 84–93 | 10 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 140–143 | 4 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 166–527 | 342 | 6 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 450–502 | 25 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 488–489 | 2 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 488–629 | 142 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 492–550 | 54 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 494–495 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 523–580 | 39 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 530–629 | 99 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 545–629 | 85 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 575–624 | 49 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 590–629 | 34 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 598–629 | 32 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 603–629 | 26 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 617–629 | 13 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 620–629 | 10 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 623–629 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `32` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `36` (4 segments found)

### Track Identity Issues

- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 139 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 144: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 144: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [24-482] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-561] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-511] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-520] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [527-556] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-485] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-515] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-567] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [574-578] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-485] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-529] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [565-582] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-456] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-466] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-474] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-485] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-489] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-514] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-475] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-482] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-611] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [616-626] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-626] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-509] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-569] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-42] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-78] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-87] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-34] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-90] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-141] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-255] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-294] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-306] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-316] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-428] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [429-442] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-485] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-155] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-197] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-464] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-478] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-485] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-599] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [604-607] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-559] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [594-599] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-482] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-517] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-548] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-98] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-103] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-111] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-148] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-154] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-182] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-480] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-485] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-489] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-535] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [541-554] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-60] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-80] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-548] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-218] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-236] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-463] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-478] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-527] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-236] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-428] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [429-436] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [439-459] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-466] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-255] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-280] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-428] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-485] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-428] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [429-436] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [440-444] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [446-457] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-479] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-485] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-557] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-451] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [483-485] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [487-502] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-489] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [492-507] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [513-550] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [494-495] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [523-529] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [548-559] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-580] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-591] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [575-576] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [578-624] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [590-613] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [603-605] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [607-629] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>