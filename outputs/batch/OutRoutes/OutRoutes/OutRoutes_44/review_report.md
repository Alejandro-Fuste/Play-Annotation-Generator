# Play-Annotation-Generator Annotation Review — OutRoutes_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 40
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 27
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunOutRoute` | SAF | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `14` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `17` | `14` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | SAF | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | SAF | defense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_PassBlock` | C | `11` | `11` | 12 | START | 12 | 70 |
| ✅ EXACT | `Action_PassBlock` | RG | `2` | `2` | 12 | START | 12 | 74 |
| ✅ EXACT | `Action_PassBlock` | LT | `7` | `7` | 12 | START | 12 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 12 | START | 12 | 65 |
| ✅ EXACT | `Action_RunOutRoute` | SAF | `1` | `1` | 16 | START | 16 | 68 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `17` | `14` | 16 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `17` | `14` | 47 | START | 74 | 74 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | SAF | `1` | `1` | 90 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | SAF | `1` | `1` | 99 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 72 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 67 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 70 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 74 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 65 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 84 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 68 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 68 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–63 | 64 | 1 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 69–180 | 112 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 74–177 | 104 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 81–180 | 98 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 83–180 | 94 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 88–180 | 79 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 155–180 | 26 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 162–180 | 19 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 165–175 | 7 | 3 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 166–180 | 15 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 168–180 | 13 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 174–176 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (Position_Unknown)
- ⚠️ `Action_ThrowPass` for actor_track_id `17` (Position_Unknown): Annotated start 47 != Inferred start 74
- ❌ Missing segment for action `Action_SecureCatch` on target `1` (SAF)
- ❌ Missing segment for action `Action_BallCarry` on target `1` (SAF)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 34 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 52: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '1' has invalid range: start=90, end=68. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=99, end=68. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '14' has invalid range: start=74, end=16. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '14' has invalid range: start=74, end=59. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-63] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [16-68] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-67] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-84] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-92] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-70] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-180] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-177] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>