# Play-Annotation-Generator Annotation Review — InsideZoneRead_142

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_142`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 438 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 438 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `20` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 21 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 438 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 426 | START | 426 | 454 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `12` | 439 | START | 439 | 446 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `16` | `15` | 439 | START | 455 | 455 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `17` | 439 | START | 439 | 519 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `21` | `20` | 439 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 439 | START | 439 | 519 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 454 | END | 426 | 454 |
| ✅ EXACT | `Action_ReadDefender` | QB | `19` | `18` | 457 | START | 457 | 469 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `13` | `12` | 464 | START | 464 | 502 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 470 | START | 470 | 484 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `22` | `21` | 485 | START | 485 | 599 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 519 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_SnapReceive` | 426 | 454 | 29 | inferred_complete_timeline |
| `Action_None` | 455 | 456 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 457 | 469 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 470 | 484 | 15 | inferred_complete_timeline |
| `Action_None` | 485 | 599 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–581
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 379 | 294 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 384 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 395 | 425 | 31 | inferred_complete_timeline |
| `Action_None` | 426 | 450 | 25 | inferred_complete_timeline |
| `Action_None` | 453 | 553 | 101 | inferred_complete_timeline |
| `Action_None` | 575 | 581 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 438 | 439 | inferred_complete_timeline |
| `Action_ZoneBlock` | 439 | 519 | 81 | inferred_complete_timeline |
| `Action_None` | 520 | 599 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 21–215
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 202 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 215 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_BallSnap` | 426 | 454 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 455 | 455 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 470 | 494 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 514 | 519 | 6 | inferred_complete_timeline |
| `Action_None` | 520 | 599 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 438 | 439 | inferred_complete_timeline |
| `Action_ZoneBlock` | 439 | 446 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 453 | 463 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 464 | 502 | 39 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 513 | 519 | 7 | inferred_complete_timeline |
| `Action_None` | 520 | 528 | 9 | inferred_complete_timeline |
| `Action_None` | 534 | 535 | 2 | inferred_complete_timeline |
| `Action_None` | 537 | 558 | 22 | inferred_complete_timeline |
| `Action_None` | 566 | 599 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 438 | 439 | inferred_complete_timeline |
| `Action_ZoneBlock` | 439 | 519 | 81 | inferred_complete_timeline |
| `Action_None` | 520 | 599 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 293 | 425 | 133 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–490
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 490 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 471 | 46 | inferred_complete_timeline |
| `Action_None` | 533 | 599 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–518
- **Visible Samples:** 519

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 518 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 395 | 396 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 425 | 1 | inferred_complete_timeline |
| `Action_None` | 426 | 426 | 1 | inferred_complete_timeline |
| `Action_None` | 431 | 448 | 18 | inferred_complete_timeline |
| `Action_None` | 451 | 538 | 88 | inferred_complete_timeline |
| `Action_None` | 541 | 558 | 18 | inferred_complete_timeline |
| `Action_None` | 562 | 569 | 8 | inferred_complete_timeline |
| `Action_None` | 571 | 599 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 599 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_None` | 426 | 562 | 137 | inferred_complete_timeline |
| `Action_None` | 565 | 571 | 7 | inferred_complete_timeline |
| `Action_None` | 578 | 599 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 40–599 | 560 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 247–300 | 34 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 342–599 | 244 | 8 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 460–599 | 140 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 551–599 | 49 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `21` (LG)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 284: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [426–454], lower_priority='Action_ZoneBlock' annotated_start=439, effective_Action_ZoneBlock_start=455.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=439, end=215. Clamping end to start.
- ⚠️ Action 'Action_None' range [426-518] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-562] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-571] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-395] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 426, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [426-426] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-448] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-538] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-558] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-569] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-599] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-490] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [439-446] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [464-502] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-528] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-558] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-471] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [426-454] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '15' starts at frame 455, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [455-455] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [470-494] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-599] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [457-469] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-379] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-384] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-425] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-450] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-553] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-581] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-202] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-266] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-293] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-370] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-389] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-394] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-469] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-599] for track '23' has 2 frames without a visible bounding box.
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

</details>