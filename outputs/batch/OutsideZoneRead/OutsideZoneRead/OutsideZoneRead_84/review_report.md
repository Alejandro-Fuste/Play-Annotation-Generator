# Play-Annotation-Generator Annotation Review — OutsideZoneRead_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_84`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 56
- **Validation Warnings:** 64
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 39
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 14 | START | 14 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 14 | START | 14 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 14 | START | 14 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 14 | START | 14 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 14 | START | 14 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 14 | START | 14 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 14 | START | 14 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 14 | START | 14 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 47 | START | 47 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `2` | `2` | 47 | START | 47 | 61 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 47 | START | 47 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 47 | START | 47 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `6` | 47 | START | 47 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `9` | `9` | 51 | START | 51 | 68 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `12` | 53 | START | 53 | 62 |
| ✅ EXACT | `Action_Handoff` | RB | `9` | `9` | 69 | START | 69 | 79 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 14–122
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 52 | 39 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 53 | 62 | 10 | inferred_complete_timeline |
| `Action_None` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_None` | 74 | 122 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 14–210
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 50 | 37 | inferred_complete_timeline |
| `Action_PressEdge` | 51 | 68 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_PressEdge` | 80 | 102 | 23 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–105
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 49 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 105 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 14–207
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 98 | 38 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 124 | 22 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 207 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–105
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 71 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 100 | 105 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 14–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 98 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 104 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 179 | 67 | inferred_complete_timeline |
| `Action_None` | 183 | 210 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 14–98
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 98 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–110
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 46 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 98 | 52 | inferred_complete_timeline |
| `Action_None` | 99 | 110 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 14–108
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 108 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–189
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 117 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 189 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–202
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 195 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 202 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 14–206
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 206 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 14–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–25
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 25 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 104–132 | 29 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 108–111 | 4 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 111–210 | 100 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 115–210 | 96 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 152–153 | 2 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 160–167 | 8 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 45 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [14-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-195] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-58] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [61-98] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-207] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-189] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [80-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-49] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-105] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '23' has 1 frames without a visible bounding box.
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