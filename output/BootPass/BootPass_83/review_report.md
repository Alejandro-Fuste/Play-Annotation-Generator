# Play-Annotation-Generator Annotation Review — BootPass_83

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_83`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 156
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 5
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `23` | `22` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `10` | `10` | 44 | END | 44 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `10` | `10` | 51 | START | 51 | 65 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `10` | `10` | 82 | START | 82 | 120 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `23` | `22` | 84 | START | 84 | 121 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `10` | `10` | 121 | START | 121 | 131 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `1` | `1` | 175 | START | 175 | 181 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–299 | 300 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–269 | 270 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–262 | 263 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–238 | 238 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–105 | 106 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–299 | 300 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–299 | 296 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–299 | 297 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–85 | 86 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–250 | 232 | 7 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–254 | 251 | 8 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–299 | 300 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–147 | 145 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–299 | 296 | 5 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–299 | 299 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–278 | 279 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–299 | 298 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–72 | 63 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–47 | 48 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–133 | 134 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–256 | 252 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–45 | 46 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 55–269 | 215 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 59–123 | 19 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 105–265 | 161 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 110–123 | 14 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 111–296 | 156 | 8 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 132–166 | 20 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 159–259 | 97 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 162–293 | 118 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 175–299 | 102 | 7 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 203–245 | 27 | 5 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 277–299 | 23 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 286–288 | 3 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 290–291 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 38 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 80 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-269] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-238] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-266] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-78] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-178] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-229] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-237] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [51-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-263] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-290] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-212] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-255] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-273] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-197] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-254] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-195] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-253] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-242] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-249] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-289] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-224] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-245] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-291] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-299] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>