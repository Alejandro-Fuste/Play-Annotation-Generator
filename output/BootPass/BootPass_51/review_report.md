# Play-Annotation-Generator Annotation Review — BootPass_51

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_51`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 146
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 6
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `16` | `16` | 42 | END | 42 | 42 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `16` | `16` | 66 | START | 66 | 78 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `16` | `16` | 81 | START | 81 | 81 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `16` | `16` | 107 | START | 107 | 122 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `16` | `16` | 123 | START | 123 | 152 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `7` | `7` | 197 | START | 197 | 205 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–269 | 266 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–269 | 269 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–195 | 190 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–191 | 192 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–243 | 197 | 9 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–269 | 248 | 7 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–269 | 263 | 5 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–269 | 257 | 6 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–248 | 244 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–110 | 80 | 8 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–268 | 196 | 9 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–183 | 171 | 11 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–172 | 164 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–268 | 223 | 10 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–252 | 171 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–170 | 153 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–170 | 157 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 56–68 | 11 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 140–172 | 27 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 213–247 | 29 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 222–269 | 48 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 35 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_FakeHandoff' for track '16' has invalid range: start=81, end=65. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-149] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-162] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-100] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-122] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-243] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-79] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-196] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-77] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-94] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-77] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-121] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-177] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-244] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-63] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-67] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-77] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-86] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-52] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-116] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-150] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-259] for track '15' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-172] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '18' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-126] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-166] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-250] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-268] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-102] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-172] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-188] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-252] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-104] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-121] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-170] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-170] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-172] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-247] for track '25' has 1 frames without a visible bounding box.
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

</details>