# Play-Annotation-Generator Annotation Review — OutRoutes_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_64`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 45
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 29
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_RunOutRoute` | LT | offense | `0` | `0` |
| ✅ EXACT | `Action_RunOutRoute` | DE1 | defense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `18` |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `21` | `18` |
| ✅ EXACT | `Action_SecureCatch` | LT | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LT | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 106 |
| ✅ EXACT | `Action_PassBlock` | LT | `0` | `0` | 7 | START | 7 | 10 |
| ✅ EXACT | `Action_PassBlock` | C | `10` | `10` | 7 | START | 7 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `12` | 7 | START | 7 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `3` | `3` | 7 | START | 7 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `5` | `5` | 7 | START | 7 | 9 |
| ✅ EXACT | `Action_RunOutRoute` | LT | `0` | `0` | 11 | START | 11 | 74 |
| ✅ EXACT | `Action_RunOutRoute` | DE1 | `1` | `1` | 11 | START | 11 | 101 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `21` | `18` | 11 | END | N/A | N/A |
| ⚠️ START CHANGED | `Action_ThrowPass` | Position_Unknown | `21` | `18` | 38 | START | 137 | 137 |
| ✅ EXACT | `Action_SecureCatch` | LT | `0` | `0` | 75 | START | 75 | 78 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LT | `0` | `0` | 82 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 10 | 4 | inferred_complete_timeline |
| `Action_RunOutRoute` | 11 | 74 | 64 | inferred_complete_timeline |
| `Action_SecureCatch` | 75 | 78 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 11 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 16 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 97 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 103 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 9 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 17 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 61 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 104 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 91 | 85 | inferred_complete_timeline |
| `Action_PassBlock` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_RunOutRoute` | 11 | 101 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 19–20 | 2 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 27–86 | 60 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 103–122 | 20 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 111–180 | 60 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 137–180 | 43 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 151–179 | 29 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 172–180 | 9 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 173–178 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (5 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `21` (Position_Unknown)
- ⚠️ `Action_ThrowPass` for actor_track_id `21` (Position_Unknown): Annotated start 38 != Inferred start 137
- ❌ Missing segment for action `Action_BallCarry` on target `0` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BallCarry' for track '0' has invalid range: start=82, end=78. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '18' has invalid range: start=137, end=11. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '18' has invalid range: start=137, end=48. Clamping end to start.
- ⚠️ Action 'Action_SecureCatch' range [75-78] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [11-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-91] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-9] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-17] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-61] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-104] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-108] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-103] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-11] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-16] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [96-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-180] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-179] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-178] for track '23' has 1 frames without a visible bounding box.
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