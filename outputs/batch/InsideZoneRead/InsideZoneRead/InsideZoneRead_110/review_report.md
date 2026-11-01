# Play-Annotation-Generator Annotation Review — InsideZoneRead_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_110`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 22
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `8` | `7` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 14 | START | 14 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 14 | START | 14 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 14 | START | 14 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 14 | START | 14 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 14 | START | 14 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 14 | START | 14 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 31 | START | 31 | 46 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 34 | START | 48 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 34 | START | 34 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 34 | START | 34 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 34 | START | 34 | 113 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 46 | END | 31 | 46 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 54 | START | 54 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `8` | `7` | 61 | START | 61 | 71 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `14` | `13` | 67 | START | 68 | 83 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `12` | 84 | START | 84 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 14–128
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 84 | 128 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 72 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 83 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 14–194
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 113 | 80 | inferred_complete_timeline |
| `Action_None` | 114 | 194 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–175
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 113 | 66 | inferred_complete_timeline |
| `Action_None` | 114 | 175 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 14–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 60 | 27 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 61 | 71 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_None` | 114 | 210 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 14–139
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 34 | 72 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 80 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 113 | 32 | inferred_complete_timeline |
| `Action_None` | 114 | 139 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 14–183
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 183 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 14–137
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 137 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 14–188
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 188 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 14–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 210 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 14–162
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 162 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 14–210 | 181 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 39–42 | 4 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 85–86 | 2 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 100–102 | 3 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 104–109 | 6 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 114–118 | 5 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 139–210 | 72 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 176–210 | 30 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 34 != Inferred start 48
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `8` (5 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `14` (QB): Annotated start 67 != Inferred start 68

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 222: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=47.
- ⚠️ Action 'Action_None' range [31-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-183] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [34-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-80] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [61-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [76-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [80-81] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [86-99] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [31-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [54-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-109] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>