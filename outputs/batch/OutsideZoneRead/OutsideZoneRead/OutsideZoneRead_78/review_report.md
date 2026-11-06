# Play-Annotation-Generator Annotation Review — OutsideZoneRead_78

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_78`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 97
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 18 | START | 18 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `10` | 18 | START | 18 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 18 | START | 18 | 44 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_PressEdge` | RB | `5` | `5` | 27 | START | 27 | 89 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `2` | `2` | 30 | START | 30 | 39 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 40 | START | 40 | 55 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_None` | 56 | 85 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PressEdge` | 27 | 89 | 63 | inferred_complete_timeline |
| `Action_None` | 90 | 194 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 98 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 144 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 95 | 20 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 51 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 76 | 123 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 44 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 102 | 27 | inferred_complete_timeline |
| `Action_None` | 108 | 179 | 72 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 107 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 151 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 154 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 210 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 84 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 107 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 122 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 147 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 65 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 210 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 20–117 | 97 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 35–51 | 10 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 38–53 | 15 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 74–210 | 123 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 85–86 | 2 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 92–210 | 117 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 94–132 | 39 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 99–126 | 28 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 102–196 | 89 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 105–169 | 53 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 105–210 | 106 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 108–210 | 99 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 138–210 | 73 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 140–161 | 22 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 201–210 | 10 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 64 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [76-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-179] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-85] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-122] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-194] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-95] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-151] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-73] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-154] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [18-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-62] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-102] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-117] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-53] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-107] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-166] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-126] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-148] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-126] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-210] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '29' has 1 frames without a visible bounding box.
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

</details>