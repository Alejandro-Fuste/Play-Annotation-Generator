# Play-Annotation-Generator Annotation Review — Draw_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_68`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 15
- **Ball Tracks:** 0
- **Action Segments:** 47
- **Validation Warnings:** 42
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 28
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `12` | `11` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 27 | START | 27 | 31 |
| ✅ EXACT | `Action_PassBlock` | RT | `1` | `0` | 30 | START | 30 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `10` | 30 | START | 59 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `4` | `3` | 30 | START | 30 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `6` | `5` | 30 | START | 30 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `8` | `7` | 30 | START | 30 | 64 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `12` | `11` | 41 | END | 36 | 41 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | Position_Unknown | `12` | `11` | 49 | START | 49 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `12` | `11` | 82 | START | 82 | 165 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 64 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 150 | 59 | inferred_complete_timeline |
| `Action_None` | 151 | 162 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 107 | 78 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 150 | 26 | inferred_complete_timeline |
| `Action_None` | 151 | 164 | 14 | inferred_complete_timeline |
| `Action_None` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 121 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 147 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 180 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 99 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 121 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 132 | 135 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 180 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 146 | 117 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 180 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 146 | 120 | inferred_complete_timeline |
| `Action_None` | 156 | 180 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 174 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 177 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 36–180 | 144 | 5 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 175–178 | 4 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_PassBlock' range [30-146] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-99] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [132-135] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-64] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [83-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [27-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-121] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [49-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-165] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [167-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.

</details>