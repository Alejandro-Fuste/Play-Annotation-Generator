# Play-Annotation-Generator Annotation Review — BootPass_58

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_58`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 44
- **Ball Tracks:** 2
- **Action Segments:** 92
- **Validation Warnings:** 168
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `17` | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `23` | `21` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `23` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `17` | N/A | 115 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `10` | `10` | 153 | END | 153 | 153 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `0` | `0` | 154 | START | 154 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `23` | `21` | 163 | START | 164 | 167 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `23` | `21` | 177 | START | 177 | 179 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `23` | `21` | 180 | START | 180 | 226 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–192 | 189 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–277 | 278 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–271 | 266 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–165 | 166 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–34 | 29 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–329 | 319 | 4 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–223 | 224 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–271 | 269 | 3 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–152 | 148 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–280 | 170 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–167 | 168 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–265 | 261 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–278 | 263 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–329 | 310 | 8 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 40–206 | 167 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 64–272 | 197 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 142–262 | 93 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 150–277 | 80 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 158–222 | 65 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 164–274 | 110 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 186–271 | 74 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 189–193 | 5 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 195–199 | 5 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 195–298 | 104 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 197–200 | 4 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 205–271 | 67 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 210–219 | 10 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 247–258 | 12 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 252–274 | 23 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 263–324 | 62 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 268–290 | 8 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 269–307 | 39 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 269–300 | 32 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 271–275 | 5 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 274–329 | 56 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 276–278 | 3 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 279–329 | 51 | 1 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 279–282 | 4 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 280–329 | 50 | 1 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 283–329 | 41 | 2 | Undefined position; Undefined team |
| `44` | `54` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 314–329 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 50 | 57 | 8 | 100.0% | None |
| `17` | `17` | 109 | 133 | 6 | 24.0% | 113–114, 116–132 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ThrowPass` on target `17` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ 44 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 44 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 146 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 88 |
| Missing visible bounding boxes during action | 78 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [162-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-192] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-271] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-271] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-152] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-268] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-280] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-171] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-246] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-278] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-38] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-256] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-166] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-272] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-221] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-277] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [164-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-193] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-219] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-274] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-271] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-307] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-275] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-278] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-329] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-282] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-321] for track '43' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-320] for track '45' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>