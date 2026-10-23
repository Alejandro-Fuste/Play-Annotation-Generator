# Play-Annotation-Generator Annotation Review — BootPass_3

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_3`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 197
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
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `52` | `35` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `11` | `11` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `11` | `11` | 32 | START | 32 | 52 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `11` | `11` | 55 | START | 55 | 113 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `11` | `11` | 155 | START | N/A | N/A |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `52` | `35` | 225 | START | 225 | 235 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–110 | 110 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–359 | 310 | 11 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–108 | 109 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–168 | 143 | 6 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–297 | 288 | 4 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–180 | 178 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–359 | 342 | 6 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–147 | 126 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–117 | 118 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–108 | 109 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–141 | 142 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–168 | 165 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–102 | 103 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–48 | 35 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–113 | 89 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–359 | 267 | 8 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–359 | 331 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–194 | 195 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–106 | 95 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–131 | 132 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–119 | 119 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 63–119 | 54 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 65–78 | 11 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 100–167 | 38 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 108–159 | 48 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 111–117 | 7 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 112–190 | 77 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 145–155 | 11 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 149–161 | 11 | 2 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 200–281 | 19 | 4 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 210–359 | 141 | 4 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 216–359 | 144 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 220–359 | 128 | 6 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 234–309 | 63 | 5 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 274–292 | 19 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 274–281 | 6 | 2 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 295–298 | 4 | 1 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 322–327 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ThrowPass` on target `11` (Position_Unknown)

### Track Identity Issues

- ⚠️ 41 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 41 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 17 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 82 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '11' has invalid range: start=155, end=141. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-182] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-305] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-327] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-343] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-120] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-159] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-297] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-177] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-196] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-299] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-334] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-131] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-155] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-66] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-107] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-292] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-327] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-294] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-331] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-194] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-106] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-119] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-119] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-102] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-121] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-151] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-117] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-150] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-190] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-155] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-161] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-210] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-303] for track '33' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-331] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-264] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-341] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-296] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-309] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-292] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-327] for track '40' has 1 frames without a visible bounding box.
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

</details>