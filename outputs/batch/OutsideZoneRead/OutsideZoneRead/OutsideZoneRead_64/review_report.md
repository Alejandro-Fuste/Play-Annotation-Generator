# Play-Annotation-Generator Annotation Review — OutsideZoneRead_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_64`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `1` | `1` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 85 | START | 85 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | C | `14` | `14` | 85 | START | 85 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 85 | START | 85 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 85 | START | 85 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 85 | START | 85 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `1` | `1` | 90 | START | 90 | 97 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `5` | 96 | START | 96 | 109 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 110 | START | 110 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 156 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PressEdge` | 90 | 97 | 8 | inferred_complete_timeline |
| `Action_PressEdge` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_PressEdge` | 115 | 155 | 41 | inferred_complete_timeline |
| `Action_None` | 156 | 302 | 147 | inferred_complete_timeline |
| `Action_None` | 308 | 321 | 14 | inferred_complete_timeline |
| `Action_None` | 323 | 324 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 162 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 216 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 329 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 120 | 36 | inferred_complete_timeline |
| `Action_None` | 121 | 162 | 42 | inferred_complete_timeline |
| `Action_None` | 175 | 329 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 120 | 36 | inferred_complete_timeline |
| `Action_None` | 121 | 329 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 120 | 36 | inferred_complete_timeline |
| `Action_None` | 121 | 183 | 63 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 329 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 120 | 36 | inferred_complete_timeline |
| `Action_None` | 121 | 170 | 50 | inferred_complete_timeline |
| `Action_None` | 178 | 187 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 120 | 36 | inferred_complete_timeline |
| `Action_None` | 121 | 282 | 162 | inferred_complete_timeline |
| `Action_None` | 284 | 329 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 145 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 173 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 199 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 88 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 97 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 136 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 172 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 329 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 230 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 242 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–329 | 309 | 10 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 115–150 | 16 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 118–199 | 40 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 129–140 | 12 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 129–144 | 11 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 129–324 | 142 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 130–329 | 188 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 139–327 | 179 | 3 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 170–191 | 22 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 180–329 | 150 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 188–329 | 142 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 191–329 | 139 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 192–329 | 130 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 212–329 | 118 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 240–302 | 63 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 251–329 | 78 | 2 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 280–282 | 3 | 1 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 280–291 | 12 | 1 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 281–293 | 13 | 1 | Undefined position; Undefined team |
| `38` | `42` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `1` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 82 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [90-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [100-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [115-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-162] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-172] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-170] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-230] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-282] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-88] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-136] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-187] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-158] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-199] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-229] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-324] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-322] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-302] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-320] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-282] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-291] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-293] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>