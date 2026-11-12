# Play-Annotation-Generator Annotation Review — SplitZone_190

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_190`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 14 | START | 15 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 14 | START | 15 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 14 | START | 15 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 14 | START | 15 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 14 | START | 51 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 14 | START | 58 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 14 | START | 15 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 14 | START | 15 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `14` | `13` | 185 | START | 185 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `1` | 188 | START | 188 | 267 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 188 | START | 188 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 188 | START | 188 | 196 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `14` | `13` | 188 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 188 | START | 188 | 279 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 201 | END | 185 | 201 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 208 | START | 208 | 220 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `15` | `14` | 221 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 279 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 15–314
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_SnapReceive` | 185 | 201 | 17 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 208 | 220 | 13 | inferred_complete_timeline |
| `Action_None` | 221 | 230 | 10 | inferred_complete_timeline |
| `Action_None` | 280 | 287 | 8 | inferred_complete_timeline |
| `Action_None` | 289 | 314 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 58–106
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 58 | 84 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 106 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 15–212
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 212 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 15–270
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 187 | 173 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 267 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 269 | 270 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 15–300
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 187 | 173 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 249 | 4 | inferred_complete_timeline |
| `Action_None` | 280 | 297 | 18 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 51–304
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 51 | 184 | 134 | inferred_complete_timeline |
| `Action_BallSnap` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_BallSnap` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_None` | 284 | 292 | 9 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 15–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 187 | 173 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 279 | 92 | inferred_complete_timeline |
| `Action_None` | 280 | 329 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 15–203
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 187 | 173 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 203 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 15–298
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 260 | 76 | inferred_complete_timeline |
| `Action_None` | 267 | 279 | 13 | inferred_complete_timeline |
| `Action_None` | 287 | 298 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 259 | 75 | inferred_complete_timeline |
| `Action_None` | 261 | 329 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 15–274
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 255 | 71 | inferred_complete_timeline |
| `Action_None` | 272 | 274 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 15–303
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 281 | 97 | inferred_complete_timeline |
| `Action_None` | 286 | 293 | 8 | inferred_complete_timeline |
| `Action_None` | 295 | 297 | 3 | inferred_complete_timeline |
| `Action_None` | 299 | 303 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 15–297
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 297 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 15–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 260 | 76 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 329 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 15–230
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 184 | 170 | inferred_complete_timeline |
| `Action_None` | 185 | 230 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 209–329 | 111 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 213–307 | 95 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 217–232 | 16 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 252–329 | 73 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 253–329 | 74 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 269–329 | 56 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 274–329 | 44 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 312–329 | 18 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 317–329 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `14` (C)
- ❌ Missing segment for action `Action_BallCarry` on target `15` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 92 frames exceeds threshold 90 frames [start=188, end=279].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 92 frames exceeds threshold 90 frames [start=188, end=279].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 92 frames exceeds threshold 90 frames [start=188, end=279].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [185–201], lower_priority='Action_ZoneBlock' annotated_start=188, effective_Action_ZoneBlock_start=202.
- ⚠️ Segment 'Action_BallCarry' for track '14' has invalid range: start=221, end=106. Clamping end to start.
- ⚠️ Action 'Action_None' range [185-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-267] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [269-270] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-281] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-303] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-260] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-260] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-298] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-184] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-314] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [188-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [246-249] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-297] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [185-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [190-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-232] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-307] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-302] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-298] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '22' has 1 frames without a visible bounding box.
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

</details>