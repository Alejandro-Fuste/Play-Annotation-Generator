# Play-Annotation-Generator Annotation Review — SplitZone_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_101`
- **Frame Range:** 0 to 719 (720 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 719
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 80
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
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 517 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 517 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 312 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 520 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `23` | `Group` | 0 | START | 104 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 517 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 525 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 520 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 543 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 406 | BOUNDARY | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `11` | `11` | 518 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `11` | `11` | 521 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `14` | `14` | 521 | START | 521 | 712 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `19` | 521 | START | 521 | 572 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 521 | START | 521 | 546 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 521 | START | 521 | 719 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `4` | `4` | 526 | START | 526 | 648 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 530 | END | 518 | 530 |
| ✅ EXACT | `Action_Handoff` | QB | `1` | `1` | 535 | START | 535 | 543 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `9` | 544 | START | 544 | 592 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_SnapReceive` | 518 | 530 | 13 | inferred_complete_timeline |
| `Action_None` | 531 | 534 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 535 | 543 | 9 | inferred_complete_timeline |
| `Action_None` | 544 | 549 | 6 | inferred_complete_timeline |
| `Action_None` | 551 | 689 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 719

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 543 | 544 | inferred_complete_timeline |
| `Action_BallCarry` | 544 | 592 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 594 | 719 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 719 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–633
- **Visible Samples:** 634

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 633 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `23`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 104–719
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 160 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 517 | 354 | inferred_complete_timeline |
| `Action_None` | 518 | 603 | 86 | inferred_complete_timeline |
| `Action_None` | 606 | 646 | 41 | inferred_complete_timeline |
| `Action_None` | 649 | 719 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 718

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 525 | 526 | inferred_complete_timeline |
| `Action_SplitBlock` | 526 | 648 | 123 | inferred_complete_timeline |
| `Action_SplitBlock` | 651 | 719 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 520 | 521 | inferred_complete_timeline |
| `Action_ZoneBlock` | 521 | 719 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 623

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 315 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 520 | 199 | inferred_complete_timeline |
| `Action_ZoneBlock` | 521 | 546 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 554 | 559 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 561 | 719 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 323 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–712
- **Visible Samples:** 713

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 520 | 521 | inferred_complete_timeline |
| `Action_ZoneBlock` | 521 | 712 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–719
- **Visible Samples:** 710

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 520 | 494 | inferred_complete_timeline |
| `Action_ZoneBlock` | 521 | 572 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 577 | 579 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 582 | 719 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 719 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–606
- **Visible Samples:** 605

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 600 | 83 | inferred_complete_timeline |
| `Action_None` | 603 | 606 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–593
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 547 | 30 | inferred_complete_timeline |
| `Action_None` | 588 | 593 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–603
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 573 | 56 | inferred_complete_timeline |
| `Action_None` | 577 | 585 | 9 | inferred_complete_timeline |
| `Action_None` | 587 | 589 | 3 | inferred_complete_timeline |
| `Action_None` | 599 | 603 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 719 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 717

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 645 | 128 | inferred_complete_timeline |
| `Action_None` | 649 | 719 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 718

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 635 | 118 | inferred_complete_timeline |
| `Action_None` | 637 | 676 | 40 | inferred_complete_timeline |
| `Action_None` | 678 | 719 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 719 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 718

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 564 | 47 | inferred_complete_timeline |
| `Action_None` | 567 | 719 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–660
- **Visible Samples:** 661

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 660 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–719
- **Visible Samples:** 720

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 517 | 518 | inferred_complete_timeline |
| `Action_None` | 518 | 719 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–44 | 45 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 46–53 | 6 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 157–164 | 8 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 216–218 | 3 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 387–552 | 166 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 571–719 | 148 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 596–719 | 124 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 618–625 | 7 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 639–719 | 81 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 659–719 | 61 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 672–685 | 12 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 681–719 | 39 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 704–719 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `11` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 199 frames exceeds threshold 90 frames [start=521, end=719].
- ⚠️ Segment 'Action_BallSnap' for track '11' has invalid range: start=518, end=323. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=521, end=323. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 192 frames exceeds threshold 90 frames [start=521, end=712].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 199 frames exceeds threshold 90 frames [start=521, end=719].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 199 frames exceeds threshold 90 frames [start=521, end=719].
- ⚠️ Action 'Action_None' range [518-719] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-549] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-689] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-633] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [526-648] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-645] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-660] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [544-592] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-323] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-635] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [637-676] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-564] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [521-712] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-547] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-593] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-573] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-585] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [587-589] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-603] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-520] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [521-572] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [577-579] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-600] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-606] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [521-546] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [554-559] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-603] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-646] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-552] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-628] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-622] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [624-625] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [672-680] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [683-685] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>