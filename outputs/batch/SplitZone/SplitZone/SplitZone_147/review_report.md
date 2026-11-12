# Play-Annotation-Generator Annotation Review — SplitZone_147

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_147`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 629
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 25 | START | 26 | 454 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 25 | START | 26 | 456 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 25 | START | 26 | 457 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 25 | START | 26 | 454 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 25 | START | 26 | 457 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 25 | START | 26 | 457 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 25 | START | 26 | 454 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 25 | START | 26 | 454 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 25 | START | 26 | 457 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 25 | START | 26 | 454 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 25 | START | 26 | 339 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 455 | START | 455 | 464 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `1` | `1` | 457 | START | 457 | 523 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 458 | START | 458 | 492 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `17` | 458 | START | 458 | 493 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `19` | `19` | 458 | START | 458 | 479 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 458 | START | 465 | 475 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 458 | START | 458 | 464 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 464 | END | 455 | 464 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 469 | START | 469 | 474 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `4` | `4` | 475 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 534 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 26–624
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_SnapReceive` | 455 | 464 | 10 | inferred_complete_timeline |
| `Action_None` | 465 | 468 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 469 | 474 | 6 | inferred_complete_timeline |
| `Action_None` | 475 | 624 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 26–339
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 339 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 26–629
- **Visible Samples:** 601

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 456 | 431 | inferred_complete_timeline |
| `Action_SplitBlock` | 457 | 523 | 67 | inferred_complete_timeline |
| `Action_SplitBlock` | 527 | 534 | 8 | inferred_complete_timeline |
| `Action_None` | 535 | 629 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 26–623
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 457 | 432 | inferred_complete_timeline |
| `Action_ZoneBlock` | 458 | 492 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 495 | 534 | 40 | inferred_complete_timeline |
| `Action_None` | 535 | 623 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 26–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 457 | 432 | inferred_complete_timeline |
| `Action_ZoneBlock` | 458 | 479 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 26–629
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_BallSnap` | 455 | 464 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 465 | 475 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 482 | 490 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 493 | 494 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 496 | 497 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 499 | 514 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 527 | 534 | 8 | inferred_complete_timeline |
| `Action_None` | 535 | 629 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 26–474
- **Visible Samples:** 444

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 457 | 432 | inferred_complete_timeline |
| `Action_ZoneBlock` | 458 | 464 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 469 | 470 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 472 | 474 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 26–629
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 457 | 432 | inferred_complete_timeline |
| `Action_ZoneBlock` | 458 | 493 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 511 | 518 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 520 | 534 | 15 | inferred_complete_timeline |
| `Action_None` | 535 | 629 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 579

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 517 | 63 | inferred_complete_timeline |
| `Action_None` | 535 | 554 | 20 | inferred_complete_timeline |
| `Action_None` | 562 | 564 | 3 | inferred_complete_timeline |
| `Action_None` | 566 | 629 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–516
- **Visible Samples:** 485

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 470 | 16 | inferred_complete_timeline |
| `Action_None` | 475 | 484 | 10 | inferred_complete_timeline |
| `Action_None` | 487 | 516 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–499
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 499 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 26–591
- **Visible Samples:** 556

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 528 | 74 | inferred_complete_timeline |
| `Action_None` | 535 | 537 | 3 | inferred_complete_timeline |
| `Action_None` | 540 | 551 | 12 | inferred_complete_timeline |
| `Action_None` | 554 | 591 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 486 | 32 | inferred_complete_timeline |
| `Action_None` | 491 | 629 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 604

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 629 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 26–524
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 524 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 26–629
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 454 | 429 | inferred_complete_timeline |
| `Action_None` | 455 | 603 | 149 | inferred_complete_timeline |
| `Action_None` | 615 | 629 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 338–629 | 288 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 480–629 | 146 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 483–565 | 71 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 500–509 | 9 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 515–629 | 115 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 519–629 | 107 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 522–555 | 9 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 558–629 | 72 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 563–572 | 9 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 577–629 | 53 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 589–628 | 40 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=475, end=339. Clamping end to start.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [455–464], lower_priority='Action_ZoneBlock' annotated_start=458, effective_Action_ZoneBlock_start=465.
- ⚠️ Action 'Action_SplitBlock' range [457-523] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-339] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-517] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-554] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-564] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-629] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-524] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-499] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-486] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-629] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [458-492] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [495-534] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-623] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-470] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-484] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-516] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-624] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-528] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-537] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-551] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-591] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [458-493] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [511-518] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-603] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [458-479] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [455-464] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [465-475] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [482-490] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [493-494] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [496-497] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [499-514] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [458-464] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [469-470] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [472-474] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-610] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-501] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-514] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-629] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-531] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-565] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-506] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-531] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-524] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-548] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-555] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-564] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-572] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-628] for track '32' has 2 frames without a visible bounding box.
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

</details>