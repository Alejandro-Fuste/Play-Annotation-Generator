# Play-Annotation-Generator Annotation Review — InsideZoneRead_186

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_186`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 476 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 435 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 435 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 432 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 435 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `6` | `Group` | 0 | START | 0 | 432 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 433 | START | 433 | 444 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 436 | START | 436 | 501 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 436 | START | 445 | 445 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `18` | 436 | START | 436 | 501 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 436 | START | 436 | 501 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 444 | END | 433 | 444 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 449 | START | 449 | 462 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 463 | START | 463 | 476 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 477 | START | 477 | 539 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 501 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_SnapReceive` | 433 | 444 | 12 | inferred_complete_timeline |
| `Action_None` | 445 | 448 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 449 | 462 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 463 | 476 | 14 | inferred_complete_timeline |
| `Action_None` | 477 | 569 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 476 | 477 | inferred_complete_timeline |
| `Action_BallCarry` | 477 | 539 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 569 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 569 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 486 | 54 | inferred_complete_timeline |
| `Action_None` | 488 | 569 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 533 | 101 | inferred_complete_timeline |
| `Action_None` | 540 | 569 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 501 | 66 | inferred_complete_timeline |
| `Action_None` | 502 | 569 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–467
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_BallSnap` | 433 | 444 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 445 | 445 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 458 | 467 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 501 | 66 | inferred_complete_timeline |
| `Action_None` | 502 | 569 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 435 | 436 | inferred_complete_timeline |
| `Action_ZoneBlock` | 436 | 501 | 66 | inferred_complete_timeline |
| `Action_None` | 502 | 569 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–494
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 494 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 455 | 23 | inferred_complete_timeline |
| `Action_None` | 458 | 569 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 432 | 389 | inferred_complete_timeline |
| `Action_None` | 433 | 539 | 107 | inferred_complete_timeline |
| `Action_None` | 546 | 559 | 14 | inferred_complete_timeline |
| `Action_None` | 561 | 565 | 5 | inferred_complete_timeline |
| `Action_None` | 568 | 569 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 12–557
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 432 | 421 | inferred_complete_timeline |
| `Action_None` | 433 | 494 | 62 | inferred_complete_timeline |
| `Action_None` | 506 | 532 | 27 | inferred_complete_timeline |
| `Action_None` | 541 | 557 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–568
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 553 | 121 | inferred_complete_timeline |
| `Action_None` | 556 | 561 | 6 | inferred_complete_timeline |
| `Action_None` | 567 | 568 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 8–569
- **Visible Samples:** 542

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 432 | 408 | inferred_complete_timeline |
| `Action_None` | 433 | 559 | 127 | inferred_complete_timeline |
| `Action_None` | 565 | 569 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–555
- **Visible Samples:** 541

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 454 | 22 | inferred_complete_timeline |
| `Action_None` | 467 | 547 | 81 | inferred_complete_timeline |
| `Action_None` | 551 | 555 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 530 | 98 | inferred_complete_timeline |
| `Action_None` | 532 | 569 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 569 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–556
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 551 | 119 | inferred_complete_timeline |
| `Action_None` | 555 | 556 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 551

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 432 | 433 | inferred_complete_timeline |
| `Action_None` | 433 | 547 | 115 | inferred_complete_timeline |
| `Action_None` | 567 | 569 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–569 | 570 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–134 | 75 | 7 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 15–83 | 7 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 446–450 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 456–460 | 5 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 499–561 | 63 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 501–567 | 62 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 529–540 | 5 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 568–569 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 372: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [433–444], lower_priority='Action_ZoneBlock' annotated_start=436, effective_Action_ZoneBlock_start=445.
- ⚠️ Action 'Action_None' range [433-486] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-533] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-551] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-455] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-569] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [477-539] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-454] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-547] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-555] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-530] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-553] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-561] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-547] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-494] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '17' starts at frame 445, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [445-445] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [458-467] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [436-501] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-119] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-539] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-559] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-432] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-559] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-569] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-494] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-532] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-557] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-450] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-460] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-561] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-505] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-567] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>