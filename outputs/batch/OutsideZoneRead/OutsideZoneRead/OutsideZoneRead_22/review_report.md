# Play-Annotation-Generator Annotation Review — OutsideZoneRead_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_22`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 2
- **Action Segments:** 68
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 97 | START | 97 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 97 | START | 97 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `10` | 97 | START | 97 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 97 | START | 97 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `4` | `4` | 98 | START | 98 | 117 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `6` | `6` | 99 | START | 99 | 111 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 112 | START | 112 | 125 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 112 | 125 | 14 | inferred_complete_timeline |
| `Action_None` | 126 | 359 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PressEdge` | 98 | 117 | 20 | inferred_complete_timeline |
| `Action_PressEdge` | 122 | 159 | 38 | inferred_complete_timeline |
| `Action_None` | 160 | 174 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 125 | 29 | inferred_complete_timeline |
| `Action_None` | 126 | 217 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 125 | 29 | inferred_complete_timeline |
| `Action_None` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 125 | 29 | inferred_complete_timeline |
| `Action_None` | 126 | 260 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 125 | 29 | inferred_complete_timeline |
| `Action_None` | 126 | 256 | 131 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 162 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 219 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 264 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 339 | 340 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 135 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 213 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 251 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 289 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 136 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 143 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 186 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 283 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–234 | 228 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 131–232 | 102 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 142–359 | 201 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 165–309 | 143 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 168–170 | 3 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 182–359 | 176 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 187–359 | 145 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 195–359 | 165 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 201–359 | 156 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 207–359 | 152 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 250–359 | 110 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 288–326 | 39 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 2 | 3 | 2 | 100.0% | None |
| `16` | `16` | 101 | 101 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [126-256] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-217] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-136] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-283] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [98-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-219] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-143] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-260] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-339] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-213] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-251] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-234] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-232] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-235] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-309] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-250] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-359] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-326] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>