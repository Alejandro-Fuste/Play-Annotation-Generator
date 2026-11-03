# Play-Annotation-Generator Annotation Review — OutRoutes_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_58`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 42
- **Validation Warnings:** 59
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 30
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | LB | defense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | LB | defense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB | defense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `6` | `6` | 21 | START | 21 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `7` | `7` | 21 | START | 21 | 28 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LG | `8` | `8` | 21 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 21 | START | 21 | 47 |
| ✅ EXACT | `Action_RunOutRoute` | LB | `4` | `4` | 27 | START | 27 | 68 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 27 | END | 27 | 27 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `10` | `10` | 70 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | LB | `4` | `4` | 101 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB | `4` | `4` | 109 | START | N/A | N/A |

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
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 57 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 72 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 47 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 79 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–11
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 28 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 70 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 44 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 68 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 81 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 67 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_RunOutRoute` | 27 | 68 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 75 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–34 | 35 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 11–73 | 40 | 7 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 13–47 | 35 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 20–71 | 51 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 41–60 | 13 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 72–120 | 49 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 74–120 | 47 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 78–120 | 43 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `8` (LG)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `10` (QB)
- ❌ Missing segment for action `Action_SecureCatch` on target `4` (LB)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (LB)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '4' has invalid range: start=101, end=68. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=109, end=68. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '8' has invalid range: start=21, end=11. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '10' has invalid range: start=70, end=57. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-75] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-81] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [27-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-28] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-70] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-57] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-67] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-73] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-47] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-71] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>