# Play-Annotation-Generator Annotation Review — JetSweep_208

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_208`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `15` | `13` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `14` |
| ⚠️ START CHANGED | `Action_Toss` | Position_Unknown | Team_Unknown | `17` | `14` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `15` | `13` | 46 | START | 49 | 58 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 50 | START | 50 | 56 |
| ✅ EXACT | `Action_LeadBlock` | TE | `7` | `6` | 51 | START | 51 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 51 | START | 58 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 51 | START | 51 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `5` | `4` | 51 | START | 51 | 98 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 51 | START | 51 | 98 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `17` | `14` | 56 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_Toss` | Position_Unknown | `17` | `14` | 69 | START | 70 | 75 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `15` | `13` | 76 | START | 76 | 112 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 98 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 113 | 64 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_LeadBlock` | 51 | 85 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 98 | 48 | inferred_complete_timeline |
| `Action_None` | 99 | 123 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 50 | 56 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 77 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 120 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 98 | 48 | inferred_complete_timeline |
| `Action_None` | 99 | 113 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 98 | 48 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 70 | 21 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 108 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 67 | 18 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 118 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 61 | 12 | inferred_complete_timeline |
| `Action_None` | 63 | 107 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 71 | 22 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 108 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |
| `Action_None` | 64 | 113 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 14–178 | 138 | 5 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 42–113 | 45 | 3 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 49–112 | 63 | 3 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 70–118 | 49 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 71–121 | 51 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 78–220 | 135 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 82–132 | 34 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 103–110 | 8 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 104–113 | 10 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 114–118 | 5 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 119–239 | 120 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 119–214 | 71 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 121–154 | 34 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 126–229 | 87 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 134–239 | 106 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 141–230 | 85 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 157–239 | 79 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 187–205 | 14 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 221–239 | 19 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 231–239 | 9 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (Position_Unknown)
- ⚠️ `Action_Toss` for actor_track_id `17` (Position_Unknown): Annotated start 69 != Inferred start 70

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 417: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 418: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [50–56], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=57.
- ⚠️ Segment 'Action_SnapReceive' for track '14' has invalid range: start=70, end=56. Clamping end to start.
- ⚠️ Action 'Action_None' range [50-70] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-108] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-67] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [51-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-107] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [50-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-77] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 50, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [50-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-99] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [49-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [76-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-220] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-154] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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