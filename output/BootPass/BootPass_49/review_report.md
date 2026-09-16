# Play-Annotation-Generator Annotation Review — BootPass_49

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 125
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 4
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `20` | `20` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `20` | `20` | 50 | END | 50 | 50 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `20` | `20` | 74 | START | 74 | 87 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `20` | `20` | 90 | START | 90 | 121 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `20` | `20` | 157 | START | 157 | 165 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `1` | `1` | 235 | START | N/A | N/A |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 19–96 | 78 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 19–215 | 195 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 19–210 | 192 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 19–158 | 140 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 19–239 | 214 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 19–201 | 182 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 19–239 | 220 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 19–230 | 212 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 19–186 | 158 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 19–239 | 220 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 19–207 | 179 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 19–239 | 214 | 5 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 19–175 | 157 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 19–239 | 221 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 19–176 | 155 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 19–208 | 178 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 19–214 | 196 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 19–225 | 207 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 19–209 | 168 | 10 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 19–210 | 192 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 19–197 | 179 | 9 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 19–213 | 193 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 100–195 | 82 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 107–111 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 157–158 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 157–162 | 5 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 189–208 | 20 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 190–239 | 44 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 221–225 | 5 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 221–239 | 17 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SecureCatch` on target `1` (Position_Unknown)

### Track Identity Issues

- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 19 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '1' has invalid range: start=235, end=215. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [19-96] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-179] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-169] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-195] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-207] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-207] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-160] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-176] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-199] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-214] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-109] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-130] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-143] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-195] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-209] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-197] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-213] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-115] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-205] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-237] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-232] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-237] for track '29' has 1 frames without a visible bounding box.
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