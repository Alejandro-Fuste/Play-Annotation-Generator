# Play-Annotation-Generator Annotation Review — InsideZoneRead_185

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_185`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 56
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 7
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `23` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | DT1 | defense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | DE1 | defense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 435 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 435 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 435 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `23` | `18` | 433 | START | 535 | 535 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 436 | START | 436 | 501 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `4` | `3` | 436 | START | 436 | 501 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 436 | START | 436 | 501 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `14` | `13` | 444 | END | 433 | 444 |
| ✅ EXACT | `Action_ReadDefender` | DT1 | `14` | `13` | 449 | START | 449 | 462 |
| ✅ EXACT | `Action_Handoff` | DT1 | `14` | `13` | 463 | START | 463 | 476 |
| ✅ EXACT | `Action_BallCarry` | DE1 | `10` | `9` | 477 | START | 477 | 579 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 501 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 628

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 471 | 39 | inferred_complete_timeline |
| `Action_None` | 474 | 629 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 501 | 66 | inferred_complete_timeline |
| `Action_None` | 502 | 629 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–595
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 501 | 66 | inferred_complete_timeline |
| `Action_None` | 502 | 595 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–535
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 501 | 66 | inferred_complete_timeline |
| `Action_None` | 502 | 535 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–579
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 476 | 477 | inferred_complete_timeline |
| `Action_BallCarry` | 477 | 579 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–518
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 518 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_SnapReceive` | 433 | 444 | 12 | inferred_complete_timeline |
| `Action_None` | 445 | 448 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 449 | 462 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 463 | 476 | 14 | inferred_complete_timeline |
| `Action_None` | 477 | 629 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–523
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 523 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–459
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 447 | 15 | inferred_complete_timeline |
| `Action_None` | 456 | 459 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–580
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 454 | 22 | inferred_complete_timeline |
| `Action_None` | 461 | 462 | 2 | inferred_complete_timeline |
| `Action_None` | 470 | 580 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–583
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 477 | 45 | inferred_complete_timeline |
| `Action_None` | 482 | 583 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–471
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 471 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–629 | 630 | 2 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 137–557 | 339 | 5 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 482–483 | 2 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 483–540 | 58 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 534–622 | 89 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 535–629 | 95 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 540–567 | 27 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 554–629 | 76 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 568–570 | 3 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 570–629 | 60 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 621–629 | 9 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 624–629 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `23` (Position_Unknown): Annotated start 433 != Inferred start 535

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 26 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 370: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=535, end=444. Clamping end to start.
- ⚠️ Action 'Action_None' range [433-471] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-447] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-595] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-432] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-477] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-583] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-523] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-471] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [477-579] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-518] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-535] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-454] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-462] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-580] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-226] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-557] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-540] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-622] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-564] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-570] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_185'; source metadata written as null.

</details>