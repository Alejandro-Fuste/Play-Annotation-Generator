# Play-Annotation-Generator Annotation Review — SlantAndGo_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_SellRoute` | WR3 | offense | `14` | `14` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 41 | START | 41 | 52 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `12` | 44 | START | 44 | 180 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `16` | 44 | START | 44 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 44 | START | 44 | 130 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `21` | `21` | 44 | START | 53 | 123 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 52 | END | 41 | 52 |
| ✅ EXACT | `Action_SellRoute` | WR3 | `14` | `14` | 73 | START | 73 | 106 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 101 | START | 101 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR3 | `14` | `14` | 107 | START | 107 | 122 |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 52 | 12 | inferred_complete_timeline |
| `Action_None` | 53 | 100 | 48 | inferred_complete_timeline |
| `Action_ThrowPass` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 112 | 132 | 21 | inferred_complete_timeline |
| `Action_None` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SellRoute` | 73 | 106 | 34 | inferred_complete_timeline |
| `Action_VerticalStem` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_VerticalStem` | 127 | 180 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 180 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 130 | 87 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 52 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 123 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 180 | 137 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 135 | 95 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 124 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 109 | 69 | inferred_complete_timeline |
| `Action_None` | 113 | 180 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 129 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 180 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–139 | 140 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–114 | 115 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–180 | 178 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–120 | 114 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–171 | 149 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 129–134 | 6 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 133–180 | 48 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 136–163 | 23 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 146–180 | 35 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 146–180 | 35 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 167–170 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `21` (C): Annotated start 44 != Inferred start 53
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 57: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '20' in grid. Overwriting previous assignment.
- ⚠️ Row 58: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [41–52], lower_priority='Action_PassBlock' annotated_start=44, effective_Action_PassBlock_start=53.
- ⚠️ Action 'Action_None' range [41-139] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-114] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-112] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [107-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [127-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-140] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-123] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>