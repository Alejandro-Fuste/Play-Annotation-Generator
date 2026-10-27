# Play-Annotation-Generator Annotation Review — CrackToss_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_56`
- **Frame Range:** 0 to 274 (275 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 274
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | Team_Unknown | `24` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | `17` | `16` | 123 | START | 123 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `14` | `13` | 126 | START | 126 | 136 |
| ⚠️ START CHANGED | `Action_PullBlock` | Position_Unknown | `24` | `20` | 126 | START | 129 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 136 | END | 123 | 136 |
| ✅ EXACT | `Action_BallCarry` | QB | `6` | `5` | 153 | START | 153 | 238 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_SnapReceive` | 123 | 136 | 14 | inferred_complete_timeline |
| `Action_None` | 137 | 152 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 238 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 138 | 16 | inferred_complete_timeline |
| `Action_None` | 143 | 186 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 231 | 109 | inferred_complete_timeline |
| `Action_None` | 233 | 274 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 216 | 94 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 274 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 274 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 217 | 95 | inferred_complete_timeline |
| `Action_None` | 223 | 257 | 35 | inferred_complete_timeline |
| `Action_None` | 274 | 274 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 216 | 94 | inferred_complete_timeline |
| `Action_None` | 225 | 263 | 39 | inferred_complete_timeline |
| `Action_None` | 267 | 274 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–263 | 263 | 3 | Undefined position; Undefined team |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–238 | 235 | 3 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–268 | 228 | 4 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–274 | 275 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 2–274 | 258 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 20–55 | 16 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 51–158 | 79 | 9 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 64–253 | 171 | 8 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 69–212 | 100 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 116–274 | 148 | 6 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 129–274 | 146 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 129–216 | 88 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 129–159 | 28 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 129–253 | 125 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 131–236 | 106 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 131–216 | 84 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 157–260 | 74 | 4 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 192–274 | 61 | 5 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 223–238 | 13 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 226–274 | 42 | 3 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 226–274 | 41 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 264–274 | 11 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 268–274 | 7 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `14` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `24` (Position_Unknown): Annotated start 126 != Inferred start 129

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 274 as fallback play end.
- ⚠️ Action 'Action_None' range [123-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-217] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-238] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-263] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-257] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-216] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-138] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-186] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-231] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-274] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-263] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-22] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-89] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-95] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [126-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [138-158] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-220] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-186] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [123-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-216] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-216] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-253] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-236] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-216] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-214] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-232] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-255] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-274] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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