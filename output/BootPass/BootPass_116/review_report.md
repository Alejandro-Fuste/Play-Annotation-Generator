# Play-Annotation-Generator Annotation Review — BootPass_116

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_116`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 55
- **Ball Tracks:** 1
- **Action Segments:** 93
- **Validation Warnings:** 195
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 2
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `8` | `8` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `20` | `19` | 50 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BootAway` | Position_Unknown | `20` | `19` | 73 | START | N/A | N/A |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `8` | `8` | 89 | START | 89 | 120 |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `20` | `19` | 96 | START | 134 | 134 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `8` | `8` | 121 | START | 121 | 128 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–269 | 265 | 3 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–252 | 213 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–148 | 149 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–232 | 230 | 3 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–99 | 100 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–193 | 190 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–146 | 147 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–230 | 231 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–128 | 129 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–153 | 154 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–189 | 180 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–154 | 153 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–229 | 217 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–158 | 152 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 59–220 | 141 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 123–124 | 2 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 128–269 | 140 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 131–134 | 4 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 134–193 | 18 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 136–189 | 54 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 152–237 | 86 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 157–269 | 105 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 162–269 | 105 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 169–269 | 100 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 177–269 | 11 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 179–235 | 57 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 182–218 | 37 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 183–191 | 9 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 184–193 | 10 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 186–269 | 84 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 186–191 | 6 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 189–215 | 13 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 190–215 | 26 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 190–193 | 4 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 192–267 | 76 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 192–205 | 14 | 1 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 194–269 | 76 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 194–210 | 6 | 2 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 194–230 | 33 | 2 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 194–226 | 33 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 209–215 | 6 | 2 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 210–246 | 32 | 2 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 214–226 | 8 | 2 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 217–232 | 16 | 1 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 218–220 | 3 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 219–224 | 6 | 1 | Undefined position; Undefined team |
| `49` | `63` | Position_Unknown | Team_Unknown | 241–269 | 29 | 1 | Undefined position; Undefined team |
| `50` | `64` | Position_Unknown | Team_Unknown | 242–269 | 14 | 3 | Undefined position; Undefined team |
| `51` | `65` | Position_Unknown | Team_Unknown | 245–269 | 17 | 2 | Undefined position; Undefined team |
| `52` | `66` | Position_Unknown | Team_Unknown | 245–266 | 15 | 3 | Undefined position; Undefined team |
| `53` | `67` | Position_Unknown | Team_Unknown | 258–264 | 7 | 1 | Undefined position; Undefined team |
| `54` | `68` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `55` | `69` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 119 | 119 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ❌ Missing segment for action `Action_BootAway` on target `20` (Position_Unknown)
- ⚠️ `Action_ThrowPass` for actor_track_id `20` (Position_Unknown): Annotated start 96 != Inferred start 134

### Track Identity Issues

- ⚠️ 55 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 55 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 50 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 110 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SnapReceive' for track '19' has invalid range: start=134, end=50. Clamping end to start.
- ⚠️ Segment 'Action_BootAway' for track '19' has invalid range: start=134, end=86. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '19' has invalid range: start=134, end=107. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-267] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-252] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-203] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-232] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [121-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-179] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-158] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-177] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-146] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-200] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-242] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-195] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-215] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-267] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-205] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-197] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-230] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-226] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-236] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-246] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-218] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-232] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-220] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-224] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-269] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-246] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-269] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-266] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-264] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '55' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.

</details>