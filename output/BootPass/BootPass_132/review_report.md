# Play-Annotation-Generator Annotation Review — BootPass_132

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_132`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 68
- **Validation Warnings:** 120
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
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `8` | `8` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `33` | `25` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `8` | `8` | 16 | END | 16 | 16 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `8` | `8` | 24 | START | 24 | 50 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `8` | `8` | 51 | START | 51 | 67 |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | Position_Unknown | `33` | `25` | 60 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `15` | `15` | 90 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `12` | `12` | 111 | START | N/A | N/A |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–104 | 105 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–79 | 80 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–359 | 351 | 5 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–130 | 127 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–119 | 120 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–108 | 109 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–105 | 99 | 8 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–98 | 98 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–204 | 188 | 7 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–125 | 126 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–102 | 101 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–359 | 353 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–112 | 113 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 47–48 | 2 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 57–100 | 44 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 79–314 | 202 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 104–151 | 48 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 137–251 | 114 | 2 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 159–359 | 162 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 175–346 | 172 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 178–359 | 179 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 185–359 | 170 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 189–359 | 171 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 203–359 | 157 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 241–359 | 119 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 244–359 | 115 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 266–359 | 81 | 5 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 313–359 | 32 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `25` | 126 | 138 | 4 | 30.8% | 127, 130–137 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_RunFlatRoute` on target `25` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `15` (Position_Unknown)
- ❌ Missing segment for action `Action_SecureCatch` on target `12` (Position_Unknown)

### Track Identity Issues

- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 113, Column 'Run Block': Could not parse frame number from '-' in entry '-,OL'.
- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '12' has invalid range: start=111, end=102. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '15' has invalid range: start=90, end=48. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-226] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-92] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-199] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-334] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-230] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-295] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-359] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-346] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-351] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-190] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-359] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-287] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-296] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-324] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '31' has 1 frames without a visible bounding box.
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

</details>