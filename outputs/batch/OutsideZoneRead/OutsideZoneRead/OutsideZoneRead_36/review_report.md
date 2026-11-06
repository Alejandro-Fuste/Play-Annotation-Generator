# Play-Annotation-Generator Annotation Review — OutsideZoneRead_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_36`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `5` | `5` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `0` | `0` | 92 | START | 92 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 92 | START | 92 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `8` | `8` | 92 | START | 92 | 118 |
| ✅ EXACT | `Action_PressEdge` | RB | `5` | `5` | 100 | START | 100 | 104 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `11` | 100 | START | 100 | 112 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 113 | START | 113 | 123 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 100 | 112 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 229 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PressEdge` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 241 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 118 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_None` | 135 | 269 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 105 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 108 | 126 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 126 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 134 | 1 | inferred_complete_timeline |
| `Action_None` | 135 | 156 | 22 | inferred_complete_timeline |
| `Action_None` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 90 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 167 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 183 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 208 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 260 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–258
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 120 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 237 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 258 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 99 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 141 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 269 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 213 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 234 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 94–269 | 176 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 94–161 | 53 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 105–159 | 52 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 116–269 | 149 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 119–149 | 31 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 126–269 | 144 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 138–269 | 132 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 157–209 | 51 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 170–204 | 35 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 204–269 | 63 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 212–217 | 6 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 236–269 | 34 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 74: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 74: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [92-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-105] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [108-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [100-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-142] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-234] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-261] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-167] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-260] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-189] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-206] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-237] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-269] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '28' has 1 frames without a visible bounding box.
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

</details>