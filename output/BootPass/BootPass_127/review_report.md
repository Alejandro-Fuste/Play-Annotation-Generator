# Play-Annotation-Generator Annotation Review — BootPass_127

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_127`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 116
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 3
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `15` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `12` | `12` | 116 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `10` | `10` | 127 | END | 127 | 127 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `10` | `10` | 136 | START | 136 | 150 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `11` | `11` | 151 | START | 151 | 178 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `15` | `13` | 157 | START | 183 | 183 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–389 | 390 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–389 | 386 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–389 | 386 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–389 | 385 | 4 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–389 | 386 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–318 | 311 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–367 | 366 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–389 | 390 | 5 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–389 | 388 | 4 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 14–32 | 19 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 183–265 | 61 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 195–264 | 57 | 6 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 195–244 | 43 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 204–253 | 50 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 206–318 | 111 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 206–264 | 54 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 207–266 | 60 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 207–264 | 57 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 223–265 | 36 | 2 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 336–338 | 3 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 343–389 | 36 | 3 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 361–389 | 29 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 361–362 | 2 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 364–389 | 25 | 2 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 375–385 | 11 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 377–389 | 13 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ThrowPass` on target `12` (Position_Unknown)
- ⚠️ `Action_SecureCatch` for actor_track_id `15` (Position_Unknown): Annotated start 157 != Inferred start 183

### Track Identity Issues

- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 121 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '12' has invalid range: start=116, end=32. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '13' has invalid range: start=183, end=175. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-365] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-379] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-386] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-287] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-318] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-362] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-367] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-265] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-258] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-244] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-311] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-264] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-264] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-338] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-373] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-367] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-389] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-385] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '29' has 1 frames without a visible bounding box.
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

</details>