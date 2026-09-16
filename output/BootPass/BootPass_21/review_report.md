# Play-Annotation-Generator Annotation Review — BootPass_21

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_21`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 188
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 5
- **Exact Matches:** 4
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `19` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `19` | `19` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `19` | `19` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `19` | `19` | 78 | END | 78 | 78 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `19` | `19` | 80 | START | 80 | 95 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `19` | `19` | 96 | START | 96 | 139 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `19` | `19` | 168 | START | 168 | 178 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–269 | 268 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–126 | 127 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–248 | 242 | 4 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–229 | 218 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–96 | 95 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–269 | 261 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–134 | 118 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–262 | 243 | 4 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–269 | 269 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–269 | 270 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–107 | 101 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–269 | 268 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–120 | 111 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–193 | 173 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–84 | 84 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–252 | 200 | 13 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–267 | 235 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–252 | 253 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–230 | 222 | 10 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–239 | 233 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–257 | 219 | 8 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–106 | 100 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 0–196 | 181 | 8 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 0–183 | 117 | 7 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 4–79 | 63 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 38–41 | 4 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 123–269 | 147 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 131–269 | 139 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 133–269 | 132 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 133–248 | 98 | 6 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 142–219 | 19 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 152–177 | 21 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 204–258 | 34 | 4 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 248–264 | 17 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 248–261 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 74 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 112 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-242] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-233] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-218] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-96] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-269] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-111] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-193] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-84] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-188] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-245] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-156] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-267] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-252] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-230] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-235] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-18] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-111] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-185] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-196] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-87] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-140] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-183] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-79] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-41] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-143] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-156] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-154] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-231] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-144] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-177] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-235] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-258] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-261] for track '36' has 1 frames without a visible bounding box.
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