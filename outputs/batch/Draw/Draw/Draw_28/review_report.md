# Play-Annotation-Generator Annotation Review — Draw_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_28`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 54
- **Validation Warnings:** 53
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
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 35
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 102 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 103 | START | 103 | 117 |
| ✅ EXACT | `Action_PassBlock` | LT | `1` | `0` | 106 | START | 106 | 178 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `10` | `9` | 106 | START | 118 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `4` | `3` | 106 | START | 106 | 153 |
| ✅ EXACT | `Action_PassBlock` | RT | `5` | `4` | 106 | START | 106 | 178 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 117 | END | 103 | 117 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `11` | `10` | 123 | START | 123 | 144 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 145 | START | 145 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 178 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_SnapReceive` | 103 | 117 | 15 | inferred_complete_timeline |
| `Action_None` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 123 | 144 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 329 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 120 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 178 | 73 | inferred_complete_timeline |
| `Action_None` | 179 | 329 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BallSnap` | 103 | 117 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 178 | 61 | inferred_complete_timeline |
| `Action_None` | 179 | 270 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 153 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 178 | 23 | inferred_complete_timeline |
| `Action_None` | 179 | 257 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 178 | 73 | inferred_complete_timeline |
| `Action_None` | 179 | 271 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 329 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 329 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 83 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 109 | 128 | 20 | inferred_complete_timeline |
| `Action_None` | 132 | 311 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 329 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 161 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 102 | 58 | inferred_complete_timeline |
| `Action_None` | 103 | 287 | 185 | inferred_complete_timeline |
| `Action_None` | 290 | 329 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 98–162 | 64 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 104–124 | 17 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 114–329 | 216 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 117–151 | 15 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 149–155 | 7 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 164–329 | 166 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 169–241 | 73 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 173–329 | 157 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 175–196 | 22 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 219–329 | 111 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `10` (C): Annotated start 106 != Inferred start 118
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 56: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [103–117], lower_priority='Action_PassBlock' annotated_start=106, effective_Action_PassBlock_start=118.
- ⚠️ Action 'Action_PassBlock' range [106-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-257] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-287] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-270] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-311] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-146] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-162] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-116] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '22' has 1 frames without a visible bounding box.
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

</details>