# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_35

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_35`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 174
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `24` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 11 | START | 11 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 11 | START | 11 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 11 | START | 11 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 11 | START | 11 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 11 | START | 11 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 11 | START | 11 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `8` | `8` | 47 | START | 47 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `10` | 47 | START | 47 | 62 |
| ✅ EXACT | `Action_ZoneBlock` | C | `11` | `11` | 47 | START | 47 | 83 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 47 | START | 47 | 76 |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `24` | `20` | 72 | START | 107 | 107 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 11–329
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_PressEdge` | 47 | 60 | 14 | inferred_complete_timeline |
| `Action_PressEdge` | 65 | 66 | 2 | inferred_complete_timeline |
| `Action_PressEdge` | 71 | 100 | 30 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_None` | 176 | 329 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 11–112
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 112 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–94
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 71 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 94 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 11–83
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 83 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 11–141
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 76 | 30 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 141 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–165
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 86 | 23 | inferred_complete_timeline |
| `Action_None` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 159 | 31 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 18–154
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 136 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 154 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 11–63
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 63 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–168
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 129 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 168 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 11–138
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 138 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 11–223
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 103 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 139 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 202 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 223 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–161
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 97 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 145 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 161 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–161
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 116 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 161 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 11–266 | 180 | 5 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 15–121 | 85 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 44–164 | 118 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 53–149 | 81 | 4 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 79–92 | 13 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 81–143 | 46 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 98–119 | 22 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 107–194 | 58 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 117–278 | 162 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 120–329 | 210 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 132–329 | 191 | 5 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 151–173 | 23 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 154–159 | 6 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 156–159 | 4 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 162–329 | 160 | 4 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 163–329 | 158 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 163–329 | 163 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 168–194 | 27 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 176–329 | 141 | 4 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 184–286 | 99 | 3 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 186–201 | 16 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 186–329 | 137 | 2 | Undefined position; Undefined team |
| `35` | `57` | Position_Unknown | Team_Unknown | 188–221 | 34 | 1 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 196–329 | 134 | 1 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 201–329 | 129 | 1 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 204–329 | 126 | 1 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |
| `40` | `65` | Position_Unknown | Team_Unknown | 208–329 | 114 | 3 | Undefined position; Undefined team |
| `41` | `66` | Position_Unknown | Team_Unknown | 208–251 | 41 | 3 | Undefined position; Undefined team |
| `42` | `68` | Position_Unknown | Team_Unknown | 263–264 | 2 | 1 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 276–327 | 52 | 1 | Undefined position; Undefined team |
| `44` | `74` | Position_Unknown | Team_Unknown | 282–329 | 41 | 2 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 286–310 | 25 | 1 | Undefined position; Undefined team |
| `46` | `77` | Position_Unknown | Team_Unknown | 288–301 | 14 | 1 | Undefined position; Undefined team |
| `47` | `80` | Position_Unknown | Team_Unknown | 320–329 | 6 | 2 | Undefined position; Undefined team |
| `48` | `82` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `24` (Position_Unknown): Annotated start 72 != Inferred start 107

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 99 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 72: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_Handoff' for track '20' has invalid range: start=107, end=84. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [11-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-139] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-202] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-71] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-138] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-112] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-145] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [47-60] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [65-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [71-100] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-121] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-56] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-89] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-121] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-119] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-278] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-173] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-253] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-288] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-293] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-279] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-262] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-313] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-189] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-286] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-207] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-329] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-329] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-234] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-231] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-243] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-251] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-327] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-292] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-310] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-301] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>