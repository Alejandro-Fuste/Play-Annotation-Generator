# Play-Annotation-Generator Annotation Review — BootPass_123

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_123`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 180
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `6` | `6` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `6` | `6` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `6` | `6` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `6` | `6` | 50 | START | 50 | 73 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `6` | `6` | 74 | START | 74 | 103 |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | `3` | `3` | 130 | START | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `20` | `20` | 186 | START | 186 | 188 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `2` | `2` | 210 | START | 210 | 222 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–179 | 180 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–266 | 221 | 8 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–122 | 119 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–277 | 278 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–270 | 262 | 3 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–271 | 272 | 6 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–329 | 330 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–129 | 130 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–179 | 164 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–145 | 139 | 5 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–186 | 187 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–278 | 279 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–261 | 262 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–300 | 298 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–329 | 313 | 8 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–251 | 226 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–170 | 171 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–75 | 65 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–188 | 189 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–92 | 93 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 51–244 | 179 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 74–107 | 21 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 110–239 | 130 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 132–134 | 3 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 136–250 | 88 | 6 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 171–253 | 59 | 8 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 183–242 | 60 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 188–274 | 77 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 197–329 | 133 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 206–244 | 37 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 217–236 | 20 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 222–247 | 24 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 247–260 | 14 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 261–315 | 55 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 261–329 | 69 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 276–283 | 7 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 291–296 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_RunFlatRoute` on target `3` (Position_Unknown)

### Track Identity Issues

- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 40 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_RunFlatRoute' for track '3' has invalid range: start=130, end=122. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-76] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-207] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-270] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-271] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-201] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-224] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [186-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-188] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-244] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-107] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-195] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-212] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-242] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-236] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-315] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-283] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-296] for track '41' has 1 frames without a visible bounding box.
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

</details>