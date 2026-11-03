# Play-Annotation-Generator Annotation Review — OutRoutes_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_46`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | LB1 | defense | `1` | `1` |
| ✅ EXACT | `Action_SecureCatch` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `9` | `Group` | 0 | START | 0 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `12` | `12` | 13 | START | 13 | 79 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `2` | 13 | START | 13 | 16 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `4` | `4` | 13 | START | 13 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `6` | `6` | 13 | START | 13 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | RT | `2` | `2` | 17 | START | 17 | 68 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `1` | `1` | 17 | END | 17 | 17 |
| ✅ EXACT | `Action_ThrowPass` | LB1 | `1` | `1` | 44 | START | 44 | 50 |
| ✅ EXACT | `Action_SecureCatch` | RT | `2` | `2` | 72 | START | 72 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `2` | `2` | 80 | START | 80 | 89 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 89 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 47 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 81 | 85 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 50 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 60 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 50 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 68 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 97 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 16 | 4 | inferred_complete_timeline |
| `Action_RunOutRoute` | 17 | 68 | 52 | inferred_complete_timeline |
| `Action_RunOutRoute` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_SecureCatch` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 80 | 89 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 97 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 85 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 137 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 17 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 43 | 26 | inferred_complete_timeline |
| `Action_ThrowPass` | 44 | 50 | 7 | inferred_complete_timeline |
| `Action_None` | 51 | 92 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–158 | 141 | 5 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 23–66 | 44 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 44–97 | 40 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 58–86 | 29 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 66–90 | 25 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 69–89 | 19 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 70–88 | 19 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 86–137 | 50 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 95–110 | 16 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 96–141 | 46 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 151–180 | 30 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 153–154 | 2 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 164–178 | 14 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 165–178 | 9 | 2 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 54: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [17-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [80-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-64] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-137] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-50] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-68] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-47] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-89] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [81-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-67] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-86] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-83] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-88] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>