# Play-Annotation-Generator Annotation Review — Power_343

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_343`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 539
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 6 | START | 6 | 539 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 6 | START | 6 | 495 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 6 | START | 6 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 6 | START | 6 | 539 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 6 | START | 6 | 406 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 6 | START | 6 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 6 | START | 6 | 523 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 6 | START | 6 | 413 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 6 | START | 6 | 518 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 6 | START | 6 | 301 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `16` | `16` | 302 | START | 302 | 333 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `7` | `7` | 302 | START | 302 | 310 |
| ✅ EXACT | `Action_PullBlock` | LG | `20` | `20` | 302 | START | 302 | 356 |

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
- **Visible Frames:** 6–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–539
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 523 | 518 | inferred_complete_timeline |
| `Action_PreSnap` | 530 | 539 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 406 | 401 | inferred_complete_timeline |
| `Action_PreSnap` | 414 | 539 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–413
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 413 | 408 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–518
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 518 | 513 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–539
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 301 | 296 | inferred_complete_timeline |
| `Action_PullBlock` | 302 | 356 | 55 | inferred_complete_timeline |
| `Action_None` | 375 | 539 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–539
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 301 | 296 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 310 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 316 | 359 | 44 | inferred_complete_timeline |
| `Action_None` | 360 | 539 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 301 | 296 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 333 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 338 | 359 | 22 | inferred_complete_timeline |
| `Action_None` | 360 | 539 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–495
- **Visible Samples:** 490

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 495 | 490 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 349 | 344 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 539 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–347
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 347 | 342 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–539
- **Visible Samples:** 525

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 346 | 341 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 539 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–379
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 370 | 365 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 375 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 379 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–353
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 353 | 348 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–417
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 417 | 412 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–539
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 539 | 534 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 6–534 | 528 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 6–356 | 351 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 6–539 | 534 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 6–539 | 518 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 66–67 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 358–495 | 138 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 385–537 | 137 | 12 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 390–519 | 127 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 391–539 | 149 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 397–539 | 138 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 397–537 | 134 | 5 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 416–479 | 62 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 418–421 | 4 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 452–453 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 462–539 | 70 | 5 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 478–525 | 16 | 4 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 484–539 | 54 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 506–507 | 2 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 528–539 | 12 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 530–539 | 10 | 1 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 535–536 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 686: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 686: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 686: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [6-347] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-406] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-345] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-534] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-413] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-518] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [302-310] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-346] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-370] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-379] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-353] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-356] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-495] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [302-333] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-417] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [302-356] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-523] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-11] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-29] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-202] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-215] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-539] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-495] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-386] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-398] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-411] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-422] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-451] for track '25' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-464] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-467] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-477] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-483] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-508] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [511-516] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-537] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-391] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-519] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-461] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-539] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-410] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-524] for track '29' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-529] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-534] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-537] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [416-471] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-479] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-421] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-453] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-465] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-470] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [473-474] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-483] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-539] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-480] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [504-506] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-516] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [518-525] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-486] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-534] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [536-539] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [506-507] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-536] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>