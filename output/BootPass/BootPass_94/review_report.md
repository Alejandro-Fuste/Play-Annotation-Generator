# Play-Annotation-Generator Annotation Review — BootPass_94

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_94`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 1
- **Action Segments:** 78
- **Validation Warnings:** 144
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 2
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ START CHANGED | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `15` | `15` |
| ⚠️ START CHANGED | `Action_BootAway` | Position_Unknown | Team_Unknown | `24` | `23` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `20` | `19` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `24` | `23` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | Position_Unknown | `15` | `15` | 52 | END | 62 | 62 |
| ⚠️ START CHANGED | `Action_FakeHandoff` | Position_Unknown | `15` | `15` | 75 | START | 80 | 91 |
| ⚠️ START CHANGED | `Action_BootAway` | Position_Unknown | `24` | `23` | 92 | START | 96 | 130 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `20` | `19` | 99 | START | 99 | 145 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `24` | `23` | 133 | START | 133 | 145 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `4` | `4` | 180 | START | N/A | N/A |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–35 | 36 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–210 | 132 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–210 | 205 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–185 | 178 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–68 | 63 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–152 | 66 | 5 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–105 | 102 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–148 | 137 | 3 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–88 | 80 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–210 | 201 | 4 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–98 | 99 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–167 | 164 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 4–60 | 50 | 6 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 7–192 | 180 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 60–86 | 26 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 62–165 | 76 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 67–87 | 21 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 77–91 | 15 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 83–111 | 29 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 90–153 | 64 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 94–141 | 48 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 94–156 | 63 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 95–170 | 76 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 96–189 | 93 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 102–162 | 29 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 114–140 | 26 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 128–137 | 9 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 134–210 | 77 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 135–196 | 61 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 157–159 | 3 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 180–185 | 6 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 182–210 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `30` | `36` | 171 | 171 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_FakeHandoff` for actor_track_id `15` (Position_Unknown): Annotated start 75 != Inferred start 80
- ⚠️ `Action_BootAway` for actor_track_id `24` (Position_Unknown): Annotated start 92 != Inferred start 96
- ❌ Missing segment for action `Action_SecureCatch` on target `4` (Position_Unknown)

### Track Identity Issues

- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 52 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '4' has invalid range: start=180, end=68. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '15' has invalid range: start=62, end=52. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-58] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-152] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-33] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-60] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-92] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-77] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 63, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [63-67] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-91] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-156] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [96-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '23' starts at frame 146, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [146-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-189] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-140] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-210] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-210] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>