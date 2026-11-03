# Play-Annotation-Generator Annotation Review — OutRoutes_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | RB | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | RB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 21 |
| ⚠️ START CHANGED | `Action_PassBlock` | LT | `19` | `19` | 22 | START | 23 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 22 | START | 22 | 38 |
| ✅ EXACT | `Action_PassBlock` | RG | `7` | `7` | 22 | START | 22 | 180 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 27 | START | 27 | 180 |
| ✅ EXACT | `Action_RunOutRoute` | RB | `16` | `16` | 27 | START | 27 | 101 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 75 | START | 75 | 86 |
| ✅ EXACT | `Action_SecureCatch` | RB | `16` | `16` | 102 | START | 102 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 112 | START | 112 | 159 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 74 | 47 | inferred_complete_timeline |
| `Action_ThrowPass` | 75 | 86 | 12 | inferred_complete_timeline |
| `Action_None` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunOutRoute` | 27 | 101 | 75 | inferred_complete_timeline |
| `Action_SecureCatch` | 102 | 111 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 159 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunOutRoute` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 23 | 180 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 38 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 180 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 87 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
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
| `6` | `6` | Position_Unknown | Team_Unknown | 0–176 | 174 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–180 | 181 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 11–180 | 162 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 75–180 | 96 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 76–180 | 93 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 83–96 | 10 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 91–180 | 49 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 101–102 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 103–180 | 78 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 103–105 | 3 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 127–133 | 6 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 155–168 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `19` (LT): Annotated start 22 != Inferred start 23
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 88: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 88: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [27-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [23-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-59] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-160] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-102] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-130] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>