# Play-Annotation-Generator Annotation Review — Counter_388

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_388`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT | defense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `12` | `11` | 35 | START | 35 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 38 | START | 58 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `9` | `8` | 38 | START | 38 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DT | `10` | `9` | 38 | START | 38 | 38 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `5` | `4` | 38 | START | 38 | 62 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 55 | END | 35 | 55 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 57 | START | 57 | 77 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `2` | `1` | 78 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_SnapReceive` | 35 | 55 | 21 | inferred_complete_timeline |
| `Action_None` | 56 | 56 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 57 | 77 | 21 | inferred_complete_timeline |
| `Action_None` | 78 | 112 | 35 | inferred_complete_timeline |
| `Action_None` | 114 | 120 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 74 | 40 | inferred_complete_timeline |
| `Action_None` | 107 | 114 | 8 | inferred_complete_timeline |
| `Action_None` | 118 | 124 | 7 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 38 | 62 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_BallSnap` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 58 | 65 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 72 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 74 | 91 | 18 | inferred_complete_timeline |
| `Action_None` | 92 | 145 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 38 | 60 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 62 | 91 | 30 | inferred_complete_timeline |
| `Action_None` | 92 | 110 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 76 | 42 | inferred_complete_timeline |
| `Action_None` | 80 | 131 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_None` | 50 | 210 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 62 | 28 | inferred_complete_timeline |
| `Action_None` | 65 | 68 | 4 | inferred_complete_timeline |
| `Action_None` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 136 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PullBlock` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_PullBlock` | 42 | 53 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 55 | 91 | 37 | inferred_complete_timeline |
| `Action_None` | 92 | 120 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 59 | 25 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 35 | 63 | 29 | inferred_complete_timeline |
| `Action_None` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_None` | 76 | 102 | 27 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_None` | 112 | 124 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 61–150 | 87 | 2 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 77–210 | 133 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 79–109 | 26 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 83–210 | 128 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 91–96 | 6 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 111–209 | 97 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 146–148 | 3 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 163–199 | 35 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 192–201 | 5 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (3 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `2` (RB)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 778: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=78, end=66. Clamping end to start.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [35–55], lower_priority='Action_DownBlock' annotated_start=38, effective_Action_DownBlock_start=56.
- ⚠️ Action 'Action_None' range [35-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-114] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-59] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-76] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [38-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-63] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-74] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-112] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [38-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' for track '9' starts at frame 38, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullBlock' range [38-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [42-53] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [55-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-120] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-62] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [35-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [52-55] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [58-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-103] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-197] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-109] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-209] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-190] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>