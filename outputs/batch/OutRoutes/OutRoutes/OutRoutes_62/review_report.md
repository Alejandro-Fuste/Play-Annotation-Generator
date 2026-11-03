# Play-Annotation-Generator Annotation Review — OutRoutes_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_62`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 3
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `9` | `9` |
| ⚠️ START CHANGED | `Action_RunOutRoute` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RB | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_PassBlock` | RT | `0` | `0` | 38 | START | 38 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `1` | `1` | 38 | START | 38 | 43 |
| ✅ EXACT | `Action_PassBlock` | RG | `2` | `2` | 38 | START | 38 | 70 |
| ✅ EXACT | `Action_PassBlock` | C | `9` | `9` | 38 | START | 38 | 91 |
| ⚠️ START CHANGED | `Action_RunOutRoute` | Position_Unknown | `11` | `11` | 44 | START | 45 | 47 |
| ✅ EXACT | `Action_SnapReceive` | RB | `4` | `4` | 44 | END | 44 | 44 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | RB | `4` | `4` | 109 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `11` | `11` | 137 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `11` | `11` | 143 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 92 | 48 | inferred_complete_timeline |
| `Action_None` | 96 | 99 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 43 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 65 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 71 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 37 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 91 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 70 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 89 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 101 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 14–47 | 24 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 22–39 | 16 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 26–299 | 271 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 29–86 | 58 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 32–299 | 222 | 7 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 33–52 | 20 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 75–110 | 31 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 84–299 | 192 | 6 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 95–299 | 178 | 6 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 98–168 | 58 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 101–230 | 128 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 143–155 | 11 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 176–299 | 124 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 182–299 | 117 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 228–280 | 34 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 231–299 | 69 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 245–254 | 10 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 250–255 | 6 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 268–299 | 32 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (3 segments found)
- ⚠️ `Action_RunOutRoute` for actor_track_id `11` (Position_Unknown): Annotated start 44 != Inferred start 45
- ❌ Missing segment for action `Action_ThrowPass` on target `4` (RB)
- ❌ Missing segment for action `Action_SecureCatch` on target `11` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `11` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 70: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 70: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_ThrowPass' for track '4' has invalid range: start=109, end=99. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '11' has invalid range: start=137, end=47. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '11' has invalid range: start=143, end=47. Clamping end to start.
- ⚠️ Action 'Action_PassBlock' range [38-89] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-43] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-71] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-70] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-92] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-101] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-34] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [45-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-279] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-82] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-204] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-283] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-134] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-190] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-103] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-297] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-257] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-255] for track '31' has 1 frames without a visible bounding box.
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

</details>