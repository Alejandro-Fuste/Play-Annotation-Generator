# Play-Annotation-Generator Annotation Review — Draw_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_20`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Slide`
- **Result Frame:** 239
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 53
- **Validation Warnings:** 46
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 33
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `10` | `9` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `4` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 48 | START | 48 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `10` | `9` | 51 | START | 51 | 116 |
| ✅ EXACT | `Action_PassBlock` | RG | `11` | `10` | 51 | START | 51 | 116 |
| ✅ EXACT | `Action_PassBlock` | RT | `2` | `1` | 51 | START | 51 | 116 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `4` | 51 | START | 51 | 116 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `7` | `6` | 51 | START | 64 | 116 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 63 | END | 48 | 63 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `9` | `8` | 65 | START | 65 | 91 |
| ✅ EXACT | `Action_BallCarry` | QB | `9` | `8` | 92 | START | 92 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 116 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_None` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 65 | 91 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 210 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 180 | 133 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 116 | 66 | inferred_complete_timeline |
| `Action_None` | 117 | 177 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 116 | 66 | inferred_complete_timeline |
| `Action_None` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 200 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 63 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 116 | 53 | inferred_complete_timeline |
| `Action_None` | 117 | 189 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 116 | 66 | inferred_complete_timeline |
| `Action_None` | 117 | 210 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 116 | 66 | inferred_complete_timeline |
| `Action_None` | 117 | 210 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 184 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 57 | 10 | inferred_complete_timeline |
| `Action_None` | 60 | 79 | 20 | inferred_complete_timeline |
| `Action_None` | 81 | 117 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 130 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 77 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 60 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 96–182 | 63 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 124–210 | 82 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 136–210 | 75 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 196–200 | 5 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `7` (C): Annotated start 51 != Inferred start 64

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 30 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_PassBlock' annotated_start=51, effective_Action_PassBlock_start=64.
- ⚠️ Action 'Action_None' range [48-77] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-117] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '20' has 1 frames without a visible bounding box.
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