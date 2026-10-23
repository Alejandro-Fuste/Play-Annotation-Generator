# Play-Annotation-Generator Annotation Review — BootPass_101

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_101`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 148
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 4
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `6` | `6` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `20` | `20` | 196 | END | 196 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `1` | `1` | 220 | START | 220 | 229 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `6` | `6` | 234 | START | 234 | 279 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `1` | `1` | 235 | START | 235 | 285 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | `5` | `5` | 249 | START | 249 | 262 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `1` | `1` | 294 | START | 294 | 306 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–349 | 350 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–389 | 388 | 7 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–318 | 305 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–389 | 382 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–239 | 240 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–389 | 380 | 8 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–389 | 386 | 6 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–385 | 380 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–389 | 389 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–217 | 218 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–238 | 238 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–237 | 234 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–389 | 299 | 7 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–373 | 362 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–389 | 344 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–255 | 256 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–389 | 356 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 224–225 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 236–255 | 16 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 257–314 | 23 | 4 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 259–276 | 17 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 293–389 | 88 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 302–389 | 88 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 319–355 | 18 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 329–353 | 13 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 336–348 | 5 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 340–370 | 31 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 355–389 | 29 | 3 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 365–389 | 16 | 4 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 374–389 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 196 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 76 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-349] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [220-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-309] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-378] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-387] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-231] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [249-262] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [266-318] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [321-358] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-374] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-369] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-385] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-320] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-351] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-247] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-318] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-364] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-373] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-355] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-255] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-255] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-337] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-240] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-255] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-258] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-268] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-276] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-295] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-314] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-336] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-332] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-341] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-338] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-348] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-370] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-362] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-376] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-389] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-366] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-374] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-387] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>