# Play-Annotation-Generator Annotation Review — SlantAndGo_45

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_45`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 269
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 166
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 5
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_SellRoute` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_VerticalStem` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `7` | `7` | 27 | START | 27 | 41 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `13` | `13` | 41 | END | 27 | 41 |
| ✅ EXACT | `Action_SellRoute` | Position_Unknown | `1` | `1` | 77 | START | 77 | 102 |
| ✅ EXACT | `Action_VerticalStem` | Position_Unknown | `1` | `1` | 103 | START | 103 | 199 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `13` | `13` | 128 | START | 128 | 136 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 11–215 | 205 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 11–199 | 189 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 11–269 | 259 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 11–101 | 84 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 11–211 | 201 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 11–41 | 31 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 11–198 | 181 | 5 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 11–197 | 179 | 5 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 11–79 | 66 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 11–135 | 116 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 11–239 | 228 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 11–208 | 198 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 11–189 | 179 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 11–187 | 176 | 6 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 11–223 | 212 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 11–222 | 204 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 11–207 | 192 | 4 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 11–185 | 175 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 11–201 | 191 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 11–196 | 179 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 11–96 | 86 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 11–97 | 77 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 78–195 | 109 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 80–188 | 63 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 90–127 | 36 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 96–98 | 3 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 108–132 | 25 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 114–116 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 120–191 | 68 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 123–134 | 12 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 128–200 | 73 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 131–135 | 5 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 141–148 | 8 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 144–167 | 24 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 149–214 | 45 | 4 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 152–163 | 12 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 154–210 | 57 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 166–181 | 11 | 2 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 218–269 | 52 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 221–269 | 49 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 222–226 | 5 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 231–269 | 39 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 239–258 | 18 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 244–252 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 45 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 45 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 11 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_PassBlock' at frame 30 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 90 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [27-215] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [103-199] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-101] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-211] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-41] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-99] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-72] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-62] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-103] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-135] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-156] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-239] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-208] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-189] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-222] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-180] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-196] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-82] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-182] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-132] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-134] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-167] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-183] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-204] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-269] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-254] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>