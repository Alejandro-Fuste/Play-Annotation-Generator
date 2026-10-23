# Play-Annotation-Generator Annotation Review — BootPass_109

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_109`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 197
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 1
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 134
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `22` | `21` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `3` | `3` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `34` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `39` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `14` | `14` | 45 | END | 45 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `22` | `21` | 53 | START | 53 | 59 |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `34` | `27` | 75 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | Position_Unknown | `3` | `3` | 82 | START | 82 | 96 |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `34` | `27` | 133 | START | 138 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | Position_Unknown | `39` | `28` | 175 | START | 197 | 200 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–264 | 261 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–247 | 221 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–269 | 252 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–168 | 132 | 9 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–269 | 253 | 7 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–265 | 258 | 4 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–187 | 183 | 3 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–269 | 264 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–201 | 195 | 4 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–267 | 265 | 3 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–131 | 132 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–63 | 63 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–269 | 241 | 8 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–182 | 177 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–121 | 122 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–211 | 212 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–177 | 172 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–73 | 74 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–269 | 223 | 8 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–64 | 65 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–264 | 204 | 18 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 6–269 | 235 | 9 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 70–264 | 101 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 71–135 | 29 | 5 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 105–269 | 165 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 112–269 | 158 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 117–217 | 65 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 138–265 | 127 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 197–269 | 70 | 5 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 202–260 | 46 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 225–263 | 38 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 226–269 | 31 | 3 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 238–260 | 21 | 2 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 254–269 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `27` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_RunFlatRoute` and target `3` (4 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `34` (Position_Unknown): Annotated start 133 != Inferred start 138
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `28` (2 segments found)

### Track Identity Issues

- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 37 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 126 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BootAway' for track '27' has invalid range: start=138, end=126. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-172] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-264] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-226] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [82-96] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [101-114] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [116-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [119-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-249] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-265] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-262] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-191] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-250] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-267] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-153] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-142] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-211] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-167] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-132] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-154] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-167] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-224] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-253] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [53-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-106] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-269] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-177] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-264] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-269] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-269] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-217] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [197-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-243] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-240] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-260] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-228] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-263] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-260] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-269] for track '33' has 1 frames without a visible bounding box.
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

</details>