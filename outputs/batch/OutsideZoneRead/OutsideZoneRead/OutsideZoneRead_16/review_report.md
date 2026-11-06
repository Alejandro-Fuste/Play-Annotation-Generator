# Play-Annotation-Generator Annotation Review — OutsideZoneRead_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_16`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `10` | `10` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 157 | START | 157 | 211 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 157 | START | 157 | 211 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 157 | START | 157 | 211 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 157 | START | 157 | 211 |
| ✅ EXACT | `Action_PressEdge` | RB | `10` | `10` | 161 | START | 161 | 169 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `8` | `8` | 162 | START | 162 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `8` | `8` | 192 | START | 192 | 387 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–396
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 162 | 191 | 30 | inferred_complete_timeline |
| `Action_Keep` | 192 | 387 | 196 | inferred_complete_timeline |
| `Action_Keep` | 395 | 396 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PressEdge` | 161 | 169 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 211 | 55 | inferred_complete_timeline |
| `Action_None` | 212 | 239 | 28 | inferred_complete_timeline |
| `Action_None` | 242 | 419 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 211 | 55 | inferred_complete_timeline |
| `Action_None` | 212 | 230 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 156 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 211 | 55 | inferred_complete_timeline |
| `Action_None` | 212 | 242 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 156 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 211 | 55 | inferred_complete_timeline |
| `Action_None` | 212 | 253 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 179 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 190 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 200 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 206 | 419 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 205 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 240 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 171 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 177 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–253 | 240 | 5 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–223 | 224 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 166–246 | 76 | 2 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 211–243 | 25 | 2 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 216–234 | 19 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 225–419 | 195 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 240–419 | 180 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 246–419 | 174 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 250–419 | 169 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 255–419 | 165 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 265–419 | 154 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 278–326 | 9 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 321–419 | 99 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 348–419 | 72 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 371–419 | 49 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 373–419 | 47 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 381–419 | 39 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 409–419 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_Keep` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 50 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 34: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 34: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-201] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-220] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-253] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-240] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [192-387] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [395-396] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [161-169] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-179] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-200] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-205] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-215] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-243] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-234] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-419] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-268] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-419] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-383] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-415] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>