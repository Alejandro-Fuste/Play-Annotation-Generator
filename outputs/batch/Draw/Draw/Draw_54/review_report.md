# Play-Annotation-Generator Annotation Review — Draw_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 19
- **Ball Tracks:** 0
- **Action Segments:** 51
- **Validation Warnings:** 47
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
- **Inferred Coverage Segments (Action_None):** 34
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 43 | START | 43 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `10` | `9` | 46 | START | 58 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `3` | `2` | 46 | START | 46 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `3` | 46 | START | 46 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `5` | `4` | 46 | START | 46 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `5` | 46 | START | 46 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 57 | END | 43 | 57 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `7` | `6` | 62 | START | 62 | 82 |
| ✅ EXACT | `Action_BallCarry` | QB | `7` | `6` | 83 | START | 83 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 109 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 62 | 82 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 210 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 75 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_None` | 110 | 128 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 91 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 109 | 13 | inferred_complete_timeline |
| `Action_None` | 110 | 167 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 57 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 109 | 37 | inferred_complete_timeline |
| `Action_None` | 110 | 166 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 109 | 64 | inferred_complete_timeline |
| `Action_None` | 110 | 157 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 104 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 109 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 156 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 121 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 174 | 132 | inferred_complete_timeline |
| `Action_None` | 176 | 189 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 201 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 172 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 210 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 73 | 31 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 32–65 | 34 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 58–210 | 138 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 69–210 | 113 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 128–210 | 76 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 163–165 | 3 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [43–57], lower_priority='Action_PassBlock' annotated_start=46, effective_Action_PassBlock_start=58.
- ⚠️ Action 'Action_None' range [43-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-189] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-172] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-124] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '18' has 1 frames without a visible bounding box.
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

</details>