# Play-Annotation-Generator Annotation Review — Draw_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_78`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 29 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 27 | START | 27 | 39 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `11` | `10` | 30 | START | 48 | 129 |
| ✅ EXACT | `Action_PassBlock` | LT | `3` | `2` | 30 | START | 30 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `5` | `4` | 30 | START | 30 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `6` | `5` | 30 | START | 30 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `7` | `6` | 30 | START | 30 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 40 | END | 27 | 40 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `12` | `11` | 47 | START | 47 | 55 |
| ✅ EXACT | `Action_BallCarry` | QB | `12` | `11` | 56 | START | 56 | 71 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_None` | 41 | 46 | 6 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 71 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 108 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 79 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 129 | 48 | inferred_complete_timeline |
| `Action_None` | 130 | 165 | 36 | inferred_complete_timeline |
| `Action_None` | 173 | 190 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 39 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 129 | 82 | inferred_complete_timeline |
| `Action_None` | 130 | 162 | 33 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 57 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 47 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 55 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 75 | 49 | inferred_complete_timeline |
| `Action_None` | 98 | 201 | 104 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 55 | 29 | inferred_complete_timeline |
| `Action_None` | 63 | 117 | 55 | inferred_complete_timeline |
| `Action_None` | 119 | 203 | 85 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 201 | 175 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 210 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–45
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 45 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 47 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 65–88 | 23 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 80–102 | 23 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 85–91 | 7 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 100–210 | 109 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 109–117 | 9 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 120–210 | 91 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 120–197 | 78 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 145–147 | 3 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 173–206 | 34 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 179–210 | 21 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `11` (C): Annotated start 30 != Inferred start 48
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [27–40], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=41.
- ⚠️ Action 'Action_None' range [27-45] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-47] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-39] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-51] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-190] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-117] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [27-39] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-71] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-91] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-202] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-197] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '23' has 1 frames without a visible bounding box.
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

</details>