# Play-Annotation-Generator Annotation Review — SplitZone_269

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_269`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 599
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `23` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 14 | START | 14 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 14 | START | 14 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 14 | START | 14 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 14 | START | 14 | 450 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 14 | START | 14 | 599 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 14 | START | 14 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `23` | `Group` | 14 | START | 52 | 450 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 14 | START | 14 | 459 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 14 | START | 14 | 489 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 14 | START | 14 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 14 | START | 14 | 450 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 451 | START | 451 | 518 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `20` | 451 | START | 451 | 504 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `23` | `21` | 451 | START | 451 | 518 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `8` | 451 | START | 451 | 487 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 451 | START | 451 | 518 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 460 | END | 460 | 460 |
| ✅ EXACT | `Action_SplitBlock` | TE | `3` | `3` | 460 | START | 460 | 518 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `14` | 468 | START | 468 | 489 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `5` | 490 | START | 490 | 510 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 518 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 459 | 446 | inferred_complete_timeline |
| `Action_SnapReceive` | 460 | 460 | 1 | inferred_complete_timeline |
| `Action_None` | 461 | 467 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 468 | 489 | 22 | inferred_complete_timeline |
| `Action_None` | 490 | 599 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–510
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 489 | 476 | inferred_complete_timeline |
| `Action_BallCarry` | 490 | 510 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 459 | 446 | inferred_complete_timeline |
| `Action_SplitBlock` | 460 | 518 | 59 | inferred_complete_timeline |
| `Action_None` | 519 | 599 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 14–519
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 102 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 108 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 450 | 332 | inferred_complete_timeline |
| `Action_ZoneBlock` | 451 | 487 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 504 | 509 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 511 | 512 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 514 | 518 | 5 | inferred_complete_timeline |
| `Action_None` | 519 | 519 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 77 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 450 | 367 | inferred_complete_timeline |
| `Action_ZoneBlock` | 451 | 504 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 507 | 516 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 518 | 518 | 1 | inferred_complete_timeline |
| `Action_None` | 519 | 526 | 8 | inferred_complete_timeline |
| `Action_None` | 533 | 599 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 450 | 437 | inferred_complete_timeline |
| `Action_ZoneBlock` | 451 | 518 | 68 | inferred_complete_timeline |
| `Action_None` | 519 | 599 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 52–527
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 52 | 450 | 399 | inferred_complete_timeline |
| `Action_ZoneBlock` | 451 | 518 | 68 | inferred_complete_timeline |
| `Action_None` | 519 | 523 | 5 | inferred_complete_timeline |
| `Action_None` | 526 | 527 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 450 | 437 | inferred_complete_timeline |
| `Action_ZoneBlock` | 451 | 518 | 68 | inferred_complete_timeline |
| `Action_None` | 519 | 599 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 573

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 123 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 599 | 452 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–460
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 460 | 447 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 535 | 522 | inferred_complete_timeline |
| `Action_PreSnap` | 539 | 541 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 566 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 568 | 599 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `24`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 84–487
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 84 | 475 | 392 | inferred_complete_timeline |
| `Action_PreSnap` | 486 | 487 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 488 | 475 | inferred_complete_timeline |
| `Action_PreSnap` | 494 | 496 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 499 | 599 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 581

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 541 | 528 | inferred_complete_timeline |
| `Action_PreSnap` | 546 | 551 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 599 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 14–588
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 588 | 575 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 599 | 586 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 14–80 | 67 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 481–599 | 119 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 512–599 | 85 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 533–599 | 67 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 540–599 | 43 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 578–584 | 7 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 590–597 | 8 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 598–599 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 39 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [14-599] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [490-510] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-460] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-102] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [451-487] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [504-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [511-512] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '8' starts at frame 519, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [519-519] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [451-518] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-588] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-541] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [546-551] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-599] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-599] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-488] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [494-496] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-535] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [539-541] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [553-566] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-599] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [451-504] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [507-516] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-526] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-523] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-527] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-475] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-487] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [512-583] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [587-599] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [540-564] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [578-584] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [590-597] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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