# Play-Annotation-Generator Annotation Review — InsideZoneRead_179

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_179`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 73
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 97 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `21` | `20` | 98 | START | 210 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `1` | `0` | 101 | START | 101 | 183 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `11` | 101 | START | 101 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 101 | START | 101 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 101 | START | 101 | 167 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `19` | `18` | 112 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `19` | `18` | 121 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `19` | `18` | 134 | START | 198 | 198 |
| ✅ EXACT | `Action_BallCarry` | QB | `5` | `4` | 141 | START | 141 | 184 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 198 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 184 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 195 | 98 | inferred_complete_timeline |
| `Action_None` | 259 | 294 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 198 | 98 | inferred_complete_timeline |
| `Action_None` | 199 | 234 | 36 | inferred_complete_timeline |
| `Action_None` | 242 | 291 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 156 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 198 | 33 | inferred_complete_timeline |
| `Action_None` | 199 | 248 | 50 | inferred_complete_timeline |
| `Action_None` | 253 | 359 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 167 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 182 | 198 | 17 | inferred_complete_timeline |
| `Action_None` | 199 | 359 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 183 | 83 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 199 | 264 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 196 | 99 | inferred_complete_timeline |
| `Action_None` | 199 | 213 | 15 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 286 | 189 | inferred_complete_timeline |
| `Action_None` | 294 | 359 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 199 | 102 | inferred_complete_timeline |
| `Action_None` | 203 | 226 | 24 | inferred_complete_timeline |
| `Action_None` | 239 | 323 | 85 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 209 | 112 | inferred_complete_timeline |
| `Action_None` | 215 | 233 | 19 | inferred_complete_timeline |
| `Action_None` | 235 | 268 | 34 | inferred_complete_timeline |
| `Action_None` | 270 | 359 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 97 | 46 | inferred_complete_timeline |
| `Action_None` | 98 | 209 | 112 | inferred_complete_timeline |
| `Action_None` | 223 | 245 | 23 | inferred_complete_timeline |
| `Action_None` | 248 | 289 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_None` | 98 | 274 | 177 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–314 | 315 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–36 | 37 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 89–359 | 259 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 183–359 | 177 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 191–235 | 45 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 198–353 | 154 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 201–359 | 159 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 210–359 | 150 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 240–259 | 6 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 249–260 | 12 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 280–359 | 76 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 283–286 | 4 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 307–309 | 3 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 322–359 | 38 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 323–359 | 37 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 162 | 162 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `21` (Position_Unknown): Annotated start 98 != Inferred start 210
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `19` (Position_Unknown)
- ⚠️ `Action_Handoff` for actor_track_id `19` (Position_Unknown): Annotated start 134 != Inferred start 198

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 10 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 358: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 358: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '0' (RT) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 98 frames exceeds threshold 90 frames [start=101, end=198].
- ⚠️ Segment 'Action_SnapReceive' for track '18' has invalid range: start=198, end=112. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '18' has invalid range: start=198, end=133. Clamping end to start.
- ⚠️ Segment 'Action_Handoff' for track '18' has invalid range: start=198, end=140. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=210, end=112. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [101-183] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-286] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-314] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-323] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-359] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-294] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-274] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-268] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-291] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-289] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-359] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-353] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-260] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-344] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-309] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_179'; source metadata written as null.

</details>