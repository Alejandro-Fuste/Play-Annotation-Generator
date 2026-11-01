# Play-Annotation-Generator Annotation Review — InsideZoneRead_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_54`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | Team_Unknown | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | `13` | `12` | 139 | START | 139 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `10` | 141 | START | 141 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 141 | START | 141 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 141 | START | 141 | 255 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 152 | END | 139 | 152 |
| ✅ EXACT | `Action_ReadDefender` | QB | `10` | `9` | 157 | START | 157 | 173 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `13` | `12` | 163 | START | 163 | 255 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `9` | 174 | START | 174 | 182 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `14` | `13` | 183 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 255 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_SnapReceive` | 139 | 152 | 14 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_None` | 183 | 246 | 64 | inferred_complete_timeline |
| `Action_None` | 258 | 261 | 4 | inferred_complete_timeline |
| `Action_None` | 273 | 343 | 71 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 140 | 54 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 164 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 198 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 158 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 173 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 255 | 115 | inferred_complete_timeline |
| `Action_None` | 256 | 337 | 82 | inferred_complete_timeline |
| `Action_None` | 339 | 353 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 213 | 75 | inferred_complete_timeline |
| `Action_None` | 243 | 448 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 214 | 76 | inferred_complete_timeline |
| `Action_None` | 219 | 319 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–317
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 317 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 293 | 155 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 304 | 324 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 176 | 38 | inferred_complete_timeline |
| `Action_None` | 179 | 309 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_None` | 139 | 288 | 150 | inferred_complete_timeline |
| `Action_None` | 325 | 336 | 12 | inferred_complete_timeline |
| `Action_None` | 340 | 341 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–174 | 175 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 13–339 | 253 | 16 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 72–149 | 78 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 85–348 | 243 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 148–226 | 78 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 181–250 | 70 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 203–305 | 103 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 218–308 | 87 | 5 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 223–449 | 212 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 260–322 | 63 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 262–449 | 183 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 270–355 | 86 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 302–345 | 32 | 2 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 323–331 | 8 | 2 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 366–408 | 43 | 1 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 376–440 | 53 | 3 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 383–449 | 67 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 397–399 | 3 | 1 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 428–449 | 22 | 1 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 431–449 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `14` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 110: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 110: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 115 frames exceeds threshold 90 frames [start=141, end=255].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '12' (Unknown) duration 93 frames exceeds threshold 90 frames [start=163, end=255].
- ⚠️ Segment 'Action_BallCarry' for track '13' has invalid range: start=183, end=149. Clamping end to start.
- ⚠️ Action 'Action_None' range [139-176] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-309] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-288] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-293] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-324] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-173] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-317] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-255] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-337] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-353] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-214] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-448] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [174-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-246] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-343] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-68] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-75] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-85] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-140] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-68] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-115] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-137] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [139-145] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-339] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-149] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-305] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-337] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-348] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-190] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-226] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-250] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-305] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-301] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-427] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-322] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-344] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-355] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-408] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-420] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-427] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-440] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-437] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-449] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>