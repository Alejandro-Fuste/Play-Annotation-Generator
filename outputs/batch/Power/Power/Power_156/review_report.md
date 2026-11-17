# Play-Annotation-Generator Annotation Review — Power_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_156`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 8
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 22 | START | 22 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 22 | START | 22 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 22 | START | 22 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 22 | START | 22 | 396 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 22 | START | 22 | 382 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 22 | START | 22 | 365 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `0` | `0` | 359 | START | 359 | 388 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `12` | 359 | START | 359 | 428 |

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
- **Visible Frames:** 22–365
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 365 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 22–434
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 358 | 337 | inferred_complete_timeline |
| `Action_DownBlock` | 359 | 388 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 425 | 428 | 4 | inferred_complete_timeline |
| `Action_None` | 429 | 434 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 22–479
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 382 | 361 | inferred_complete_timeline |
| `Action_PreSnap` | 387 | 434 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 440 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 458 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 22–253
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 201 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 215 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 253 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–479
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 65 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 155 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 358 | 194 | inferred_complete_timeline |
| `Action_PullBlock` | 359 | 428 | 70 | inferred_complete_timeline |
| `Action_None` | 429 | 479 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–416
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 396 | 375 | inferred_complete_timeline |
| `Action_PreSnap` | 398 | 416 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–479
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 479 | 458 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–408
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 401 | 380 | inferred_complete_timeline |
| `Action_PreSnap` | 404 | 408 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 338–457
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 338 | 457 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 46–249
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 58 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 245 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 249 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–479
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 90 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 137 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 438 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 442 | 479 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 22–36
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 36 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 38–387
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 38 | 387 | 350 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–479
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 479 | 458 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 22–57 | 36 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 22–459 | 410 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 22–479 | 381 | 6 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 368–390 | 23 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 369–479 | 107 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 370–479 | 110 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 383–472 | 76 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 407–479 | 71 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 421–428 | 7 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 432–479 | 45 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 451–479 | 29 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 468–477 | 10 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 468–479 | 12 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 314: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [359-388] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-36] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-90] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-438] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-396] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-416] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-382] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-434] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-440] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-458] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-479] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-365] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-401] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-408] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-405] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-422] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-429] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-453] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [456-459] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-215] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-253] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-26] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-78] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-360] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-387] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-245] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-457] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-390] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-445] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-479] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-397] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-472] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-474] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-424] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-428] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-467] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [469-476] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-477] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>