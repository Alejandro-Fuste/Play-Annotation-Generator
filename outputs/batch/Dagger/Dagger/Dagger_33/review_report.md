# Play-Annotation-Generator Annotation Review — Dagger_33

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_33`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 1
- **Action Segments:** 75
- **Validation Warnings:** 135
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 0
- **Exact Matches:** 0
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–285 | 276 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–290 | 287 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–287 | 276 | 4 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–289 | 272 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–247 | 248 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–292 | 292 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–280 | 281 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–184 | 182 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–389 | 378 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–231 | 231 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–287 | 261 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–232 | 233 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–196 | 189 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–290 | 286 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–182 | 183 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–287 | 285 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 11–226 | 206 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 174–285 | 108 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 195–229 | 35 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 208–235 | 26 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 208–285 | 67 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 210–226 | 12 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 227–291 | 55 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 237–389 | 148 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 254–286 | 12 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 262–286 | 14 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 273–281 | 7 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 278–389 | 110 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 286–375 | 87 | 4 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 289–389 | 101 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 315–389 | 75 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `26` | 242 | 243 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 71 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-285] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-287] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-287] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-276] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-289] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-292] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-280] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-295] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-205] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-287] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-276] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-290] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-276] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-287] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-201] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-226] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-229] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-213] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-235] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-250] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-285] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-219] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-245] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-281] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-287] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-291] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-318] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-327] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-286] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-286] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-364] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-321] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-362] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-375] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-389] for track '30' has 3 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>