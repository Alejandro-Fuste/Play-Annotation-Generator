# Play-Annotation-Generator Annotation Review — InsideZoneRead_50

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_50`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 42 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 135 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `13` | 134 | START | 134 | 152 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 136 | START | 136 | 236 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `13` | 136 | START | 153 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 136 | START | 136 | 224 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 136 | START | 136 | 177 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 152 | END | 134 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `6` | `5` | 155 | START | 155 | 165 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 169 | START | 169 | 174 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `1` | 175 | START | 175 | 176 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `9` | `8` | 178 | START | 178 | 198 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 236 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 133 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 134 | 152 | 19 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_ReadDefender` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_None` | 175 | 209 | 35 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 283 | 57 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 174 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 177 | 42 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 178 | 198 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 202 | 236 | 35 | inferred_complete_timeline |
| `Action_None` | 237 | 290 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 42–301
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 42 | 45 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 133 | 84 | inferred_complete_timeline |
| `Action_BallSnap` | 134 | 152 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 173 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 236 | 54 | inferred_complete_timeline |
| `Action_None` | 237 | 256 | 20 | inferred_complete_timeline |
| `Action_None` | 260 | 301 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 224 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 236 | 10 | inferred_complete_timeline |
| `Action_None` | 237 | 250 | 14 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 236 | 101 | inferred_complete_timeline |
| `Action_None` | 237 | 324 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 159 | 26 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |
| `Action_None` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 244 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 220 | 87 | inferred_complete_timeline |
| `Action_None` | 229 | 324 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 133 | 24 | inferred_complete_timeline |
| `Action_None` | 134 | 144 | 11 | inferred_complete_timeline |
| `Action_None` | 146 | 189 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 187 | 54 | inferred_complete_timeline |
| `Action_None` | 189 | 315 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_None` | 134 | 329 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 20–294
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 27 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 133 | 105 | inferred_complete_timeline |
| `Action_None` | 134 | 244 | 111 | inferred_complete_timeline |
| `Action_None` | 250 | 294 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–215 | 210 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–122 | 123 | 1 | Undefined position; Undefined team |
| `14` | `20` | Position_Unknown | Team_Unknown | 185–223 | 39 | 1 | Undefined position; Undefined team |
| `15` | `24` | Position_Unknown | Team_Unknown | 204–304 | 101 | 1 | Undefined position; Undefined team |
| `16` | `26` | Position_Unknown | Team_Unknown | 235–304 | 70 | 1 | Undefined position; Undefined team |
| `17` | `27` | Position_Unknown | Team_Unknown | 248–252 | 5 | 1 | Undefined position; Undefined team |
| `18` | `28` | Position_Unknown | Team_Unknown | 253–329 | 77 | 1 | Undefined position; Undefined team |
| `19` | `32` | Position_Unknown | Team_Unknown | 267–280 | 13 | 2 | Undefined position; Undefined team |
| `20` | `34` | Position_Unknown | Team_Unknown | 269–281 | 13 | 1 | Undefined position; Undefined team |
| `21` | `35` | Position_Unknown | Team_Unknown | 269–329 | 61 | 1 | Undefined position; Undefined team |
| `22` | `37` | Position_Unknown | Team_Unknown | 273–286 | 11 | 4 | Undefined position; Undefined team |
| `23` | `40` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `24` | `41` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 320–329 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 102: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 101 frames exceeds threshold 90 frames [start=136, end=236].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 101 frames exceeds threshold 90 frames [start=136, end=236].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 101 frames exceeds threshold 90 frames [start=136, end=236].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [134–152], lower_priority='Action_ZoneBlock' annotated_start=136, effective_Action_ZoneBlock_start=153.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [175-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-159] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-224] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-250] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-203] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [155-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-209] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-283] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-324] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [178-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-290] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-324] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-173] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-236] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-256] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-301] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-223] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-304] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-304] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-280] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-286] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>