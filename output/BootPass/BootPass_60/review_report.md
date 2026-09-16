# Play-Annotation-Generator Annotation Review — BootPass_60

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_60`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 174
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 4
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `15` | `15` | 65 | END | 65 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `15` | `15` | 74 | START | 74 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | `15` | `15` | 88 | START | 88 | 92 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `2` | `2` | 97 | START | 97 | 135 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `15` | `15` | 135 | START | 135 | 146 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `2` | `2` | 214 | START | 214 | 221 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–87 | 88 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–173 | 174 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–359 | 313 | 8 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–167 | 168 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–128 | 129 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–164 | 102 | 3 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–389 | 366 | 4 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–114 | 102 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–339 | 331 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–144 | 143 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–136 | 126 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–103 | 100 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–167 | 168 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–136 | 137 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–58 | 59 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–389 | 376 | 10 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 18–153 | 118 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 72–132 | 61 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 81–117 | 37 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 90–171 | 82 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 96–102 | 7 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 106–111 | 6 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 108–389 | 262 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 111–136 | 26 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 114–163 | 50 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 118–148 | 31 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 150–389 | 215 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 154–332 | 135 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 157–166 | 10 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 168–222 | 52 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 168–173 | 6 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 168–188 | 21 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 171–177 | 7 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 172–203 | 32 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 174–389 | 184 | 4 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 181–256 | 76 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 260–265 | 6 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 267–344 | 78 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 273–312 | 31 | 3 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 291–296 | 6 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 376–389 | 14 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 384–389 | 6 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ 47 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 47 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 57 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 94 |
| Missing visible bounding boxes during action | 78 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-238] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-95] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-339] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [74-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [85-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' for track '15' starts at frame 88, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BootAway' range [88-92] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-21] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-60] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-153] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-360] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-296] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-222] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-173] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-177] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-250] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-348] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-256] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-265] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-344] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-290] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-312] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-296] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>