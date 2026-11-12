# Play-Annotation-Generator Annotation Review — SplitZone_209

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_209`
- **Frame Range:** 0 to 809 (810 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 809
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_Handoff` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 5 | START | 6 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 5 | START | 6 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 5 | START | 6 | 430 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 5 | START | 6 | 430 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 5 | START | 6 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 5 | START | 6 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 5 | START | 6 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 5 | START | 6 | 430 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 5 | START | 6 | 427 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 5 | START | 6 | 464 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 428 | START | 428 | 433 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 431 | START | 431 | 701 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 431 | START | 431 | 701 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `19` | `19` | 431 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 431 | START | 431 | 652 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `5` | 431 | START | 434 | 701 |
| ✅ EXACT | `Action_SnapReceive` | RG | `19` | `19` | 433 | END | 428 | 433 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `1` | `1` | 434 | START | 434 | 701 |
| ✅ EXACT | `Action_Handoff` | RG | `19` | `19` | 448 | START | 448 | 464 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 465 | START | 465 | 667 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 701 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–724
- **Visible Samples:** 719

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 724 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–771
- **Visible Samples:** 765

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 464 | 459 | inferred_complete_timeline |
| `Action_BallCarry` | 465 | 667 | 203 | inferred_complete_timeline |
| `Action_BallCarry` | 669 | 771 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–809
- **Visible Samples:** 804

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 809 | 382 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–808
- **Visible Samples:** 803

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 808 | 381 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–746
- **Visible Samples:** 741

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 746 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 6–754
- **Visible Samples:** 749

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 430 | 425 | inferred_complete_timeline |
| `Action_ZoneBlock` | 431 | 701 | 271 | inferred_complete_timeline |
| `Action_None` | 702 | 754 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–780
- **Visible Samples:** 769

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 430 | 425 | inferred_complete_timeline |
| `Action_ZoneBlock` | 431 | 652 | 222 | inferred_complete_timeline |
| `Action_ZoneBlock` | 656 | 694 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 698 | 701 | 4 | inferred_complete_timeline |
| `Action_None` | 702 | 780 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–764
- **Visible Samples:** 759

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_BallSnap` | 428 | 433 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 434 | 701 | 268 | inferred_complete_timeline |
| `Action_None` | 702 | 764 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–751
- **Visible Samples:** 738

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_SnapReceive` | 428 | 433 | 6 | inferred_complete_timeline |
| `Action_None` | 434 | 447 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 448 | 464 | 17 | inferred_complete_timeline |
| `Action_None` | 465 | 700 | 236 | inferred_complete_timeline |
| `Action_None` | 709 | 751 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–762
- **Visible Samples:** 756

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 430 | 425 | inferred_complete_timeline |
| `Action_ZoneBlock` | 431 | 701 | 271 | inferred_complete_timeline |
| `Action_None` | 702 | 735 | 34 | inferred_complete_timeline |
| `Action_None` | 737 | 762 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–788
- **Visible Samples:** 782

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 780 | 353 | inferred_complete_timeline |
| `Action_None` | 782 | 788 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–780
- **Visible Samples:** 771

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 718 | 291 | inferred_complete_timeline |
| `Action_None` | 723 | 780 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–755
- **Visible Samples:** 750

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 755 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–756
- **Visible Samples:** 743

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 661 | 234 | inferred_complete_timeline |
| `Action_None` | 670 | 756 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–766
- **Visible Samples:** 761

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 766 | 339 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–809
- **Visible Samples:** 804

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 809 | 382 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–809
- **Visible Samples:** 804

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 809 | 382 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–735
- **Visible Samples:** 730

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 735 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–809
- **Visible Samples:** 804

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 809 | 382 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–809
- **Visible Samples:** 802

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 729 | 302 | inferred_complete_timeline |
| `Action_None` | 732 | 809 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–808
- **Visible Samples:** 792

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 427 | 422 | inferred_complete_timeline |
| `Action_None` | 428 | 789 | 362 | inferred_complete_timeline |
| `Action_None` | 797 | 799 | 3 | inferred_complete_timeline |
| `Action_None` | 804 | 808 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 6–793 | 788 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 307–427 | 88 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 420–425 | 6 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 678–681 | 4 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 690–691 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 708–709 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 741–809 | 69 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 775–784 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 431 != Inferred start 434
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 420: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 809 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 271 frames exceeds threshold 90 frames [start=431, end=701].
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [428–433], lower_priority='Action_ZoneBlock' annotated_start=431, effective_Action_ZoneBlock_start=434.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RT) duration 271 frames exceeds threshold 90 frames [start=431, end=701].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 271 frames exceeds threshold 90 frames [start=431, end=701].
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=431, end=427. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 271 frames exceeds threshold 90 frames [start=431, end=701].
- ⚠️ Action 'Action_None' range [428-808] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-793] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-766] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-789] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [797-799] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [804-808] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-764] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-729] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-809] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-735] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [465-667] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [669-771] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-780] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [782-788] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-755] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-718] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [723-780] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-809] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-746] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-735] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [737-762] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-661] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [670-756] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-754] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-700] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [709-751] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-724] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [431-652] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [656-694] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [702-780] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-348] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-381] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-388] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-401] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-412] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-427] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-425] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [678-681] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [690-691] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [708-709] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [775-777] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [783-784] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>