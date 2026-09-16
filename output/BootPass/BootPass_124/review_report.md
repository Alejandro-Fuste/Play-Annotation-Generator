# Play-Annotation-Generator Annotation Review — BootPass_124

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_124`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 143
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 1
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `23` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | Team_Unknown | `23` | `20` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `16` | `16` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `23` | `20` | 79 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | `23` | `20` | 114 | START | 118 | 151 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `22` | `19` | 120 | START | 120 | 171 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `16` | `16` | 174 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `8` | `8` | 197 | START | N/A | N/A |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–359 | 332 | 6 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–112 | 112 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–359 | 356 | 2 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–359 | 355 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–359 | 353 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–126 | 127 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–359 | 354 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–359 | 325 | 6 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–46 | 47 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–359 | 346 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–154 | 155 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–118 | 117 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–359 | 345 | 6 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 108–118 | 11 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 111–358 | 242 | 4 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 118–359 | 214 | 6 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–358 | 232 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 131–146 | 16 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 135–359 | 225 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 144–359 | 201 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 160–359 | 169 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 199–359 | 157 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 245–328 | 74 | 6 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 246–250 | 5 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 248–265 | 15 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 280–295 | 6 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 312–359 | 48 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 315–359 | 42 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 318–359 | 31 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 335–355 | 21 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 342–359 | 18 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 347–355 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `20` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `20` (4 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `16` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `8` (Position_Unknown)

### Track Identity Issues

- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 79 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '8' has invalid range: start=197, end=126. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '16' has invalid range: start=174, end=118. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '20' has invalid range: start=118, end=79. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-281] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-310] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-320] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-346] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-148] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-287] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-233] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-343] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-358] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [118-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [154-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [166-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-358] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-319] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-330] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-301] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-230] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-325] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-257] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-326] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-355] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-355] for track '36' has 2 frames without a visible bounding box.
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