# Play-Annotation-Generator Annotation Review — SplitZone_196

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_196`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 719
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `15` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 11 | START | 12 | 482 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 11 | START | 12 | 482 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 11 | START | 12 | 482 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 11 | START | 12 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 11 | START | 33 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 11 | START | 12 | 507 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 11 | START | 12 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 11 | START | 12 | 482 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 11 | START | 12 | 479 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 480 | START | 480 | 496 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `0` | `0` | 483 | START | 483 | 607 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 483 | START | 483 | 512 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 483 | START | 483 | 498 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `5` | 483 | START | 497 | 513 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 483 | START | 483 | 519 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `15` | `15` | 486 | START | 486 | 607 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 496 | END | 480 | 496 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 503 | START | 503 | 507 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 508 | START | 508 | 512 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 607 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 12–719
- **Visible Samples:** 669

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_SnapReceive` | 480 | 496 | 17 | inferred_complete_timeline |
| `Action_None` | 497 | 502 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 503 | 507 | 5 | inferred_complete_timeline |
| `Action_None` | 508 | 575 | 68 | inferred_complete_timeline |
| `Action_None` | 587 | 683 | 97 | inferred_complete_timeline |
| `Action_None` | 685 | 688 | 4 | inferred_complete_timeline |
| `Action_None` | 690 | 691 | 2 | inferred_complete_timeline |
| `Action_None` | 718 | 719 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 12–719
- **Visible Samples:** 703

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 507 | 496 | inferred_complete_timeline |
| `Action_BallCarry` | 508 | 512 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 518 | 719 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 33–653
- **Visible Samples:** 614

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 479 | 447 | inferred_complete_timeline |
| `Action_None` | 480 | 492 | 13 | inferred_complete_timeline |
| `Action_None` | 500 | 653 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 12–719
- **Visible Samples:** 707

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 485 | 456 | inferred_complete_timeline |
| `Action_SplitBlock` | 486 | 607 | 122 | inferred_complete_timeline |
| `Action_None` | 608 | 719 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–709
- **Visible Samples:** 697

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 482 | 471 | inferred_complete_timeline |
| `Action_ZoneBlock` | 483 | 607 | 125 | inferred_complete_timeline |
| `Action_None` | 608 | 702 | 95 | inferred_complete_timeline |
| `Action_None` | 704 | 709 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–519
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 482 | 471 | inferred_complete_timeline |
| `Action_ZoneBlock` | 483 | 519 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 12–513
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_BallSnap` | 480 | 496 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 497 | 513 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–653
- **Visible Samples:** 636

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 482 | 471 | inferred_complete_timeline |
| `Action_ZoneBlock` | 483 | 512 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 515 | 534 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 539 | 607 | 69 | inferred_complete_timeline |
| `Action_None` | 608 | 653 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–498
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 482 | 471 | inferred_complete_timeline |
| `Action_ZoneBlock` | 483 | 498 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–541
- **Visible Samples:** 484

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 491 | 12 | inferred_complete_timeline |
| `Action_None` | 535 | 536 | 2 | inferred_complete_timeline |
| `Action_None` | 540 | 541 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–217
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 66 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 114 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 137 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 167 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 217 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–536
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 488 | 9 | inferred_complete_timeline |
| `Action_None` | 535 | 536 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 12–719
- **Visible Samples:** 708

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 719 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–719
- **Visible Samples:** 707

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 695 | 216 | inferred_complete_timeline |
| `Action_None` | 697 | 719 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 12–565
- **Visible Samples:** 544

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 535 | 56 | inferred_complete_timeline |
| `Action_None` | 546 | 565 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 12–719
- **Visible Samples:** 707

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 617 | 138 | inferred_complete_timeline |
| `Action_None` | 619 | 719 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 12–716
- **Visible Samples:** 701

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 479 | 468 | inferred_complete_timeline |
| `Action_None` | 480 | 706 | 227 | inferred_complete_timeline |
| `Action_None` | 711 | 716 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 29–719
- **Visible Samples:** 686

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 479 | 451 | inferred_complete_timeline |
| `Action_None` | 480 | 572 | 93 | inferred_complete_timeline |
| `Action_None` | 578 | 719 | 142 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 12–30 | 19 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 381–601 | 221 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 493–719 | 227 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 504–675 | 169 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 510–513 | 4 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 512–661 | 135 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 555–657 | 101 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 558–673 | 116 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 567–580 | 12 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 579–661 | 82 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 581–586 | 6 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 624–719 | 96 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 627–719 | 57 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 647–709 | 63 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 664–719 | 56 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 716–717 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 483 != Inferred start 497
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 125 frames exceeds threshold 90 frames [start=483, end=607].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 125 frames exceeds threshold 90 frames [start=483, end=607].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [480–496], lower_priority='Action_ZoneBlock' annotated_start=483, effective_Action_ZoneBlock_start=497.
- ⚠️ Action 'Action_None' range [608-702] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [704-709] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [483-512] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [515-534] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [539-607] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-653] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-617] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-535] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-565] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [508-512] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [497-513] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-488] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [483-519] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-695] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-575] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-683] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [685-688] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-691] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-706] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [711-716] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-491] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-536] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-30] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [483-498] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [486-607] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-66] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-85] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-114] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-167] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-572] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-492] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-653] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-601] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-506] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-675] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-513] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-514] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-531] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-661] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-574] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-657] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-673] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-570] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-580] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-655] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [657-661] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-586] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [627-650] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [661-686] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [647-709] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [716-717] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>