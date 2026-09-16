# Play-Annotation-Generator Annotation Review — BootPass_62

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_62`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 174
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 3
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `11` | `11` | 58 | END | 58 | 58 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `11` | `11` | 65 | START | 65 | 80 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | `11` | `11` | 81 | START | 81 | 82 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `16` | `16` | 81 | START | 81 | 124 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `9` | `9` | 180 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `14` | `14` | 203 | START | N/A | N/A |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 16–99 | 79 | 3 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 16–329 | 302 | 5 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 16–194 | 179 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 16–158 | 140 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 16–108 | 81 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 16–125 | 110 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 16–105 | 83 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 16–93 | 58 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 16–115 | 100 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 16–117 | 102 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 16–70 | 55 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 16–179 | 140 | 9 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 16–121 | 106 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 16–89 | 71 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 16–149 | 117 | 7 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 72–101 | 29 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 80–329 | 250 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 102–117 | 11 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 109–189 | 81 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 114–170 | 56 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 162–329 | 153 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 179–329 | 138 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 184–309 | 121 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 194–268 | 75 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 200–252 | 47 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 222–263 | 40 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 228–241 | 14 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 231–329 | 95 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 232–247 | 16 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 233–251 | 19 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 235–329 | 94 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 235–249 | 7 | 2 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 244–268 | 25 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 246–329 | 84 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 248–321 | 74 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 256–305 | 50 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 268–329 | 58 | 3 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 272–329 | 58 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 277–329 | 53 | 1 | Undefined position; Undefined team |
| `41` | `46` | Position_Unknown | Team_Unknown | 294–329 | 34 | 2 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 319–329 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BootAway` and target `11` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `9` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `14` (Position_Unknown)

### Track Identity Issues

- ⚠️ 43 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 43 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 16 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 86 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '9' has invalid range: start=180, end=117. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '14' has invalid range: start=203, end=149. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [16-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-99] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-315] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-194] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-134] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-108] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-84] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-93] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-115] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-70] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-55] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' for track '11' starts at frame 58, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SnapReceive' range [58-58] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [65-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [81-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-44] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-69] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-212] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-282] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-329] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-296] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-300] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-329] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-302] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-252] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-309] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-251] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-329] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-321] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-305] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-309] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-320] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-329] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-321] for track '41' has 2 frames without a visible bounding box.
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

</details>