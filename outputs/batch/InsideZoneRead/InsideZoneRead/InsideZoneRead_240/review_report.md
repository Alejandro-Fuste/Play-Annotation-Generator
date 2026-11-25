# Play-Annotation-Generator Annotation Review — InsideZoneRead_240

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_240`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | RG | offense | `11` | `10` |
| ✅ EXACT | `Action_Keep` | RG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 3 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `20` | 1 | START | 64 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 4 | START | 4 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 4 | START | 4 | 63 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 4 | START | 4 | 51 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 4 | START | 4 | 72 |
| ✅ EXACT | `Action_SnapReceive` | RG | `11` | `10` | 12 | END | 1 | 12 |
| ✅ EXACT | `Action_ReadDefender` | RG | `11` | `10` | 16 | START | 16 | 31 |
| ✅ EXACT | `Action_Keep` | RG | `11` | `10` | 32 | START | 32 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RG | `11` | `10` | 42 | START | 42 | 132 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 76 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |
| `Action_None` | 61 | 95 | 35 | inferred_complete_timeline |
| `Action_None` | 103 | 163 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 75 | 75 | inferred_complete_timeline |
| `Action_None` | 78 | 95 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 72 | 69 | inferred_complete_timeline |
| `Action_None` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 51 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 12 | 12 | inferred_complete_timeline |
| `Action_None` | 13 | 15 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 16 | 31 | 16 | inferred_complete_timeline |
| `Action_Keep` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 42 | 132 | 91 | inferred_complete_timeline |
| `Action_BallCarry` | 138 | 150 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 153 | 180 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 63 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_None` | 78 | 92 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 73 | 73 | inferred_complete_timeline |
| `Action_None` | 78 | 122 | 45 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 144 | 9 | inferred_complete_timeline |
| `Action_None` | 147 | 180 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 101 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 9 | 9 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 132 | 132 | inferred_complete_timeline |
| `Action_None` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 171 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–180 | 181 | 2 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–27 | 28 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–88 | 89 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 33–39 | 7 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 39–91 | 52 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 43–44 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 48–99 | 47 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 56–164 | 98 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 64–180 | 101 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 70–180 | 107 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 82–92 | 6 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 96–98 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 107–172 | 66 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 110–180 | 71 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 139–174 | 36 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 145–160 | 16 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 169–179 | 9 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 1 != Inferred start 64
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 3 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 480: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=4, end=0. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '20' has invalid range: start=64, end=12. Clamping end to start.
- ⚠️ Action 'Action_None' range [1-132] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-51] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-27] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-163] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-72] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-75] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [42-132] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [138-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [153-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [66-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-73] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-180] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-9] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-57] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-91] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-152] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-172] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-160] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-179] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_240'; source metadata written as null.

</details>