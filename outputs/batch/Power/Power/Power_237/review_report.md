# Play-Annotation-Generator Annotation Review — Power_237

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_237`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 599
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 139
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `27` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 7 | START | 7 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `12` | `Group` | 7 | START | 7 | 567 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 7 | START | 7 | 444 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 7 | START | 7 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 7 | START | 7 | 290 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 7 | START | 7 | 596 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 7 | START | 19 | 330 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `22` | `Group` | 7 | START | 162 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 7 | START | 7 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `13` | 445 | START | 445 | 461 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `16` | `16` | 445 | START | 445 | 446 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `27` | `22` | 445 | START | 445 | 495 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 19–599
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 330 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 474 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 476 | 527 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 529 | 599 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 7–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 599 | 593 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 596 | 590 | inferred_complete_timeline |
| `Action_PreSnap` | 598 | 599 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 567 | 561 | inferred_complete_timeline |
| `Action_PreSnap` | 571 | 572 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 576 | 599 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `22`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 162–269
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 162 | 269 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 7–599
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 290 | 284 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 461 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 599 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–546
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 444 | 438 | inferred_complete_timeline |
| `Action_DownBlock` | 445 | 461 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 466 | 467 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 472 | 488 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 491 | 495 | 5 | inferred_complete_timeline |
| `Action_None` | 496 | 500 | 5 | inferred_complete_timeline |
| `Action_None` | 505 | 546 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–453
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 290 | 284 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 444 | 145 | inferred_complete_timeline |
| `Action_DownBlock` | 445 | 446 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 448 | 453 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 7–505
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 269 | 263 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 459 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 473 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 488 | 491 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 500 | 505 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–599
- **Visible Samples:** 563

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 294 | 288 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 307 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 313 | 316 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 328 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 457 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 468 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 529 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 532 | 599 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–209
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 209 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 7–599
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 269 | 263 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 286 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 452 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 479 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 482 | 483 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 486 | 509 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 512 | 528 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 530 | 599 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 7–490
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 209 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 269 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 284 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 461 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 468 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 481 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 484 | 490 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–599
- **Visible Samples:** 587

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 548 | 542 | inferred_complete_timeline |
| `Action_PreSnap` | 550 | 553 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 556 | 560 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 562 | 590 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 593 | 599 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 7–495
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 495 | 489 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–597
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 597 | 591 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 548 | 542 | inferred_complete_timeline |
| `Action_PreSnap` | 550 | 599 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 7–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 599 | 593 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 7–599 | 589 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 7–495 | 479 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 7–349 | 287 | 7 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 280–599 | 243 | 12 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 441–521 | 77 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 459–598 | 138 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 495–533 | 30 | 5 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 497–521 | 20 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 506–599 | 63 | 7 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 515–589 | 17 | 4 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 566–599 | 34 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 572–599 | 28 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 572–599 | 28 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 584–599 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 476: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [7-599] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-575] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [577-585] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-596] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [598-599] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-461] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-467] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-477] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-495] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-597] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-290] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-461] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-599] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-548] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-548] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [550-553] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [556-560] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-590] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [593-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-269] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-286] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-452] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-479] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-483] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-509] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [512-528] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [530-599] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-294] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-316] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-457] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-468] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-529] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-599] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-495] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-567] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [571-572] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [445-461] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [466-467] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [472-488] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-546] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-459] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-473] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-491] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-505] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-290] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-444] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [445-446] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [448-453] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-209] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-269] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-284] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-461] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-468] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-481] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-490] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-103] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-132] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-334] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-349] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-474] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-527] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-286] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-320] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-461] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-468] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-491] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [493-500] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-507] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [512-525] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [562-591] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-507] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-518] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-521] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-594] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [597-598] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [495-501] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-509] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-517] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-527] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-533] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-507] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-517] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [520-521] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [506-527] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-533] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-554] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [556-565] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [569-572] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [575-586] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [589-599] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-524] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [561-562] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [568-569] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [587-589] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [572-599] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>